# Gerar a semana de posts do Doutor Agenda

Rotina da tarefa programada "Doutor Agenda — gerar semana" (quintas 09:47, horário de Brasília) e da skill
`doutor-agenda-posts`. Gera uma semana (seg, qua e sex) e deixa `status: "pendente"` até o Ted aprovar.

**Semana alvo:** a primeira segunda-feira futura que ainda NÃO tem pasta em `semanas/` (se a próxima já existe, gere a seguinte; nunca sobrescreva uma semana existente).

## Setup (sessão nova)
```bash
git clone https://github.com/evandroverasted-code/doutoragenda-posts /home/claude/doutoragenda-posts   # após add_repo (push)
cd /home/claude/doutoragenda-posts && npm i --no-audit --no-fund   # Chromium já existe em /opt/pw-browsers
```

## 1. Pesquisa (sempre, antes de escrever)
- WebSearch (modo extended) sobre: assuntos de saúde em alta no Brasil nesta semana; campanhas do mês
  (calendário da saúde: Janeiro Branco, Fevereiro Roxo/Laranja, Março Lilás, Abril Azul, Maio Amarelo,
  Junho Vermelho, Julho Amarelo, Agosto Dourado, Setembro Amarelo, Outubro Rosa, Novembro Azul, Dezembro Vermelho);
  surtos/sazonalidade (dengue, gripe, calor/frio) no Paraná/Londrina; notícias Anvisa/Ministério da Saúde;
  temas virais (ex.: canetas emagrecedoras, vitaminas, sono, ansiedade, mitos).
- Todo dado de saúde citado precisa de fonte confiável recente (Ministério da Saúde, Anvisa, sociedades médicas, Inca).
  Na dúvida, escreva de forma geral e mande "converse com o seu médico".
- Registre as fontes em `semanas/<data>/FONTES.md`.

## 2. Pauta (3 posts por semana — seg, qua, sex; decisão do Ted, 27/10/2026)
| Slot | Formato | Linha |
|---|---|---|
| Seg 11:52 (manha) | Carrossel | tema do mês / campanha ou assunto de saúde em alta (educativo) |
| Qua 11:52 (manha) | Carrossel | exames: mito ou verdade / dúvida de exame / check-up |
| Sex 18:52 (noite) | Reels | tema viral do momento + cuidado + especialista, ou oferta (exames até 50%* / consultas) |
Sempre: assuntos de saúde relevantes do momento, ligando a **agendar com um especialista** ou **fazer o orçamento de exames** no WhatsApp.
Mix na semana: pelo menos 1 de exames e 1 de consultas. IDs: `p1` (seg), `p2` (qua), `r3` (sex).

## 3. Regras de conteúdo (obrigatórias)
- Público: pessoas sem plano de saúde em Londrina e região. Tom simples, acolhedor, direto.
- CTA único: WhatsApp oficial **(43) 98829-7260** / link da bio.
- **Nunca** pedir para o cliente enviar código (ex.: "Envie o código ORG-…") na legenda nem na arte: desestimula o contato (decisão do Ted, 21/10/2026).
- "até 50% de desconto*" só para **exames**, sempre com `*em relação ao preço particular de tabela.`
- Nunca: diagnóstico, dose, nome de remédio como recomendação, promessa de cura/resultado, antes/depois,
  preço que não foi confirmado pelo Ted, depoimento inventado.
- Conteúdo de saúde leva "Conteúdo informativo, não substitui consulta médica."
- Hashtags: **no máximo 5 por post** (regra do Instagram). Use o ranking e os conjuntos de `HASHTAGS.md`:
  `#londrina` + 1 local rotativa + 2 do tema (100 mil–1 mi) + 1 de apoio. Não repita as mesmas 5 em todos os posts.
  No captions.py, defina `TAGS` por post (ver modelo da semana 2026-10-19).
- Legenda ≤ 2.200 caracteres.

