import requests

class VendaRepository:
    BASE_URL = "http://localhost:5000/vendas"

    @staticmethod
    def registrar_venda(venda):
        response = requests.post(VendaRepository.BASE_URL, json=venda.__dict__)
        return response.json()
