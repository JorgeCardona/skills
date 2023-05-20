def suma(x, y):
    
    resultado =  x + y
    print(f'el resultado de la SUMA {x} + {y} es {resultado}')

def resta(x, y):
    
    resultado =  x - y
    print(f'el resultado de la RESTA  {x} - {y}es {resultado}')

def multiplicacion(x, y):
    
    resultado =  x * y
    print(f'el resultado de la MULTIPLICACION  {x} * {y} es {resultado}')

def division_decimal(x, y):
    
    resultado =  x / y
    print(f'el resultado de la DIVISION DECIMAL {x} / {y} es {resultado}')

def division_entera(x, y):
    
    resultado =  x // y
    print(f'el resultado de la DIVISION ENTERA {x} // {y} es {resultado}')

def potencia(x, y):
    
    resultado =  x ** y
    print(f'el resultado de la POTENCIA  {x} elevado a {y} es {resultado}')
 
def raiz_cuadrada(x, y):
    import math
    
    resultado =  math.sqrt(abs(x + y))
    print(f'el resultado de la raiz cuadrada del valor absoluto de {x} + {y} es {resultado}')

def logaritmo(x, y):
    import math
    
    resultado = math.log(abs(x), abs(y))
    print(f'el logaritmo del valor absoluto de {x} en base {y} es {resultado}')

def piso(x, y):
    import math
    
    resultado = math.floor(x/y)
    print(f'el piso de {x} dividido {y} es {resultado}')

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