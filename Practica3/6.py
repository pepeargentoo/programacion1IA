"""
Escribir un programa que le pregunte a las personas su
fecha de cumplea˜nos y en base a eso imprimir
su signo zod´ıaco. Recomendaci´on, pedirle a la persona
ingresar la fecha con cierto formato, por ejemplo
DD/MM y si la persona no lo respeta, imprimir un mensaje de error.
"""


def validate(fecha):
    if len(fecha) == 5:
        tmp = fecha.split("/")
        try:
            tmp[0] = int(tmp[0])
            tmp[1] = int(tmp[1])
            if (tmp[0] >= 1 and tmp[0] <= 31) and (
                    tmp[1] >= 1 and tmp[1] <= 12):
                return True
            else:
                return False
        except BaseException:
            return False
    else:
        return False


def date_valid(mes, dias):
    if mes == 2 and dias > 29:
        return False

    if mes == 4 and dias > 30:
        return False

    if mes == 6 and dias > 30:
        return False

    if mes == 9 and dias > 30:
        return False

    if mes == 11 and dias > 30:
        return False
    return True


def get_sign(fecha):
    tmp = fecha.split("/")
    dias = int(tmp[0])
    mes = int(tmp[1])
    if date_valid(mes, dias):
        print("llego aca", mes, dias)
        # aca solo falta definir dia por signo pero me dio paja
    else:
        return "La fecha no es valida"


fecha = input("fecha = fecha de cumpleaños DD/MM: \n")
if validate(fecha):
    print(get_sign(fecha))
else:
    print("Formato erroneo de fecha dd/mm")
