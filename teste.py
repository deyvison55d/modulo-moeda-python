import moeda
help(moeda.aumentar)
p = int(input('Digite um valor: R$'))
print(f'O dobro de R${p} é {moeda.dobro(p,False)}.')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'Aumentando 10% temos {moeda.aumentar(p,20, True)}.')
print(f'Diminuindo 10% temos {moeda.diminuir(p,10, True)}.')


