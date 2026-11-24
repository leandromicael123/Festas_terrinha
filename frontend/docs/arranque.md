# Iniciar o frontend da Rota do Arraial

O frontend usa React e TypeScript. Este guia assume Vite e npm para o desenvolvimento local. Os comandos aplicam-se a uma cópia do projeto já inicializada, com `frontend/package.json`, o script `dev` e `frontend/package-lock.json`.

## 1. Preparar o ambiente

Instala Node.js e npm na versão indicada pelo projeto. Abre um terminal na raiz do repositório e executa:

```sh
cd frontend
node --version
npm --version
npm ci
```

Na primeira configuração do projeto, quem cria a aplicação gera o ficheiro `package-lock.json` com `npm install` e inclui-o no Git. A partir daí, o grupo usa `npm ci`.

## 2. Iniciar o site

```sh
npm run dev
```

Abre o endereço apresentado na linha `Local` do terminal. Mantém o processo aberto enquanto trabalhas. Para o terminar, usa `Ctrl+C`.

## 3. Verificar a ligação à API

Para testar a pesquisa de festas, inicia também os serviços indicados no [guia do backend](../../backend/docs/arranque.md). A configuração proposta usa pedidos relativos a `/api/`. No servidor de desenvolvimento do Vite, o proxy de `/api` deve apontar para o endereço do gateway publicado pelo Docker Compose.

Abre a página de pesquisa. Nas ferramentas de desenvolvimento do navegador, confirma que o pedido de listagem de edições recebe HTTP 200 e uma resposta JSON. Uma lista vazia é válida enquanto o Catálogo estiver sem dados de exemplo.
