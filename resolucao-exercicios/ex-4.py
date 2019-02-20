# 4) Escreva um programa que lê as notas de
# duas avaliações de um aluno. O programa
# deverá ter uma função que receba
# as duas notas por parâmetro e calcule a
# média dessas notas. Se o aluno obter 
# média maior ou igual a 6.0, mostre a
# mensagem "Parabéns! Você foi aprovado!".

# Para este exercício, vou mostrar um jeito
# diferente de implementação.

# Primeiro definiremos uma função
# que calcula a média entre duas notas:
def media(nota1, nota2):
	media = (nota1 + nota2)/2
	return media
	
# E agora definiremos uma função que
# lê a média do aluno e diz se ele foi
# aprovado ou não. Note que passei
# as notas para a função, e não a média já
# calculada:
def verificar_aluno(nota1, nota2):
	
	# Dentro da função verifica_aluno, é possível
	# chamar a função média!
	media_do_aluno = media(nota1, nota2)
	
	if  media_do_aluno >= 6.0:
		print(f'Parabéns! O aluno foi aprovado  com nota {media_do_aluno}!')
	else:
		print(f'O aluno foi reprovado com nota {media_do_aluno}.')
		
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Agora só precisamos chamar uma única
# função!
verificar_aluno(nota1, nota2)


