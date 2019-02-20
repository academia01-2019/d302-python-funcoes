# 1) Faça uma função que recebe um número
# inteiro por parâmetro e retorna verdadeiro
# se ele for par e falso se for ímpar.

# Declarar a função
def e_par(numero):
	if numero % 2 == 0:
		return True # Se o número é par, retorne True
	return False # Se é ímpar, retorne False

# Pego o input do teclado		
num = int(input("Digite um número: "))

# Como a função retorna um valor,
# podemos chamar a função direto em
# uma atribuição à uma variável
resultado = e_par(num)

# Validação do retorno da função
if resultado is True:
	print(f'O número {num} é par!')
else:
	print(f'O número {num} é ímpar!')
