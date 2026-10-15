"""Gera posts.json (calendário + legendas) da semana 26/10 a 01/11/2026."""
import json, os, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))

WA = '📲 WhatsApp oficial: (43) 98829-7260, ou toque no link da bio'
D = '*em relação ao preço particular de tabela.'
INFO = 'Conteúdo informativo, não substitui consulta médica.'

def files(prefix):
    return sorted(os.path.basename(f) for f in glob.glob(f'out/{prefix}*') if f.endswith(('.png', '.mp4')))

posts = [
 dict(id='p1', data='2026-10-26', turno='manha', tipo='carrossel', tema='Outubro Rosa — 4 cuidados da mulher', arquivos=files('p1_'),
      legenda=f"""Outubro acaba. O cuidado, não 🎀

4 cuidados com a saúde da mulher para o ano todo 👇

1️⃣ Consulta com o ginecologista: é nela que o médico avalia a sua saúde e indica os exames certos para a sua idade
2️⃣ Exame preventivo do colo do útero: indicado para mulheres de 25 a 64 anos, na frequência que o médico orientar
3️⃣ Mamografia: a partir dos 40 anos, em decisão conjunta com o médico; dos 50 aos 74, o rastreamento regular é indicado
4️⃣ Conheça o seu corpo: notou nódulo, secreção ou qualquer mudança nas mamas? Procure um médico, em qualquer idade

Sem plano de saúde? Agende sua consulta com ginecologista e faça seus exames em Londrina, com até 50% de desconto* nos exames. Envie o código ORG-MULHER-1026.
{WA}

Compartilhe com uma mulher que você ama 💗
{INFO}
{D}"""),
 dict(id='p2', data='2026-10-27', turno='manha', tipo='imagem', tema='Pressão 12 por 8 é pré-hipertensão (consultas)', arquivos=files('p2'),
      legenda=f"""12 por 8 não é mais considerada pressão normal 🩺

Pela Diretriz Brasileira de Hipertensão Arterial 2025 (Sociedade Brasileira de Cardiologia, de Nefrologia e de Hipertensão), a pressão normal é abaixo de 12 por 8. Quem está nessa faixa entra como pré-hipertensão.

A ideia é descobrir cedo e cuidar antes que vire hipertensão. Pressão alta muitas vezes não dá sintomas, por isso medir e acompanhar com um médico faz diferença.

Sem plano de saúde? Agende sua consulta com cardiologista ou clínico geral em Londrina, com preço acessível. Envie o código ORG-PRESSAO-1027.
{WA}

{INFO}"""),
 dict(id='r3', data='2026-10-27', turno='noite', tipo='reels', tema='Suplementos não tratam resistência à insulina (alerta Anvisa)', arquivos=files('r3'),
      legenda=f"""Viu vídeo dizendo que suplemento trata resistência à insulina? Calma 👇

⚠️ Em outubro, a Anvisa alertou para vídeos nas redes que indicam suplementos (como berberina, magnésio e mio-inositol) para tratar resistência à insulina. Segundo a agência, não há comprovação de que funcionem como tratamento, e trocar o tratamento por suplemento pode ser perigoso.

O caminho seguro:
1️⃣ Avaliação com um médico, como o endocrinologista
2️⃣ Exames, se o médico pedir
3️⃣ Alimentação e atividade física, que são a base do cuidado

Cuide com quem entende: consulta com endocrinologista e exames em Londrina, sem plano de saúde. Envie o código ORG-INSULINA-1027.
{WA}

{INFO}"""),
 dict(id='p4', data='2026-10-28', turno='manha', tipo='carrossel', tema='Mito ou verdade — colesterol', arquivos=files('p4_'),
      legenda=f"""Colesterol alto: o que é mito e o que é verdade? 🤔

❌ MITO: magro não tem colesterol alto. Genética e hábitos também pesam, e só o exame de sangue mostra
✅ VERDADE: costuma não dar sintomas. Por isso os exames de rotina são importantes
❌ MITO: só idoso precisa medir. O médico indica quando e com que frequência fazer o exame
✅ VERDADE: histórico na família pesa. Conte ao seu médico se há casos de colesterol alto ou doença do coração

Já tem o pedido médico? Faça seu orçamento grátis com até 50% de desconto* nos exames. Envie o código ORG-COLEST-1028.
{WA}

Salve e mande para quem diz que "não precisa" 📌
{INFO}
{D}"""),
 dict(id='p5', data='2026-10-29', turno='manha', tipo='carrossel', tema='Dia Mundial do AVC — sinais (SAMU)', arquivos=files('p5_'),
      legenda=f"""Hoje, 29 de outubro, é o Dia Mundial do AVC. Saber reconhecer os sinais pode salvar uma vida 🧠

Lembre da palavra SAMU 👇
S: Sorria. Um lado do rosto fica torto ou caído?
A: Abrace. Ao levantar os dois braços, um deles cai ou fica fraco?
M: Música. Ao cantar ou repetir uma frase, a fala sai enrolada?
U: Urgente. Notou algum sinal? Ligue 192 na hora. No AVC, cada minuto conta.

Pressão alta, diabetes, colesterol alto, cigarro e obesidade aumentam o risco. Muitos deles não dão sinais, e só a consulta e os exames de rotina mostram.

Prevenir começa no check-up: consulta com clínico geral ou cardiologista e exames com até 50% de desconto*, sem plano de saúde. Envie o código ORG-AVC-1029.
{WA}

Salve este post e compartilhe. Ele pode ajudar alguém 🙏
{INFO}
{D}"""),
 dict(id='r6', data='2026-10-30', turno='noite', tipo='reels', tema='Oferta — exames com até 50%*', arquivos=files('r6'),
      legenda=f"""Pedido de exame parado na gaveta? 📄

Exames com até 50% de desconto* em Londrina, sem plano de saúde. Simples assim:
✔️ Mande a foto do pedido no WhatsApp
✔️ Receba o orçamento grátis
✔️ Agende o seu exame

Envie o código ORG-EXAMES-1030.
{WA}

{D}"""),
 dict(id='p7', data='2026-10-31', turno='manha', tipo='imagem', tema='Onda de calor — cuidados', arquivos=files('p7'),
      legenda=f"""Dias de calorão: cuide-se ☀️

Os meteorologistas alertam para mais ondas de calor até o fim do ano. Na nossa região, vale reforçar os cuidados:
💧 Beba água ao longo do dia, mesmo sem sede
☀️ Evite sol forte e atividade física intensa nas horas mais quentes
👵 Atenção redobrada com crianças, idosos, gestantes e quem tem doença crônica

Confusão, desmaio ou mal-estar forte: procure atendimento na hora.

Precisa de consulta com clínico geral sem plano de saúde? Agende pelo WhatsApp. Envie o código ORG-CALOR-1031.
{WA}

{INFO}"""),
 dict(id='p8', data='2026-11-01', turno='manha', tipo='imagem', tema='Começou o Novembro Azul', arquivos=files('p8'),
      legenda=f"""Começou o Novembro Azul 💙

Homem, a sua vez de se cuidar:
✅ Consulta com urologista
✅ Pressão em dia
✅ Glicemia e colesterol em dia

Converse com o urologista sobre o exame de próstata e o momento certo para você.

Consulta e exames sem plano de saúde em Londrina, com até 50% de desconto* nos exames. Envie o código ORG-AZUL-1101.
{WA}

Marque um homem que precisa desse lembrete 👊
{INFO}
{D}"""),
]
# Instagram: máximo 5 hashtags por post (regra desde dez/2025). Ranking em HASHTAGS.md.
TAGS = {
 'p1': '#londrina #londrinapr #outubrorosa #mamografia #saudedamulher',
 'p2': '#londrina #londrinando #cardiologia #consultamedica #saudeemprimeirolugar',
 'r3': '#londrina #londrinapr #endocrinologia #exameslaboratoriais #clinicamedica',
 'p4': '#londrina #londrinando #exames #exameslaboratoriais #examesderotina',
 'p5': '#londrina #londrinaofficial #cardiologia #medicinapreventiva #checkup',
 'r6': '#londrina #londrinapr #exames #laboratorioclinico #exameslaboratoriais',
 'p7': '#londrina #londrinando #saudepublica #clinicamedica #prevencao',
 'p8': '#londrina #londrinapr #novembroazul #saudedohomem #urologia',
}
for p in posts:
    linhas = [l for l in p['legenda'].rstrip().split('\n') if not l.startswith('#')]
    p['legenda'] = '\n'.join(linhas).rstrip() + '\n\n' + TAGS[p['id']]
    assert p['legenda'].count('#') == 5, p['id']
for p in posts:
    assert p['arquivos'], p['id']
    assert len(p['legenda']) <= 2200, (p['id'], len(p['legenda']))
    p['publicado'] = {'instagram': None, 'facebook': None}

cal = dict(
    semana='2026-10-26',
    status='pendente',          # pendente | aprovado — só publica se 'aprovado'
    instagram_account_id='17841410873155652',   # @doutoragenda (Zapier: Instagram for Business)
    facebook_page_id='2018258928221781',        # página Doutor Agenda (Zapier: Facebook Pages)
    base_url='https://raw.githubusercontent.com/evandroverasted-code/doutoragenda-posts/main/semanas/2026-10-26/out/',
    turnos={'manha': '11:52', 'noite': '18:52'},
    posts=posts)
json.dump(cal, open('posts.json', 'w'), ensure_ascii=False, indent=1)
for p in posts:
    print(p['id'], p['data'], p['turno'], p['tipo'], len(p['arquivos']), 'arquivos', len(p['legenda']), 'chars')
