def aumentar(valor=0, taxa=0, formato=False):
    """
    Calcula o aumento de um valor com base em uma taxa percentual.

    Args:
        valor: Valor a ser aumentado.
        taxa: Taxa de aumento.
        formato: Se True, retorna o valor formatado como moeda.

    Returns:
        float | str: O valor aumentado, com número ou string formatada.
    """
    res = valor + valor * (taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(valor=0, taxa=0, formato=False):
    res = valor - valor * (taxa / 100)
    return res if formato is False else moeda(res)


def dobro(valor=0, formato=False):
    res = valor * 2
    return res if formato is False else moeda(res)


def metade(valor=0, formato=False):
    res = valor / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$', formato=False):
    return f'{moeda}{preço:>7.2f}'.replace('.',',')

