"""Gera posts.json (calendário + legendas) da semana 16 a 22/11/2026."""
import json, os, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))

WA = '📲 WhatsApp oficial: (43) 98829-7260, ou toque no link da bio'
D = '*em relação ao preço particular de tabela.'
INFO = 'Conteúdo informativo, não substitui consulta médica.'

def files(prefix):
    return sorted(os.path.basename(f) for f in glob.glob(f'out/{prefix}*') if f.endswith(('.png', '.mp4')))

posts = [
 dict(id='p1', data='2026-11-16', turno='manha', tipo='carrossel', tema='Novembro Roxo — prematuridade: o cuidado continua em casa', arquivos=files('p1_'),
      legenda=f"""Novembro Roxo 💜 Amanhã, 17/11, é o Dia Mundial da Prematuridade. 4 pontos que toda família deveria saber 👇

👶 O que é: é considerado prematuro o bebê que nasce antes das 37 semanas de gestação
🤰 Pré-natal desde o início: acompanhar a gestação com o médico desde o começo é o primeiro cuidado
🏠 Depois da alta: crescimento, alimentação, respiração e desenvolvimento seguem sendo acompanhados
⚠️ Pele amarelada: entre prematuros que voltaram ao hospital nos primeiros 30 dias de vida, a icterícia foi a causa mais comum (DRG Brasil, via Agência Brasil). Na dúvida, procure o pediatra

Cuidar cedo faz diferença. Consulta com ginecologista/obstetra ou pediatra em Londrina, sem plano de saúde. Exames com até 50% de desconto*.
{WA}

Compartilhe com uma gestante ou uma família de prematuro 💜
{INFO}
{D}"""),
 dict(id='p2', data='2026-11-18', turno='manha', tipo='carrossel', tema='Mito ou verdade — exame de PSA (Novembro Azul)', arquivos=files('p2_'),
      legenda=f"""Exame de PSA: o que é mito e o que é verdade? 💙 4 dúvidas do Novembro Azul 👇

❌ MITO: PSA alto é sempre câncer. Outras alterações da próstata, como o aumento benigno e inflamações, também podem elevar o PSA
✅ VERDADE: é um exame de sangue. O PSA é medido numa coleta comum. Confirme o preparo com o laboratório
❌ MITO: todo homem precisa fazer já aos 30. A Sociedade Brasileira de Urologia recomenda conversar com o urologista a partir dos 50 anos, ou dos 45 para homens negros e quem tem caso de câncer de próstata na família
✅ VERDADE: o médico define a frequência. Pode ser todo ano ou a cada alguns anos. Quem decide com você é o urologista

Resultado em mãos? Quem interpreta é o médico.

Consulta com urologista em Londrina, sem plano de saúde, e exames com até 50% de desconto*. Orçamento grátis.
{WA}

Marque um homem que precisa ver isso 💙
{INFO}
{D}"""),
 dict(id='r3', data='2026-11-20', turno='noite', tipo='reels', tema='Oferta — feche o ano com o check-up em dia (exames até 50%*)', arquivos=files('r3'),
      legenda=f"""O ano está acabando. E o seu check-up? 🗓️

Exames em Londrina, sem plano de saúde, com até 50% de desconto*. É simples:
1️⃣ Pedido em mãos: tem o pedido médico? Tire uma foto. Não tem? Agende uma consulta com a gente
2️⃣ Mande no WhatsApp: envie a foto do pedido para o Doutor Agenda
3️⃣ Orçamento grátis: você recebe o orçamento e escolhe onde e quando fazer

Comece 2027 em dia 💚
{WA}

Mande para quem está adiando os exames 😉
{D}"""),
]
# Instagram: máximo 5 hashtags por post. Ranking em HASHTAGS.md.
TAGS = {
 'p1': '#londrina #londrinapr #prematuridade #saudedamulher #consultamedica',
 'p2': '#londrina #londrinando #novembroazul #prostata #urologia',
 'r3': '#londrina #londrinaofficial #checkup #exames #medicinapreventiva',
}
for p in posts:
    linhas = [l for l in p['legenda'].rstrip().split('\n') if not l.startswith('#')]
    p['legenda'] = '\n'.join(linhas).rstrip() + '\n\n' + TAGS[p['id']]
    assert p['legenda'].count('#') == 5, p['id']
    assert 'ORG-' not in p['legenda'], p['id']
for p in posts:
    assert p['arquivos'], p['id']
    assert len(p['legenda']) <= 2200, (p['id'], len(p['legenda']))
    p['publicado'] = {'instagram': None, 'facebook': None}

cal = dict(
    semana='2026-11-16',
    status='pendente',          # pendente | aprovado — só publica se 'aprovado'
    instagram_account_id='17841410873155652',
    facebook_page_id='2018258928221781',
    base_url='https://raw.githubusercontent.com/evandroverasted-code/doutoragenda-posts/main/semanas/2026-11-16/out/',
    turnos={'manha': '11:52', 'noite': '18:52'},
    posts=posts)
json.dump(cal, open('posts.json', 'w'), ensure_ascii=False, indent=1)
for p in posts:
    print(p['id'], p['data'], p['turno'], p['tipo'], len(p['arquivos']), 'arquivos', len(p['legenda']), 'chars')
