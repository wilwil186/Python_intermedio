def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 1:
            divisors.append(i)
    return divisors


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric() and int(num) > 0, "¡ya la cago! debe ingresar UN NUMERO MAYOR QUE CERO"
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()