from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/buscar-endereco/{cep}")
def buscar_endereco(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code != 200:
        return {"erro": "Não foi possível obter os dados do endereço"}
    
    dados = response.json()

    if "erro" in dados:
        return {"erro": "CEP inválido"}
    
    return {
        "Cep": dados["cep"],
        "Logradouro": dados["logradouro"],
        "Bairro": dados["bairro"],
        "Cidade": dados["localidade"],
        "Estado": dados["uf"]
    }

