# Base SQLite da Rota do Arraial

A base de trabalho é `backend/db.sqlite3`. O Git guarda os modelos, as migrações e uma cópia de demonstração em `database/db_demo.sqlite3`. Cada elemento da equipa altera apenas a sua base local.

## Inicializar ou atualizar

Com o ambiente Python ativo, executar em `backend/`:

```sh
python manage.py migrate
python manage.py carregar_demo
python manage.py showmigrations contas catalogo comunidade
```

As migrações criam as tabelas e as chaves estrangeiras. O comando de demonstração acrescenta duas edições fictícias aprovadas e duas atuações. Pode ser repetido numa base de desenvolvimento. O utilizador fictício não permite iniciar sessão.

A cópia pronta a usar está em `database/db_demo.sqlite3`. Numa extração nova do ZIP, também podes copiar esse ficheiro para `backend/db.sqlite3` antes de ligar o Django. Se já tiveres uma base de trabalho, usa as migrações para a atualizar. O comando `carregar_demo` é opcional quando usas a cópia pronta.

## Relações que a equipa vai usar

| Origem | Relação |
|---|---|
| PerfilUtilizador | Uma conta por perfil. Vários interesses por perfil. Campo público: `nome_publico`. |
| EdicaoFesta | `festa` referencia Festa e `organizador` referencia User. A lista pública mostra apenas edições aprovadas. |
| Avaliacao, Post e Favorito | `user` e `edicao` são chaves estrangeiras para User e EdicaoFesta. |
| MediaPost, ComentarioPost e LikePost | Referenciam o Post. O par conta/publicação é único nos gostos. |
| Favorito | O par conta/edição é único. |

Com `python manage.py shell`, as edições aprovadas podem ser consultadas com `from catalogo.models import EdicaoFesta` e `EdicaoFesta.objects.filter(aprovada=True).values("id", "recinto", "data_inicio")`.

## Preparar o ZIP

O ZIP do GitHub inclui `database/db_demo.sqlite3`. Para entregar a versão do trabalho com registos próprios, extrair o código numa pasta limpa e incluir a base em `backend/db.sqlite3`, juntamente com as imagens de demonstração de `backend/media/`. Usar uma cópia de entrega apenas com dados de demonstração. Extrair o ZIP noutro diretório, aplicar as migrações e confirmar as edições pela API.
