from flask import Flask, make_response, jsonify, request
from bd import Carros

app = Flask(__name__)

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(
            mensagem='Lista de carros.',
            dados=Carros
        )
    )

@app.route('/carros', methods=['POST'])
def creat_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            messagem='carro cadastrado com sucesso.',
            carro=carro
        )
    )

app.run()

