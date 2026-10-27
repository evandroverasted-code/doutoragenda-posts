# Publicar os posts do turno (Instagram + Facebook + YouTube Shorts via Zapier)

Rotina executada pela tarefa programada "Doutor Agenda — publicar posts" (seg, qua e sex, 11:52 e 18:52, horário de Brasília).

## Valores fixos (NUNCA trocar, NUNCA publicar em outra conta)
- Instagram @doutoragenda → Zapier app **Instagram for Business**, `instagramPageId` = `17841410873155652`
- Página Facebook **Doutor Agenda** → Zapier app **Facebook Pages**, `page` = `2018258928221781`
- YouTube canal **Doutor Agenda** (@doutoragenda) → Zapier app **YouTube**, canal `UCl1tl8NrgfZqxif3YO_IpjQ`, categoria `27` (Education)
- A conexão Zapier (ted_veras@hotmail.com) enxerga outras contas (Sohoostyle, Monnet, clientes). Use somente os IDs acima.

## Passos
1. Repositório: `add_repo` evandroverasted-code/doutoragenda-posts (access push) e clone em `/home/claude/doutoragenda-posts`.
2. Hora atual em America/Sao_Paulo. Turno = `manha` se antes das 15h, senão `noite`.
3. Abra `semanas/*/posts.json` cuja semana contém hoje. Só continue se `status == "aprovado"`.
   Se estiver `pendente`, NÃO publique: avise o Ted que a semana ainda aguarda aprovação.
4. Selecione os posts com `data == hoje` e (`turno` == turno atual, ou `manha` atrasado se agora é `noite`)
   (ignore a lista `cancelados`) e com `publicado.instagram` ou `publicado.facebook` ainda `null`.
5. Para cada post, URLs públicas = `base_url + arquivo` (na ordem de `arquivos`). Antes de executar, confirme os
   nomes de parâmetros com `inspect_zapier_actions` (tool_name abaixo).
   - **imagem / carrossel**
     - Instagram: `instagram_for_business_publish_photo_s` → `instagramPageId`, `media` = [urls] (1–10), `caption` = legenda
     - Facebook: `facebook_pages_create_page_photo` → `page`, `source` = [urls], `message` = legenda
   - **reels** (mp4 1080x1920)
     - Instagram: `instagram_for_business_publish_video` (Reel) → conta fixa, URL do vídeo, legenda
     - Facebook: `facebook_pages_create_page_video` → página fixa, URL do vídeo, descrição = legenda
6. Grave o resultado em `publicado.instagram` / `publicado.facebook`
   (`{"ok": true, "id": ..., "quando": ISO}` ou `{"ok": false, "erro": "..."}`), faça commit e push.
   Nunca tente o mesmo post mais de 2 vezes na mesma execução. Nunca republicar um post já `ok`.
7. Confirme: leitura `instagram_for_business_new_media_posted_in_my_acco` (deve aparecer a mídia nova) e
   `facebook_pages_new_post_by_you`.
8. **YouTube Shorts** (canal @doutoragenda) — Shorts próprios, 2x por semana (terça e quinta, turno `noite`):
   - `python3 engine/youtube_fila.py` lista a fila de `youtube.json` e marca `PUBLICAR AGORA` o que está pronto.
   - Publique só vídeos com `publicado == null`, `aprovado == true`, `data <= hoje` e `turno` == turno atual
     (ou `manha`/`noite` de dia anterior que ficou atrasado). Se `aprovado == false` e a data é hoje, NÃO publique:
     avise o Ted que o Short do dia aguarda aprovação.
   - Zapier app **YouTube**, `youtube_upload_video` → `video` = `video_url`, `title` = `titulo`, `description` = `descricao`,
     `tags` = `tags`, `privacy_status` = `public`, `made_for_kids` = `false`, `notify_subscribers` = `true`,
     `category_id` = `youtube.json → categoria_id` (27, Education).
   - Antes do primeiro envio, confirme com `youtube_make_api_get_request` (`/youtube/v3/channels?part=snippet&mine=true`)
     que o canal é `UCl1tl8NrgfZqxif3YO_IpjQ` (Doutor Agenda). Se não for ou não houver conexão, não publique e avise o Ted.
   - Grave `publicado` = `{"ok": true, "id": <videoId>, "url": "https://youtube.com/shorts/<videoId>", "quando": ISO}`
     ou `{"ok": false, "erro": "..."}`; commit e push. Máx. 2 tentativas, nunca republicar um `ok`.
   - `espelhar_reels` = `false`: os Reels do Instagram NÃO vão mais para o YouTube (decisão do Ted, 27/10/2026).
9. Avise o Ted (mensagem curta): o que saiu, links/IDs, e qualquer erro com a sugestão de publicar manualmente
   pelo Meta Business Suite (ou YouTube Studio). Se nada era do turno, encerre sem mensagem.

## Regras
- Nunca turbinar, nunca criar anúncio, nunca gastar.
- Nunca editar legenda ou arte na hora de publicar; publique exatamente o que foi aprovado.
- Se um carrossel no Facebook sair como vários posts separados (verificar no passo 7), avise o Ted e,
  nas próximas semanas, publique no Facebook só a capa do carrossel com a legenda completa (anote em `NOTAS.md`).
