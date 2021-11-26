from base import empleados
import os


def list_person():
    print("Listado de empleados:")
    cont = 1
    for person in empleados:
        print(str(cont) + " - " + person["name"])
        cont += 1


def friends(id):
    for person in empleados:
        if person["id"] == id:
            print("\nLos amigos de " + person["name"] + " son:")
            for item in person["friends"]:
                print(item["name"])
            return
    print("Empleado no encontrado")


def salary_less_2000():
    cont = 1
    for person in empleados:
        if float(person["salary"].replace(",", "")) < 2000:
            print(str(cont) + " - " + person["name"] + " -- $" + person["salary"])
            cont += 1


def update_person(id):
    for person in empleados:
        if person["id"] == id:
            name = input("Ingrese el nombre: ")
            salary = input("Ingrese el salario: ")
            age = input("Ingrese la edad: ")
            gender = input("Ingrese el genero: ")
            email = input("Ingrese el correo: ")

            person["name"] = name
            person["salary"] = salary
            person["age"] = int(age)
            person["gender"] = gender
            person["email"] = email

            print("Empleado actualizado")
            os.system("PAUSE")
            return
    print("Empleado no encontrado")
    os.system("PAUSE")


def person_information(id):
    for person in empleados:
        if person["id"] == id:
            print("\n")
            print("Nombre: " + person["name"])
            print("Salario: $" + person["salary"])
            print("Edad: " + str(person["age"]))
            print("Genero: " + person["gender"])
            print("Correo: " + person["email"])
            if person["isActive"]:
                print("Estado: activo")
            else:
                print("Estado: inactivo")
            print("\n")


def search_by_name():
    os.system("cls")
    name = ""
    while name != "0":
        print("(0) Salir de busqueda")
        name = input("\nNombre a buscar: ")
        cont = 0
        if name == "0":
            break

        for person in empleados:
            if name.lower() in person["name"].lower():
                cont += 1
                print("(id: " + str(person["id"]) + ") " + person["name"])

        if cont == 0:
            print("El empleado no existe")
        else:
            id = input("Ver información de (id): ")
            if id != "0":
                person_information(int(id))
        os.system("PAUSE")
        os.system("cls")


def delete_person(id):
    for index in range(len(empleados)):
        if empleados[index]["id"] == id:
            print(empleados[index]["name"])
            op = input(
                "Seguro que deseas eliminar a "
                + empleados[index]["name"]
                + " (si o no): "
            )
            if op == "si":
                del empleados[index]
            os.system("PAUSE")
            return
    print("Empleado no encontrado")
    os.system("PAUSE")


def tributar():
    edad = int(input("Ingrese su edad"))
    ingresos = float(input("Ingrese sus ingresos"))

    if edad >= 16 and ingresos >= 1000:
        print("Usted debe de tributar")
        return

    print(" No es necesario que haga el tributo")


op = ""
while op != "0":
    os.system("cls")
    print("Menu:\n")
    print("(1) Listar empleados")
    print("(2) Imprimir Amigos")
    print("(3) Salario menor a 2000")
    print("(4) Buscar empleado")
    print("(5) Actualizar empleado")
    print("(6) Eliminar empleado")
    print("(0) Salir")
    op = str(input("Ingrese una opcion:"))
    print("\n")

    if op == "1":
        list_person()
        print("\n")
        os.system("PAUSE")
    elif op == "2":
        id = int(input("Id de empleado:"))
        friends(id)
        print("\n")
        os.system("PAUSE")
    elif op == "3":
        salary_less_2000()
        print("\n")
        os.system("PAUSE")
    elif op == "4":
        search_by_name()
    elif op == "5":
        id = int(input("Id de empleado: "))
        update_person(id)
    elif op == "6":
        id = int(input("Id de empleado: "))
        delete_person(id)
    elif op == "0":
        print("\nBye bye ...")
    else:
        print("Opcion no valida")
        print("\n")
        os.system("PAUSE")
