def taxes():
    renta = float(input('Ingrese su renta $: '))

    if renta <= 0:
        print('Valor no válido')
        return

    if renta < 10000:
        print("Impuesto: {0:.2f}".format(renta * 0.05))
    elif renta < 20000:
        print("Impuesto: {0:.2f}".format(renta * 0.15))
    elif renta < 35000:
        print("Impuesto: {0:.2f}".format(renta * 0.2))
    elif renta <= 60000:
        print("Impuesto: {0:.2f}".format(renta * 0.3))
    else:
        print("Impuesto: {0:.2f}".format(renta * 0.45))


def precio_sala():
    edad = int(input('Cual es su edad: '))

    if edad >= 0:
        print('Edad no válida')
        return

    if edad < 4:
        print('Entrada gratis')
    elif edad <= 18:
        print('Monto a pagar: $5')
    else:
        print('Monto a pagar: $10')


def phone_number():
    phone = input('Ingrese el numero de telefono: ')
    phone_format = phone.split('-')
    print(phone_format[1])


def numero_impar():
    cantidad = int(input('Ingrese una cantidad: '))
    impares = []
    for i in range(cantidad):
        if (i + 1) % 2 != 0:
            impares.append(str(i + 1))

    print(','.join(impares))


def invertir_palabra():
    palabra = input('Ingrese una palabra: ')
    for i in range(len(palabra) - 1, -1, -1):
        print(palabra[i], end=" ")


def buscar_palabra():
    frase = input('Ingrese una frase: ')
    palabra = input('Palabra a buscar: ')

    print(frase.count(palabra))


def cuadrado():
    return pow(((3 + 2) / (2 * 5)), 2)


def escribe_fichero():
    n = int(input('Introduce un numero entero entre 1 y 10:'))
    file_name = 'tabla-' + str(n) + '.txt'
    file = open(file_name, 'w')
    for i in range(1, 11):
        file.write(f'{n} x {i} = {n * i} \n')
    file.close()


escribe_fichero()
