from acesso_cep import BuscaEndereco
import requests

cep = 87043180
cep_objeto = BuscaEndereco(cep)
r = requests.get("https://viacep.com.br/ws/87043180/json/")
# print(r.json())

# cep, estado, cidade, bairro, rua = cep_objeto.acessa_via_cep()
# print(cep, estado, cidade, bairro, rua)

print(cep_objeto)