## 4. Arte (motor em `engine/`)
- Copie `semanas/2026-10-19/build.py` e `captions.py` como modelo para `semanas/<segunda>/`.
- Cores: #009632 verde · #FFCD00 amarelo · #00642B verde escuro · #B8D8B0 · #E8F5E8 · branco. Fonte Poppins.
  Cor de campanha (rosa, azul) só em detalhe (tag), nunca no fundo.
- Mascote (assets/): `masc_prancheta, masc_joinha, masc_apresenta, masc_celular, masc_aponta, masc_folha, mao_celular`.
  Logo e mascote nunca distorcidos (só `height`). Sem ícones desenhados à mão.
- Feed 1080x1350 (`page()`), Reels 1080x1920 (`reel()` + `scene()`/`move()`), 10–13 s, sem música.
- `python3 semanas/<data>/build.py && node engine/render.js semanas/<data>` → `out/*.png|mp4`.
- **Revise visualmente**: monte uma folha de contatos (PIL) e confira sobreposição de texto/mascote, quebras
  de palavra e corte; nos reels, extraia frames (ffmpeg -ss) de cada cena. Corrija e renderize de novo.

## 5. Calendário
- `python3 semanas/<data>/captions.py` gera `posts.json` (ver modelo). `status: "pendente"`.
- Commit + push (`out/` entra no git; `html/` e `frames/` não).

## 5b. YouTube Shorts (2 por semana: terça e quinta, 18:52)
Objetivo: **constância** no canal @doutoragenda. São vídeos próprios, separados dos posts do Instagram/Facebook.
- **Semana dos Shorts:** sempre a semana que começa na PRÓXIMA segunda-feira (independe da semana alvo dos posts),
  para o assunto estar fresco. Se `youtube.json` já tem `<segunda>/s1` e `s2`, pule. Se a pasta da semana já existe
  (posts aprovados), só acrescente `shorts.py`, `out/s1.mp4`, `out/s2.mp4` e as fontes; não mexa no resto.
- Pauta: assuntos de saúde **do momento no Brasil** (notícia da semana, alerta da Anvisa/Ministério, tema viral,
  campanha do mês), sempre trazidos para **quem mora em Londrina** (onde fazer, o que muda aqui) e fechando com
  consulta/exames sem plano no WhatsApp. Não repetir o tema dos Reels da mesma semana. Fonte recente em `FONTES.md`.
- Arte: `semanas/<segunda>/shorts.py` (modelo: `semanas/2026-10-26/shorts.py`), ids `s1` (terça) e `s2` (quinta),
  1080x1920, ~15 s: gancho com número/pergunta → 3 cenas → CTA. Render: `node engine/render.js semanas/<data> s`.
  Revise os frames como nos Reels.
- Fila: acrescente em `youtube.json → videos` um item por Short (`chave` `<segunda>/s1`, `data`, `turno: "noite"`,
  `aprovado: false`, `video_url` = base_url + `s1.mp4`, `titulo` ≤ 70 caracteres terminando em `| Londrina`,
  `descricao`, `tags`, `fonte`, `publicado: null`). Modelo: itens `2026-10-26/s1` e `s2`.
- Descrição: texto do vídeo + link https://wa.me/5543988297260 + "(43) 98829-7260 · doutoragenda.com" +
  "Conteúdo informativo, não substitui consulta médica." + hashtags.
- **Hashtags (YouTube): as de maior volume de Londrina, não precisam ser de saúde** — `youtube.json → hashtags_londrina`
  (#londrina #londrinando #parana #Shorts #londrinaofficial #londrinapr #cambe #arapongas #apucarana) + 1 do tema.
  As 3 primeiras aparecem acima do título. Máximo 15 no total (acima disso o YouTube ignora todas).
- Na aprovação da semana, envie também os 2 Shorts; quando o Ted aprovar, marque `aprovado: true` nos dois.

## 6. Aprovação
- Envie ao Ted a folha de contatos + o reels + os 2 Shorts + resumo da pauta (dia, tema).
- Só quando ele aprovar: `status: "aprovado"` (e `aprovado: true` nos Shorts da semana em `youtube.json`), commit e push. Ajustes pedidos: corrigir, renderizar, reenviar.
