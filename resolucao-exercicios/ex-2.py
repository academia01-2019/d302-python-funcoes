# 2) Faça um programa com uma função que
# encontre e imprima todos os números pares
# dentro de um intervalo especificado
# pelo usuário. A função deve receber dois
# parâmetros: valor de início e fim do intervalo.

# Vamos pensar primeiro no algoritmo:
# Para percorrer um intervalo de números,
# passando por cada número, podemos usar
# a função range(), passando como parâmetros
# o valor inicial e final de contagem.

def verificar_intervalo(inicio, fim):
	# Colocamos esse range() como o "objeto"
    # no qual vamos iterar no for
	for num in range(inicio, fim):
		if num % 2 == 0:
			print(f'O número {num} é par!')
		else:
			print(f'O número {num} é ímpar!')
			
valor_inicial = int(input("Digite um valor inicial: "))
valor_final = int(input("Digite um valor final: "))

# A função verificar_intervalo não retorna 
# nenhum valor, então não há necessidade de
# atribui-la a uma variável
verificar_intervalo(valor_inicial, valor_final)
