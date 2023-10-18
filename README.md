# Reto_9

1.De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
para este punto tome tres funciones y las cambie de tal manera que las funciones se pueden definir de una manera mas corta usando lambda

    1.1. este primer programa se basa en el calculo de la pobliacion contagiada a partir de una tasa de contagios y una poblacion inicial.

```pseudocode
    if __name__ == "__main__":
        p= int(input("ingresa la poblacion inicial:"))
        d= int(input("ingresa los dias transcurridos:"))
        contagt= lambda p,d: p*(2**d)
        contag= contagt (p,d)
        print("la poblacion contagiada es de " +str(contag))
```

    1.2. el segundo programa se basa en el codigo creado en el reto anterior, el cual calculaba la cantidad de carne total dadas ciertas generalidades sobre los pesos de cada tipo de carne.

```pseudocode
    Gallina = 6
    Gallo = 7
    pollo = 1

    if __name__ == "__main__":
        n= int(input("ingresa la cantidad de gallinas:"))
        m= int(input("ingresa la cantidad de gallos:"))
        k= int(input("ingresa la cantidad de pollos:"))
        carneT= lambda n,m,k: n*Gallina + m*Gallo + k*pollo
        carne = carneT(n,m,k)
        print("la cantidade de carne en total es " +str(carne)+ "Kg")
```

    1.3. para el tercer programa utilice el codigo del reto anterior cuya funcion era calcular el interes compuesto dado un capital, interes y ls años a evaluar.
    
```pseudocode
    if __name__ == "__main__":
        ci= int(input("ingresa el capital prestado:"))
        i= int(input("ingresa el interes anual:"))
        n= int(input("ingresa los años a los que quieres proyectr el interes:"))
        intercompuest= lambda ci,i,n: ci*(1+ i)**n
        capital= intercompuest(ci,i,n)
        print("el capital final es de " +str(capital))
```


2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

   para el desarrollo de este punto me base en funciones que se basaban en ciertos paramentros solicutados con anterioridad, posteriormente los cambie de modo que dichos paramentros se cambiaran por argumentos que se definiran despues.

   2.1. el promer programa es el codigo desarrollado con anterioridad para calcular el area superficial de una figura dada

![figura 1 reto 9](https://github.com/AndresBustamant/Repo-6/assets/141858005/deb0f541-dc75-4e3f-b84d-5dd3e5df225d)


  ```pseudocode
import math
def area_esfera(*args) -> float:
    areaesfe= 4* math.pi* r1**2
    return areaesfe
def area_cono(*args) -> float:
    areacon= math.pi*r2(r2+ (r2**2+h**2)**1/2)
    return areacon
def volumen_esfera(*args) -> float:
    volumenesfe= (4* math.pi*r1**3)/3
    return volumenesfe
def volumen_cono(*args) -> float:
    volumencon= (math.pi*r2**2*h)/33
    return volumencon

def volumen_total(*args) -> float:
    return (math.pi*r2**2*h)/3 + (4* math.pi*r1**3)/3
def area_total(*args) :
    return (4* math.pi* (r1**2)) + (math.pi*r2*(math.sqrt(r2+ (r2**2+h**2))))

if __name__ == "__main__":
    r1= int(input("ingresa el radio de la esfera:"))
    r2= int(input("ingresa el radio del cono:"))
    h= int(input("ingresa la altura del cono:"))
    volumen= volumen_total(r1,r2,h)

    area= area_total(r1,r2,h)
    print("el voluen superficial de la figura es " +str(volumen))
    print("el area superficial de la figura es " +str(area))
  ```
   2.2. el segundo programa se basa en el calculo del area de una figura dada

![figura 2 reto 9](https://github.com/AndresBustamant/Repo-6/assets/141858005/f9b710ca-b5e3-45fd-9b4c-8de629c38740) 

 ```pseudocode
import math
def area_base_circular(*args) -> float:
    area_circular= math.pi*r**2
    return area_circular
def area_cuadrada(*args) -> float:
    area_cuadrado= 2*math.pi* a*b
    return area_cuadrado
def area_total(*args) -> float:
    areat= 2*math.pi*a*b + 2*math.pi*r**2
    return areat
def perimetro_base_circular(*args) -> float:
    perimetro_circular= 2*math.pi*r
    return perimetro_circular
def perimetro_cuadrada(*args) -> float:
    perimetro_cuadrado= a*b
    return perimetro_cuadrado
def perimetro_total(*args) -> float:
    perimetrot= 2*math.pi*r + a*b
    return perimetrot
if __name__ == "__main__":
    r= int(input("ingresa el radio de la base:"))
    b= int(input("ingresa lo que mide la base cuadrada:"))
    a= int(input("ingresa la altura de la parte cuadrada:"))
    area= area_total(r,a,b)
    perimetro= perimetro_total(r,a,b)
    print("el perimetro superficial de la figura es " +str(perimetro))
    print("el area superficial de la figura es " +str(area))
 ```

   2.3. por ultimo el cerser programa se fundamenta en el calculo de las devueltas de una compra de ciertos elementos con un presupuesto dado

 ```pseudocode
panes = 300
leche = 3300
huevos = 350
B:int
def precio_a_pagar (*args) ->int:
    precio_panes= p*panes
    precio_leche= m*leche
    precio_huevos= h*huevos
    precio_total= (p*panes)+(m*leche)+(h*huevos)
    devuelta= B - precio_total
    if devuelta<0:
        print("hace falta dinero para pagar")
    else:
      return devuelta

if __name__ == "__main__":
    p= int(input("ingresa la cantidad de panes:"))
    m= int(input("ingresa la cantidad de bolsas de leche:"))
    h= int(input("ingresa la cantidad de huevos:"))
    B= int(input("ingresa la cantidad de dinero que te dieron: "))
    devueltas= precio_a_pagar(p,m,h)
    print("la cantidade de dinero restante es " +str(devueltas))
 ```

3.Escriba una función recursiva para calcular la operación de la potencia. 

- para este punto base la recursividad en tres casos el primero es entender que la pontencia 0 de cualquier numero es 1, el segundo es entender que la potencia 1 en cualquier numero es si mismo y por ultimo la potencia n de un numero es el numero elevado a la n; dados estos casos plantee un programa con tres condicionales recursivas las cuales permitiran calcular la potencia de una base y un exponente dado

 ```pseudocode
  n: int
i: int
def potencia(n:int, i:int)->int:
  if i==0:
    return 1
  elif i==1:
    return n
  else:
    return n**i

if __name__ == "__main__":
  n = int(input("Ingrese numero base de la potencia: "))
  i = int(input("ingresa el expinente de la potencia: "))
  resultpotencia = potencia(n,i)
  print("el resultado de la potencia con base " + str(n) + " elevadas a " +str(i)+ " es " + str(resultpotencia))
 ```
4. Utilice la siguiente plantilla de code para contar el tiempo:

 ```pseudocode
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
 ```

Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.

programa implementando el medidor de tiempo:

 ```pseudocode
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
 ```

analisis: al evaluar en varios casos se puede evidenciar que al ingresar un numero entre 1-100 el tiempo estimado ronda entre 2 a 2,5 segundos; por tro lado al inngresar numeros como 1000 o mayores se puede evidenciar una diferencia nototria ya que pasa de 2 segundos a 4 segundos en su proceso de realizacion.

5.Crear cuenta en stackoverflow y adjuntar imagen en el repo

![stackoverflow](https://github.com/AndresBustamant/Reto_9/assets/141858005/ed68aadd-9c9c-485c-8cdc-64310c8e5a0c)

6. Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

https://www.linkedin.com/public-profile/settings
