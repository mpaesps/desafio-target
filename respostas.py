// Resposta 1

indice = 13
soma = 0 
k = 0

while(k < indice):
    k = k + 1
    soma = soma + k

print(soma);

// Resposta 2 

def verifica_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n
	
numero = 34
if verifica_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

// Resposta 3 

/* 
3a)9
3b)128
3c)49
3d)100
3e)13
3f)200
*/

// Resposta 4

/*
Entendendo que há 3 salas cada um com uma lâmapda:
Na primeira ida:

- Ligo o interruptor  1 por 5 minutos e o desligo, ligo oo interruptor 2 e na mesma hora vou até uma das 3 salas
- Se a lampada estiver acessa, pertence ao interruptor 2, se estiver desligada e quente pertence ao interruptor 1, se estiver desligada e fria pertence ao interruptor 3.

Na segunda ida:
- Sabendo já a qual pertence um interruptor, apenas deixo um ligado e outro desligado entre o restantes
- Vou até outra sala e descubro os outros dois.
*/

  // Resposta 5

def inverte_string(str):
    inversa = ''
    for i in range(len(str) - 1, -1, -1):
        inversa += str[i]
    print(f"Palavra invertida: {inversa}")

# Exemplo de uso
inverte_string("exemplo")
