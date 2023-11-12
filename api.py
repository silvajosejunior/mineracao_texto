from flask import Flask, request, jsonify

# Importe as funções e variáveis relacionadas à classificação de emoções do arquivo mineracao.py
from analise import aplicastemmer, extratorpalavras, classificador

app = Flask(__name__)

# Rota para a raiz do aplicativo (pode ser acessada via navegador)
@app.route('/')
def index():
    return "Bem-vindo à API de classificação de emoções!"

# Função para classificar uma nova frase e calcular as probabilidades
def classificar_frase():
    frase = request.json.get('frase')
    testestemming = aplicastemmer([(frase, '')])
    nova_frase = extratorpalavras(testestemming[0][0])
    distribuicao = classificador.prob_classify(nova_frase)
    emocao_prevista = distribuicao.max()

    # Corrigir as probabilidades
    probabilidades = {}
    for label in classificador.labels():
        probabilidades[label] = distribuicao.prob(label)

    return emocao_prevista, probabilidades

# Rota para classificação de emoções
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
