import os
import json

persons = []
file_name = 'base-personas.txt'


def load_data():
    base = open(file_name, 'r')
    json_object = json.load(base)
    return list(json_object)


def list_person():
    os.system('cls')
    print(' ------- Listado de personas -------\n')
    print('Nº |  NOMBRE ')

    if (len(persons) > 0):
        for i in range(len(persons)):
            print('-------------------------------')
            print((i + 1), ' | ', persons[i]["name"], persons[i]["last_name"])
    else:
        print('No hay personas registradas')

    print('\n')
    os.system('pause')


def write_to_file():
    json_object = json.dumps(persons, indent=4)
    with open(file_name, 'w') as base:
        base.write(json_object)
        base.close()


def add_person():
    os.system('cls')
    name = input('Ingrese el nombre: ')
    last_name = input('Ingreso el apellido: ')
    email = input('Ingrese el correo: ')
    salary = input('Ingrese el salario $: ')
    phone = input('Ingrese el numero telefonico: ')
    address = input('Ingrese la dirección: ')
    dui = input('Ingrese el numero de DUI: ')

    person = {
        'name': name,
        'last_name': last_name,
        'email': email,
        'salary': salary,
        'phone': phone,
        'address': address,
        'dui': dui
    }

    persons.append(person)
    write_to_file()

    os.system('pause')


def delete_person():
    os.system('cls')
    dui = input('Ingrese el numero de DUI: ')

    for person in persons:

        if dui.lower() in person['dui'].lower():
            print('Persona a eliminar: ', person["name"], "con el No.", person["dui"])
            eliminar = input('¿Desea eliminarla? (si/no): ')

            if eliminar == 'si' | 's':
                persons.remove(person)
                write_to_file()
                print('Persona eliminada.')

    os.system('pause')

def refresh_person():
    modificar =""
    os.system('cls')
    dui_persona = input('Ingrese el DUI de la persona a modificar: ')
    for i in persons:
        if dui_persona == i['dui']:
            modificar = input('¿Desea modificar dato? (si/no): ')
            if modificar == 'si':
                name =  input('Ingrese nombre: ')    
                i['name'] =  name if name != "" else i['name']
                apellido = input('Ingrese apellido: ')  
                i['last_name'] =  apellido if apellido != "" else i['last_name']
                correo = input('Ingrese nuevoa dirección de correo: ')
                i['email'] = correo if correo != "" else i['email']
                salario = input('Ingrese valor de salario: ')
                i['salary'] = salario if salario != "" else i['salary']
                telefono = input('Ingrese numero de telefono: ')
                i['phone'] = telefono if telefono != "" else i['phone']
                direccion = input('Ingrese nueva dirección: ')
                i['address'] = direccion if direccion != "" else i['address']
                dui = input('Ingrese número de DUI: ')
                i['dui'] = dui if dui != "" else i['dui']
            
                write_to_file()
                print('campo modificado')
                os.system('pause')
                return
            else:
                return

op = ''

# Load content to persons list
persons = load_data()

while(op != 'exit'):
    os.system('cls')
    print('---------- Menu ----------')
    print('(1)..... Listar personas')
    print('(2)..... Agregar personas')
    print('(3)..... Actualizar datos')
    print('(4)..... Eliminar persona')
    print('(exit).. Salir')
    print('\n')
    op = input('Ingrese una opción: ')

    if op == '1':
        list_person()
    elif op == '2':
        add_person()
    elif op == '3':
        refresh_person()
    elif op == '4':    
        delete_person()
    elif op == 'exit':
        print('Fin del programa')
    else:
        print('Opción no válida')
        os.system('pause')
