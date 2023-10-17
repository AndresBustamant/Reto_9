import time

start_time = time.time()
def fibonacci(n: int) -> int:
    i: int = 1

    n1: int =0
    n2: int =1
    print(1)
    while i <= n-1:
        sumfibo  = n1 + n2

        print(sumfibo)
        n1=n2
        n2=sumfibo
        i += 1

    return sumfibo

n = int(input("Ingrese número de elementos de la sucesión de Fibonacci: "))
sucesionFibo = fibonacci(n)
print("La sucesión de Fibonacci hasta "+str(n)+" es " +str(sucesionFibo))

end_time = time.time()

timer = end_time - start_time
print( "el tiempo es " + str(timer))