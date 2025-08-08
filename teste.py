"""
Modifique as funções que foram criadas no desafio 107
para que elas aceitem um parâmetro a mais, informando
por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.
"""
import moeda
help(moeda.aumentar)
p = int(input('Digite um valor: R$'))
print(f'O dobro de R${p} é {moeda.dobro(p,False)}.')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'Aumentando 10% temos {moeda.aumentar(p,20, True)}.')
print(f'Diminuindo 10% temos {moeda.diminuir(p,10, True)}.')

