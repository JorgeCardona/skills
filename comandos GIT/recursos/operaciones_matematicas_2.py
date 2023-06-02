def logaritmo(x, y):
    import math
    
    resultado = math.log(abs(x), abs(y))
    print(f'el logaritmo del valor absoluto de {x} en base {y} es {resultado}')

def piso(x, y):
    import math
    
    resultado = math.floor(x/y)
    print(f'el piso de {x} dividido {y} es {resultado}')
