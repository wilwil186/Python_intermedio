"""
La propiedad más conocida de estos números es que si p es primo;
p divide a X(p). 
Por ejemplo, X(11)=22, que es múltiplo de 11
"""
def perrin(n):
    perrin = [3, 0, 2]
    for i in range(1, n+1):
        if i > 2:
            perrin.append(perrin[-2]+perrin[-3])
    return perrin

def es_primo(n):
    numeros_primos = [2]
    for i in range(3, n+1):
        if i % perrin[i] == 0: 
            numeros_primos.append(i)
    return numeros_primos
            

def run():
    n = input('Ingresa un número: ')
    assert n.isnumeric() and int(n) > 2, "debe ingresar UN NUMERO MAYOR QUE DOS"
    print(es_primo(int(n)))

if __name__ == '__main__':
    run()