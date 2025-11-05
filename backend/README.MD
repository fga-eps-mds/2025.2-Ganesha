# ⚙️ Guia de Configuração do Backend (Flask & MySQL)

Este guia detalha os passos para configurar o ambiente de desenvolvimento local, garantindo que o servidor Flask e a conexão com o MySQL funcionem corretamente para todos os desenvolvedores.

## 1. 🧱 Estrutura de Diretórios

O código-fonte do *backend* está isolado na pasta `backend/src/`. A estrutura segue um padrão de camadas (MVC adaptado) para manter a separação de responsabilidades:

Com certeza!

Aqui está a estrutura de diretórios do seu backend Flask/MySQL, formatada em código Markdown para fácil leitura e inclusão na sua documentação:

backend/

├── src/

│   ├── app.py          # ⬅️ Ponto de entrada do Flask e inicialização do DB.

│   ├── controller/     # Lógica de Roteamento (Blueprints e Rotas da API)

│   ├── service/        # Regras de Negócio e Lógica Principal

│   ├── model/          # Classes de Modelo de Dados (SQLAlchemy)

│   ├── dao/            # Data Access Objects (CRUD direto com o DB)

│   └── tests/          # Testes Unitários e de Integração

├── .env        # Modelo de Configuração Local

├── requirements.txt    # Dependências do Python

└── venv/               # Ambiente virtual (Ignorado pelo Git)

## 2. 📝 Configuração do Ambiente Local

O ambiente utiliza um Ambiente Virtual Python (`venv`) e variáveis de ambiente para lidar com chaves secretas e credenciais do banco de dados.

### 2.1. Variáveis de Ambiente (`.env`)

O arquivo **`.env`** na raiz de `backend/` lista as variáveis necessárias.

1.  **Crie seu Arquivo Local:** Copie o arquivo modelo para criar o seu arquivo de ambiente local.
    ```bash
    cp backend/.env backend/.env
    ```
2.  **Preencha as Credenciais:** Edite o arquivo **`.env`** e preencha as chaves:
    * `SECRET_KEY`: Chave secreta longa e aleatória.
    * `DB_USER` e `DB_PASSWORD`: Credenciais do seu servidor MySQL local.

> **Atenção:** O arquivo `.env` **nunca** deve ser comitado. Ele deve estar listado no `.gitignore`.

### 2.2. MySQL e Banco de Dados

1.  **Inicie o Servidor MySQL:** Garanta que seu servidor MySQL (via Docker, XAMPP, ou instalação direta) esteja **rodando** e acessível em `DB_HOST` e `DB_PORT` (padrão `127.0.0.1:3306`).
2.  **Crie o Banco de Dados:** Você deve criar o banco de dados vazio com o nome especificado em `DB_NAME` (`ganesha_db`) **antes** de executar qualquer migração.

## 3. 📦 Instalação das Dependências

Com o Ambiente Virtual (`venv`) ativado, instale as dependências usando o `requirements.txt`.

### 3.1. Ativação do Ambiente Virtual

| Sistema Operacional | Comando de Ativação |
| :--- | :--- |
| **Windows** | `.\venv\Scripts\activate` |
| **Linux/macOS** | `source venv/bin/activate` |

### 3.2. Instalação de Pacotes

O `requirements.txt` contém o Flask, o SQLAlchemy e o *driver* MySQL.

```bash
# O 'python -m pip' garante o uso do pip correto do venv
(venv) $ python -m pip install -r backend/requirements.txt
```

## 4. 🚀 Inicialização do Servidor

O Flask está configurado para iniciar o aplicativo (`src.app:app`) no modo desenvolvimento.

### 4.1. Rodar o Servidor

Execute o comando a seguir no terminal, na raiz do projeto:

```bash
(venv) $ python backend/src/app.py
```

O servidor deve iniciar e carregar as configurações do `.env`. Você pode testar o status da API no seu navegador (geralmente em `http://127.0.0.1:5000/`).

### 4.2. Migrações e Inicialização do Schema

O projeto utiliza o Flask-SQLAlchemy, mas você precisará de uma ferramenta de migração (como Flask-Migrate/Alembic) para criar e evoluir o esquema do banco de dados (tabelas) em `ganesha_db`.

> **A Ferramenta de Migração será configurada em um guia posterior.**

## 5. 🧪 Testes

Para executar os testes unitários e de integração (usando `pytest`), execute o comando na raiz do *backend* após a instalação das dependências:

```bash
(venv) $ pytest backend/src/tests/
```