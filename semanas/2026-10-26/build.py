"""Semana 26/10 a 01/11/2026 — Outubro Rosa (encerramento), pressão 12x8, suplementos x resistência à insulina (alerta Anvisa),
colesterol, Dia Mundial do AVC (29/10), oferta de exames, onda de calor, início do Novembro Azul."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'engine'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from lib import *

SW = '<div class="swipe" style="color:#FFCD00">Arraste para o lado →</div>'

# ============ P1 — SEG 26 — Carrossel Outubro Rosa: cuidados da mulher (6) ============
page('p1_1', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag tagr">Outubro Rosa</div><div class="pg" style="color:#fff">1/6</div>
<div class="h" style="top:190px;font-size:96px;width:700px">Outubro acaba. <span>O cuidado, não.</span></div>
<div class="p" style="top:620px;font-size:36px;color:#fff;width:500px;font-weight:400">4 cuidados com a saúde da mulher para o ano todo.</div>
{mascot('masc_apresenta','right:-180px;bottom:130px;height:720px')}{SW}{foot(INFO)}''')
mulher = [
 ('Todo ano', 'Consulta com o ginecologista', 'É nela que o médico avalia a sua saúde e indica os exames certos para a sua idade.'),
 ('Colo do útero', 'Exame preventivo', 'Indicado para mulheres de 25 a 64 anos. O médico orienta a frequência ideal para você.'),
 ('Mamas', 'Mamografia', 'A partir dos 40 anos, em decisão conjunta com o médico. Dos 50 aos 74, o rastreamento regular é indicado.'),
 ('No dia a dia', 'Conheça o seu corpo', 'Notou algo diferente nas mamas, como nódulo ou secreção? Procure um médico, em qualquer idade.'),
]
for i, (k, t, d) in enumerate(mulher, start=2):
    page(f'p1_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:-200px"></div>
<div class="tag tagr">Outubro Rosa</div><div class="pg" style="color:#00642B">{i}/6</div>
<div class="card" style="top:190px"><div class="k" style="background:#FDE7F1;color:#C93B7E">{k}</div><h3 style="font-size:{72 if len(t) < 20 else 62}px">{t}</h3><p style="font-size:34px">{d}</p></div>
{mascot('masc_aponta','right:60px;bottom:130px;height:500px;transform:scaleX(-1)')}
<div class="p" style="bottom:200px;top:auto;font-size:32px;color:#00642B;width:560px">Consulta ou exame sem plano?<br><b style="color:#009632;font-weight:800">Agende pelo WhatsApp</b></div>
{foot(INFO)}''', bg='l')
page('p1_6', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">6/6</div>
<div class="h" style="top:150px;font-size:84px;width:760px">Marque o seu cuidado <span>de novembro.</span></div>
<div class="p" style="top:480px;font-size:34px;color:#fff;width:560px;font-weight:400">Consulta com ginecologista e exames em Londrina, sem plano de saúde. Exames com <b style="color:#FFCD00">até 50% de desconto*</b>.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>orçamento grátis</small></div>{foot()}''')

# ============ P2 — TER 27 — Estático Pressão 12 por 8 (consultas) ============
page('p2', f'''<div class="ringd" style="width:900px;height:900px;right:-330px;top:-260px"></div>
<div class="tag">Pressão arterial</div>
<div class="num" style="top:190px;font-size:250px;color:#009632;letter-spacing:-10px">12 por 8</div>
<div class="h dk" style="top:480px;font-size:76px;width:900px">agora é<br><span style="white-space:nowrap">pré‑hipertensão.</span></div>
<div class="p" style="top:680px;font-size:33px;color:#1f4d2e;width:560px;font-weight:400">Pela nova diretriz brasileira (2025), a pressão normal é <b style="color:#00642B">abaixo de 12 por 8</b>. Descobrir cedo ajuda a cuidar antes que vire hipertensão.</div>
{mascot('masc_prancheta','right:-210px;bottom:130px;height:620px')}
<div class="cta ctag" style="bottom:200px">Consulta com cardiologista<small>agende pelo WhatsApp</small></div>{foot(INFO)}''', bg='l')

# ============ R3 — TER 27 noite — Reels Suplementos x resistência à insulina (13s) ============
T = 13
b = ['<div class="ring" style="width:1100px;height:1100px;right:-450px;top:500px"></div>']
b.append(f'''<div class="a" style="position:absolute;left:80px;top:300px;width:920px;{scene(0.1,3.0,T)}">
 <div style="color:#FFCD00;font-weight:800;font-size:60px;{move(0.1,.6,T,'translateY(50px)')}">Viu vídeo dizendo que</div>
 <div style="color:#fff;font-weight:900;font-size:100px;line-height:1.02;letter-spacing:-4px;margin-top:16px;{move(0.4,.7,T,'translateY(80px)')}">suplemento trata resistência à insulina?</div>
 <div style="color:#fff;font-weight:600;font-size:46px;margin-top:40px;{move(1.2,.6,T,'translateY(40px)')}">Veja o alerta da Anvisa.</div></div>
<img style="position:absolute;right:-200px;bottom:200px;height:760px;{scene(0.5,3.0,T)}" src="{A}/masc_prancheta.png">''')
passos = [('1', 'Alerta da Anvisa', 'Não há comprovação de que suplementos tratem resistência à insulina.', 'l', '#00642B', '#009632', 'masc_folha'),
          ('2', 'Avaliação médica', 'O endocrinologista avalia o seu caso e pode pedir exames.', 'y', '#00642B', '#009632', 'masc_prancheta'),
          ('3', 'Hábitos contam', 'Alimentação e atividade física são a base do cuidado.', 'g', '#fff', '#FFCD00', 'masc_joinha')]
for i, (n, t, d, bg, fc, nc, im) in enumerate(passos):
    t0 = 3.0 + i * 2.4; t1 = t0 + 2.4
    bgc = {'l': '#E8F5E8', 'y': '#FFCD00', 'g': '#009632'}[bg]
    b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:{bgc};{scene(t0,t1,T,.25)}">
 <div style="position:absolute;left:80px;top:220px;color:{nc};font-weight:900;font-size:420px;line-height:.8;letter-spacing:-14px;transform-origin:left top;{move(t0+.05,.6,T,'scale(.2)','scale(1)')}">{n}</div>
 <div style="position:absolute;left:80px;top:640px;width:900px;color:{fc};font-weight:900;font-size:{104 if len(t) < 13 else 86}px;line-height:1.02;letter-spacing:-3px;{move(t0+.3,.6,T,'translateY(70px)')}">{t}</div>
 <div style="position:absolute;left:80px;top:{780 if len(t) < 16 else 800}px;width:600px;color:{fc};font-weight:600;font-size:46px;line-height:1.3;{move(t0+.5,.6,T,'translateY(50px)')}">{d}</div>
 <img style="position:absolute;right:-180px;bottom:120px;height:700px;{move(t0+.2,.7,T,'translateX(700px)')}" src="{A}/{im}.png">
</div>''')
b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#E8F5E8;{scene(10.2,T,T,.3)}">
 <div style="position:absolute;left:80px;top:240px;color:#00642B;font-weight:900;font-size:116px;line-height:1;letter-spacing:-4px;{move(10.3,.6,T,'translateY(80px)')}">Cuide com<br><span style="color:#009632">quem entende.</span></div>
 <div style="position:absolute;left:80px;top:540px;width:600px;color:#00642B;font-weight:600;font-size:46px;line-height:1.3;{move(10.6,.6,T,'translateY(50px)')}">Consulta com endocrinologista e exames em Londrina, sem plano.</div>
 <div style="position:absolute;left:80px;top:820px;background:#009632;color:#fff;font-weight:800;font-size:56px;padding:34px 56px;border-radius:80px;box-shadow:0 14px 0 #00642B;z-index:5;{move(10.9,.6,T,'scale(0)','scale(1)')}">Agende no WhatsApp</div>
 <div style="position:absolute;left:80px;top:990px;color:#00642B;font-weight:600;font-size:40px;{scene(11.2,T,T)}">link na bio</div>
 <img style="position:absolute;right:20px;bottom:220px;height:820px;{move(10.5,.7,T,'translateX(600px)')}" src="{A}/masc_celular.png">
 {foot(INFO)}
</div>''')
reel('r3', T, '\n'.join(b))

# ============ P4 — QUA 28 — Carrossel Mito ou verdade: colesterol (6) ============
page('p4_1', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag tagy">Mito ou verdade?</div><div class="pg" style="color:#fff">1/6</div>
<div class="h" style="top:190px;font-size:96px;width:700px">Colesterol alto: <span>o que é mito?</span></div>
<div class="p" style="top:620px;font-size:36px;color:#fff;width:500px;font-weight:400">4 frases que todo mundo já ouviu.</div>
{mascot('masc_prancheta','right:-170px;bottom:130px;height:700px')}{SW}{foot(INFO)}''')
mv = [('MITO', 'mito', 'Magro não tem colesterol alto', 'O peso não conta a história toda. Genética e hábitos também pesam. Só o exame de sangue mostra.'),
      ('VERDADE', 'verd', 'Costuma não dar sintomas', 'Na maioria das vezes, o colesterol alto é silencioso. Por isso os exames de rotina são importantes.'),
      ('MITO', 'mito', 'Só idoso precisa medir', 'Adultos de várias idades podem precisar do exame. O médico indica quando e com que frequência.'),
      ('VERDADE', 'verd', 'Família pesa', 'Casos de colesterol alto ou doença do coração na família pedem mais atenção. Conte isso ao seu médico.')]
for i, (lab, cls, t, d) in enumerate(mv, start=2):
    page(f'p4_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:-200px"></div>
<div class="tag">Mito ou verdade?</div><div class="pg" style="color:#00642B">{i}/6</div>
<div class="card" style="top:190px"><div class="mv {cls}">{lab}</div><h3 style="font-size:{70 if len(t) < 22 else 60}px">{t}</h3><p style="font-size:34px">{d}</p></div>
{mascot('masc_aponta','right:60px;bottom:130px;height:500px;transform:scaleX(-1)')}
<div class="p" style="bottom:200px;top:auto;font-size:32px;color:#00642B;width:560px">Faz tempo que não mede?<br><b style="color:#009632;font-weight:800">Orçamento grátis no WhatsApp</b></div>
{foot(INFO)}''', bg='l')
page('p4_6', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">6/6</div>
<div class="h" style="top:150px;font-size:80px;width:760px">Tem o pedido? <span>A gente faz o orçamento.</span></div>
<div class="p" style="top:470px;font-size:34px;color:#fff;width:560px;font-weight:400">Exames de colesterol e outros exames de sangue com <b style="color:#FFCD00">até 50% de desconto*</b>, aqui em Londrina.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Faça seu orçamento<small>grátis pelo WhatsApp</small></div>{foot()}''')

# ============ P5 — QUI 29 — Carrossel Dia Mundial do AVC: SAMU (7) ============
page('p5_1', f'''<div class="ringd" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag">29/10 · Dia Mundial do AVC</div><div class="pg" style="color:#00642B">1/7</div>
<div class="h dk" style="top:190px;font-size:86px;width:700px">Reconheça um AVC com a palavra <span>SAMU</span></div>
<div class="p" style="top:560px;font-size:34px;color:#00642B;width:480px">Salve este post. Ele pode ajudar alguém.</div>
{mascot('masc_aponta','right:-60px;bottom:130px;height:640px;transform:scaleX(-1)')}
<div class="swipe" style="color:#00642B">Arraste para o lado →</div>{foot(INFO)}''', bg='y')
samu = [('S', 'Sorria', 'Peça para a pessoa sorrir. Veja se um lado do rosto fica torto ou caído.'),
        ('A', 'Abrace', 'Peça para levantar os dois braços. Veja se um deles cai ou fica fraco.'),
        ('M', 'Música', 'Peça para cantar ou repetir uma frase simples. Veja se a fala sai enrolada.'),
        ('U', 'Urgente', 'Notou algum sinal? Ligue 192 na hora. No AVC, cada minuto conta.')]
for i, (l, t, d) in enumerate(samu, start=2):
    page(f'p5_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:420px"></div>
<div class="tag">Sinal de AVC</div><div class="pg" style="color:#00642B">{i}/7</div>
<div class="num" style="top:180px;font-size:300px;color:#009632">{l}</div>
<div class="h dk" style="top:450px;font-size:96px;width:640px">{t}</div>
<div class="p" style="top:580px;font-size:34px;color:#1f4d2e;width:540px;font-weight:{700 if l == 'U' else 400}">{d}</div>
{mascot('masc_folha','right:-120px;bottom:130px;height:600px')}{foot(INFO)}''', bg='l')
fat = ['Pressão alta', 'Diabetes', 'Colesterol alto', 'Cigarro', 'Obesidade']
page('p5_6', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:420px"></div>
<div class="tag">Prevenção</div><div class="pg" style="color:#00642B">6/7</div>
<div class="h dk" style="top:180px;font-size:76px;width:900px">Controlar estes fatores ajuda a <span>prevenir o AVC:</span></div>
<div style="position:absolute;left:80px;top:430px;width:560px;z-index:4">{''.join(f'<span class="pill" style="font-size:34px">{e}</span>' for e in fat)}</div>
<div class="p" style="top:760px;font-size:32px;color:#1f4d2e;width:520px;font-weight:400">Muitos deles não dão sinais. Só a consulta e os exames de rotina mostram.</div>
{mascot('masc_prancheta','right:-230px;bottom:130px;height:560px')}{foot(INFO)}''', bg='l')
page('p5_7', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">7/7</div>
<div class="h" style="top:150px;font-size:84px;width:760px">Prevenir começa no <span>check-up.</span></div>
<div class="p" style="top:420px;font-size:34px;color:#fff;width:560px;font-weight:400">Consulta com clínico geral ou cardiologista e exames com <b style="color:#FFCD00">até 50% de desconto*</b>, sem plano de saúde.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>consulta e exames sem plano</small></div>{foot()}''')

# ============ R6 — SEX 30 noite — Reels Oferta de exames (12s) ============
T = 12
b = ['<div class="ring" style="width:1100px;height:1100px;right:-450px;top:600px"></div>']
b.append(f'''<div style="position:absolute;left:80px;top:320px;width:920px;{scene(0.1,2.8,T)}">
 <div style="color:#FFCD00;font-weight:800;font-size:66px;{move(0.1,.6,T,'translateY(50px)')}">Pedido de exame</div>
 <div style="color:#fff;font-weight:900;font-size:128px;line-height:1;letter-spacing:-4px;margin-top:20px;{move(0.4,.7,T,'translateY(80px)')}">parado na gaveta?</div></div>
<img style="position:absolute;right:-200px;bottom:180px;height:820px;{scene(0.5,2.8,T)}" src="{A}/masc_prancheta.png">''')
b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#FFCD00;{scene(2.8,7.0,T,.25)}">
 <div style="position:absolute;left:80px;top:220px;color:#00642B;font-weight:800;font-size:70px;{move(2.9,.5,T,'translateY(50px)')}">Exames com</div>
 <div style="position:absolute;left:60px;top:300px;color:#009632;font-weight:900;font-size:300px;line-height:1;letter-spacing:-14px;transform-origin:left center;{move(3.2,.7,T,'scale(.2)','scale(1)')}">até<br>50%*</div>
 <div style="position:absolute;left:80px;top:950px;color:#00642B;font-weight:800;font-size:70px;{move(3.8,.5,T,'translateY(50px)')}">de desconto</div>
 <div style="position:absolute;left:80px;top:1060px;width:560px;color:#00642B;font-weight:600;font-size:34px;{move(4.1,.5,T,'translateY(30px)')}">*em relação ao preço particular de tabela</div>
 <img style="position:absolute;right:-200px;bottom:120px;height:700px;{move(3.4,.7,T,'translateX(700px)')}" src="{A}/masc_joinha.png">
</div>''')
itens = ['Mande a foto do pedido', 'Receba o orçamento grátis', 'Agende o seu exame']
check = ''.join(f'<div style="display:flex;align-items:center;gap:30px;margin-bottom:56px;{move(7.2+i*.4,.5,T,"translateX(-900px)")}"><div style="flex:none;width:110px;height:110px;border-radius:50%;background:#FFCD00;color:#00642B;font-weight:900;font-size:70px;display:flex;align-items:center;justify-content:center">✓</div><div style="color:#fff;font-weight:800;font-size:66px;line-height:1.05">{t}</div></div>' for i, t in enumerate(itens))
b.append(f'''<div style="position:absolute;left:80px;top:420px;width:920px;{scene(7.0,9.4,T)}"><div style="color:#FFCD00;font-weight:800;font-size:60px;margin-bottom:70px">Simples assim:</div>{check}</div>''')
b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#E8F5E8;{scene(9.4,T,T,.3)}">
 <div style="position:absolute;left:80px;top:250px;color:#00642B;font-weight:900;font-size:120px;line-height:1;letter-spacing:-4px;{move(9.5,.6,T,'translateY(80px)')}">Faça seu<br><span style="color:#009632">orçamento</span></div>
 <div style="position:absolute;left:80px;top:560px;width:560px;color:#00642B;font-weight:600;font-size:46px;line-height:1.3;{move(9.8,.6,T,'translateY(50px)')}">Em Londrina, sem plano de saúde.</div>
 <div style="position:absolute;left:80px;top:760px;background:#009632;color:#fff;font-weight:800;font-size:58px;padding:34px 56px;border-radius:80px;box-shadow:0 14px 0 #00642B;z-index:5;{move(10.0,.6,T,'scale(0)','scale(1)')}">Chame no WhatsApp</div>
 <div style="position:absolute;left:80px;top:930px;color:#00642B;font-weight:600;font-size:40px;{scene(10.3,T,T)}">link na bio</div>
 <img style="position:absolute;right:20px;bottom:220px;height:820px;{move(9.7,.7,T,'translateX(600px)')}" src="{A}/masc_celular.png">
 {foot()}
</div>''')
reel('r6', T, '\n'.join(b))

# ============ P7 — SÁB 31 — Estático Onda de calor ============
page('p7', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag tagy">Alerta de calor</div>
<div class="h" style="top:170px;font-size:88px;width:900px">Dias de calorão: <span style="white-space:nowrap">cuide‑se.</span></div>
<div class="card" style="top:420px;right:330px;padding:36px 42px"><div class="k">3 cuidados</div>
<p style="font-size:31px;margin-top:4px">💧 Beba água, mesmo sem sede.</p>
<p style="font-size:31px">☀️ Evite sol forte nas horas mais quentes.</p>
<p style="font-size:31px">👵 Atenção a crianças, idosos e quem tem doença crônica.</p></div>
<div class="p" style="top:900px;font-size:32px;color:#fff;width:600px;font-weight:400">Confusão ou desmaio: <b style="color:#FFCD00">procure atendimento</b> na hora.</div>
{mascot('masc_aponta','right:-90px;bottom:130px;height:640px;transform:scaleX(-1)')}
<div class="cta" style="bottom:170px">Consulta com clínico geral<small>agende pelo WhatsApp</small></div>{foot(INFO)}''')

# ============ P8 — DOM 01/11 — Estático Começou o Novembro Azul ============
it = ['Consulta com urologista', 'Pressão', 'Glicemia', 'Colesterol']
page('p8', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag" style="background:#1E6FD9">Novembro Azul</div>
<div class="h" style="top:170px;font-size:92px;width:900px">Começou o <span>Novembro Azul.</span></div>
<div class="p" style="top:400px;font-size:34px;color:#fff;width:560px;font-weight:400">Homem, a sua vez de se cuidar:</div>
<div style="position:absolute;left:80px;top:480px;width:560px;z-index:4">{''.join(f'<span class="pill">{e}</span>' for e in it)}</div>
<div class="p" style="top:790px;font-size:32px;color:#fff;width:540px;font-weight:400">Converse com o urologista sobre o exame de próstata e o momento certo para você.</div>
{mascot('masc_apresenta','right:-200px;bottom:130px;height:660px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>consulta e exames sem plano</small></div>{foot(INFO)}''', bg='dg')
print('ok')
