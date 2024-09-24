import requests

class CloudService:
    @staticmethod
    def enviar_dados(dados):
        response = requests.post("http://api-nuvem.com/dados", json=dados)
        return response.json()
