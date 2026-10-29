"""Gera posts.json (calendário + legendas) da semana 09 a 15/11/2026."""
import json, os, glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))

WA = '📲 WhatsApp oficial: (43) 98829-7260, ou toque no link da bio'
D = '*em relação ao preço particular de tabela.'
INFO = 'Conteúdo informativo, não substitui consulta médica.'

def files(prefix):
    return sorted(os.path.basename(f) for f in glob.glob(f'out/{prefix}*') if f.endswith(('.png', '.mp4')))

posts = [
 dict(id='p1', data='2026-11-09', turno='manha', tipo='carrossel', tema='Novembro Azul — saúde do homem vai além da próstata', arquivos=files('p1_'),
      legenda=f"""Novembro Azul não é só próstata 💙 4 cuidados que todo homem deveria ter no radar 👇

📊 Homem vai menos ao médico: 69% dos homens consultaram um médico em 1 ano. Entre as mulheres, 82% (Pesquisa Nacional de Saúde/IBGE)
❤️ Pressão alta: muitas vezes não dá sintomas. Medir a pressão faz parte de uma consulta simples
🩸 Diabetes e obesidade: estão entre os cuidados contínuos que o Ministério da Saúde destaca para os homens
🧠 Saúde mental: ansiedade, estresse e tristeza que não passa também são assunto para o médico

Uma consulta por ano já é um começo. Clínico geral ou urologista em Londrina, sem plano de saúde. Exames com até 50% de desconto*.
{WA}

Compartilhe com um homem que você ama 💙
{INFO}
{D}"""),
 dict(id='p2', data='2026-11-11', turno='manha', tipo='carrossel', tema='Mito ou verdade — jejum para exame de sangue', arquivos=files('p2_'),
      legenda=f"""Exame de sangue: precisa mesmo de 12 horas de jejum? 🤔 Mito ou verdade 👇

❌ MITO: colesterol sempre pede 12h de jejum. Desde 2016, sociedades médicas brasileiras deixaram de exigir jejum para colesterol e triglicerídeos na maioria dos casos
✅ VERDADE: glicemia de jejum pede 8 horas. Para esse exame, o mínimo de 8 horas continua valendo
❌ MITO: quanto mais jejum, melhor. Jejum acima de 16 horas não é recomendado para a maioria dos exames
✅ VERDADE: a hemoglobina glicada pode ser feita sem jejum

Cada exame tem o seu preparo: na dúvida, confirme com o seu médico ou com o laboratório antes da coleta.

Pedido médico em mãos? Faça seu orçamento grátis. Exames em Londrina, sem plano de saúde, com até 50% de desconto*.
{WA}

Salve para lembrar antes do próximo exame 📌
{INFO}
{D}"""),
 dict(id='r3', data='2026-11-13', turno='noite', tipo='reels', tema='Trend de parar o protetor solar x dermatologista', arquivos=files('r3'),
      legenda=f"""Trend nas redes: parar de usar protetor solar? Não caia nessa ☀️

O câncer de pele não melanoma é o tipo de câncer mais comum no Brasil, segundo o INCA. E o verão está chegando.

3 cuidados do Ministério da Saúde:
1️⃣ Protetor todo dia: FPS 15 ou mais, reaplicando a cada 2 horas, mesmo com tempo nublado
2️⃣ Fuja do sol forte: entre 10h e 16h, procure sombra. Chapéu e óculos ajudam
3️⃣ Olho nas pintas: mudou de tamanho, forma ou cor, coça ou sangra? Procure um dermatologista

Consulta com dermatologista em Londrina, sem plano de saúde, com preço acessível.
{WA}

Mande para quem vive dizendo que "não precisa de protetor" 😉
{INFO}"""),
]
# Instagram: máximo 5 hashtags por post. Ranking em HASHTAGS.md.
TAGS = {
 'p1': '#londrina #londrinando #novembroazul #saudedohomem #clinicamedica',
 'p2': '#londrina #londrinapr #exameslaboratoriais #exames #examesderotina',
 'r3': '#londrina #londrinaofficial #dermatologia #consultamedica #prevencao',
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
    semana='2026-11-09',
    status='pendente',          # pendente | aprovado — só publica se 'aprovado'
    instagram_account_id='17841410873155652',
    facebook_page_id='2018258928221781',
    base_url='https://raw.githubusercontent.com/evandroverasted-code/doutoragenda-posts/main/semanas/2026-11-09/out/',
    turnos={'manha': '11:52', 'noite': '18:52'},
    posts=posts)
json.dump(cal, open('posts.json', 'w'), ensure_ascii=False, indent=1)
for p in posts:
    print(p['id'], p['data'], p['turno'], p['tipo'], len(p['arquivos']), 'arquivos', len(p['legenda']), 'chars')
