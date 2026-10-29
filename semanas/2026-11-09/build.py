"""Semana 09 a 15/11/2026 — Novembro Azul além da próstata (seg), mito ou verdade: jejum para exame de sangue (qua),
Reels trend de parar o protetor solar x dermatologista (sex)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'engine'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from lib import *

SW = '<div class="swipe" style="color:#FFCD00">Arraste para o lado →</div>'
AZUL = '#1E6FD9'   # Novembro Azul: só em detalhe (tag)
TAGA = f'<div class="tag" style="background:{AZUL}">Novembro Azul</div>'

# ============ P1 — SEG 09 — Carrossel Novembro Azul: saúde do homem vai além da próstata (6) ============
page('p1_1', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
{TAGA}<div class="pg" style="color:#fff">1/6</div>
<div class="h" style="top:190px;font-size:86px;width:720px">Novembro Azul <span>não é só próstata.</span></div>
<div class="p" style="top:520px;font-size:34px;color:#fff;width:460px;font-weight:400">4 cuidados que todo homem deveria ter no radar.</div>
{mascot('masc_apresenta','right:-200px;bottom:130px;height:700px')}{SW}{foot(INFO)}''')
itens = [
 ('Dado', 'Homem vai menos ao médico', '69% dos homens consultaram um médico em 1 ano. Entre as mulheres, 82% (PNS/IBGE).'),
 ('Pressão', 'Pressão alta', 'Muitas vezes não dá sintomas. Medir a pressão faz parte de uma consulta simples.'),
 ('Glicose e peso', 'Diabetes e obesidade', 'Estão entre os cuidados contínuos que o Ministério da Saúde destaca para os homens.'),
 ('Cabeça também', 'Saúde mental', 'Ansiedade, estresse e tristeza que não passa também são assunto para o médico.'),
]
for i, (k, t, d) in enumerate(itens, start=2):
    page(f'p1_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:-200px"></div>
{TAGA}<div class="pg" style="color:#00642B">{i}/6</div>
<div class="card" style="top:190px"><div class="k" style="background:#E3EEFC;color:{AZUL}">{k}</div><h3 style="font-size:{72 if len(t) < 20 else 62}px">{t}</h3><p style="font-size:34px">{d}</p></div>
{mascot('masc_aponta','right:60px;bottom:130px;height:480px;transform:scaleX(-1)')}
<div class="p" style="bottom:200px;top:auto;font-size:32px;color:#00642B;width:560px">Consulta sem plano de saúde?<br><b style="color:#009632;font-weight:800">Agende pelo WhatsApp</b></div>
{foot(INFO)}''', bg='l')
page('p1_6', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">6/6</div>
<div class="h" style="top:150px;font-size:84px;width:760px">Uma consulta por ano <span>já é um começo.</span></div>
<div class="p" style="top:450px;font-size:34px;color:#fff;width:540px;font-weight:400">Clínico geral ou urologista em Londrina, sem plano de saúde. Exames com <b style="color:#FFCD00">até 50% de desconto*</b>.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>consulta e exames sem plano</small></div>{foot()}''')

# ============ P2 — QUA 11 — Carrossel Mito ou verdade: jejum para exame de sangue (6) ============
page('p2_1', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag tagy">Mito ou verdade?</div><div class="pg" style="color:#fff">1/6</div>
<div class="h" style="top:190px;font-size:84px;width:720px">Exame de sangue: <span>precisa mesmo de 12h de jejum?</span></div>
<div class="p" style="top:640px;font-size:36px;color:#fff;width:460px;font-weight:400">4 dúvidas comuns, respondidas.</div>
{mascot('masc_prancheta','right:-170px;bottom:130px;height:700px')}{SW}{foot(INFO)}''')
mv = [('MITO', 'mito', 'Colesterol sempre pede 12h de jejum', 'Desde 2016, sociedades médicas brasileiras deixaram de exigir jejum para colesterol e triglicerídeos na maioria dos casos.'),
      ('VERDADE', 'verd', 'Glicemia de jejum pede 8 horas', 'Para a glicemia de jejum, o mínimo de 8 horas continua valendo.'),
      ('MITO', 'mito', 'Quanto mais jejum, melhor', 'Jejum acima de 16 horas não é recomendado para a maioria dos exames.'),
      ('VERDADE', 'verd', 'Glicada pode ser sem jejum', 'A hemoglobina glicada pode ser feita sem jejum. Na dúvida, confirme o preparo com o médico ou o laboratório.')]
for i, (lab, cls, t, d) in enumerate(mv, start=2):
    page(f'p2_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:-200px"></div>
<div class="tag">Mito ou verdade?</div><div class="pg" style="color:#00642B">{i}/6</div>
<div class="card" style="top:190px"><div class="mv {cls}">{lab}</div><h3 style="font-size:{70 if len(t) < 22 else 58}px">{t}</h3><p style="font-size:34px">{d}</p></div>
{mascot('masc_aponta','right:60px;bottom:130px;height:480px;transform:scaleX(-1)')}
<div class="p" style="bottom:200px;top:auto;font-size:32px;color:#00642B;width:560px">Exames com até 50% de desconto*<br><b style="color:#009632;font-weight:800">Orçamento grátis no WhatsApp</b></div>
{foot()}''', bg='l')
page('p2_6', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">6/6</div>
<div class="h" style="top:150px;font-size:80px;width:760px">Pedido médico em mãos? <span>Faça seu orçamento.</span></div>
<div class="p" style="top:470px;font-size:34px;color:#fff;width:520px;font-weight:400">Exames em Londrina, sem plano de saúde, com <b style="color:#FFCD00">até 50% de desconto*</b>.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:620px')}
<div class="cta" style="bottom:200px">Faça seu orçamento<small>grátis pelo WhatsApp</small></div>{foot()}''')

# ============ R3 — SEX 13 noite — Reels: trend de parar o protetor solar (13s) ============
T = 13
b = ['<div class="ring" style="width:1100px;height:1100px;right:-450px;top:500px"></div>']
b.append(f'''<div style="position:absolute;left:80px;top:280px;width:920px;{scene(0.1,3.0,T)}">
 <div style="color:#FFCD00;font-weight:800;font-size:60px;{move(0.1,.6,T,'translateY(50px)')}">Trend nas redes:</div>
 <div style="color:#fff;font-weight:900;font-size:112px;line-height:.98;letter-spacing:-4px;margin-top:14px;width:760px;{move(0.4,.7,T,'translateY(80px)')}">parar de usar protetor solar?</div>
 <div style="color:#fff;font-weight:700;font-size:56px;line-height:1.15;width:600px;margin-top:30px;{move(1.0,.6,T,'translateY(40px)')}">Não caia nessa.</div>
 <div style="color:#B8D8B0;font-weight:600;font-size:32px;margin-top:30px;width:620px;{move(1.4,.5,T,'translateY(30px)')}">O câncer de pele não melanoma é o mais comum no Brasil (INCA)</div></div>
<img style="position:absolute;right:-220px;bottom:200px;height:780px;{scene(0.5,3.0,T)}" src="{A}/masc_prancheta.png">''')
passos = [('1', 'Protetor todo dia', 'FPS 15 ou mais. Reaplique a cada 2 horas, mesmo com tempo nublado.', 'l', 'masc_aponta'),
          ('2', 'Fuja do sol forte', 'Entre 10h e 16h, procure sombra. Chapéu e óculos ajudam.', 'y', 'masc_folha'),
          ('3', 'Olho nas pintas', 'Mudou de tamanho, forma ou cor, coça ou sangra? Procure um dermatologista.', 'g', 'masc_joinha')]
for i, (n, t, d, bg, im) in enumerate(passos):
    t0 = 3.0 + i * 2.4; t1 = t0 + 2.4
    bgc = {'l': '#E8F5E8', 'y': '#FFCD00', 'g': '#009632'}[bg]
    fc = '#fff' if bg == 'g' else '#00642B'
    nc = '#FFCD00' if bg == 'g' else '#009632'
    fl = im == 'masc_aponta'
    b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:{bgc};{scene(t0,t1,T,.25)}">
 <div style="position:absolute;left:80px;top:220px;color:{nc};font-weight:900;font-size:420px;line-height:.8;letter-spacing:-14px;transform-origin:left top;{move(t0+.05,.6,T,'scale(.2)','scale(1)')}">{n}</div>
 <div style="position:absolute;left:80px;top:640px;width:900px;color:{fc}">
  <div style="font-weight:900;font-size:{84 if len(t) >= 16 else 100}px;line-height:1.02;letter-spacing:-3px;{move(t0+.3,.6,T,'translateY(70px)')}">{t}</div>
  <div style="width:580px;margin-top:36px;font-weight:600;font-size:46px;line-height:1.3;{move(t0+.5,.6,T,'translateY(50px)')}">{d}</div>
 </div>
 <img style="position:absolute;right:{0 if fl else -110}px;bottom:120px;height:{700 if fl else 680}px;{'transform:scaleX(-1);' if fl else ''}{move(t0+.2,.7,T,'translateX(700px)' + (' scaleX(-1)' if fl else ''), 'scaleX(-1)' if fl else 'none')}" src="{A}/{im}.png">
</div>''')
b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#E8F5E8;{scene(10.2,T,T,.3)}">
 <div style="position:absolute;left:80px;top:240px;color:#00642B;font-weight:900;font-size:108px;line-height:1;letter-spacing:-4px;{move(10.3,.6,T,'translateY(80px)')}">Pinta estranha?<br><span style="color:#009632">Dermatologista.</span></div>
 <div style="position:absolute;left:80px;top:540px;width:600px;color:#00642B;font-weight:600;font-size:46px;line-height:1.3;{move(10.6,.6,T,'translateY(50px)')}">Consulta em Londrina, sem plano de saúde.</div>
 <div style="position:absolute;left:80px;top:820px;background:#009632;color:#fff;font-weight:800;font-size:56px;padding:34px 56px;border-radius:80px;box-shadow:0 14px 0 #00642B;z-index:5;{move(10.9,.6,T,'scale(0)','scale(1)')}">Agende no WhatsApp</div>
 <div style="position:absolute;left:80px;top:990px;color:#00642B;font-weight:600;font-size:40px;{scene(11.2,T,T)}">link na bio</div>
 <img style="position:absolute;right:20px;bottom:220px;height:820px;{move(10.5,.7,T,'translateX(600px)')}" src="{A}/masc_celular.png">
 {foot(INFO)}
</div>''')
reel('r3', T, '\n'.join(b))
print('ok')
