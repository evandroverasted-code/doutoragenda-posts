"""Semana 19 a 25/10/2026 — Outubro Rosa, canetas, jejum, check-up, consultas, dengue, Novembro Azul."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'engine'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from lib import *

SW = '<div class="swipe" style="color:#FFCD00">Arraste para o lado →</div>'

# ============ P1 — SEG 19 — Carrossel Outubro Rosa (6) ============
page('p1_1', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag tagr">Outubro Rosa</div><div class="pg" style="color:#fff">1/6</div>
<div class="h" style="top:190px;font-size:104px;width:700px">Mamografia: <span>quando fazer?</span></div>
<div class="p" style="top:560px;font-size:36px;color:#fff;width:520px;font-weight:400">O que mudou e o que toda mulher precisa saber.</div>
{mascot('masc_apresenta','right:-180px;bottom:130px;height:720px')}{SW}{foot(INFO)}''')
rosa = [
 ('Novidade', 'A partir dos 40 anos', 'Desde 2025, o Ministério da Saúde recomenda que mulheres de 40 a 49 anos possam fazer a mamografia mesmo sem sintomas, em decisão conjunta com o médico.'),
 ('Rastreamento', 'Dos 50 aos 74 anos', 'É a faixa em que o rastreamento regular é indicado. O seu médico define a frequência ideal para você.'),
 ('Atenção', 'Histórico na família?', 'Casos de câncer de mama ou de ovário em parentes próximos podem antecipar os exames. Converse com um especialista.'),
 ('Sinais de alerta', 'Não espere a idade', 'Nódulo, pele repuxada, secreção no mamilo ou mudança no formato da mama: procure um médico em qualquer idade.'),
]
for i, (k, t, d) in enumerate(rosa, start=2):
    page(f'p1_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:-200px"></div>
<div class="tag tagr">Outubro Rosa</div><div class="pg" style="color:#00642B">{i}/6</div>
<div class="card" style="top:190px"><div class="k" style="background:#FDE7F1;color:#C93B7E">{k}</div><h3 style="font-size:{72 if len(t) < 20 else 62}px">{t}</h3><p style="font-size:34px">{d}</p></div>
{mascot('masc_aponta','right:60px;bottom:130px;height:500px;transform:scaleX(-1)')}
<div class="p" style="bottom:200px;top:auto;font-size:32px;color:#00642B;width:560px">Precisa de mamografia ou consulta?<br><b style="color:#009632;font-weight:800">Agende pelo WhatsApp</b></div>
{foot(INFO)}''', bg='l')
page('p1_6', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">6/6</div>
<div class="h" style="top:150px;font-size:86px;width:760px">Cuidar de você <span>não pode esperar.</span></div>
<div class="p" style="top:480px;font-size:34px;color:#fff;width:560px;font-weight:400">Consulta com ginecologista ou mastologista e mamografia em Londrina, sem plano de saúde. Exames com <b style="color:#FFCD00">até 50% de desconto*</b>.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>orçamento grátis</small></div>{foot()}''')

# ============ P2 — TER 20 — Estático Consultas ============
esp = ['Ginecologia', 'Cardiologia', 'Dermatologia', 'Endocrinologia', 'Ortopedia', 'Pediatria']
page('p2', f'''<div class="ringd" style="width:900px;height:900px;left:-300px;top:450px"></div>
<div class="tag">Sem plano de saúde</div>
<div class="h dk" style="top:170px;font-size:92px;width:900px">Consulta com <span>especialista</span> sem plano?</div>
<div class="p" style="top:480px;font-size:36px;color:#00642B;width:520px">Tem, sim. Com preço acessível, aqui em Londrina.</div>
<div style="position:absolute;left:80px;top:600px;width:620px;z-index:4">{''.join(f'<span class="pill">{e}</span>' for e in esp)}<span class="pill" style="background:#00642B;color:#fff">e outras</span></div>
{mascot('masc_celular','right:-60px;bottom:130px;height:760px')}
<div class="cta ctag" style="bottom:200px">Agende pelo WhatsApp<small>link na bio</small></div>{foot('Consultas e exames com preços acessíveis')}''', bg='y')

# ============ R3 — TER 20 noite — Reels Canetas (13s) ============
T = 13
b = ['<div class="ring" style="width:1100px;height:1100px;right:-450px;top:500px"></div>']
b.append(f'''<div class="a" style="position:absolute;left:80px;top:300px;width:920px;{scene(0.1,3.0,T)}">
 <div style="color:#FFCD00;font-weight:800;font-size:64px;{move(0.1,.6,T,'translateY(50px)')}">Pensando em usar</div>
 <div style="color:#fff;font-weight:900;font-size:112px;line-height:1;letter-spacing:-4px;margin-top:16px;{move(0.4,.7,T,'translateY(80px)')}">caneta emagrecedora?</div>
 <div style="color:#fff;font-weight:600;font-size:46px;margin-top:40px;{move(1.2,.6,T,'translateY(40px)')}">Veja 3 cuidados antes.</div></div>
<img style="position:absolute;right:-200px;bottom:200px;height:860px;{scene(0.5,3.0,T)}" src="{A}/masc_prancheta.png">''')
passos = [('1', 'Receita médica', 'A farmácia retém a receita. É regra da Anvisa.', 'l', '#00642B', '#009632', 'masc_folha'),
          ('2', 'Avaliação e exames', 'O médico avalia o seu caso e pode pedir exames antes de começar.', 'y', '#00642B', '#009632', 'masc_prancheta'),
          ('3', 'Acompanhamento', 'Durante o uso, o acompanhamento ajuda a evitar riscos à saúde.', 'g', '#fff', '#FFCD00', 'masc_joinha')]
for i, (n, t, d, bg, fc, nc, im) in enumerate(passos):
    t0 = 3.0 + i * 2.4; t1 = t0 + 2.4
    bgc = {'l': '#E8F5E8', 'y': '#FFCD00', 'g': '#009632'}[bg]
    b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:{bgc};{scene(t0,t1,T,.25)}">
 <div style="position:absolute;left:80px;top:220px;color:{nc};font-weight:900;font-size:420px;line-height:.8;letter-spacing:-14px;transform-origin:left top;{move(t0+.05,.6,T,'scale(.2)','scale(1)')}">{n}</div>
 <div style="position:absolute;left:80px;top:640px;width:900px;color:{fc};font-weight:900;font-size:{104 if len(t) < 13 else 86}px;line-height:1.02;letter-spacing:-3px;{move(t0+.3,.6,T,'translateY(70px)')}">{t}</div>
 <div style="position:absolute;left:80px;top:{780 if len(t) < 16 else 880}px;width:620px;color:{fc};font-weight:600;font-size:46px;line-height:1.3;{move(t0+.5,.6,T,'translateY(50px)')}">{d}</div>
 <img style="position:absolute;right:-110px;bottom:120px;height:780px;{'transform:scaleX(-1);' if im=='masc_aponta' else ''}{move(t0+.2,.7,T,'translateX(700px)', 'scaleX(-1)' if im=='masc_aponta' else 'none')}" src="{A}/{im}.png">
</div>''')
b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#E8F5E8;{scene(10.2,T,T,.3)}">
 <div style="position:absolute;left:80px;top:240px;color:#00642B;font-weight:900;font-size:116px;line-height:1;letter-spacing:-4px;{move(10.3,.6,T,'translateY(80px)')}">Faça do<br><span style="color:#009632">jeito certo.</span></div>
 <div style="position:absolute;left:80px;top:540px;width:600px;color:#00642B;font-weight:600;font-size:46px;line-height:1.3;{move(10.6,.6,T,'translateY(50px)')}">Consulta com endocrinologista e exames em Londrina, sem plano.</div>
 <div style="position:absolute;left:80px;top:820px;background:#009632;color:#fff;font-weight:800;font-size:56px;padding:34px 56px;border-radius:80px;box-shadow:0 14px 0 #00642B;z-index:5;{move(10.9,.6,T,'scale(0)','scale(1)')}">Agende no WhatsApp</div>
 <div style="position:absolute;left:80px;top:990px;color:#00642B;font-weight:600;font-size:40px;{scene(11.2,T,T)}">link na bio</div>
 <img style="position:absolute;right:20px;bottom:220px;height:820px;{move(10.5,.7,T,'translateX(600px)')}" src="{A}/masc_celular.png">
 {foot(INFO)}
</div>''')
reel('r3', T, '\n'.join(b))

# ============ P4 — QUA 21 — Carrossel Mito ou verdade: jejum (6) ============
page('p4_1', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag tagy">Mito ou verdade?</div><div class="pg" style="color:#fff">1/6</div>
<div class="h" style="top:190px;font-size:84px;width:720px">Todo exame de sangue precisa de <span>12 horas de jejum?</span></div>
{mascot('masc_prancheta','right:-170px;bottom:130px;height:700px')}{SW}{foot(INFO)}''')
mv = [('MITO', 'mito', '12 horas de jejum para tudo', 'Cada exame tem a sua regra. E jejum longo demais também pode alterar alguns resultados.'),
      ('VERDADE', 'verd', 'Glicemia pede jejum', 'Para a glicemia, o jejum costuma ser de 8 horas. Confirme sempre com o laboratório.'),
      ('MITO', 'mito', 'Colesterol só em jejum', 'Hoje muitos laboratórios aceitam o exame de colesterol sem jejum, se o médico não pedir o contrário.'),
      ('VERDADE', 'verd', 'Água pode', 'Beber água durante o jejum é liberado, a não ser que haja orientação diferente.')]
for i, (lab, cls, t, d) in enumerate(mv, start=2):
    page(f'p4_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:-200px"></div>
<div class="tag">Mito ou verdade?</div><div class="pg" style="color:#00642B">{i}/6</div>
<div class="card" style="top:190px"><div class="mv {cls}">{lab}</div><h3 style="font-size:{70 if len(t) < 22 else 60}px">{t}</h3><p style="font-size:34px">{d}</p></div>
{mascot('masc_aponta','right:60px;bottom:130px;height:500px;transform:scaleX(-1)')}
<div class="p" style="bottom:200px;top:auto;font-size:32px;color:#00642B;width:560px">Dúvida sobre o preparo?<br><b style="color:#009632;font-weight:800">Fale com a gente no WhatsApp</b></div>
{foot(INFO)}''', bg='l')
page('p4_6', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">6/6</div>
<div class="h" style="top:150px;font-size:80px;width:760px">Já tem o pedido? <span>A gente cuida do resto.</span></div>
<div class="p" style="top:470px;font-size:34px;color:#fff;width:560px;font-weight:400">Orçamento grátis com <b style="color:#FFCD00">até 50% de desconto*</b> e as orientações de preparo do laboratório.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Faça seu orçamento<small>grátis pelo WhatsApp</small></div>{foot()}''')

# ============ P5 — QUI 22 — Carrossel 5 sinais de check-up (7) ============
page('p5_1', f'''<div class="ringd" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag">Check-up</div><div class="pg" style="color:#00642B">1/7</div>
<div class="h dk" style="top:190px;font-size:90px;width:680px">5 sinais de que está na hora do seu <span style="white-space:nowrap">check-up</span></div>
{mascot('masc_aponta','right:-60px;bottom:130px;height:640px;transform:scaleX(-1)')}
<div class="swipe" style="color:#00642B">Arraste para o lado →</div>{foot(INFO)}''', bg='y')
sinais = [('Seu último exame foi há mais de 1 ano', 'Exames de rotina ajudam a acompanhar a sua saúde ao longo do tempo.'),
          ('Cansaço que não passa', 'Pode ter muitas causas. Vale investigar com um médico.'),
          ('Casos na família', 'Pressão alta, diabetes ou doenças do coração em parentes próximos pedem mais atenção.'),
          ('Peso mudou sem explicação', 'Ganhar ou perder peso sem motivo aparente é um sinal para conversar com o médico.'),
          ('Passou dos 40 e nunca fez', 'Com a idade, alguns exames passam a ser recomendados. O médico indica quais.')]
for i, (t, d) in enumerate(sinais, start=2):
    page(f'p5_{i}', f'''<div class="ringd" style="width:800px;height:800px;right:-300px;top:420px"></div>
<div class="tag">Sinal {i-1}</div><div class="pg" style="color:#00642B">{i}/7</div>
<div class="num" style="top:180px;font-size:300px;color:#009632">{i-1}</div>
<div class="h dk" style="top:450px;font-size:{72 if len(t) < 26 else 64}px;width:640px">{t}</div>
<div class="p" style="top:{740 if len(t) < 26 else 800}px;font-size:32px;color:#1f4d2e;width:540px;font-weight:400">{d}</div>
{mascot('masc_folha','right:-120px;bottom:130px;height:600px')}{foot(INFO)}''', bg='l')
page('p5_7', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="pg" style="color:#fff">7/7</div>
<div class="h" style="top:150px;font-size:84px;width:760px">O primeiro passo é uma <span>consulta.</span></div>
<div class="p" style="top:420px;font-size:34px;color:#fff;width:560px;font-weight:400">O clínico geral avalia e pede os exames certos. Depois, a gente faz o orçamento com <b style="color:#FFCD00">até 50% de desconto*</b>.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>consulta e exames sem plano</small></div>{foot()}''')

# ============ R6 — SEX 23 noite — Reels Especialistas (12s) ============
T = 12
b = ['<div class="ring" style="width:1100px;height:1100px;right:-450px;top:600px"></div>']
b.append(f'''<div style="position:absolute;left:80px;top:320px;width:920px;{scene(0.1,2.8,T)}">
 <div style="color:#FFCD00;font-weight:800;font-size:66px;{move(0.1,.6,T,'translateY(50px)')}">Sem plano de saúde?</div>
 <div style="color:#fff;font-weight:900;font-size:128px;line-height:1;letter-spacing:-4px;margin-top:20px;{move(0.4,.7,T,'translateY(80px)')}">Consulta com especialista</div></div>
<img style="position:absolute;right:-220px;bottom:180px;height:820px;{scene(0.5,2.8,T)}" src="{A}/masc_apresenta.png">''')
lista = ['Ginecologia', 'Cardiologia', 'Dermatologia', 'Endocrinologia', 'Ortopedia', 'Pediatria', 'e outras']
pills = ''.join(f'<div style="display:inline-block;background:{"#00642B" if e == "e outras" else "#fff"};color:{"#fff" if e == "e outras" else "#00642B"};font-weight:800;font-size:60px;padding:22px 44px;border-radius:70px;margin:0 0 30px 0;box-shadow:0 10px 0 #00642B;{move(3.0+i*.45,.45,T,"translateX(-1100px)")}">{e}</div><br>' for i, e in enumerate(lista))
b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#FFCD00;{scene(2.8,7.0,T,.25)}">
 <div style="position:absolute;left:80px;top:200px;color:#00642B;font-weight:900;font-size:80px;letter-spacing:-2px;{move(2.9,.5,T,'translateY(50px)')}">Especialidades:</div>
 <div style="position:absolute;left:80px;top:360px">{pills}</div></div>''')
itens = ['Escolha o especialista', 'Veja o valor antes', 'Agende pelo WhatsApp']
check = ''.join(f'<div style="display:flex;align-items:center;gap:30px;margin-bottom:56px;{move(7.2+i*.4,.5,T,"translateX(-900px)")}"><div style="width:110px;height:110px;border-radius:50%;background:#FFCD00;color:#00642B;font-weight:900;font-size:70px;display:flex;align-items:center;justify-content:center">✓</div><div style="color:#fff;font-weight:800;font-size:68px;line-height:1.05">{t}</div></div>' for i, t in enumerate(itens))
b.append(f'''<div style="position:absolute;left:80px;top:420px;width:920px;{scene(7.0,9.4,T)}"><div style="color:#FFCD00;font-weight:800;font-size:60px;margin-bottom:70px">Simples assim:</div>{check}</div>''')
b.append(f'''<div style="position:absolute;left:0;top:0;width:1080px;height:1920px;background:#E8F5E8;{scene(9.4,T,T,.3)}">
 <div style="position:absolute;left:80px;top:250px;color:#00642B;font-weight:900;font-size:120px;line-height:1;letter-spacing:-4px;{move(9.5,.6,T,'translateY(80px)')}">Agende sua<br><span style="color:#009632">consulta</span></div>
 <div style="position:absolute;left:80px;top:560px;width:560px;color:#00642B;font-weight:600;font-size:46px;line-height:1.3;{move(9.8,.6,T,'translateY(50px)')}">Em Londrina, com preço acessível.</div>
 <div style="position:absolute;left:80px;top:760px;background:#009632;color:#fff;font-weight:800;font-size:58px;padding:34px 56px;border-radius:80px;box-shadow:0 14px 0 #00642B;z-index:5;{move(10.0,.6,T,'scale(0)','scale(1)')}">Chame no WhatsApp</div>
 <div style="position:absolute;left:80px;top:930px;color:#00642B;font-weight:600;font-size:40px;{scene(10.3,T,T)}">link na bio</div>
 <img style="position:absolute;right:20px;bottom:220px;height:820px;{move(9.7,.7,T,'translateX(600px)')}" src="{A}/masc_celular.png">
 {foot('Consultas e exames com preços acessíveis')}
</div>''')
reel('r6', T, '\n'.join(b))

# ============ P7 — SÁB 24 — Estático Dengue ============
page('p7', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag tagy">Alerta dengue</div>
<div class="h" style="top:170px;font-size:92px;width:900px">Calor e chuva: <span>a dengue volta.</span></div>
<div class="card" style="top:420px;right:330px;padding:36px 42px"><div class="k">Sinais de alerta</div>
<p style="font-size:31px;margin-top:4px">Febre alta, dor atrás dos olhos, dor no corpo e manchas na pele.</p>
<p style="font-size:31px;font-weight:700;color:#00642B">Não se automedique: procure atendimento.</p></div>
<div class="p" style="top:940px;font-size:32px;color:#fff;width:600px;font-weight:400"><b style="color:#FFCD00">10 minutos por semana</b> eliminando água parada já fazem diferença.</div>
{mascot('masc_aponta','right:-90px;bottom:130px;height:640px;transform:scaleX(-1)')}
<div class="cta" style="bottom:170px">Consulta com clínico geral<small>agende pelo WhatsApp</small></div>{foot(INFO)}''')

# ============ P8 — DOM 25 — Estático Novembro Azul ============
page('p8', f'''<div class="ring" style="width:900px;height:900px;right:-330px;top:300px"></div>
<div class="tag" style="background:#1E6FD9">Novembro Azul</div>
<div class="h" style="top:170px;font-size:84px;width:900px">Homem também <span>faz check-up.</span></div>
<div class="p" style="top:400px;font-size:34px;color:#fff;width:560px;font-weight:400">Novembro Azul está chegando. Converse com um urologista sobre o momento certo para o exame de próstata e faça seus exames de rotina.</div>
{mascot('masc_joinha','right:-170px;bottom:130px;height:640px')}
<div class="cta" style="bottom:200px">Agende pelo WhatsApp<small>consulta e exames sem plano</small></div>{foot()}''', bg='dg')
print('ok')
