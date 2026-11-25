# Arrancar o frontend

Com Node 22.12 ou posterior, executar em `frontend/`:

```sh
npm ci
npm run dev
```

Abrir **http://localhost:5173** com o [backend](../../backend/docs/arranque.md) em execução. Para verificar TypeScript e compilar a aplicação, executar `npm run build`.

## Dados para os componentes

O tipo comum está em `src/api.ts`. A página inicial pede `GET /api/catalogo/edicoes/`. Cada resultado tem `id`, `festa` e `organizador` (identificadores numéricos), `nome_festa`, `localidade`, `ano`, `data_inicio`, `data_fim`, `recinto`, `latitude`, `longitude`, `preco` e `aprovada`. As coordenadas são números, o preço é uma cadeia decimal e as datas têm o formato AAAA-MM-DD.

| Página prevista | Dados de entrada |
|---|---|
| P1, Explorar festas | O mapa e o calendário recebem a mesma lista de resultados. |
| P3, Edição da festa | O cartaz recebe a edição selecionada. |
| P7, Editor de edição | O editor recebe a edição a alterar. A API tem de verificar a permissão de escrita. |

A página inicial já distingue carregamento, lista vazia e falha do pedido. Para a testar com dados, correr `python manage.py carregar_demo` no backend. A documentação da sessão descreve como enviar os cookies e o cabeçalho CSRF.

## Ligação ao Django

Em desenvolvimento local, Vite encaminha `/api` e `/media` para `http://127.0.0.1:8000`. Em Docker, o Compose define `BACKEND_URL=http://backend:8000` para o servidor Vite. Os componentes usam sempre caminhos relativos.
