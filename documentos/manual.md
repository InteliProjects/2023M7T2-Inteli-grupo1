# Executando a Aplicação

## 1. Com Docker Compose

### Requisitos:
- Docker e Docker Compose instalados

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/2023M7T2-Inteli/Blue-SkAI
   cd aplicacao

Execute o Docker Compose:

```bash
docker-compose up
```


Acesse a Aplicação Web:
#### Frontend (Next.js com Ant Design): http://localhost:3000
#### Backend (FastAPI com Uvicorn): http://localhost:3001/docs


## 2. Ligando o Servidor de Back e de Front Localmente

Requisitos:
- Node.js instalado
- Clone o Repositório do Frontend:

Acesse a Pasta de Front: 

```https://github.com/2023M7T2-Inteli/Blue-SkAI/tree/main/aplicacao/frontend/blueskai```

Instale as Dependências e Inicie o Servidor:

```bash
npm install
npm run dev
```

Acesse a Aplicação Web:

http://localhost:3000


FastAPI com Uvicorn

Requisitos:
- Python 3 instalado
- Acesse a pasta do Backend:

```https://github.com/2023M7T2-Inteli/Blue-SkAI/tree/main/aplicacao/backend```


Crie e Ative um Ambiente Virtual (Opcional)

```bash
python3 -m venv venv
source venv/bin/activate
```


Instale as Dependências e Inicie o Servidor:

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 3001 --reload
```

Acesse a API:
```
http://localhost:3001/docs
```

## 3. Execução via EC2 Puxando Imagens do Docker Hub
Requisitos:
- EC2 Instanciada e acessível
- Docker instalado na instância

Conecte-se à Instância EC2:

1. Clone o Repositório

```bash
git clone https://seurepositorio.com/seuprojeto
cd seuprojeto
docker-compose up
```

Imagens da Aplicação 
- Frontend: https://hub.docker.com/repository/docker/gabinteli/azul-front/general
- Backend: https://hub.docker.com/repository/docker/gabinteli/azul-back/general

3. Acesse a Aplicação Web:

Frontend (Next.js com Ant Design): http://{ip-da-sua-instancia}:3000
Backend (FastAPI com Uvicorn): http://{ip-da-sua-instancia}:3001/docs


Este é um guia abrangente que inclui todos os passos necessários para executar a aplicação em diferentes cenários. Certifique-se de ajustar os comandos conforme necessário com base nos detalhes específicos do seu projeto.



