def Primo(x):
	return all(x > 1 and x % i for i in xrange(2,x))
def Suma(x):
	return sum(int(valor) for valor in str(x))

ValorInicial = raw_input("Por Favor indique el numero inicial:")
ValorInicial = int(ValorInicial)
Solucion = []
while(len(Solucion) < 2):
	ValorInicial+=1
	if(Primo(Suma(ValorInicial))and Primo(ValorInicial)):
		primes.append(ValorInicial)
print Solucion
