# Iniciar o backend da Rota do Arraial

Os serviços Django são Contas, Catálogo e Comunidade. Cada um tem modelos, migrações e base de dados próprios. Cada serviço usa um ficheiro SQLite próprio. Em desenvolvimento local, o Django pode criá-lo junto do respetivo `manage.py`.

## 1. Confirmar a configuração

Instala Docker com o comando `docker compose` disponível. Executa os comandos seguintes na raiz do repositório, onde ficará o ficheiro `compose.yaml`.

```sh
docker compose version
docker compose config --services
```

Os exemplos assumem os nomes `contas`, `catalogo`, `comunidade` e `gateway` (Nginx). Se os nomes usados no projeto forem diferentes, substitui-os pelos apresentados no segundo comando. Antes do primeiro arranque, prepara as variáveis previstas no Compose e nas configurações Django. Se existir `.env.example`, copia-o para o nome indicado pelo projeto e preenche os valores locais.

## 2. Configurar os ficheiros SQLite

Em cada serviço Django, configura a ligação em `settings.py`. O exemplo usa a variável de ambiente `SQLITE_PATH` em Docker e o diretório do serviço no arranque local.

```python
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("SQLITE_PATH") or BASE_DIR / "db.sqlite3",
    }
}
```

No `compose.yaml`, cada serviço recebe o seu próprio volume. O excerto abaixo mostra as linhas a integrar nas definições existentes. O processo Django deve ter permissão de escrita no diretório `/dados` do respetivo volume.

```yaml
services:
  contas:
    environment:
      SQLITE_PATH: /dados/db.sqlite3
    volumes:
      - contas_sqlite:/dados
  catalogo:
    environment:
      SQLITE_PATH: /dados/db.sqlite3
    volumes:
      - catalogo_sqlite:/dados
  comunidade:
    environment:
      SQLITE_PATH: /dados/db.sqlite3
    volumes:
      - comunidade_sqlite:/dados

volumes:
  contas_sqlite:
  catalogo_sqlite:
  comunidade_sqlite:
```

O caminho interno é igual nos três contentores. O nome do volume determina que ficheiro pertence a cada serviço. No Git, guarda as migrações Django e inclui `*.sqlite3` e `*.sqlite3-*` no `.gitignore`.

## 3. Arrancar os serviços

```sh
docker compose up -d --build contas catalogo comunidade gateway
docker compose ps
```

## 4. Aplicar as migrações

Os exemplos assumem que o diretório de trabalho de cada contentor contém o respetivo `manage.py`.

```sh
docker compose exec contas python manage.py migrate
docker compose exec catalogo python manage.py migrate
docker compose exec comunidade python manage.py migrate
```

Para confirmar o estado do Catálogo, executa `docker compose exec catalogo python manage.py showmigrations`. As migrações aplicadas aparecem com `[X]`.

## 5. Verificar a API

Consulta a coluna `PORTS` de `docker compose ps` para identificar a porta local do gateway. Abre o endereço do gateway e acrescenta o caminho de listagem de edições definido na arquitetura, `/api/catalogo/edicoes`. Se o router Django usar barra final, acrescenta `/` ao caminho. O resultado esperado é HTTP 200 com a lista de edições aprovadas, que pode estar vazia.

Se algum serviço terminar durante o arranque, consulta o respetivo registo. Por exemplo:

```sh
docker compose logs catalogo
```

Para parar o ambiente local preservando os volumes de dados:

```sh
docker compose stop
```
