"""Fila do YouTube Shorts (youtube.json).
Desde 27/10/2026: Shorts próprios 2x/semana (terça e quinta, turno noite), gerados com a semana (GERAR.md),
com `aprovado` por vídeo. Com `espelhar_reels: true` volta a copiar os Reels já publicados no Instagram.

Uso:  python3 engine/youtube_fila.py          -> atualiza youtube.json e lista o que está pendente
Regra: só entra na fila o Reels que já está `ok` no Instagram (mesma arte aprovada, mesmo vídeo).
"""
import json, glob, os, re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILA = os.path.join(RAIZ, 'youtube.json')
RAW = 'https://raw.githubusercontent.com/evandroverasted-code/doutoragenda-posts/main/'
WHATS = 'https://wa.me/5543988297260'

# Títulos por Reels (máx. 100 caracteres, com #Shorts). Chave = "<semana>/<id>".
TITULOS = {
    '2026-10-19/r3': '3 cuidados antes de usar caneta emagrecedora #Shorts',
    '2026-10-19/r6': 'Consulta com especialista sem plano de saúde em Londrina #Shorts',
    '2026-10-26/r3': 'Suplemento trata resistência à insulina? Alerta da Anvisa #Shorts',
    '2026-10-26/r6': 'Exames até 50% mais baratos sem plano em Londrina #Shorts',
}


def descricao(legenda, tags_tema):
    """Legenda do Instagram sem a linha de hashtags + link clicável do WhatsApp + 3 hashtags do YouTube."""
    linhas = [l for l in legenda.strip().split('\n') if not re.fullmatch(r'\s*(#\S+\s*)+', l)]
    texto = '\n'.join(linhas).strip()
    texto = texto.replace('ou toque no link da bio', f'ou toque aqui: {WHATS}')
    if WHATS not in texto:
        texto += f'\n📲 WhatsApp: {WHATS}'
    return f"{texto}\n\n#Shorts #londrina #{tags_tema}"[:5000]


def tag_tema(legenda):
    tags = re.findall(r'#(\w+)', legenda)
    resto = [t for t in tags if not t.startswith('londrina') and t not in ('parana', 'norteparana', 'doutoragenda')]
    return resto[0] if resto else 'saude'


def carregar():
    if os.path.exists(FILA):
        return json.load(open(FILA, encoding='utf-8'))
    return {"canal": "@doutoragenda", "categoria_id": None, "videos": []}


def main():
    fila = carregar()
    chaves = {v['chave'] for v in fila['videos']}
    espelhar = fila.get('espelhar_reels', True)   # false = Shorts próprios (ter/qui), sem copiar os Reels
    semanas = sorted(glob.glob(os.path.join(RAIZ, 'semanas', '*', 'posts.json'))) if espelhar else []
    for pj in semanas:
        sem = json.load(open(pj, encoding='utf-8'))
        for p in sem['posts']:
            ig = (p.get('publicado') or {}).get('instagram')
            if p['tipo'] != 'reels' or not (ig and ig.get('ok')):
                continue
            chave = f"{sem['semana']}/{p['id']}"
            if chave in chaves:
                continue
            fila['videos'].append({
                'chave': chave,
                'video_url': sem['base_url'] + p['arquivos'][0],
                'titulo': TITULOS.get(chave, (p['tema'][:88] + ' #Shorts')),
                'descricao': descricao(p['legenda'], tag_tema(p['legenda'])),
                'tags': ['Doutor Agenda', 'Londrina', 'sem plano de saúde', p['tema']],
                'instagram': ig.get('permalink'),
                'publicado': None,
            })
            chaves.add(chave)
    json.dump(fila, open(FILA, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    import datetime as dt
    hoje = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=3)).date().isoformat()   # America/Sao_Paulo
    pend = [v for v in fila['videos'] if not v['publicado']]
    print(f"{len(pend)} pendente(s) no YouTube (hoje {hoje}):")
    for v in pend:
        st = 'APROVADO' if v.get('aprovado', True) else 'aguarda aprovação'
        quando = f"{v.get('data', '-')} {v.get('turno', '')}"
        pronto = v.get('aprovado', True) and v.get('data', hoje) <= hoje
        print(f" - {v['chave']} | {quando} | {st} | {'PUBLICAR AGORA' if pronto else 'ainda não'} | {v['titulo']}")


if __name__ == '__main__':
    main()
