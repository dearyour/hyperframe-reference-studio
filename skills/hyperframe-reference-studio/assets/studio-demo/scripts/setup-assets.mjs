import { copyFile, mkdir, readFile, writeFile } from 'node:fs/promises';

const root = new URL('../', import.meta.url);
const vendor = new URL('assets/vendor/', root);
const gsap = new URL('node_modules/gsap/', root);
const pkg = JSON.parse(await readFile(new URL('package.json', gsap), 'utf8'));
if (pkg.version !== '3.15.0') throw new Error('Run npm ci to install GSAP 3.15.0.');
await mkdir(vendor, { recursive: true });
await copyFile(new URL('dist/gsap.min.js', gsap), new URL('gsap.min.js', vendor));
// GSAP's npm package embeds its copyright/license notice in the runtime header.
const runtime = await readFile(new URL('dist/gsap.min.js', gsap), 'utf8');
const notice = runtime.match(/^\/\*![\s\S]*?\*\//)?.[0];
if (!notice) throw new Error('Missing upstream GSAP license header.');
await writeFile(new URL('GSAP-NOTICE.txt', vendor), `${notice}\n\n${pkg.license}\n`);
console.log('Local GSAP runtime and upstream license notice are ready. Fonts are bundled.');
