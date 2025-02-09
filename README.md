# Flask Carros API

Este projeto é uma API simples construída com o framework [Flask](https://flask.palletsprojects.com/), permitindo gerenciar uma lista de carros. Ele oferece funcionalidades para listar e cadastrar carros com informações como marca, modelo e ano.

## Funcionalidades

- **GET /carros**: Lista todos os carros cadastrados.
- **POST /carros**: Cadastra um novo carro com as informações fornecidas.

## Pré-requisitos

Antes de começar, você precisa ter o seguinte instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

## Como rodar o projeto

### 1. Clonar o repositório

git clone https://github.com/GabrielSales10/flask-carros-api.git
cd flask-carros-api

### 2. Criar um ambiente virtual
bash
Copiar
Editar
python -m venv venv
3. Ativar o ambiente virtual
Windows:
bash
Copiar
Editar
.\venv\Scripts\activate
Mac/Linux:
bash
Copiar
Editar
source venv/bin/activate
4. Instalar as dependências
bash
Copiar
Editar
pip install -r requirements.txt
5. Rodar o projeto
Após configurar o ambiente, você pode rodar o projeto com o comando:

bash
Copiar
Editar
python main.py
O servidor estará disponível por padrão em http://127.0.0.1:5000/.

Endpoints da API
GET /carros: Retorna uma lista de todos os carros cadastrados.

Exemplo de resposta:
json
Copiar
Editar
{
    "mensagem": "Lista de carros.",
    "dados": [
        {
            "id": 1,
            "marca": "Fiat",
            "modelo": "Marea",
            "ano": 1999
        },
        {
            "id": 2,
            "marca": "Fiat",
            "modelo": "Uno",
            "ano": 1992
        }
    ]
}
POST /carros: Cadastra um novo carro com as informações fornecidas no corpo da requisição.

Exemplo de requisição:
json
Copiar
Editar
{
    "id": 6,
    "marca": "Honda",
    "modelo": "Civic",
    "ano": 2022
}
Exemplo de resposta:
json
Copiar
Editar
{
    "mensagem": "Carro cadastrado com sucesso.",
    "carro": {
        "id": 6,
        "marca": "Honda",
        "modelo": "Civic",
        "ano": 2022
    }
}
Estrutura do projeto
main.py: Arquivo principal da aplicação Flask que define as rotas e lógica da API.
bd.py: Arquivo que contém a lista de carros (simulando um banco de dados) para persistência de dados.
Tecnologias utilizadas
Flask: Framework web para Python.
perl
Copiar
Editar

### Explicação:

- O README agora está detalhado conforme sua implementação no `main.py` e `bd.py`.
- Incluímos informações sobre como rodar o projeto, a estrutura das requisições e respostas, e uma breve descrição sobre os arquivos principais.
- Não há banco de dados real, já que os carros estão sendo armazenados em uma lista no arquivo `bd.py`.

Você pode copiar e colar o conteúdo acima no seu arquivo `README.md`.
