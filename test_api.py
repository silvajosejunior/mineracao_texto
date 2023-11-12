import requests

# Fazer uma solicitação GET para a raiz da API
response = requests.get("http://localhost:5000/")
print("Resposta da raiz da API:")
print(response.text)

# Fazer uma solicitação POST para a rota de classificação de emoções
frase_para_classificar = "tristeza"
data = {"frase": frase_para_classificar}
response = requests.post("http://localhost:5000/classificar_emocao", json=data)
print("\nResposta da classificação de emoções:")
print(response.json())
