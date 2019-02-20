# Funções em Python são definidas da seguinte maneira:
def nome_da_funcao(parametro1, parametro2, ..., parametroN):
    print('Essa mensagem aparecerá no terminal quando executar a função!')

# Funções tbm podem retornar valores. Esses valores podem ser de qualquer tipo, exemplos:
def soma(numero1, numero2):
    return numero1 + numero2 # Retorna um número (inteiro ou float)

def bem_vindo(nome):
    return f'Olá, {nome}, seja bem-vindo(a)!' # Retorna uma string

def transformar_numeros_em_vetor(numero1, numero2, numero3):
    lista = []
    lista.append(numero1)
    lista.append(numero2)
    lista.append(numero3)
    return lista # Retorna uma lista

# Ao chamar funções que tenham mais do que um parâmetro, podemos
# colocar os argumentos de cada parâmetro de duas maneiras:
    # 1) Na mesma ordem em que foram escritas na declaração
    # da função, exemplo:
    def somar(a, b):
        return a+b

    # Chamando a função:
    somar(2, 5) # Nesse caso o Python concluirá que a=2 e b=5
    somar(19, 2) # a=19 e b=2
    somar(-2.9, 8.125) # a=-2.9 e b=8.125

    # 2) Atribuindo de forma explícita a qual parâmetro queremos
    # que o argumento pertenca, exemplo:
    somar(b=19, a=21)
    somar(a=32, b=-2)
    somar(b=20, a=5)

    # P.S.: Nesse caso, não é necessário que os argumentos sejam
    # declarados na mesma ordem em que foram declarados os
    # parâmetros