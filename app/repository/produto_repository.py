import requests

class ProdutoRepository:
    BASE_URL = "http://localhost:5000/produtos"

    @staticmethod
    def adicionar_produto(produto):
        response = requests.post(ProdutoRepository.BASE_URL, json=produto.__dict__)
        return response.json()

    @staticmethod
    def atualizar_quantidade(produto_id, quantidade):
        response = requests.put(f"{ProdutoRepository.BASE_URL}/{produto_id}", json={"quantidade": quantidade})
        return response.json()
