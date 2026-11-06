#!/usr/bin/env node
// L2 smoke for single-file HTML deliverables. Usage: node smoke_html_cdp.mjs <file.html> [--shot out.png]
// Headless Chrome via CDP, node>=22 builtin WebSocket -- no playwright/puppeteer dep.
// Captures console.error/exception/Log.error, counts DOM probes (data-slide), optional screenshot.
// Prints one JSON line {slides,title,nav,errors,nErrors}; exit 0 clean / 1 artifact has errors / 2 harness failure.
// Fixture the verifier both ways before trusting it on real artifacts (see references/judge-tools.md).
import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync, writeFileSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';

const htmlPath = path.resolve(process.argv[2]);
const shotIdx = process.argv.indexOf('--shot');
const shotPath = shotIdx > 0 ? path.resolve(process.argv[shotIdx + 1]) : null;
const hardTimer = setTimeout(() => { console.log(JSON.stringify({ fatal: 'timeout' })); process.exit(2); }, 45000);

const prof = mkdtempSync(path.join(tmpdir(), 'smoke-'));
const chrome = spawn('google-chrome', [
  '--headless=new', '--disable-gpu', '--no-first-run', '--hide-scrollbars',
  `--user-data-dir=${prof}`, '--window-size=1600,1000',
  '--remote-debugging-port=0', 'about:blank',
], { stdio: ['ignore', 'ignore', 'pipe'] });

let wsBrowser = null;
let stderrBuf = '';
chrome.stderr.on('data', d => {
  stderrBuf += String(d);
  const m = stderrBuf.match(/DevTools listening on (ws:\/\/\S+)/);
  if (m && !wsBrowser) wsBrowser = m[1];
});
chrome.on('exit', code => { if (!wsBrowser) { console.log(JSON.stringify({ fatal: `chrome exited ${code}`, stderr: stderrBuf.slice(-400) })); process.exit(2); } });

const sleep = ms => new Promise(r => setTimeout(r, ms));
for (let i = 0; i < 100 && !wsBrowser; i++) await sleep(100);
if (!wsBrowser) { console.log(JSON.stringify({ fatal: 'no devtools url', stderr: stderrBuf.slice(-400) })); process.exit(2); }

const httpPort = new URL(wsBrowser).port;
let targets;
for (let i = 0; i < 50; i++) {
  try { targets = await (await fetch(`http://127.0.0.1:${httpPort}/json/list`)).json(); if (targets?.length) break; } catch {}
  await sleep(100);
}
const page = targets.find(t => t.type === 'page');
if (!page) { console.log(JSON.stringify({ fatal: 'no page target' })); process.exit(2); }

const ws = new WebSocket(page.webSocketDebuggerUrl);
await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });

let mid = 0;
const pending = new Map();
const errors = [];
const send = (method, params = {}) => new Promise(res => {
  const id = ++mid; pending.set(id, res);
  ws.send(JSON.stringify({ id, method, params }));
});
ws.onmessage = ev => {
  const msg = JSON.parse(ev.data);
  if (msg.id && pending.has(msg.id)) { pending.get(msg.id)(msg.result ?? msg.error); pending.delete(msg.id); return; }
  const { method, params } = msg;
  if (method === 'Runtime.consoleAPICalled' && params.type === 'error')
    errors.push(params.args?.map(a => a.value ?? a.description ?? '').join(' ').slice(0, 300));
  if (method === 'Runtime.exceptionThrown')
    errors.push((params.exceptionDetails?.exception?.description || params.exceptionDetails?.text || 'exception').slice(0, 300));
  if (method === 'Log.entryAdded' && params.entry?.level === 'error')
    errors.push(`log:${params.entry.text}`.slice(0, 300));
};

for (const m of ['Page.enable', 'Runtime.enable', 'Log.enable']) await send(m);
await send('Page.navigate', { url: `file://${htmlPath}` });
await sleep(3000); // load + animation-loop settle

const ev = await send('Runtime.evaluate', { returnByValue: true, expression:
  `JSON.stringify({slides: document.querySelectorAll('[data-slide]').length, title: document.title, hasNav: !!document.querySelector('nav, [data-nav], .nav')})` });
const stats = JSON.parse(ev.result?.value || '{}');

if (shotPath) {
  mkdirSync(path.dirname(shotPath), { recursive: true });
  const shot = await send('Page.captureScreenshot', { format: 'png' });
  if (shot?.data) writeFileSync(shotPath, Buffer.from(shot.data, 'base64'));
}

console.log(JSON.stringify({ slides: stats.slides ?? null, title: stats.title ?? null, nav: !!stats.hasNav, errors, nErrors: errors.length }));
clearTimeout(hardTimer);
ws.close(); chrome.kill('SIGTERM');
// Guarded cleanup: chrome flushes the profile dir async after SIGTERM; unguarded rmSync ENOTEMPTY-crashes
// AFTER the verdict is printed and pollutes the exit code (a clean run would exit 1).
try { rmSync(prof, { recursive: true, force: true, maxRetries: 3, retryDelay: 200 }); } catch {}
process.exit(errors.length ? 1 : 0);
