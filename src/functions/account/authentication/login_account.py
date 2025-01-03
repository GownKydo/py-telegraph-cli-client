from functions.account.account import getAccountInfo
from functions.account.management.edit_account import editAccountInfo
from functions.account.utils.remove_access_token import revokeAccessToken
from functions.utils.clear_screen import clear

def login(access_token: str):
    """
    Inicio de sesión en cuenta existente.

    Args:
        access_token (str): Token de acceso a una cuenta existente.
    Returns:
        bool: Retorna False cuando se termina el inicio de sesión.
    Example:
        >>> login(
            "f1c7cc248f2d3e1fea44c28a0b93148e4dea0e7a24b7cfe791a993a13413"
            )
        False
    """
    while True:
        account = getAccountInfo(access_token)

        if account.ok:
            print("\nEsta es una sesión temporal")
            print(f"Hola, {account.short_name} ({account.author_name})")
            print()
            print("1. Mostrar información")
            print("2. Editar Información")
            print("3. Crear nuevo token de acceso")
            print("0. Salir")
            user_input = input("> ")

            if user_input == "1":
                print("1. Mostrar Información Pública")
                print("2. Mostrar Información Pública y Privada")
                print("0. Regresar")
                user_input = input("> ")

                if user_input == "1":
                    clear()
                    account.printInfo("default")
                elif user_input == "2":
                    clear()
                    account.printInfo("all")
                elif user_input == "0":
                    clear()
                else:
                    clear()
                    print("Entrada no válida. Regresando al menú principal")
            elif user_input == "2":
                print("1. Cambiar nombre corto")
                print("2. Cambiar autor")
                print("3. Cambiar URL de autor")
                print("0. Regresar")
                user_input = input("> ")

                if user_input == "1":
                    clear()
                    print("Ingresar nuevo nombre corto")
                    new_short_name = input("> ")

                    editAccountInfo(access_token, "short_name", new_short_name)
                elif user_input == "2":
                    clear()
                    print("Ingresar nuevo autor")
                    new_author_name = input("> ")

                    editAccountInfo(access_token, "author_name",
                                    new_author_name)
                elif user_input == "3":
                    clear()
                    print("Ingresar nueva URL")
                    new_author_url = input("> https://")
                    new_author_url = f"https://{new_author_url}"

                    editAccountInfo(access_token, "author_url", new_author_url)
                elif user_input == "0":
                    clear()
                else:
                    clear()
                    print("Entrada no válida. Regresando al menú principal")
            elif user_input == "3":
                clear()
                print("Ingresar 'OK' si deseas cerrar todas las sesiones, "
                      "generar nuevo token de acceso y generar nueva URL "
                      "para navegadores web\n"
                      "Después de ingresar 'OK' se te proporcionará un nuevo "
                      "token y nueva URL para navegadores web. Guardar el "
                      "nuevo token ya que es la unica forma de acceder "
                      "a la cuenta\n"
                      "Una vez generado el nuevo token de acceso, el token "
                      "anterior quedará inutilizable")
                user_input = input("> ")

                if user_input == "OK":
                    revokeAccessToken(access_token)

                    while True:
                        print(
                            "Si ya has guardado tu nuevo token de acceso, "
                            "ingresa 'EXIT' para cerrar del programa"
                        )
                        user_input = input("> ")

                        if user_input == "EXIT":
                            print("Cerrando programa")

                            return False
                else:
                    print("Acción cancelada")
            elif user_input == "0":
                print("Saliendo...")

                return False
            else:
                print("Entrada no válida")
        else:
            print("La cuenta no existe.")
            print(f'Token "{account.access_token}" no válido')

            return False