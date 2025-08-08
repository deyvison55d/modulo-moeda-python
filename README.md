# Módulo Moeda em Python

Esse módulo contém funções para manipulação e formatação de valores monetários em reais (R$).  
Ideal para quem está começando em Python e quer facilitar cálculos financeiros básicos, como:  

- Aumentar um valor em uma porcentagem;
- Diminuir um valor em uma porcentagem;
- Calcular o dobro de um valor;
- Calcular a metade de um valor;
- Formatar números como moeda brasileira, com símbolo R$ e vírgulas.

O código é simples, com docstrings explicativas para facilitar o entendimento e reutilização.  
Perfeito para estudos, projetos pessoais e para aprender boas práticas com funções e módulos em Python.

---

## Como usar

Importe o módulo e utilize as funções passando valores e parâmetros para formatar o resultado como preferir.

```python
import moeda

preco = 150.0
print(moeda.aumentar(preco, 10, True))  # Aumenta 10% e formata
print(moeda.metade(preco, True))         # Calcula a metade formatada