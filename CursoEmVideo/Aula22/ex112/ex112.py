"""
Dentro do pacote Utilidades que criamos no desafio 111,
temos um módulo chamado dado. Crie uma função chamada
leiaDinheiro() que seja capaz de funcionar como a função
input(), mas com uma validação de dados para aceitar
apenas valores que sejam monetários.
"""

from Aula22.ex112.utilidades import moeda
from Aula22.ex112.utilidades import dado

preco = dado.leiaDinheiro("Preço: R$")


moeda.resumo(preco, 35, 10)
