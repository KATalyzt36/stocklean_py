import os
from time import sleep

from Modules.DataBase.SQLite import Database
from Modules.Utils import Color, Input, Special_msgs as msg

db_path = 'Modules/DataBase/stock.db'
db = Database(db_path)
db.create_table()

prompt = f"{Color.YELLOW}->{Color.RESET} "


def confirm(accion: str):
    msg.red(f"¿Estás seguro de {accion}?")

    print("1. Si")
    print("2. No")

    confirm_exit = Input.char(prompt)

    return confirm_exit


def answer_ver():

    clear()

    msg.green("[Menú ver producto/s]\n")

    print("1. Mostrar un producto.")
    print("2. Mostrar todos los productos.\n")

    print("0. Para volver al menú principal.")

    select_get = Input.char(prompt)

    if select_get == "1":

        clear()

        msg.green("[Un solo producto]\n")

        msg.cyan("Ingresar ID del producto.")
        item_id = Input.integer(prompt)

        clear()

        msg.green("[Producto]\n")

        if not db.get_value_from(item_id):

            return msg.red(f"ID {item_id} no encontrado.\n")

        if db.get_value_from(item_id):

            for fila in db.get_value_from(item_id):

                print(f":: ID: {fila[1]}")
                print(f":: Nombre: {fila[2]}")
                print(f":: Cantidad: {fila[3]}")
                print(f":: Precio contado: {fila[4]}")
                print(f":: Precio de lista: {fila[5]}")
                print(f":: Proveedor: {fila[6]}\n")

    elif select_get == "2":

        clear()

        msg.green("[Productos]\n")

        if not db.get_all_values():

            return msg.red("No hay productos en la base de datos.")

        for fila in db.get_all_values():

            msg.red("////////")

            print(f"ID: {fila[1]}")
            print(f"Nombre: {fila[2]}")
            print(f"Cantidad: {fila[3]}")
            print(f"Precio contado {fila[4]}")
            print(f"Precio de lista: {fila[5]}")
            print(f"Proveedor: {fila[6]}")

            msg.red("////////\n")

    elif select_get == "0":
        return

    else:
        msg.red("Ingrese una opción correcta.")
        sleep(2)
        answer_ver()


def answer_create():

    clear()

    msg.green("[Creando un articulo]\n")

    item_id = Input.integer("Codigo: ")
    if db.get_value_from(item_id):
        return msg.red(f"Un producto con el ID {item_id} ya existe. Se debe modificar.")
    name = Input.string("Nombre: ")
    quantity = Input.integer("Cantidad: ")
    price = Input.integer("Precio contado: ")
    provider = Input.string("Proveedor: ")

    db.create_item(item_id, name, quantity, price, provider)  # Accion

    msg.green("\nEl articulo fue creado correctamente.\n")


def answer_edit():

    clear()

    msg.green("[Menú de edicion]\n")

    item_id = Input.integer("ID: ")
    if not db.get_value_from(item_id):
        return msg.red(f"\nEl ID {item_id} no fue encontrado.\n")
    name = Input.string("Nombre: ")
    quantity = Input.integer("Cantidad: ")
    price = Input.integer("Precio contado ")
    provider = Input.string("Proveedor: ")

    db.update_values(item_id, name, quantity, price, provider)  # Accion

    msg.green(f"\nProducto con ID {item_id} modificado.\n")


def answer_delete():

    clear()

    msg.green("[Menú de borrado]\n")

    msg.cyan("Elegir una opción:\n")

    print(f"1. Para eliminar {Color.RED}UN SOLO{Color.RESET} articulo de la lista.")
    print(f"2. {Color.RED}BORRA TODO{Color.RESET} el contenido de la base de datos.\n")

    print(f"9. {Color.RED}ELIMINAR LA BASE DE DATOS POR COMPLETO{Color.RESET}\n")

    print("0. Volver al menú principal.")

    clear_action = Input.char(prompt)

    if clear_action == "1":

        clear()

        msg.red("Para BORRAR un articulo, ingrese su ID.\n")

        item_to_delete = Input.integer(f"ID: ")

        print()

        if not db.get_value_from(item_to_delete):
            return msg.red(f"El ID {item_to_delete} no fue encontrado.\n")

        c_delete = confirm(f"borrar el articulo {item_to_delete}.")

        if c_delete != "1":
            print()
            return

        db.clear_item(item_to_delete)  # Accion

        msg.red(f'\nEl articulo con ID {item_to_delete} fue eliminado.\n')

    if clear_action == "2":

        print()

        c_delete = confirm("borrar TODO")

        if c_delete != "1":
            return

        db.clear_table()

        msg.red("\nTODO el contenido fue borrado.\n")

    if clear_action == "9":
        print()
        c_delete = confirm("eliminar la base de datos completamente")

        if c_delete != "1":
            return

        if os.path.exists(db_path):
            os.remove(db_path)
            msg.red("\nLA BASE DE DATOS FUE TOTALMENTE ELIMINADA.\n")
        else:
            msg.cyan(f"\nNo se encontró {db_path}\n")

    if clear_action == "0":
        return


def answer_exit():

    clear()

    msg.green("[Menu de salida]\n")

    c_exit = confirm("salir")

    if c_exit != "1":
        return

    clear()
    exit()


def wrong_answer():
    msg.red("Operación no encontrada.")


def clear():
    os.system("clear")


def get_answer(answer_received):
    answer = {
        "1": answer_ver,
        "2": answer_create,
        "3": answer_edit,
        "4": answer_delete,
        "0": answer_exit
    }
    return answer.get(answer_received, wrong_answer)()


while True:
    clear()
    msg.green("[Menú principal]\n")

    print("1. Ver")
    print("2. Crear")
    print("3. Editar")
    print(f"4. {Color.RED}BORRAR{Color.RESET}")

    print("\n0. Salir")
    action = Input.char(prompt)

    get_answer(action)

    input(f"{Color.CYAN}Apretá ENTER para terminar.{Color.RESET}")

