# Flask Carros API 🚗💻

Bem-vindo à **Flask Carros API**, uma aplicação simples desenvolvida com o framework [Flask](https://flask.palletsprojects.com/), que fornece uma maneira de gerenciar uma lista de carros. Aqui você pode listar e cadastrar carros com informações como **marca**, **modelo** e **ano**.

---

## 🚀 Funcionalidades

- **GET `/carros`**: Retorna todos os carros cadastrados.
- **POST `/carros`**: Cadastra um novo carro com as informações fornecidas.
- **PUT `/carros/<id>`**: Atualiza as informações de um carro específico.
- **DELETE `/carros/<id>`**: Remove um carro do banco de dados.

---

## 🛠️ Pré-requisitos

Antes de rodar o projeto, você precisa ter o seguinte instalado:

- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

---

## 📥 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/GabrielSales10/flask-carros-api.git
cd flask-carros-api
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

- **Windows**:

```bash
.\venv\Scripts\activate
```

- **Mac/Linux**:

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Rode o projeto

Agora você pode rodar o servidor:

```bash
python main.py
```

O servidor estará disponível em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## 📂 Endpoints da API

### **GET `/carros`**: Lista todos os carros cadastrados

- **Resposta**:
    ```json
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
    ```

### **POST `/carros`**: Cadastra um novo carro

- **Exemplo de corpo da requisição**:
    ```json
    {
        "id": 6,
        "marca": "Honda",
        "modelo": "Civic",
        "ano": 2022
    }
    ```

- **Resposta**:
    ```json
    {
        "mensagem": "Carro cadastrado com sucesso.",
        "carro": {
            "id": 6,
            "marca": "Honda",
            "modelo": "Civic",
            "ano": 2022
        }
    }
    ```

---

## 🗂️ Estrutura do Projeto

```
.
├── main.py            # Arquivo principal que define as rotas e lógica da API
├── bd.py              # Contém a lista de carros (simulando um banco de dados)
├── requirements.txt   # Dependências do projeto
└── README.md          # Este arquivo!
```

---

## 🔧 Tecnologias Utilizadas

- **Flask**: Framework web para Python, usado para desenvolver a API.
- **Python 3.x**: Linguagem de programação usada para a construção do backend.

---

## 🤝 Contribuindo

Se você quiser contribuir para este projeto, fique à vontade! Envie um **Pull Request** ou abra uma **Issue**.

---
