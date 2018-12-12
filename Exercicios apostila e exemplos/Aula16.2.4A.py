#Aula 16 exercicio 1,2,3,4
#Adicionar 4 metodos novos. Distancia entre 2 pontos, Refexão do ponto em x, inclinação da reta e eq. da reta entre 2 pontos.
class ponto:
	def __init__(self, x=0, y=0):
#__int__ é o nome da variavel especial do python, assim como o main uasdo em modulo.
		'''cria um novo ponto posicionado na origem'''
		self.x=x  #self é uma palavra chave. Dentro dela mesma.
		self.y=y
#DICA: from ponto import * 

	def distancia_da_origem(self):
		""" Calcula minha distânica da origem """
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5
	def ponto_medio(self, alvo):
		""" Retorna o ponto medio entre esse ponto e o alvo """
		mx = (self.x + alvo.x)/2
		my = (self.y + alvo.y)/2
		return ponto(mx, my) #retorna a propria claase, um objeto que é um ponto
	def __str__(self):
		return "({0}, {1})".format(self.x, self.y)

	def  dist_ponto(self,alvo):
		r=self.distancia_da_origem(); R=alvo.distancia_da_origem()
		D=abs(R-r)
		return(D) 
	
	def reflexao_x(self):
		self.y = -self.y
		return self
	
	def inclinacao_origem(self, alvo):
		print("teste")
		inc = (self.y-alvo.y)/(self.x-alvo.x)
		return inc

	def parametros_reta(self,alvo):		
		a = self.inclinacao_origem(alvo)
		b = alvo.y - a
		return (a,b)
		

