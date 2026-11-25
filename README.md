# Rota do Arraial

Website de festas populares com React e TypeScript e uma API Django REST Framework. As apps `contas`, `catalogo` e `comunidade` usam a mesma base SQLite.

## Primeiro arranque com Docker

Na raiz do repositório:

```sh
docker compose up --build -d
docker compose exec backend python manage.py carregar_demo
```

Abrir **http://localhost:5173**. A página inicial mostra duas edições fictícias. A API está em **http://localhost:8000/api/catalogo/edicoes/**. O Compose aplica as migrações e guarda a base de trabalho em `backend/db.sqlite3`.

## Arranque local

Usar Python 3.12 e Node 22.12 ou posterior. No primeiro terminal, a partir da raiz:

```sh
cd backend
python -m venv .venv
```

Ativar o ambiente: no PowerShell, `.\.venv\Scripts\Activate.ps1`; em macOS ou Linux, `source .venv/bin/activate`. A seguir:

```sh
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py carregar_demo
python manage.py runserver
```

No segundo terminal, a partir da raiz:

```sh
cd frontend
npm ci
npm run dev
```

Nos arranques seguintes bastam `python manage.py runserver` em `backend/` com o ambiente ativo e `npm run dev` em `frontend/`. Após receber novas migrações, executar `python manage.py migrate`.

## O que já funciona

| Componente | Disponível |
|---|---|
| Django e SQLite | 12 modelos da proposta, migrações e administração Django. As contas usam o modelo User do Django. |
| API pública | Lista e detalhe das edições aprovadas, com datas, preço, coordenadas e organizador. |
| Sessão | Consultar a sessão, entrar e sair com cookie e proteção CSRF. |
| React | Página inicial que consulta a API e apresenta as edições. Os filtros, mapa, calendário e formulários serão desenvolvidos nas branches da equipa. |
| Dados de exemplo | Duas festas, duas edições, duas atuações e um organizador fictício sem acesso à sessão. |

## Guias

- [Backend e sessão](backend/docs/arranque.md)
- [Frontend e dados das edições](frontend/docs/arranque.md)
- [Base de dados, cópia inicial e ZIP de entrega](database/docs/arranque.md)
- [Arranque e alterações em Docker](DOCKER.md)
- [Arquitetura e responsabilidades das três apps](docs/arquitetura.md)
