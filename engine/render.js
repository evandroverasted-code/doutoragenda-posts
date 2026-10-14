// Renderiza as artes de uma semana.
// Uso: node engine/render.js semanas/AAAA-MM-DD [prefixo]
//  - html sem data-total  -> PNG estático (out/<nome>.png)
//  - html com data-total  -> frames + MP4 30fps (out/<nome>.mp4) via ffmpeg
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), { execSync } = require('child_process');
(async () => {
  const week = path.resolve(process.argv[2]); const only = process.argv[3];
  const htmlDir = path.join(week, 'html'), outDir = path.join(week, 'out');
  fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }).catch(() => chromium.launch());
  for (const f of fs.readdirSync(htmlDir).filter(f => f.endsWith('.html') && (!only || f.startsWith(only))).sort()) {
    const html = fs.readFileSync(path.join(htmlDir, f), 'utf8');
    const w = +(html.match(/data-w="(\d+)"/) || [0, 1080])[1], h = +(html.match(/data-h="(\d+)"/) || [0, 1350])[1];
    const total = (html.match(/data-total="([\d.]+)"/) || [])[1];
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + path.join(htmlDir, f)); await p.waitForTimeout(700);
    const name = f.replace('.html', '');
    if (!total) { await p.screenshot({ path: path.join(outDir, name + '.png') }); console.log('png', name); }
    else {
      const fps = 30, fr = path.join(week, 'frames', name); fs.rmSync(fr, { recursive: true, force: true }); fs.mkdirSync(fr, { recursive: true });
      const n = Math.round(+total * fps);
      for (let i = 0; i < n; i++) {
        await p.evaluate(t => document.getAnimations().forEach(a => { a.pause(); a.currentTime = t * 1000; }), i / fps);
        await p.screenshot({ path: `${fr}/${String(i).padStart(4, '0')}.png` });
      }
      // trilha de áudio silenciosa (AAC) — a API de Reels do Instagram é mais estável com áudio presente
      execSync(`ffmpeg -y -loglevel error -framerate ${fps} -i ${fr}/%04d.png -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=44100 -shortest -c:v libx264 -pix_fmt yuv420p -crf 18 -c:a aac -b:a 128k -movflags +faststart ${path.join(outDir, name + '.mp4')}`);
      fs.rmSync(fr, { recursive: true, force: true });
      console.log('mp4', name, n, 'frames');
    }
    await p.close();
  }
  await b.close();
})();
