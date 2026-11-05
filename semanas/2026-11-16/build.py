"""Semana 16 a 22/11/2026 — Novembro Roxo: prematuridade (seg), mito ou verdade: PSA (qua),
Reels oferta: feche o ano com o check-up em dia (sex)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'engine'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from lib import *

SW = '<div class="swipe" style="color:#FFCD00">Arraste para o lado →</div>'
ROXO = '#7B3FB5'   # Novembro Roxo: só em detalhe (tag)
AZUL = '#1E6FD9'   # Novembro Azul: só em detalhe (tag)
TAGR = f'<div class="tag" style="background:{ROXO}">Novembro Roxo</div>'
TAGA = f'<div class="tag" style="background:{AZUL}">Novembro Azul</div>'

# ============ P1 — SEG 16 — Carrossel Novembro Roxo: prematuridade (6) ============
page('p1_1', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
{TAGR}<div class="pg" style="color:#fff">1/6</div>
<div class="h" style="top:190px;font-size:84px;width:720px">Bebê prematuro: <span>o cuidado continua em casa.</span></div>
<div class="p" style="top:640px;font-size:34px;color:#fff;width:460px;font-weight:400">17/11 é o Dia Mundial da Prematuridade. 4 pontos para saber.</div>
{mascot('masc_apresenta','right:-200px;bottom:130px;height:700px')}{SW}{foot(INFO)}''')
itens = [
 ('O que é', 'Antes das 37 semanas', 'É considerado prematuro o bebê que nasce antes das 37 semanas de gestação.'),
 ('Gravidez', 'Pré-natal desde o início', 'Acompanhar a gestação com o médico desde o começo é o primeiro cuidado.'),
 ('Depois da alta', 'Acompanhamento', 'Crescimento, alimentação, respiração e desenvolvimento seguem sendo acompanhados.'),
 ('Sinal de atenção', 'Pele amarelada', 'A icterícia foi a principal causa de volta ao hospital nos primeiros 30 dias. Na dúvida, procure o pediatra.'),
]
for i, (k, t, d) in enumerate(itens, start=2):
    page(f'p1_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:-200px"></div>
{TAGR}<div class="pg" style="color:#00642B">{i}/6</div>
<div class="card" style="top:190px"><div class="k" style="background:#EFE5F8;color:{ROXO}">{k}</div><h3 style="font-size:{72 if len(t) < 20 else 60}px">{t}</h3><p style="font-size:34px">{d}</p></div>
{mascot('masc_aponta','right:60px;bottom:130px;height:480px;transform:scaleX(-1)')}
<div class="p" style="bottom:200px;top:auto;font-size:32px;color:#00642B;width:560px">Pediatra ou obstetra sem plano?<br><b style="color:#009632;font-weight:800">Agende pelo WhatsApp</b></div>
{foot(INFO)}''', bg='l')
page('p1_6', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">6/6</div>
<div class="h" style="top:150px;font-size:84px;width:760px">Cuidar cedo <span>faz diferença.</span></div>
<div class="p" style="top:400px;font-size:34px;color:#fff;width:540px;font-weight:400">Consulta com ginecologista/obstetra ou pediatra em Londrina, sem plano de saúde. Exames com <b style="color:#FFCD00">até 50% de desconto*</b>.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>consulta e exames sem plano</small></div>{foot()}''')

# ============ P2 — QUA 18 — Carrossel Mito ou verdade: PSA (6) ============
page('p2_1', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag tagy">Mito ou verdade?</div><div class="pg" style="color:#fff">1/6</div>
<div class="h" style="top:190px;font-size:84px;width:720px">Exame de PSA: <span>o que é mito e o que é verdade?</span></div>
<div class="p" style="top:640px;font-size:36px;color:#fff;width:460px;font-weight:400">4 dúvidas do Novembro Azul.</div>
{mascot('masc_prancheta','right:-170px;bottom:130px;height:700px')}{SW}{foot(INFO)}''')
mv = [('MITO', 'mito', 'PSA alto é sempre câncer', 'Outras alterações da próstata, como o aumento benigno e inflamações, também podem elevar o PSA.'),
      ('VERDADE', 'verd', 'É um exame de sangue', 'O PSA é medido numa coleta de sangue comum. Confirme o preparo com o laboratório.'),
      ('MITO', 'mito', 'Todo homem já aos 30', 'A SBU recomenda conversar com o urologista a partir dos 50 anos, ou dos 45 para negros e quem tem caso na família.'),
      ('VERDADE', 'verd', 'O médico define a frequência', 'Pode ser todo ano ou a cada alguns anos. Quem decide com você é o urologista.')]
for i, (lab, cls, t, d) in enumerate(mv, start=2):
    page(f'p2_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:-200px"></div>
{TAGA}<div class="pg" style="color:#00642B">{i}/6</div>
<div class="card" style="top:190px"><div class="mv {cls}">{lab}</div><h3 style="font-size:{70 if len(t) < 22 else 58}px">{t}</h3><p style="font-size:34px">{d}</p></div>
{mascot('masc_aponta','right:60px;bottom:130px;height:480px;transform:scaleX(-1)')}
<div class="p" style="bottom:200px;top:auto;font-size:32px;color:#00642B;width:560px">Exames com até 50% de desconto*<br><b style="color:#009632;font-weight:800">Orçamento grátis no WhatsApp</b></div>
{foot()}''', bg='l')
page('p2_6', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">6/6</div>
<div class="h" style="top:150px;font-size:80px;width:760px">Urologista e PSA <span>sem plano de saúde.</span></div>
<div class="p" style="top:470px;font-size:34px;color:#fff;width:520px;font-weight:400">Consulta em Londrina e exames com <b style="color:#FFCD00">até 50% de desconto*</b>.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:620px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>consulta e orçamento grátis</small></div>{foot()}''')

# ============ R3 — SEX 20 noite — Reels oferta: feche o ano com o check-up em dia (13s) ============
T = 13
b = ['<div class="ring" style="width:1100px;height:1100px;right:-450px;top:500px"></div>']
b.append(f'''<div style="position:absolute;left:80px;top:280px;width:920px;{scene(0.1,3.0,T)}">
 <div style="color:#FFCD00;font-weight:800;font-size:60px;{move(0.1,.6,T,'translateY(50px)')}">O ano está acabando.</div>
 <div style="color:#fff;font-weight:900;font-size:112px;line-height:.98;letter-spacing:-4px;margin-top:14px;width:760px;{move(0.4,.7,T,'translateY(80px)')}">E o seu check-up?</div>
 <div style="color:#fff;font-weight:700;font-size:56px;line-height:1.15;width:600px;margin-top:30px;{move(1.0,.6,T,'translateY(40px)')}">Exames com até 50% de desconto*</div>
 <div style="color:#B8D8B0;font-weight:600;font-size:32px;margin-top:30px;width:620px;{move(1.4,.5,T,'translateY(30px)')}">Londrina, sem plano de saúde</div></div>
<img style="position:absolute;right:-220px;bottom:200px;height:780px;{scene(0.5,3.0,T)}" src="{A}/masc_prancheta.png">''')
passos = [('1', 'Pedido em mãos', 'Tem o pedido médico? Tire uma foto. Não tem? Agende uma consulta.', 'l', 'masc_aponta'),
          ('2', 'Mande no WhatsApp', 'Envie a foto do pedido para o Doutor Agenda.', 'y', 'masc_folha'),
          ('3', 'Orçamento grátis', 'Você recebe o orçamento e escolhe onde e quando fazer.', 'g', 'masc_joinha')]
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
 <div style="position:absolute;left:80px;top:240px;color:#00642B;font-weight:900;font-size:108px;line-height:1;letter-spacing:-4px;{move(10.3,.6,T,'translateY(80px)')}">Comece 2027<br><span style="color:#009632">em dia.</span></div>
 <div style="position:absolute;left:80px;top:540px;width:600px;color:#00642B;font-weight:600;font-size:46px;line-height:1.3;{move(10.6,.6,T,'translateY(50px)')}">Exames com até 50% de desconto* em Londrina.</div>
 <div style="position:absolute;left:80px;top:820px;background:#009632;color:#fff;font-weight:800;font-size:56px;padding:34px 56px;border-radius:80px;box-shadow:0 14px 0 #00642B;z-index:5;{move(10.9,.6,T,'scale(0)','scale(1)')}">Peça seu orçamento</div>
 <div style="position:absolute;left:80px;top:990px;color:#00642B;font-weight:600;font-size:40px;{scene(11.2,T,T)}">no WhatsApp · link na bio</div>
 <img style="position:absolute;right:20px;bottom:220px;height:820px;{move(10.5,.7,T,'translateX(600px)')}" src="{A}/masc_celular.png">
 {foot()}
</div>''')
reel('r3', T, '\n'.join(b))
print('ok')
