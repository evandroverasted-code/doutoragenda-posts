"""Semana 02 a 08/11/2026 — Novembro Azul (próstata), skincare de rede social, fake news de saúde,
mito ou verdade diabetes, check-up do homem, consultas sem plano, sarampo, lembrete Novembro Azul."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'engine'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from lib import *

SW = '<div class="swipe" style="color:#FFCD00">Arraste para o lado →</div>'
AZUL = '#1E6FD9'   # Novembro Azul: só em detalhe (tag)
TAGA = f'<div class="tag" style="background:{AZUL}">Novembro Azul</div>'

# ============ P1 — SEG 02 — Carrossel Novembro Azul: quando conversar com o urologista (6) ============
page('p1_1', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
{TAGA}<div class="pg" style="color:#fff">1/6</div>
<div class="h" style="top:190px;font-size:84px;width:720px">Próstata: <span>quando conversar com o urologista?</span></div>
<div class="p" style="top:580px;font-size:34px;color:#fff;width:460px;font-weight:400">O que todo homem precisa saber neste Novembro Azul.</div>
{mascot('masc_apresenta','right:-200px;bottom:130px;height:700px')}{SW}{foot(INFO)}''')
azul = [
 ('A partir dos 50', 'Mesmo sem sintomas', 'A Sociedade Brasileira de Urologia orienta que, a partir dos 50 anos, o homem procure um urologista para uma avaliação individual.'),
 ('Mais cedo: 45 anos', 'Se você tem mais risco', 'Homens negros ou com pai ou irmão que teve câncer de próstata devem começar essa conversa aos 45 anos.'),
 ('Decisão em conjunto', 'PSA e toque: converse', 'O médico explica os riscos e os benefícios dos exames e decide com você o que faz sentido no seu caso.'),
 ('Sinais de alerta', 'Não espere a idade', 'Dificuldade para urinar, jato fraco, vontade de urinar muitas vezes ou sangue na urina: procure um médico.'),
]
for i, (k, t, d) in enumerate(azul, start=2):
    page(f'p1_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:-200px"></div>
{TAGA}<div class="pg" style="color:#00642B">{i}/6</div>
<div class="card" style="top:190px"><div class="k" style="background:#E3EEFC;color:{AZUL}">{k}</div><h3 style="font-size:{72 if len(t) < 20 else 62}px">{t}</h3><p style="font-size:34px">{d}</p></div>
{mascot('masc_aponta','right:60px;bottom:130px;height:480px;transform:scaleX(-1)')}
<div class="p" style="bottom:200px;top:auto;font-size:32px;color:#00642B;width:560px">Consulta com urologista sem plano?<br><b style="color:#009632;font-weight:800">Agende pelo WhatsApp</b></div>
{foot(INFO)}''', bg='l')
page('p1_6', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">6/6</div>
<div class="h" style="top:150px;font-size:86px;width:760px">Cuidar da saúde <span>também é coisa de homem.</span></div>
<div class="p" style="top:520px;font-size:34px;color:#fff;width:540px;font-weight:400">Consulta com urologista em Londrina, sem plano de saúde. Exames com <b style="color:#FFCD00">até 50% de desconto*</b>.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>orçamento grátis</small></div>{foot()}''')

# ============ P2 — TER 03 — Estático Skincare de rede social x dermatologista (consultas) ============
page('p2', f'''<div class="ringd" style="width:900px;height:900px;left:-300px;top:450px"></div>
<div class="tag">Sem plano de saúde</div>
<div class="h dk" style="top:170px;font-size:88px;width:900px">Skincare de 10 passos <span>que viu na internet?</span></div>
<div class="p" style="top:500px;font-size:34px;color:#00642B;width:560px">Produto demais pode irritar a pele. Quem monta a rotina certa para você é o <b style="color:#009632">dermatologista</b>.</div>
<div style="position:absolute;left:80px;top:760px;width:600px;z-index:4"><span class="pill">Acne</span><span class="pill">Manchas</span><span class="pill">Pintas</span><span class="pill">Queda de cabelo</span><span class="pill" style="background:#00642B;color:#fff">e mais</span></div>
{mascot('masc_celular','right:-60px;bottom:130px;height:760px')}
<div class="cta ctag" style="bottom:200px">Consulta com dermatologista<small>agende pelo WhatsApp</small></div>{foot(INFO)}''', bg='y')

# ============ R3 — TER 03 noite — Reels Fake news de saúde (13s) ============
T = 13
b = ['<div class="ring" style="width:1100px;height:1100px;right:-450px;top:500px"></div>']
b.append(f'''<div style="position:absolute;left:80px;top:280px;width:920px;{scene(0.1,3.0,T)}">
 <div style="color:#FFCD00;font-weight:800;font-size:60px;{move(0.1,.6,T,'translateY(50px)')}">Viu no WhatsApp?</div>
 <div style="color:#fff;font-weight:900;font-size:250px;line-height:1;letter-spacing:-10px;margin-top:10px;{move(0.4,.7,T,'scale(.3)','scale(1)')}">87%</div>
 <div style="color:#fff;font-weight:700;font-size:56px;line-height:1.15;width:640px;margin-top:20px;{move(1.0,.6,T,'translateY(40px)')}">dos conteúdos virais de saúde analisados eram falsos.</div>
 <div style="color:#B8D8B0;font-weight:600;font-size:32px;margin-top:30px;{move(1.4,.5,T,'translateY(30px)')}">Levantamento da Agência Lupa, out/2026</div></div>
<img style="position:absolute;right:-220px;bottom:200px;height:820px;{scene(0.5,3.0,T)}" src="{A}/masc_prancheta.png">''')
passos = [('1', 'Desconfie de milagre', 'Cura rápida, sem esforço e “que os médicos escondem”? Sinal de alerta.', 'l', '#00642B', '#009632', 'masc_aponta'),
          ('2', 'Olhe a fonte', 'Ex.: a Anvisa lembrou que a ashwagandha não é permitida em suplementos no Brasil.', 'y', '#00642B', '#009632', 'masc_folha'),
          ('3', 'Pergunte a um especialista', 'Antes de comprar ou mudar algo, converse com um médico.', 'g', '#fff', '#FFCD00', 'masc_joinha')]
for i, (n, t, d, bg, fc, nc, im) in enumerate(passos):
    t0 = 3.0 + i * 2.4; t1 = t0 + 2.4
    bgc = {'l': '#E8F5E8', 'y': '#FFCD00', 'g': '#009632'}[bg]
    fl = im == 'masc_aponta'
    b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:{bgc};{scene(t0,t1,T,.25)}">
 <div style="position:absolute;left:80px;top:220px;color:{nc};font-weight:900;font-size:420px;line-height:.8;letter-spacing:-14px;transform-origin:left top;{move(t0+.05,.6,T,'scale(.2)','scale(1)')}">{n}</div>
 <div style="position:absolute;left:80px;top:640px;width:900px;color:{fc};font-weight:900;font-size:{100 if len(t) < 16 else 84}px;line-height:1.02;letter-spacing:-3px;{move(t0+.3,.6,T,'translateY(70px)')}">{t}</div>
 <div style="position:absolute;left:80px;top:{780 if len(t) < 16 else 880}px;width:600px;color:{fc};font-weight:600;font-size:46px;line-height:1.3;{move(t0+.5,.6,T,'translateY(50px)')}">{d}</div>
 <img style="position:absolute;right:{0 if im == 'masc_aponta' else -110}px;bottom:120px;height:{760 if im == 'masc_aponta' else 740}px;{'transform:scaleX(-1);' if fl else ''}{move(t0+.2,.7,T,'translateX(700px)' + (' scaleX(-1)' if fl else ''), 'scaleX(-1)' if fl else 'none')}" src="{A}/{im}.png">
</div>''')
b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#E8F5E8;{scene(10.2,T,T,.3)}">
 <div style="position:absolute;left:80px;top:240px;color:#00642B;font-weight:900;font-size:112px;line-height:1;letter-spacing:-4px;{move(10.3,.6,T,'translateY(80px)')}">Na dúvida,<br><span style="color:#009632">pergunte.</span></div>
 <div style="position:absolute;left:80px;top:540px;width:600px;color:#00642B;font-weight:600;font-size:46px;line-height:1.3;{move(10.6,.6,T,'translateY(50px)')}">Consulta com especialista em Londrina, sem plano.</div>
 <div style="position:absolute;left:80px;top:820px;background:#009632;color:#fff;font-weight:800;font-size:56px;padding:34px 56px;border-radius:80px;box-shadow:0 14px 0 #00642B;z-index:5;{move(10.9,.6,T,'scale(0)','scale(1)')}">Agende no WhatsApp</div>
 <div style="position:absolute;left:80px;top:990px;color:#00642B;font-weight:600;font-size:40px;{scene(11.2,T,T)}">link na bio</div>
 <img style="position:absolute;right:20px;bottom:220px;height:820px;{move(10.5,.7,T,'translateX(600px)')}" src="{A}/masc_celular.png">
 {foot(INFO)}
</div>''')
reel('r3', T, '\n'.join(b))

# ============ P4 — QUA 04 — Carrossel Mito ou verdade: diabetes (6) ============
page('p4_1', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag tagy">Mito ou verdade?</div><div class="pg" style="color:#fff">1/6</div>
<div class="h" style="top:190px;font-size:90px;width:720px">Diabetes <span>sempre dá sintomas?</span></div>
<div class="p" style="top:620px;font-size:36px;color:#fff;width:480px;font-weight:400">4 dúvidas comuns, respondidas.</div>
{mascot('masc_prancheta','right:-170px;bottom:130px;height:700px')}{SW}{foot(INFO)}''')
mv = [('MITO', 'mito', 'Sempre dá sintomas', 'Pode passar anos em silêncio. Cerca de 1 em cada 3 pessoas com diabetes não sabe que tem.'),
      ('VERDADE', 'verd', 'Exame de sangue ajuda a descobrir', 'Glicemia de jejum e hemoglobina glicada estão entre os exames que o médico pode pedir.'),
      ('MITO', 'mito', 'Só quem come muito doce tem', 'Histórico na família, excesso de peso, sedentarismo e idade também contam.'),
      ('VERDADE', 'verd', 'Muita sede é sinal de alerta', 'Sede excessiva, urinar muito, visão embaçada e perda de peso sem motivo pedem consulta.')]
for i, (lab, cls, t, d) in enumerate(mv, start=2):
    page(f'p4_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:-200px"></div>
<div class="tag">Mito ou verdade?</div><div class="pg" style="color:#00642B">{i}/6</div>
<div class="card" style="top:190px"><div class="mv {cls}">{lab}</div><h3 style="font-size:{70 if len(t) < 22 else 58}px">{t}</h3><p style="font-size:34px">{d}</p></div>
{mascot('masc_aponta','right:60px;bottom:130px;height:480px;transform:scaleX(-1)')}
<div class="p" style="bottom:200px;top:auto;font-size:32px;color:#00642B;width:560px">Exames com até 50% de desconto*<br><b style="color:#009632;font-weight:800">Orçamento grátis no WhatsApp</b></div>
{foot()}''', bg='l')
page('p4_6', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">6/6</div>
<div class="h" style="top:150px;font-size:70px;width:760px">14/11 é o Dia Mundial do Diabetes. <span>Sua glicemia está em dia?</span></div>
<div class="p" style="top:480px;font-size:34px;color:#fff;width:520px;font-weight:400">Consulta com clínico geral ou endocrinologista e exames com <b style="color:#FFCD00">até 50% de desconto*</b>.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:620px')}
<div class="cta" style="bottom:200px">Faça seu orçamento<small>grátis pelo WhatsApp</small></div>{foot()}''')

# ============ P5 — QUI 05 — Carrossel Check-up do homem (7) ============
page('p5_1', f'''<div class="ringd" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag" style="background:{AZUL}">Novembro Azul</div><div class="pg" style="color:#00642B">1/7</div>
<div class="h dk" style="top:190px;font-size:90px;width:680px">Check-up do homem: <span>5 exames que o médico pode pedir</span></div>
{mascot('masc_aponta','right:-60px;bottom:130px;height:640px;transform:scaleX(-1)')}
<div class="swipe" style="color:#00642B">Salve este post 📌</div>{foot(INFO)}''', bg='y')
ex = [('Glicemia', 'Mostra o nível de açúcar no sangue e ajuda a investigar o diabetes.'),
      ('Colesterol e triglicerídeos', 'Gorduras no sangue ligadas à saúde do coração.'),
      ('Hemograma', 'Avalia as células do sangue, como glóbulos vermelhos e brancos.'),
      ('Creatinina', 'Ajuda a avaliar como estão funcionando os rins.'),
      ('PSA', 'Exame de sangue da próstata. Pedido depois da conversa com o médico sobre riscos e benefícios.')]
for i, (t, d) in enumerate(ex, start=2):
    page(f'p5_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:420px"></div>
<div class="tag">Exame {i-1}</div><div class="pg" style="color:#00642B">{i}/7</div>
<div class="num" style="top:180px;font-size:300px;color:#009632">{i-1}</div>
<div class="h dk" style="top:450px;font-size:{80 if len(t) < 14 else 66}px;width:640px">{t}</div>
<div class="p" style="top:{580 if len(t) < 14 else 660}px;font-size:34px;color:#1f4d2e;width:540px;font-weight:400">{d}</div>
{mascot('masc_folha','right:-120px;bottom:130px;height:560px')}{foot(INFO)}''', bg='l')
page('p5_7', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">7/7</div>
<div class="h" style="top:150px;font-size:84px;width:760px">Quem define os exames é o <span>seu médico.</span></div>
<div class="p" style="top:420px;font-size:34px;color:#fff;width:560px;font-weight:400">Consulta com clínico geral ou urologista sem plano. Com o pedido em mãos, orçamento com <b style="color:#FFCD00">até 50% de desconto*</b>.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>consulta e exames sem plano</small></div>{foot()}''')

# ============ R6 — SEX 06 noite — Reels Consulta sem plano: veja o valor antes (12s) ============
T = 12
b = ['<div class="ring" style="width:1100px;height:1100px;right:-450px;top:600px"></div>']
b.append(f'''<div style="position:absolute;left:80px;top:320px;width:920px;{scene(0.1,2.8,T)}">
 <div style="color:#FFCD00;font-weight:800;font-size:66px;{move(0.1,.6,T,'translateY(50px)')}">Sem plano de saúde?</div>
 <div style="color:#fff;font-weight:900;font-size:120px;line-height:1;letter-spacing:-4px;margin-top:20px;width:700px;{move(0.4,.7,T,'translateY(80px)')}">Você vê o valor antes.</div>
 <div style="color:#fff;font-weight:600;font-size:46px;margin-top:40px;width:560px;{move(1.2,.6,T,'translateY(40px)')}">Consulta com especialista em Londrina.</div></div>
<img style="position:absolute;right:-220px;bottom:180px;height:820px;{scene(0.5,2.8,T)}" src="{A}/masc_apresenta.png">''')
lista = ['Urologia', 'Dermatologia', 'Endocrinologia', 'Cardiologia', 'Ginecologia', 'Clínico geral', 'e outras']
pills = ''.join(f'<div style="display:inline-block;background:{"#00642B" if e == "e outras" else "#fff"};color:{"#fff" if e == "e outras" else "#00642B"};font-weight:800;font-size:60px;padding:22px 44px;border-radius:70px;margin:0 0 30px 0;box-shadow:0 10px 0 #00642B;{move(3.0+i*.45,.45,T,"translateX(-1100px)")}">{e}</div><br>' for i, e in enumerate(lista))
b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#FFCD00;{scene(2.8,7.0,T,.25)}">
 <div style="position:absolute;left:80px;top:200px;color:#00642B;font-weight:900;font-size:80px;letter-spacing:-2px;{move(2.9,.5,T,'translateY(50px)')}">Especialidades:</div>
 <div style="position:absolute;left:80px;top:360px">{pills}</div></div>''')
itens = ['Chame no WhatsApp', 'Escolha o especialista', 'Veja o valor e agende']
check = ''.join(f'<div style="display:flex;align-items:center;gap:30px;margin-bottom:56px;{move(7.2+i*.4,.5,T,"translateX(-900px)")}"><div style="width:110px;height:110px;flex:none;border-radius:50%;background:#FFCD00;color:#00642B;font-weight:900;font-size:70px;display:flex;align-items:center;justify-content:center">{i+1}</div><div style="color:#fff;font-weight:800;font-size:66px;line-height:1.05">{t}</div></div>' for i, t in enumerate(itens))
b.append(f'''<div style="position:absolute;left:80px;top:420px;width:920px;{scene(7.0,9.4,T)}"><div style="color:#FFCD00;font-weight:800;font-size:60px;margin-bottom:70px">Como funciona:</div>{check}</div>''')
b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#E8F5E8;{scene(9.4,T,T,.3)}">
 <div style="position:absolute;left:80px;top:250px;color:#00642B;font-weight:900;font-size:120px;line-height:1;letter-spacing:-4px;{move(9.5,.6,T,'translateY(80px)')}">Agende sua<br><span style="color:#009632">consulta</span></div>
 <div style="position:absolute;left:80px;top:560px;width:560px;color:#00642B;font-weight:600;font-size:46px;line-height:1.3;{move(9.8,.6,T,'translateY(50px)')}">E faça seus exames com até 50% de desconto*.</div>
 <div style="position:absolute;left:80px;top:820px;background:#009632;color:#fff;font-weight:800;font-size:58px;padding:34px 56px;border-radius:80px;box-shadow:0 14px 0 #00642B;z-index:5;{move(10.0,.6,T,'scale(0)','scale(1)')}">Chame no WhatsApp</div>
 <div style="position:absolute;left:80px;top:990px;color:#00642B;font-weight:600;font-size:40px;{scene(10.3,T,T)}">link na bio</div>
 <img style="position:absolute;right:20px;bottom:220px;height:820px;{move(9.7,.7,T,'translateX(600px)')}" src="{A}/masc_celular.png">
 {foot()}
</div>''')
reel('r6', T, '\n'.join(b))

# ============ P7 — SÁB 07 — Estático Sarampo: caderneta em dia ============
page('p7', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag tagy">Alerta sarampo</div>
<div class="h" style="top:170px;font-size:90px;width:900px">Sua vacina contra o sarampo <span>está em dia?</span></div>
<div class="card" style="top:470px;right:330px;padding:36px 42px"><div class="k">Fique de olho</div>
<p style="font-size:31px;margin-top:4px">O Brasil teve 52 casos em 2026, todos trazidos de outros países, e reforçou a vigilância.</p>
<p style="font-size:31px;font-weight:700;color:#00642B">A vacina é gratuita no SUS: confira a caderneta na UBS.</p></div>
{mascot('masc_aponta','right:-90px;bottom:130px;height:640px;transform:scaleX(-1)')}
<div class="cta" style="bottom:200px">Consulta com clínico ou pediatra<small>agende pelo WhatsApp</small></div>{foot(INFO)}''')

# ============ P8 — DOM 08 — Estático "Manda pro homem da sua vida" (Novembro Azul leve) ============
page('p8', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag" style="background:{AZUL}">Novembro Azul</div>
<div class="h" style="top:170px;font-size:82px;width:900px">Manda para o homem <span>que vive adiando o médico.</span></div>
<div class="img" style="z-index:3;left:80px;top:460px;width:580px">
 <div style="background:#fff;border-radius:30px 30px 30px 8px;padding:22px 28px;font-size:32px;color:#1f4d2e;font-weight:600;margin-bottom:20px;box-shadow:0 8px 0 rgba(0,0,0,.15)">Pai, já marcou o urologista? 💙</div>
 <div style="background:#fff;border-radius:30px 30px 30px 8px;padding:22px 28px;font-size:32px;color:#1f4d2e;font-weight:600;margin-bottom:20px;box-shadow:0 8px 0 rgba(0,0,0,.15)">Dá para agendar pelo WhatsApp, sem plano de saúde.</div>
 <div style="background:#FFCD00;border-radius:30px 30px 8px 30px;padding:22px 28px;font-size:32px;color:#00642B;font-weight:700;margin-left:60px;box-shadow:0 8px 0 rgba(0,0,0,.15)">Tá bom, vou marcar essa semana! 👍</div>
</div>
{mascot('masc_celular','right:-40px;bottom:130px;height:700px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>consulta sem plano de saúde</small></div>{foot(INFO)}''', bg='dg')
print('ok')
