#Projeto para imprimir a quantidade de números da sequência de fibonacci que o usuário desejar
def fibonacci (contador):
    c = contador
    num1 = 1
    fib = 1
    print ('1')
    print ('1')
    for x in range (1, c-1):
        num2 = fib
        fib = num1 + num2
        print (fib)
        num1 = num2

c = int(input('Quanto números da sequência de fibonacci você quer conhecer?'))
fibonacci(c)
