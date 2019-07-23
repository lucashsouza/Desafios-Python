"""

Crie um código em Python que teste se o site PUDIM
está acessível pelo computador usado.

"""
from urllib import request
from time import sleep

mensagem = "Tentativa de conexão ao PUDIM:"
print('\n\033[1;94m {:^45}\033[m\n'.format(mensagem))
print("Obs: pudim.com.br \n")
try:
    pudim = request.urlopen("http://pudim.com.br/")

except():
    sleep(2)
    print("\033[1;31mConexão falhou!\033[m")

else:
    sleep(2)
    print("\033[1;92m Conectado com sucesso!\033[m")
