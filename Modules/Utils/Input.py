from Modules.Utils import Special_msgs as msg


def integer(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            return value
        except ValueError:
            msg.red("Debe ser un número entero no vacío. Intente de nuevo.")
            continue


def string(prompt):
    while True:
        value = input(prompt)
        if value:
            return value
        msg.red("No puede estar vacío. Intente de nuevo.")


def char(prompt):
    while True:
        value = input(prompt)
        if len(value) == 1:
            return value
        msg.red("Debe ser un carácter. Intente de nuevo.")
