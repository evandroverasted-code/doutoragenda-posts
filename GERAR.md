# Gerar a semana de posts do Doutor Agenda

Rotina da tarefa programada "Doutor Agenda — gerar semana" (quintas 09:47, horário de Brasília) e da skill
`doutor-agenda-posts`. Gera a semana seguinte (segunda a domingo) e deixa `status: "pendente"` até o Ted aprovar.

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

## 2. Pauta (8 posts por semana)
| Slot | Formato | Linha |
|---|---|---|
| Seg manhã | Carrossel | tema do mês / campanha (educativo) |
| Ter manhã | Imagem | consultas com especialista sem plano |
| Ter noite | Reels | tema viral do momento + cuidado + especialista |
| Qua manhã | Carrossel | mito ou verdade / dúvida de exame |
| Qui manhã | Carrossel | check-up / lista de sinais / "salve este post" |
| Sex noite | Reels | oferta: exames até 50%* ou consultas |
| Sáb manhã | Imagem | alerta sazonal / dica rápida |
| Dom manhã | Imagem | lembrete leve / campanha que vem |
Sempre: ligar o assunto a **agendar com um especialista** ou **fazer o orçamento de exames** no WhatsApp.
Mix mínimo: 2 de exames, 2 de consultas, 2 de dicas/virais, 2 reels.

## 3. Regras de conteúdo (obrigatórias)
- Público: pessoas sem plano de saúde em Londrina e região. Tom simples, acolhedor, direto.
- CTA único: WhatsApp oficial **(43) 98829-7260** / link da bio. Código de rastreio por post: `ORG-<TEMA>-<MMDD>`.
- "até 50% de desconto*" só para **exames**, sempre com `*em relação ao preço particular de tabela.`
- Nunca: diagnóstico, dose, nome de remédio como recomendação, promessa de cura/resultado, antes/depois,
  preço que não foi confirmado pelo Ted, depoimento inventado.
- Conteúdo de saúde leva "Conteúdo informativo, não substitui consulta médica."
- Hashtags: `#londrina #londrinapr #norteparana #semplanodesaude #saudeacessivel #doutoragenda` + 3–4 do tema.
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

## 6. Aprovação
- Envie ao Ted a folha de contatos + os 2 reels + resumo da pauta (dia, tema, código).
- Só quando ele aprovar: `status: "aprovado"`, commit e push. Ajustes pedidos: corrigir, renderizar, reenviar.
