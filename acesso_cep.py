import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self._cep = cep
        else:
            raise ValueError("CEP inválido!!")

    def __str__(self):
        return self.format_endereco()

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_endereco(self):
        cep, estado, cidade, bairro, rua = self.acessa_via_cep()
        return " CEP: {}\n Estado: {}\n Cidade: {}\n Bairro: {}\n Rua: {}".format(cep, estado, cidade, bairro, rua)

    def acessa_via_cep(self):
        url = ("https://viacep.com.br/ws/{}/json/").format(self._cep)
        r = requests.get(url)
        dados = r.json()

        cep = dados['cep']
        estado = dados['uf']
        cidade = dados['localidade']
        bairro = dados['bairro']
        rua = dados['logradouro']

        return cep, estado, cidade, bairro, rua

