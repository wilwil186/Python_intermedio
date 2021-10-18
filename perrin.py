def perrin(n):
    perrin = [3, 0, 2]
    for i in range(1, n+1):
        if i > 2:
            perrin.append(perrin[-2]+perrin[-3])
    return perrin


def run():
    n = input('Ingresa un número, mayor que dos: ')
    assert n.isnumeric() and int(n) > 2, "debe ingresar UN NUMERO MAYOR QUE DOS"
    print(perrin(int(n)))
    print("Terminó mi programa")
    
if __name__ == '__main__':
    run()