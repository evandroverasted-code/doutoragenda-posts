"""YouTube Shorts da semana 26/10 a 01/11/2026 (terça e quinta).
s1 (ter 27/10) — Anvisa proíbe picolé com melatonina e suplemento proteico (26/10/2026)
s2 (qui 29/10) — 3 milhões de adolescentes sem a 2ª dose da vacina da dengue (MS, out/2026)
Render: python3 semanas/2026-10-26/shorts.py && node engine/render.js semanas/2026-10-26 s
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'engine'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from lib import *

T = 15


def short(name, intro, passos, final):
    b = ['<div class="ring" style="width:1100px;height:1100px;right:-450px;top:500px"></div>']
    kick, big, big_size, txt, fonte, masc = intro
    b.append(f'''<div style="position:absolute;left:80px;top:260px;width:920px;{scene(0.1,3.2,T)}">
 <div style="color:#FFCD00;font-weight:800;font-size:60px;{move(0.1,.6,T,'translateY(50px)')}">{kick}</div>
 <div style="color:#fff;font-weight:900;font-size:{big_size}px;line-height:.98;letter-spacing:-6px;margin-top:14px;transform-origin:left top;{move(0.4,.7,T,'scale(.3)','scale(1)')}">{big}</div>
 <div style="color:#fff;font-weight:700;font-size:54px;line-height:1.18;width:620px;margin-top:28px;{move(1.0,.6,T,'translateY(40px)')}">{txt}</div>
 <div style="color:#B8D8B0;font-weight:600;font-size:32px;margin-top:30px;{move(1.4,.5,T,'translateY(30px)')}">{fonte}</div></div>
<img style="position:absolute;right:-220px;bottom:200px;height:780px;{scene(0.5,3.2,T)}" src="{A}/{masc}.png">''')
    for i, (n, t, d, bg, im) in enumerate(passos):
        t0 = 3.2 + i * 2.8; t1 = t0 + 2.8
        bgc = {'l': '#E8F5E8', 'y': '#FFCD00', 'g': '#009632'}[bg]
        fc = '#fff' if bg == 'g' else '#00642B'
        nc = '#FFCD00' if bg == 'g' else '#009632'
        fl = im == 'masc_aponta'
        long_t = len(t) >= 16
        b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:{bgc};{scene(t0,t1,T,.25)}">
 <div style="position:absolute;left:80px;top:220px;color:{nc};font-weight:900;font-size:420px;line-height:.8;letter-spacing:-14px;transform-origin:left top;{move(t0+.05,.6,T,'scale(.2)','scale(1)')}">{n}</div>
 <div style="position:absolute;left:80px;top:640px;width:900px;color:{fc}">
  <div style="font-weight:900;font-size:{84 if long_t else 100}px;line-height:1.02;letter-spacing:-3px;{move(t0+.3,.6,T,'translateY(70px)')}">{t}</div>
  <div style="width:580px;margin-top:36px;font-weight:600;font-size:46px;line-height:1.3;{move(t0+.5,.6,T,'translateY(50px)')}">{d}</div>
 </div>
 <img style="position:absolute;right:{0 if fl else -110}px;bottom:120px;height:{700 if fl else 680}px;{'transform:scaleX(-1);' if fl else ''}{move(t0+.2,.7,T,'translateX(700px)' + (' scaleX(-1)' if fl else ''), 'scaleX(-1)' if fl else 'none')}" src="{A}/{im}.png">
</div>''')
    h1, h2, sub = final
    b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#E8F5E8;{scene(11.6,T,T,.3)}">
 <div style="position:absolute;left:80px;top:240px;color:#00642B;font-weight:900;font-size:104px;line-height:1;letter-spacing:-4px;{move(11.7,.6,T,'translateY(80px)')}">{h1}<br><span style="color:#009632">{h2}</span></div>
 <div style="position:absolute;left:80px;top:560px;width:600px;color:#00642B;font-weight:600;font-size:46px;line-height:1.3;{move(12.0,.6,T,'translateY(50px)')}">{sub}</div>
 <div style="position:absolute;left:80px;top:850px;background:#009632;color:#fff;font-weight:800;font-size:56px;padding:34px 56px;border-radius:80px;box-shadow:0 14px 0 #00642B;z-index:5;{move(12.3,.6,T,'scale(0)','scale(1)')}">Agende no WhatsApp</div>
 <div style="position:absolute;left:80px;top:1020px;color:#00642B;font-weight:600;font-size:40px;{scene(12.6,T,T)}">(43) 98829-7260</div>
 <img style="position:absolute;right:20px;bottom:220px;height:800px;{move(11.9,.7,T,'translateX(600px)')}" src="{A}/masc_celular.png">
 {foot(INFO)}
</div>''')
    reel(name, T, '\n'.join(b))


# ============ S1 — TER 27/10 — Anvisa proíbe picolé com melatonina ============
short('s1',
      ('Viu essa?', 'Picolé com<br>melatonina?', 104, 'A Anvisa proibiu a venda e o consumo.', 'Anvisa, 26/10/2026', 'masc_prancheta'),
      [('1', 'Picolé “relaxante”', 'Melatonina e inositol não são permitidos em sorvete ou picolé.', 'l', 'masc_aponta'),
       ('2', 'Suplemento de proteína', 'Também proibido: ingrediente sem avaliação de segurança e propaganda irregular.', 'y', 'masc_folha'),
       ('3', 'O que fazer?', 'Não compre nem consuma esses lotes. Dorme mal? Fale com um médico.', 'g', 'masc_joinha')],
      ('Sono ruim', 'tem causa.', 'Consulta com clínico geral em Londrina, sem plano de saúde.'))

# ============ S2 — QUI 29/10 — 2ª dose da vacina da dengue ============
short('s2',
      ('Vacina da dengue', '3 milhões', 190, 'de adolescentes ainda não tomaram a 2ª dose.', 'Ministério da Saúde, out/2026', 'masc_prancheta'),
      [('1', '10 a 14 anos', 'É a faixa que toma a vacina da dengue no SUS.', 'l', 'masc_aponta'),
       ('2', 'São 2 doses', 'A 2ª é 3 meses depois da 1ª. Sem ela, o esquema fica incompleto.', 'y', 'masc_folha'),
       ('3', 'Na UBS, de graça', 'Em Londrina, leve a caderneta à Unidade Básica de Saúde.', 'g', 'masc_joinha')],
      ('Calor e chuva:', 'a dengue volta.', 'Consulta com pediatra ou clínico geral em Londrina, sem plano.'))
