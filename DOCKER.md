# Docker para desenvolvimento

Na raiz, `compose.yaml` define dois contentores: backend Django e frontend React. O backend inclui as três apps e aplica as migrações antes de abrir a porta 8000.

| Ação | Comando |
|---|---|
| Validar a configuração | `docker compose config --quiet` |
| Construir e iniciar | `docker compose up --build -d` |
| Carregar os exemplos | `docker compose exec backend python manage.py carregar_demo` |
| Ver o estado e os registos | `docker compose ps` e `docker compose logs backend frontend` |
| Executar os testes | `docker compose exec backend python manage.py test` |
| Criar um administrador local | `docker compose exec backend python manage.py createsuperuser` |
| Parar | `docker compose down` |

Abrir o site em **http://localhost:5173**. A pasta `backend/` está montada em `/app`: a base `db.sqlite3` e as fotografias em `media/` ficam no computador e sobrevivem à recriação dos contentores. Docker e o arranque local usam o mesmo ficheiro. Usar só um dos dois modos de cada vez.

## Alterar a configuração

- **Dependências Python:** atualizar `backend/requirements.txt` e executar `docker compose up -d --build backend`.
- **Dependências npm:** usar `npm install` em `frontend/`, guardar o `package-lock.json` e reconstruir o frontend.
- **Código:** alterações no backend e em `frontend/src/` são lidas diretamente. Após alterar `vite.config.js` ou `index.html`, reconstruir o frontend.
- **Versões de Python ou Node:** alterar a imagem `FROM` no Dockerfile do respetivo componente e voltar a construir.
- **Portas:** alterar a porta do computador no mapeamento em `compose.yaml`. A ligação interna do Vite continua a usar a porta 8000 do backend.
