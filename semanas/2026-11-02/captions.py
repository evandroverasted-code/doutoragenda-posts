"""Gera posts.json (calendário + legendas) da semana 02 a 08/11/2026."""
import json, os, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))

WA = '📲 WhatsApp oficial: (43) 98829-7260, ou toque no link da bio'
D = '*em relação ao preço particular de tabela.'
INFO = 'Conteúdo informativo, não substitui consulta médica.'

def files(prefix):
    return sorted(os.path.basename(f) for f in glob.glob(f'out/{prefix}*') if f.endswith(('.png', '.mp4')))

posts = [
 dict(id='p1', data='2026-11-02', turno='manha', tipo='carrossel', tema='Novembro Azul — quando conversar com o urologista', arquivos=files('p1_'),
      legenda=f"""Próstata: quando conversar com o urologista? 💙 Neste Novembro Azul, a gente explica 👇

✅ A partir dos 50 anos, mesmo sem sintomas, a Sociedade Brasileira de Urologia orienta procurar um urologista para uma avaliação individual
✅ Homens negros ou com pai ou irmão que teve câncer de próstata devem começar essa conversa aos 45 anos
✅ PSA e toque: o médico explica os riscos e os benefícios dos exames e decide com você o que faz sentido no seu caso
⚠️ Dificuldade para urinar, jato fraco, vontade de urinar muitas vezes ou sangue na urina: procure um médico, em qualquer idade

Sem plano de saúde? Agende sua consulta com urologista em Londrina. Exames com até 50% de desconto*.
{WA}

Compartilhe com um homem que você ama 💙
{INFO}
{D}"""),
 dict(id='p2', data='2026-11-03', turno='manha', tipo='imagem', tema='Skincare da internet x dermatologista (consultas)', arquivos=files('p2'),
      legenda=f"""Skincare de 10 passos que viu na internet? 🧴

Dermatologistas alertam: produto demais, escolhido pelo que viralizou, pode irritar a pele. Rotina boa não precisa ser complicada, precisa ser a certa para você.

Acne, manchas, pintas, queda de cabelo: quem avalia e monta o cuidado ideal é o dermatologista.

Consulta com dermatologista em Londrina, sem plano de saúde, com preço acessível. Você vê o valor antes de agendar.
{WA}

{INFO}"""),
 dict(id='r3', data='2026-11-03', turno='noite', tipo='reels', tema='Fake news de saúde — 3 cuidados', arquivos=files('r3'),
      legenda=f"""Viu no WhatsApp? Desconfie 👀

Um levantamento da Agência Lupa (outubro/2026) analisou 764 conteúdos virais sobre saúde: 87% eram falsos.

Antes de acreditar ou repassar:
1️⃣ Desconfie de milagre: cura rápida, sem esforço e "que os médicos escondem" é sinal de alerta
2️⃣ Olhe a fonte: a Anvisa, por exemplo, lembrou em outubro que a ashwagandha não é permitida em suplementos no Brasil
3️⃣ Pergunte a um especialista antes de comprar ou mudar qualquer coisa

Na dúvida, pergunte a quem entende. Consulta com especialista em Londrina, sem plano de saúde.
{WA}

Mande para aquele grupo da família 😉
{INFO}"""),
 dict(id='p4', data='2026-11-04', turno='manha', tipo='carrossel', tema='Mito ou verdade — diabetes', arquivos=files('p4_'),
      legenda=f"""Diabetes sempre dá sintomas? 🤔 Mito ou verdade 👇

❌ MITO: sempre dá sintomas. Pode passar anos em silêncio: cerca de 1 em cada 3 pessoas com diabetes não sabe que tem
✅ VERDADE: exame de sangue ajuda a descobrir. Glicemia de jejum e hemoglobina glicada estão entre os exames que o médico pode pedir
❌ MITO: só quem come muito doce tem. Histórico na família, excesso de peso, sedentarismo e idade também contam
✅ VERDADE: muita sede é sinal de alerta. Sede excessiva, urinar muito, visão embaçada e perda de peso sem motivo pedem consulta

14/11 é o Dia Mundial do Diabetes. Sua glicemia está em dia? Consulta com clínico geral ou endocrinologista e exames com até 50% de desconto*.
{WA}

Salve e compartilhe 📌
{INFO}
{D}"""),
 dict(id='p5', data='2026-11-05', turno='manha', tipo='carrossel', tema='Check-up do homem — 5 exames', arquivos=files('p5_'),
      legenda=f"""Check-up do homem: 5 exames que o médico pode pedir 👇

1️⃣ Glicemia: nível de açúcar no sangue
2️⃣ Colesterol e triglicerídeos: gorduras ligadas à saúde do coração
3️⃣ Hemograma: avalia as células do sangue
4️⃣ Creatinina: ajuda a avaliar os rins
5️⃣ PSA: exame de sangue da próstata, pedido depois da conversa com o médico sobre riscos e benefícios

Quem define os exames certos para a sua idade e histórico é o seu médico. Consulta com clínico geral ou urologista sem plano de saúde e, com o pedido em mãos, orçamento grátis com até 50% de desconto*.
{WA}

Salve este post para levar na consulta 📌
{INFO}
{D}"""),
 dict(id='r6', data='2026-11-06', turno='noite', tipo='reels', tema='Consulta sem plano — veja o valor antes', arquivos=files('r6'),
      legenda=f"""Sem plano de saúde? Você vê o valor antes de agendar 💚

Urologia, dermatologia, endocrinologia, cardiologia, ginecologia, clínico geral e outras especialidades em Londrina, com preço acessível.

Como funciona:
1️⃣ Chame no WhatsApp
2️⃣ Escolha o especialista
3️⃣ Veja o valor e agende

E os exames saem com até 50% de desconto*.
{WA}

{D}"""),
 dict(id='p7', data='2026-11-07', turno='manha', tipo='imagem', tema='Sarampo — caderneta em dia', arquivos=files('p7'),
      legenda=f"""Sua vacina contra o sarampo está em dia? 💉

Com o avanço do sarampo nas Américas, o Brasil reforçou a vigilância. Em 2026, o país teve 52 casos confirmados, todos trazidos de outros países, segundo o Ministério da Saúde.

A vacina é gratuita no SUS. Confira a sua caderneta e a das crianças na UBS mais perto de você.

Ficou com dúvida ou precisa de atendimento? Consulta com clínico geral ou pediatra sem plano de saúde em Londrina.
{WA}

{INFO}"""),
 dict(id='p8', data='2026-11-08', turno='manha', tipo='imagem', tema='Novembro Azul — manda para o homem que adia o médico', arquivos=files('p8'),
      legenda=f"""Todo mundo tem um homem assim na vida 😅💙

Aquele que "tá tudo bem", que "depois eu vejo", que vive adiando o médico.

Neste Novembro Azul, manda este post para ele. Dá para agendar consulta com urologista ou clínico geral pelo WhatsApp, em Londrina, sem plano de saúde.
{WA}

Marque ele aqui nos comentários 👇
{INFO}"""),
]
# Instagram: máximo 5 hashtags por post. Ranking em HASHTAGS.md.
TAGS = {
 'p1': '#londrina #londrinapr #novembroazul #urologia #prostata',
 'p2': '#londrina #londrinando #dermatologia #consultamedica #saudeemprimeirolugar',
 'r3': '#londrina #londrinapr #saudeemprimeirolugar #clinicamedica #medicina',
 'p4': '#londrina #londrinando #exameslaboratoriais #exames #checkup',
 'p5': '#londrina #londrinaofficial #checkup #saudedohomem #exameslaboratoriais',
 'r6': '#londrina #londrinapr #consultamedica #clinicamedica #medicinapreventiva',
 'p7': '#londrina #londrinando #saudepublica #prevencao #saudeemprimeirolugar',
 'p8': '#londrina #londrinapr #novembroazul #saudedohomem #urologia',
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
    semana='2026-11-02',
    status='pendente',          # pendente | aprovado — só publica se 'aprovado'
    instagram_account_id='17841410873155652',   # @doutoragenda (Zapier: Instagram for Business)
    facebook_page_id='2018258928221781',        # página Doutor Agenda (Zapier: Facebook Pages)
    base_url='https://raw.githubusercontent.com/evandroverasted-code/doutoragenda-posts/main/semanas/2026-11-02/out/',
    turnos={'manha': '11:52', 'noite': '18:52'},
    posts=posts)
json.dump(cal, open('posts.json', 'w'), ensure_ascii=False, indent=1)
for p in posts:
    print(p['id'], p['data'], p['turno'], p['tipo'], len(p['arquivos']), 'arquivos', len(p['legenda']), 'chars')
