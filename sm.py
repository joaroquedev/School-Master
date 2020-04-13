import os
import math

def banner():
	os.system('clear')
	logo_menu = """
	      _____      _                 _ __  __       _   _
	     / ____|    | |               | |  \/  |     | | | |
	    | (___   ___| |__   ___   ___ | | \  / | __ _| |_| |__
	     \___ \ / __| '_ \ / _ \ / _ \| | |\/| |/ _` | __| '_ 
	     ____) | (__| | | | (_) | (_) | | |  | | (_| | |_| | | |
	    |_____/ \___|_| |_|\___/ \___/|_|_|  |_|\__,_|\__|_| |_|
	    ╔══════════════════════════════════════════════════════╝
	    ╚[04-2020]══════════════[Joa Roque]═════════════[V.1.0]$\n
	    2 - Calcular Média
	    1 - Cálculos Básicos
	    3 - Calcular Idade.
	    0 - Sair
	    """
	print(logo_menu)

def media():
	nota1 = int(input("Digite a primeira nota: "))
	nota2 = int(input("Digite a segunda nota: "))
	nota3 = int(input("Digite a terceira nota: "))
	media = (nota1+nota2+nota3)/2
	print("\t\t1º - Trimestre: {}\n\t\t2º - Trimestre: {}\n\t\t3º Trimestre: {}".format(nota1,nota2,nota3))

	if media >= 10:
		print("\t\tAprovado\nMedia: {}".format(media))
	elif media == 9:
		print("\t\tRecurso\nMedia: {}".format(media))
	else:
		print("\t\tReprovado\nMedia: {}".format(media))
	pass

def calc_basico():
	print("""
		[2- CÁLCULOS BÁSICOS:]

		1 - Multiplicação
		2 - Adição
		3 - Subtração
		4 - Divisão
		5 - Raíz Quadrada
		6 - Tabuada
		7 - Sair
	""")

	#-------[Funcões]-------#
	#-Multiplicação
	def mult(num1,num2):
		d = num1*num2
		print("\t\t{} x {} = {}".format(num1,num2,d))
		pass
	#-Adição
	def add(num1,num2):
		d = num1+num2
		print("\t\t{} + {} = {}".format(num1,num2,d))
		pass
	#-Subtração
	def sub(num1,num2):
		d = num1-num2
		print("\t\t{} - {} = {}".format(num1,num2,d))
		pass
	#-Divisão
	def div(num1,num2):
		d = num1/num2
		print("\t\t{} / {} = {}".format(num1,num2,d))
		pass
	#-Raiz
	def raiz(num):
		d = math.sqrt(num)
		print("\t\tA raíz quadrada de {} é: {}".format(num,d))
		pass
	def tab(num1,num2):
		for num1 in range(num2):
			print(num1)
		#print("\t\t{}".format(d))
		pass

	op = int(input("Escolha uma opção: "))
	if op == 1:
		n1 = int(input("\t\tDigite 1º número: "))
		n2 = int(input("\t\tDigite 2º número: "))
		mult(n1,n2)
		pass

	elif op == 2:
		n1 = int(input("\t\tDigite 1º número: "))
		n2 = int(input("\t\tDigite 2º número: "))
		add(n1,n2)
		pass

	elif op == 3:
		n1 = int(input("\t\tDigite 1º número: "))
		n2 = int(input("\t\tDigite 2º número: "))
		sub(n1,n2)
		pass
	
	elif op == 4:
		n1 = int(input("\t\tDigite 1º número: "))
		n2 = int(input("\t\tDigite 2º número: "))
		div(n1,n2)
		pass
	elif op == 5:
		n1 = int(input("\t\tDigite um número: "))
		raiz(n1)
		pass
	elif op == 6:
		n1 = int(input("\t\tDigite 1º número: "))
		n2 = int(input("\t\tDigite 2º número: "))
		tab(n1,n2)
		pass
	else:
		print("\t\tOpção inexistente!")
		pass
	pass

def calc_idade():
	idade = int(input("Digite a tua idade: "))
	i = 6
	if idade < i:
		print("\t\tCriancinha vai para cresce")
	elif idade < 10 & idade >= i:
		print("\t\tEnsino: Regular\nPeríodo: Manhã\nTurma: A")
	elif idade > 10 & idade <= 15:
		print("\t\tEnsino: Regular\nPeríodo: Manhã\nTurma: B")
	else:
		print("\t\tEnsino: Adulto\nPeríodo: Noite\nTurma: C")
	pass

def main():
	banner()
	op = int(input("Escolha uma opção: "))
	if op == 1:
		media()
	elif op == 2:
		calc_basico()
	elif op == 3:
		calc_idade()
	else:
		banner()
if __name__ == '__main__':
	main()