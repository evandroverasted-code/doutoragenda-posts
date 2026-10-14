"""Doutor Agenda — motor de artes (feed 1080x1350 e reels 1080x1920).

Uso dentro de semanas/AAAA-MM-DD/build.py:
    import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'engine'))
    from lib import *
    page('p1_1', body_html, bg='g')          # gera html/p1_1.html (feed)
    reel('r1', total_seconds, body_html)      # gera html/r1.html (reels, use scene()/move())
Depois: node engine/render.js <pasta_da_semana>  e  bash engine/make_reels.sh <pasta_da_semana>
"""
import os

ENGINE = os.path.dirname(os.path.abspath(__file__))
A = 'file://' + os.path.join(ENGINE, 'assets')          # caminho absoluto dos assets
OUT = os.path.join(os.getcwd(), 'html')                   # build.py roda de dentro da pasta da semana

# Paleta oficial
VERDE, AMARELO, VERDE_ESC, VERDE_CLARO, VERDE_SUAVE, BRANCO = '#009632', '#FFCD00', '#00642B', '#B8D8B0', '#E8F5E8', '#FFFFFF'
ROSA = '#E8559A'   # só para Outubro Rosa (detalhe), nunca como cor principal

FONTS = ''.join(
    f"@font-face{{font-family:P;font-weight:{w};src:url({A}/fonts/poppins-latin-{w}-normal.woff2)}}"
    for w in (400, 600, 700, 800, 900))

CSS = FONTS + """
*{margin:0;padding:0;box-sizing:border-box}
body{width:%(w)dpx;height:%(h)dpx;font-family:P,sans-serif;overflow:hidden}
.c{position:relative;width:%(w)dpx;height:%(h)dpx;overflow:hidden}
.g{background:#009632}.y{background:#FFCD00}.l{background:#E8F5E8}.w{background:#fff}.dg{background:#00642B}
.ring{position:absolute;border-radius:50%%;border:70px solid rgba(255,255,255,.07)}
.ringd{position:absolute;border-radius:50%%;border:70px solid rgba(0,100,43,.07)}
.tag{position:absolute;left:80px;top:80px;background:#00642B;color:#fff;font-weight:600;font-size:30px;padding:12px 28px;border-radius:40px;z-index:5}
.tagy{background:#FFCD00;color:#00642B}.tagr{background:#E8559A;color:#fff}
.h{position:absolute;left:80px;color:#fff;font-weight:800;line-height:1.03;letter-spacing:-2px;z-index:3}
.h span{color:#FFCD00}
.dk{color:#00642B}.dk span{color:#009632}
.p{position:absolute;left:80px;font-weight:600;line-height:1.4;z-index:3}
.num{position:absolute;left:80px;font-weight:900;color:#FFCD00;line-height:.8;letter-spacing:-8px;z-index:3}
.badge{position:absolute;background:#FFCD00;border-radius:36px;color:#00642B;transform:rotate(-3deg);box-shadow:0 12px 0 #00642B;z-index:4}
.cta{position:absolute;left:80px;z-index:4;background:#fff;color:#00642B;font-weight:800;font-size:40px;padding:24px 44px;border-radius:60px;box-shadow:0 10px 0 #00642B}
.cta small{display:block;font-weight:600;font-size:24px;color:#009632}
.ctag{background:#009632;color:#fff;box-shadow:0 10px 0 #00642B}.ctag small{color:#FFCD00}
.img{position:absolute;z-index:2}
.foot{position:absolute;left:0;bottom:0;width:100%%;height:130px;background:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 80px;z-index:5}
.foot img{height:80px}
.foot .t{text-align:right;color:#00642B;font-weight:700;font-size:26px;line-height:1.3}
.foot .t span{display:block;font-weight:400;font-size:19px;color:#3a6b4a}
.pg{position:absolute;right:80px;top:92px;font-weight:700;font-size:26px;z-index:5}
.swipe{position:absolute;left:80px;bottom:170px;font-weight:700;font-size:30px;z-index:5}
.card{position:absolute;left:80px;right:80px;background:#fff;border-radius:36px;padding:44px 50px;z-index:3;box-shadow:0 12px 0 #00642B}
.card h3{font-size:56px;font-weight:800;color:#00642B;letter-spacing:-1px;line-height:1.05}
.card p{font-size:32px;font-weight:400;color:#1f4d2e;line-height:1.4;margin-top:16px}
.card .k{display:inline-block;background:#E8F5E8;color:#009632;font-weight:700;font-size:24px;padding:6px 18px;border-radius:20px;margin-bottom:18px}
.pill{display:inline-block;background:#fff;color:#00642B;font-weight:700;font-size:30px;padding:14px 26px;border-radius:40px;margin:0 12px 16px 0;box-shadow:0 6px 0 #00642B}
.mv{display:inline-block;font-weight:900;font-size:30px;padding:8px 22px;border-radius:30px;margin-bottom:18px}
.mito{background:#00642B;color:#fff}.verd{background:#FFCD00;color:#00642B}
"""

