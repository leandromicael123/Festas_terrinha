# Arquitetura da Rota do Arraial

React e TypeScript apresentam os dados da API Django REST Framework. Há um único projeto Django, um `manage.py` e uma ligação SQLite. O backend consulta os modelos de todas as apps pelo ORM.

| App | Modelos | Utilização |
|---|---|---|
| `contas` | PerfilUtilizador, Interesse e o User do Django | Identidade, nome público, preferências, validação do organizador e sessão. |
| `catalogo` | Festa, EdicaoFesta, ItemCartaz, MediaEdicao | Datas, recinto, coordenadas, aprovação, cartaz e multimédia oficial. |
| `comunidade` | Avaliacao, Post, MediaPost, ComentarioPost, LikePost, Favorito | Atividade dos participantes associada a uma conta e a uma edição. |

O organizador de uma edição é uma chave estrangeira para User. Avaliacao, Post e Favorito referenciam User e EdicaoFesta diretamente na mesma base. O perfil tem a relação 1:1 com User e uma relação N:M com Interesse. A divisão em apps permite trabalhar nas várias funcionalidades e aplicar todas as migrações com um único comando.

**Pontos de integração.** As edições públicas já estão disponíveis na API. A sessão usa cookies Django e CSRF. O nome público está em `PerfilUtilizador.nome_publico`. Para a futura API de publicações, combinar `id`, `texto`, `data`, `autor_nome` e `fotos` (lista de URLs). Os gostos e comentários referenciam o id de Post.

**Trabalho nas branches.** Filtros, mapa, calendário, criação e edição de festas, moderação, respostas, recomendações e interações do utilizador são entregas da equipa. A existência de um modelo ou de um formulário de administração não substitui a página nem o endpoint da funcionalidade.
