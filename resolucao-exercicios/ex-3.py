# 3) Faça um programa que leia o raio de um 
# círculo e faça duas funções: uma que
# calcule a área do círculo e outra que calcule
# o comprimento do círculo.

# Podemos utilizar a biblioteca math
# para facilitar nossos cálculos
import math

def calcular_area(raio):
	area = math.pi * math.pow(raio, 2)
	return area
	
def calcular_comprimento(raio):
	comp = 2 * math.pi * raio
	return comp
	
r = float(input("Digite um raio: "))

area = calcular_area(r)
print(f'Uma circunferência de raio {r} tem uma área de {area}.')

comp = calcular_comprimento(r)
print(f'E comprimento {comp}.')