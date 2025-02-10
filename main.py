from flask import Flask, make_response, jsonify, request
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados
conn = psycopg2.connect(
    dbname="carros_db",  # nome do seu banco
    user="postgres",     # seu usuário do PostgreSQL
    password="#800VSea1000@",  # sua senha do PostgreSQL
    host="localhost",    # servidor local
    port="5432"          # porta do PostgreSQL
)
cursor = conn.cursor()

# Rota GET para obter todos os carros
@app.route('/carros', methods=['GET'])
def get_carros():
    cursor.execute("SELECT * FROM carros;")
    carros = cursor.fetchall()  # Recupera todos os carros

    # Se não encontrar carros
    if not carros:
        return make_response(
            jsonify(
                mensagem='Nenhum carro encontrado.'
            ), 404
        )

    return make_response(
        jsonify(
            mensagem='Lista de carros.',
            dados=carros
        )
    )

# Rota POST para cadastrar um novo carro
@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json

    # Validação para garantir que o carro tem todos os campos necessários
    if not carro.get('marca') or not carro.get('modelo') or not carro.get('ano'):
        return make_response(
            jsonify(
                mensagem='Dados inválidos! Faltam campos obrigatórios.'
            ), 400
        )

    # Inserindo o novo carro no banco de dados
    cursor.execute("""
        INSERT INTO carros (marca, modelo, ano)
        VALUES (%s, %s, %s)
        RETURNING id;
    """, (carro['marca'], carro['modelo'], carro['ano']))
    id_gerado = cursor.fetchone()[0]  # Pegando o ID gerado pelo banco

    # Salvando no banco
    conn.commit()

    # Retornando o carro com ID gerado
    return make_response(
        jsonify(
            mensagem='Carro cadastrado com sucesso.',
            carro={**carro, 'id': id_gerado}
        ), 201
    )

# Rota PUT para atualizar as informações de um carro
@app.route('/carros/<int:id>', methods=['PUT'])
def update_carro(id):
    carro = request.json

    # Verificando se o carro existe no banco
    cursor.execute("SELECT * FROM carros WHERE id = %s;", (id,))
    carro_bd = cursor.fetchone()

    if not carro_bd:
        return make_response(
            jsonify(
                mensagem='Carro não encontrado.'
            ), 404
        )

    # Atualizando os dados do carro
    cursor.execute("""
        UPDATE carros
        SET marca = %s, modelo = %s, ano = %s
        WHERE id = %s;
    """, (carro['marca'], carro['modelo'], carro['ano'], id))
    
    conn.commit()

    return make_response(
        jsonify(
            mensagem='Carro atualizado com sucesso.',
            carro={**carro, 'id': id}
        )
    )

# Rota DELETE para remover um carro
@app.route('/carros/<int:id>', methods=['DELETE'])
def delete_carro(id):
    # Verificando se o carro existe no banco
    cursor.execute("SELECT * FROM carros WHERE id = %s;", (id,))
    carro_bd = cursor.fetchone()

    if not carro_bd:
        return make_response(
            jsonify(
                mensagem='Carro não encontrado.'
            ), 404
        )

    # Deletando o carro
    cursor.execute("DELETE FROM carros WHERE id = %s;", (id,))
    conn.commit()

    return make_response(
        jsonify(
            mensagem='Carro removido com sucesso.'
        )
    )

if __name__ == '__main__':
    app.run(debug=True)
