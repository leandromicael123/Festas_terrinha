# Arrancar o backend

Executar em `backend/`, com o ambiente Python 3.12 ativo. A preparação do ambiente e o arranque com Docker estão no [README da raiz](../../README.md).

```sh
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py carregar_demo
python manage.py runserver
```

Django ouve em **http://127.0.0.1:8000**. Para abrir a administração em `/admin/`, criar uma conta local com `python manage.py createsuperuser`. A conta dos dados fictícios serve apenas para relacionar os registos.

## API disponível

| Método | Caminho | Resultado |
|---|---|---|
| GET | `/api/catalogo/edicoes/` | Lista pública de edições aprovadas, ordenadas por data e id. |
| GET | `/api/catalogo/edicoes/<id>/` | Dados de uma edição aprovada. Uma edição inexistente ou pendente devolve 404. |
| GET | `/api/contas/sessao/` | Devolve `user` (ou `null`) e `csrfToken`. Inicializa a proteção CSRF. |
| POST | `/api/contas/sessao/` | Recebe JSON com `username` e `password`. Devolve a conta e o novo token CSRF. |
| DELETE | `/api/contas/sessao/` | Termina a sessão. Devolve `user: null` e um token CSRF. |

No React, usar caminhos relativos a `/api/`. O Vite encaminha o pedido para o Django. O navegador envia o cookie de sessão no mesmo domínio. Nos pedidos de escrita, enviar o token mais recente no cabeçalho `X-CSRFToken`. Após entrar, usar o token devolvido pelo POST. O backend identifica o autor por `request.user`.

Um pedido de escrita sem CSRF válido é recusado com 403. No início de sessão, dados malformados devolvem 400 e credenciais inválidas devolvem 401. As funcionalidades de escrita de publicações, avaliações e cartaz pertencem às respetivas branches. Na edição do cartaz, verificar no servidor o organizador da edição e a sua validação.

## Após alterar modelos

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py check
python manage.py test
```

Guardar o modelo e a respetiva migração no mesmo commit. Os testes usam uma base temporária.

## Horários e fotografias

As datas de uma edição são datas civis. Para as atuações, `ItemCartaz.inicio` guarda data e hora com fuso. O projeto usa `USE_TZ = True` e `TIME_ZONE = "Europe/Lisbon"`. Em Lisboa, uma atuação às 21h de 15 de junho corresponde às 20h UTC.

Pillow está incluída nas dependências para os campos `ImageField`. Os ficheiros ficam em `backend/media/`, servidos em `/media/` no ambiente de desenvolvimento. SQLite guarda o caminho do ficheiro.
