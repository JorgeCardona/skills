def potencia(x, y):
    
    resultado =  x ** y
    print(f'el resultado de la POTENCIA  {x} elevado a {y} es {resultado}')
 
def raiz_cuadrada(x, y):
    import math
    
    resultado =  math.sqrt(abs(x + y))
    print(f'el resultado de la raiz cuadrada del valor absoluto de {x} + {y} es {resultado}')
    
def techo(x, y):
    import math
    
    resultado = math.ceil(x/y)
    print(f'el techo de {x} dividido {y} es {resultado}')

def factorial(x, y):
    import math
    
    resultado = math.factorial(abs(x)) + math.factorial(abs(y))
    print(f'la suma del factorial de {x} mas, la suma del factorial de {y} es {resultado}')

def imaginarios(x, y):
    
    resultado = x * y
    print(f'la multiplicacion del numero imaginario {x} con el numero imaginario {y} es {resultado}')