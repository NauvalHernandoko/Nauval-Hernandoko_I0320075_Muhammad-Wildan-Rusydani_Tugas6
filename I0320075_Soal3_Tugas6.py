print('=====Bilangan Prima dan Bukan Prima=====')
for x in range(10,25):
    if x >= 10:
        for i in range(2, x):
            if x % i == 0:
                print(x, 'bukan bilangan prima')
                break
        else:
            print(x, 'adalah bilangan prima')
    else:
        print()