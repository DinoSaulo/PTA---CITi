def funcaoPar(x):
    if (x % 2) == 0:
        return True
    else:
        return False
num = int(input('digite um número : '))

if funcaoPar(num) == True:
    print('o número {} é par' .format(num))
else:
    print('O Número {} é impar' .format(num))