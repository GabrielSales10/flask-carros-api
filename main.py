from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados
conn = psycopg2.connect(
    dbname="carros_db",
    user="postgres",
    password="#800VSea1000@",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

@app.route('/carros', methods=['GET'])
def get_carros():
    cursor.execute("SELECT * FROM carros;")
    carros = cursor.fetchall()
    return jsonify({"mensagem": "Lista de carros.", "dados": carros})

@app.route('/carros', methods=['POST'])
def create_carro():
    data = request.json
    cursor.execute("INSERT INTO carros (marca, modelo, ano) VALUES (%s, %s, %s) RETURNING id;", 
                   (data['marca'], data['modelo'], data['ano']))
    carro_id = cursor.fetchone()[0]
    conn.commit()
    return jsonify({"mensagem": "Carro cadastrado com sucesso!", "id": carro_id})

if __name__ == "__main__":
    app.run(debug=True)
