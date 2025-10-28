
# 🏛️ ARQUITETURA DO PRODUTO (GRANA ZERO)

## Padrão Arquitetural

**Model-View-Controller (MVC)**

O sistema Saldo Zero será construído seguindo o padrão arquitetural **Model-View-Controller (MVC)**. Este padrão visa separar as preocupações do aplicativo em três partes interconectadas, facilitando a manutenção e a escalabilidade:

* **Model (Modelo):** Responsável pela lógica de dados, regras de negócio, e interação direta com o banco de dados.
* **View (Visão):** Responsável pela interface do usuário (UI), apresentando os dados do Modelo. No nosso caso, o front-end Web.
* **Controller (Controlador):** Atua como um intermediário, recebendo a entrada do usuário (da View), processando-a, e atualizando o Modelo e a View conforme necessário.

## ⚙️ Sobre os Microserviços

Para o MVP e os incrementos iniciais, utilizaremos uma arquitetura **Monolítica** que implementa o padrão MVC, dado o cronograma de 45 dias e o escopo inicial. A migração para **Microserviços** será avaliada em ondas futuras, conforme o crescimento da base de usuários e a complexidade das funcionalidades (Onda 4 em diante).

## 📝 Casos de Uso

A listagem detalhada dos Casos de Uso será documentada em seção separada, mas os principais abrangem as funcionalidades do MVP:

* UC01: Cadastrar Usuário
* UC02: Cadastrar Finança (Conta)
* UC03: Cadastrar Transação (Receita/Despesa)

## 💾 Modelagem de Dados

### Modelagem Conceitual (DER)

Será desenvolvida para representar as entidades principais do sistema e seus relacionamentos (e.g., Usuário, Finança, Transação).

### Modelagem Lógica

Será focada na definição das tabelas, colunas, chaves primárias e chaves estrangeiras, abstraindo a tecnologia de banco de dados específica.

### Modelagem Física

Detalhará a implementação no banco de dados escolhido (e.g., PostgreSQL ou MySQL), incluindo tipos de dados específicos, índices e restrições.