DISC = '*em relação ao preço particular de tabela'
INFO = 'Conteúdo informativo. Siga sempre a orientação do seu médico.'


def foot(text=DISC):
    return f'<div class="foot"><img src="{A}/logo.png"><div class="t">doutoragenda.com<span>{text}</span></div></div>'


def mascot(name, style):
    """name: masc_prancheta | masc_joinha | masc_apresenta | masc_celular | masc_aponta | masc_folha | mao_celular.
    Nunca distorcer: defina só height (largura automática)."""
    return f'<img class="img" src="{A}/{name}.png" style="{style}">'


def chat(bubbles, style):
    """bubbles: lista de (lado, texto) com lado 'in' (cliente) ou 'out' (Doutor Agenda)."""
    h = ''
    for side, t in bubbles:
        if side == 'in':
            h += f'<div style="background:#E8F5E8;border-radius:22px 22px 22px 6px;padding:14px 18px;font-size:21px;color:#1f4d2e;font-weight:600;margin-bottom:14px">{t}</div>'
        else:
            h += f'<div style="background:#009632;border-radius:22px 22px 6px 22px;padding:14px 18px;font-size:21px;color:#fff;font-weight:600;margin:0 0 14px 28px">{t}</div>'
    return f'<div class="img" style="z-index:3;{style}">{h}</div>'


def _write(name, html):
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, name + '.html'), 'w').write(html)


def page(name, body, bg='g', css='', w=1080, h=1350):
    """Arte estática de feed (1080x1350)."""
    _write(name, f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS % dict(w=w, h=h)}{css}</style></head>'
                 f'<body data-w="{w}" data-h="{h}"><div class="c {bg}">{body}</div></body></html>')


# ---------------- Motion (reels 1080x1920, sem áudio) ----------------
_kf = []
_n = [0]


def scene(t0, t1, total, fade=0.35):
    """CSS de animação: elemento visível entre t0 e t1 (segundos)."""
    _n[0] += 1; nm = f's{_n[0]}'
    p = lambda t: max(0, min(100, t / total * 100))
    end = 0 if t1 < total else 1
    _kf.append(f"@keyframes {nm}{{0%{{opacity:0}}{p(t0):.2f}%{{opacity:0}}{p(t0+fade):.2f}%{{opacity:1}}"
               f"{p(t1-fade):.2f}%{{opacity:1}}{p(t1):.2f}%{{opacity:{end}}}100%{{opacity:{end}}}}}")
    return f"animation:{nm} {total}s linear both"


def move(t0, dur, total, frm, to='none', ease='cubic-bezier(.2,.9,.3,1.25)'):
    """CSS de entrada: de transform `frm` para `to`, com fade-in."""
    _n[0] += 1; nm = f'm{_n[0]}'
    p = lambda t: max(0, min(100, t / total * 100))
    _kf.append(f"@keyframes {nm}{{0%{{transform:{frm};opacity:0}}{p(t0):.2f}%{{transform:{frm};opacity:0;animation-timing-function:{ease}}}"
               f"{p(t0+dur*0.4):.2f}%{{opacity:1}}{p(t0+dur):.2f}%{{transform:{to};opacity:1}}100%{{transform:{to};opacity:1}}}}")
    return f"animation:{nm} {total}s linear both"


def reel(name, total, body, bg='g'):
    """Reels 1080x1920. `body` deve usar scene()/move() gerados ANTES desta chamada."""
    css = CSS % dict(w=1080, h=1920) + '.foot{height:200px}.foot img{height:110px}.foot .t{font-size:34px}.foot .t span{font-size:22px}'
    _write(name, f'<!doctype html><html><head><meta charset="utf-8"><style>{css}{"".join(_kf)}</style></head>'
                 f'<body data-w="1080" data-h="1920" data-total="{total}"><div class="c {bg}">{body}</div>'
                 f'<script>window.TOTAL={total}</script></body></html>')
    _kf.clear()
