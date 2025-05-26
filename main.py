from divisao import *
from multiplicacao import *
from soma import *
from subtracao import *
from potenciacao import *

print("Bem-vindo a minha calculadora")
print("Digite o primeiro numero")
primeiro_numero = float(input())
print("Digite o segundo numero")

segundo_numero = float(input())

print("Soma = ", soma(primeiro_numero, segundo_numero))
print("Subtracao = ", subtracao(primeiro_numero, segundo_numero))
print("Multiplicacao = ", multiplicacao(primeiro_numero, segundo_numero))
print("Divisao = ", divisao(primeiro_numero, segundo_numero))
print("Potenciação = ", potenciacao(primeiro_numero, segundo_numero))
print("ok")