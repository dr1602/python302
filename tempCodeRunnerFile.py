data = [21, 17, 35, '🍎', 40, 15]

for index, item in enumerate(data):
    try:
        if item >= 18:
            print(f'El número {item} es mayor de edad.')
        else:
            print(f'El número {item} es menor de edad.')
    except:
        print(f'Este elemento no es un número.')
