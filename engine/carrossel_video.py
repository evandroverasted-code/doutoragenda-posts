#!/usr/bin/env python3
"""Converte um carrossel em vídeo para o Facebook (decisão do Ted, 12/11/2026).

No Facebook o carrossel saía como um amontoado de fotos. Agora os slides viram
um vídeo único: 3,5 s por slide, transição suave (fade), 1080x1350, com trilha
silenciosa (alguns players do Facebook rejeitam vídeo sem áudio).

Uso:
  python3 engine/carrossel_video.py semanas/<data>            # todos os carrosséis da semana
  python3 engine/carrossel_video.py semanas/<data> p1 p2      # só esses posts

Saída: semanas/<data>/out/<id>_fb.mp4 (mesmos slides, mesma ordem de `arquivos`).
"""
import json
import subprocess
import sys
from pathlib import Path

SEG = 3.5     # duração de cada slide
FADE = 0.4    # duração da transição
W, H = 1080, 1350


def montar(out: Path, pid: str, arquivos: list[str]) -> Path:
    slides = [out / a for a in arquivos]
    falta = [s.name for s in slides if not s.exists()]
    if falta:
        raise SystemExit(f"{pid}: slides não encontrados: {falta}")
    destino = out / f"{pid}_fb.mp4"
    n = len(slides)
    cmd = ["ffmpeg", "-y", "-loglevel", "error"]
    for s in slides:
        cmd += ["-loop", "1", "-t", str(SEG + FADE), "-i", str(s)]
    cmd += ["-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100"]
    filtros = [
        f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=decrease,"
        f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white,setsar=1,fps=30,format=yuv420p[v{i}]"
        for i in range(n)
    ]
    atual = "v0"
    for i in range(1, n):
        filtros.append(
            f"[{atual}][v{i}]xfade=transition=fade:duration={FADE}:offset={i * SEG:.2f}[x{i}]"
        )
        atual = f"x{i}"
    total = n * SEG + FADE
    cmd += [
        "-filter_complex", ";".join(filtros),
        "-map", f"[{atual}]", "-map", f"{n}:a",
        "-t", f"{total:.2f}",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "20", "-preset", "medium",
        "-c:a", "aac", "-b:a", "128k", "-shortest",
        "-movflags", "+faststart", str(destino),
    ]
    subprocess.run(cmd, check=True)
    return destino


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    semana = Path(sys.argv[1])
    ids = set(sys.argv[2:])
    dados = json.loads((semana / "posts.json").read_text(encoding="utf-8"))
    out = semana / "out"
    for p in dados["posts"]:
        if p.get("tipo") != "carrossel" or (ids and p["id"] not in ids):
            continue
        destino = montar(out, p["id"], p["arquivos"])
        print(f"{p['id']}: {destino} ({len(p['arquivos'])} slides)")


if __name__ == "__main__":
    main()
