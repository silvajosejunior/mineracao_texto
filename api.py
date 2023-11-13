from flask import Flask, request, jsonify

from analise import aplicastemmer, extratorpalavras, classificador

app = Flask(__name__)

@app.route('/')
def index():
    return "Bem-vindo à API de classificação de emoções!"


def classificar_frase():
    frase = request.json.get('frase')
    testestemming = aplicastemmer([(frase, '')])
    nova_frase = extratorpalavras(testestemming[0][0])
    distribuicao = classificador.prob_classify(nova_frase)
    emocao_prevista = distribuicao.max()

    
    probabilidades = {}
    for label in classificador.labels():
        probabilidades[label] = distribuicao.prob(label)

    return emocao_prevista, probabilidades

@app.route('/classificar_emocao', methods=['POST'])
def classificar_emocao_endpoint():
    emocao_prevista, probabilidades = classificar_frase()
    response = {
        "emocao_prevista": emocao_prevista,
        "probabilidades": probabilidades
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
