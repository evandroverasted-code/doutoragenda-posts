"""Gera posts.json (calendário + legendas) da semana 19 a 25/10/2026."""
import json, os, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))

WA = '📲 WhatsApp oficial: (43) 98829-7260, ou toque no link da bio'
D = '*em relação ao preço particular de tabela.'
INFO = 'Conteúdo informativo, não substitui consulta médica.'
H = '#londrina #londrinapr #norteparana #semplanodesaude #saudeacessivel #doutoragenda'

def files(prefix):
    return sorted(os.path.basename(f) for f in glob.glob(f'out/{prefix}*') if f.endswith(('.png', '.mp4')))

posts = [
 dict(id='p1', data='2026-10-19', turno='manha', tipo='carrossel', tema='Outubro Rosa — mamografia', arquivos=files('p1_'),
      legenda=f"""Mamografia: quando fazer? 🎀 Neste Outubro Rosa, a gente explica 👇

✅ A partir dos 40 anos, você já pode fazer a mamografia, mesmo sem sintomas, em decisão conjunta com o médico (recomendação do Ministério da Saúde desde 2025)
✅ Dos 50 aos 74 anos, o rastreamento regular é indicado
✅ Histórico de câncer de mama ou ovário na família pede atenção antes
⚠️ Nódulo, pele repuxada ou secreção no mamilo: procure um médico em qualquer idade

Sem plano de saúde? Agende sua consulta com ginecologista ou mastologista e faça sua mamografia em Londrina. Exames com até 50% de desconto*.
{WA}

Compartilhe com uma mulher que você ama 💗
{INFO}
{D}

{H} #outubrorosa #mamografia #saudedamulher #prevencao"""),
 dict(id='p2', data='2026-10-20', turno='manha', tipo='imagem', tema='Consultas com especialista', arquivos=files('p2'),
      legenda=f"""Consulta com especialista sem plano de saúde? Tem, sim 💚

Ginecologia, cardiologia, dermatologia, endocrinologia, ortopedia, pediatria e outras especialidades, com preço acessível aqui em Londrina.

Você escolhe o especialista, vê o valor antes e agenda tudo pelo WhatsApp.
{WA}

{H} #consultamedica #especialista #medicolondrina"""),
 dict(id='r3', data='2026-10-20', turno='noite', tipo='reels', tema='Canetas emagrecedoras — cuidados', arquivos=files('r3'),
      legenda=f"""Pensando em usar caneta emagrecedora? Veja 3 cuidados antes 👇

1️⃣ Receita médica: a farmácia retém a receita (regra da Anvisa)
2️⃣ Avaliação e exames: o médico avalia o seu caso e pode pedir exames antes de começar
3️⃣ Acompanhamento: durante o uso, ele ajuda a evitar riscos à saúde

Faça do jeito certo: consulta com endocrinologista e exames em Londrina, sem plano de saúde.
{WA}

{INFO}

{H} #canetaemagrecedora #emagrecimento #endocrinologista #saude"""),
 dict(id='p4', data='2026-10-21', turno='manha', tipo='carrossel', tema='Mito ou verdade — jejum', arquivos=files('p4_'),
      legenda=f"""Todo exame de sangue precisa de 12 horas de jejum? 🤔 Mito ou verdade 👇

❌ MITO: 12 horas de jejum para tudo. Cada exame tem a sua regra
✅ VERDADE: glicemia pede jejum, geralmente de 8 horas
❌ MITO: colesterol só em jejum. Muitos laboratórios já aceitam sem jejum, se o médico não pedir o contrário
✅ VERDADE: água pode!

Sempre confirme o preparo com o laboratório. Já tem o pedido? Orçamento grátis com até 50% de desconto*.
{WA}

Salve para lembrar no dia do exame 📌
{INFO}
{D}

{H} #exameslondrina #examedesangue #jejum #mitoouverdade"""),
 dict(id='p5', data='2026-10-22', turno='manha', tipo='carrossel', tema='5 sinais para fazer check-up', arquivos=files('p5_'),
      legenda=f"""5 sinais de que está na hora do seu check-up 👇

1️⃣ Seu último exame foi há mais de 1 ano
2️⃣ Cansaço que não passa
3️⃣ Pressão alta, diabetes ou doenças do coração na família
4️⃣ Peso mudou sem explicação
5️⃣ Passou dos 40 e nunca fez um check-up

Se marcou pelo menos um, o primeiro passo é uma consulta com o clínico geral. Ele pede os exames certos, e a gente faz o orçamento com até 50% de desconto*.
{WA}

Marque alguém que precisa ver isso 👀
{INFO}
{D}

{H} #checkup #saudepreventiva #exameslondrina #clinicogeral"""),
 dict(id='r6', data='2026-10-23', turno='noite', tipo='reels', tema='Especialistas sem plano', arquivos=files('r6'),
      legenda=f"""Sem plano de saúde? Consulta com especialista em Londrina, com preço acessível 💚

✔️ Escolha o especialista
✔️ Veja o valor antes
✔️ Agende pelo WhatsApp

{WA}

{H} #consultamedica #especialista #medicolondrina"""),
 dict(id='p7', data='2026-10-24', turno='manha', tipo='imagem', tema='Dengue — sinais de alerta', arquivos=files('p7'),
      legenda=f"""Calor e chuva: a dengue volta 🦟

Fique atento aos sinais: febre alta, dor atrás dos olhos, dor no corpo e manchas na pele. Não se automedique e procure atendimento.

E não esqueça: 10 minutos por semana eliminando água parada já fazem diferença na sua casa.

Precisa de consulta com clínico geral sem plano de saúde? Agende pelo WhatsApp.
{WA}

{INFO}

{H} #dengue #combateadengue #aedesaegypti"""),
 dict(id='p8', data='2026-10-25', turno='manha', tipo='imagem', tema='Novembro Azul — esquenta', arquivos=files('p8'),
      legenda=f"""Homem também faz check-up 💙

Novembro Azul está chegando. Converse com um urologista sobre o momento certo para o exame de próstata e coloque os exames de rotina em dia.

Consulta e exames sem plano de saúde em Londrina, com exames com até 50% de desconto*.
{WA}

Marque um homem que precisa desse lembrete 👊
{INFO}
{D}

{H} #novembroazul #saudedohomem #urologista #checkup"""),
]
# Instagram: máximo 5 hashtags por post (regra desde dez/2025). Ranking em HASHTAGS.md.
TAGS = {
 'p1': '#londrina #londrinapr #outubrorosa #mamografia #saudedamulher',
 'p2': '#londrina #londrinando #consultamedica #clinicamedica #medicinapreventiva',
 'r3': '#londrina #londrinapr #endocrinologia #emagrecimentocomsaude #saudeemprimeirolugar',
 'p4': '#londrina #londrinando #exames #exameslaboratoriais #laboratorioclinico',
 'p5': '#londrina #londrinapr #checkup #medicinapreventiva #examesderotina',
 'r6': '#londrina #londrinando #consultamedica #clinicamedica #saudeemprimeirolugar',
 'p7': '#londrina #londrinapr #dengue #prevencao #saudepublica',
 'p8': '#londrina #londrinando #novembroazul #saudedohomem #checkup',
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
    semana='2026-10-19',
    status='aprovado',          # pendente | aprovado — só publica se 'aprovado'
    instagram_account_id='17841410873155652',   # @doutoragenda (Zapier: Instagram for Business)
    facebook_page_id='2018258928221781',        # página Doutor Agenda (Zapier: Facebook Pages)
    base_url='https://raw.githubusercontent.com/evandroverasted-code/doutoragenda-posts/main/semanas/2026-10-19/out/',
    turnos={'manha': '11:52', 'noite': '18:52'},
    posts=posts)
json.dump(cal, open('posts.json', 'w'), ensure_ascii=False, indent=1)
for p in posts:
    print(p['id'], p['data'], p['turno'], p['tipo'], len(p['arquivos']), 'arquivos', len(p['legenda']), 'chars')
