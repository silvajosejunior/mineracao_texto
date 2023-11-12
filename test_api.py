import requests


response = requests.get("http://localhost:5000/")
print("Resposta da raiz da API:")
print(response.text)


frase_para_classificar = "tristeza"
data = {"frase": frase_para_classificar}
response = requests.post("http://localhost:5000/classificar_emocao", json=data)
print("\nResposta da classificação de emoções:")
print(response.json())
