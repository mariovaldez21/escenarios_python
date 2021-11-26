# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

empleado = {
    "nombre": "Tito",
    "apellido": "Merino",
    "cargo": "developer",
    "estado": False,
    "edad": 28,
}

cargos = ["developer", "docente", "jefe", "administrador"]


def nombre_completo():
    return empleado["nombre"] + " " + empleado["apellido"]


def estado_civil():
    if empleado["estado"]:
        return "Casado"
    else:
        return "Soltero"


def modificar(nombre, apellido):
    empleado["nombre"] = nombre
    empleado["apellido"] = apellido


def edad():
    if empleado["edad"] < 18:
        return "Nino"
    elif empleado["edad"] < 30:
        return "Joven"
    else:
        return "Adulto"


def cargo():
    bandera = False
    for cargo in cargos:
        if cargo == empleado["cargo"]:
            bandera = True
            break

    if bandera:
        return "El cargo existe"
    else:
        return "El cargo no existe"


def cargo_mejorado():
    if empleado["cargo"] in cargos:
        return "El cargo existe"
    else:
        return "El cargo no existe"


print(nombre_completo())
print(estado_civil())
modificar("Isai", "Aguilar")
print(nombre_completo())
print(edad())
print(cargo())
print(cargo_mejorado())
