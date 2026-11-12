"""Gera posts.json (calendário + legendas) da semana 23 a 29/11/2026."""
import json, os, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))

WA = '📲 WhatsApp oficial: (43) 98829-7260, ou toque no link da bio'
D = '*em relação ao preço particular de tabela.'
INFO = 'Conteúdo informativo, não substitui consulta médica.'

def files(prefix):
    return sorted(os.path.basename(f) for f in glob.glob(f'out/{prefix}*') if f.endswith(('.png', '.mp4')) and '_fb' not in f)

posts = [
 dict(id='p1', data='2026-11-23', turno='manha', tipo='carrossel', tema='Novembro — diabetes: 16,6 milhões de adultos no Brasil', arquivos=files('p1_'),
      legenda=f"""16,6 milhões de adultos vivem com diabetes no Brasil, segundo o Atlas da Federação Internacional de Diabetes 💙 Novembro é o mês de falar disso. 4 pontos para ficar de olho 👇

💧 Sede intensa, boca seca e vontade de urinar muitas vezes merecem atenção
😮‍💨 Cansaço fora do comum, visão embaçada e feridas que demoram a cicatrizar também
👨‍👩‍👧 Histórico na família, excesso de peso, sedentarismo e idade aumentam o risco
🩸 Nenhum sinal confirma sozinho: quem pede e avalia o exame de glicemia é o médico

Descobrir cedo faz diferença. Consulta com clínico geral ou endocrinologista em Londrina, sem plano de saúde. Exames com até 50% de desconto*.
{WA}

Mande para alguém da família que está adiando a consulta 💙
{INFO}
{D}"""),
 dict(id='p2', data='2026-11-25', turno='manha', tipo='carrossel', tema='Mito ou verdade — exames de glicose (jejum, glicada)', arquivos=files('p2_'),
      legenda=f"""Exames de glicose: o que é mito e o que é verdade? 🩸 4 dúvidas sobre jejum e diabetes 👇

✅ VERDADE: glicemia pede jejum. Para a glicemia de jejum, o preparo costuma ser de 8 horas. Confirme com o laboratório
❌ MITO: quanto mais jejum, melhor. Jejum muito longo, acima de 16 horas, não é recomendado e pode atrapalhar o resultado
✅ VERDADE: hemoglobina glicada não exige jejum. Ela mostra a média da glicose dos últimos meses
❌ MITO: só quem está acima do peso tem diabetes. Histórico na família, idade e sedentarismo também aumentam o risco

Resultado em mãos? Quem interpreta é o médico.

Glicemia e hemoglobina glicada em Londrina, sem plano de saúde, com até 50% de desconto*. Mande a foto do pedido médico e receba o orçamento grátis.
{WA}

Salve para lembrar do preparo no dia do exame 📌
{INFO}
{D}"""),
 dict(id='r3', data='2026-11-27', turno='noite', tipo='reels', tema='Black Friday da saúde — exames até 50%* e consulta com especialista', arquivos=files('r3'),
      legenda=f"""Hoje é Black Friday 🛍️ E a sua saúde? O desconto que vale a pena 👇

1️⃣ Exames até 50%*: desconto em exames de sangue e de imagem, sem plano de saúde
2️⃣ Especialistas: consulta com especialista em Londrina, agendada pelo WhatsApp
3️⃣ Orçamento grátis: mande a foto do pedido médico e receba o orçamento

Cuide de você, mesmo sem plano 💚
{WA}

Marque quem só pensa nas ofertas e esquece dos exames 😉
{D}"""),
]
# Instagram: máximo 5 hashtags por post. Ranking em HASHTAGS.md.
TAGS = {
 'p1': '#londrina #londrinapr #endocrinologia #clinicamedica #diabetes',
 'p2': '#londrina #londrinando #exames #exameslaboratoriais #examesderotina',
 'r3': '#londrina #londrinaofficial #exames #consultamedica #saudeemprimeirolugar',
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
    semana='2026-11-23',
    status='pendente',          # pendente | aprovado — só publica se 'aprovado'
    instagram_account_id='17841410873155652',
    facebook_page_id='2018258928221781',
    base_url='https://raw.githubusercontent.com/evandroverasted-code/doutoragenda-posts/main/semanas/2026-11-23/out/',
    turnos={'manha': '11:52', 'noite': '18:52'},
    posts=posts)
json.dump(cal, open('posts.json', 'w'), ensure_ascii=False, indent=1)
for p in posts:
    print(p['id'], p['data'], p['turno'], p['tipo'], len(p['arquivos']), 'arquivos', len(p['legenda']), 'chars')
