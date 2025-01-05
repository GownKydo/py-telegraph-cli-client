from functions.account.account import getAccountInfo
from functions.account.management.edit_account import editAccountInfo
from functions.account.utils.remove_access_token import revokeAccessToken
from functions.utils.clear_screen import clear
from styles.styles import StrStyle

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
            print(f"\n{StrStyle.SUCCESS}Esta es una sesión temporal{StrStyle.ENDC}")
            print(f"{StrStyle.SUCCESS}Hola, {account.short_name} ({account.author_name}){StrStyle.ENDC}")
            print()
            print(f"{StrStyle.INFO}1. Mostrar información{StrStyle.ENDC}")
            print(f"{StrStyle.INFO}2. Editar Información{StrStyle.ENDC}")
            print(f"{StrStyle.INFO}3. Crear nuevo token de acceso{StrStyle.ENDC}")
            print(f"{StrStyle.INFO}0. Salir{StrStyle.ENDC}")
            user_input = input("> ")

            if user_input == "1":
                print(f"{StrStyle.INFO}1. Mostrar Información Pública{StrStyle.ENDC}")
                print(f"{StrStyle.INFO}2. Mostrar Información Pública y Privada{StrStyle.ENDC}")
                print(f"{StrStyle.INFO}0. Regresar{StrStyle.ENDC}")
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
                    print(f"{StrStyle.FAIL}Entrada no válida. Regresando al menú principal{StrStyle.ENDC}")
            
            elif user_input == "2":
                print(f"{StrStyle.INFO}1. Cambiar nombre corto{StrStyle.ENDC}")
                print(f"{StrStyle.INFO}2. Cambiar autor{StrStyle.ENDC}")
                print(f"{StrStyle.INFO}3. Cambiar URL de autor{StrStyle.ENDC}")
                print(f"{StrStyle.INFO}0. Regresar{StrStyle.ENDC}")
                user_input = input("> ")

                if user_input == "1":
                    clear()
                    print(f"{StrStyle.INFO}Ingresar nuevo nombre corto{StrStyle.ENDC}")
                    new_short_name = input("> ")
                    editAccountInfo(access_token, "short_name", new_short_name)
            
                elif user_input == "2":
                    clear()
                    print(f"{StrStyle.INFO}Ingresar nuevo autor{StrStyle.ENDC}")
                    new_author_name = input("> ")
                    editAccountInfo(access_token, "author_name", new_author_name)
            
                elif user_input == "3":
                    clear()
                    print(f"{StrStyle.INFO}Ingresar nueva URL{StrStyle.ENDC}")
                    new_author_url = input("> https://")
                    new_author_url = f"https://{new_author_url}"
                    editAccountInfo(access_token, "author_url", new_author_url)
            
                elif user_input == "0":
                    clear()
            
                else:
                    clear()
                    print(f"{StrStyle.FAIL}Entrada no válida. Regresando al menú principal{StrStyle.ENDC}")
            
            elif user_input == "3":
                clear()
                print(f"{StrStyle.INFO}Ingresar 'OK' si deseas cerrar todas las sesiones, "
                    "generar nuevo token de acceso y generar nueva URL para navegadores web\n"
                    "Después de ingresar 'OK' se te proporcionará un nuevo token y nueva URL para navegadores web. "
                    "Guardar el nuevo token ya que es la unica forma de acceder a la cuenta\n"
                    "Una vez generado el nuevo token de acceso, el token anterior quedará inutilizable{StrStyle.ENDC}")
                user_input = input("> ")

                if user_input == "OK":
                    revokeAccessToken(access_token)

                    while True:
                        print(f"{StrStyle.INFO}Si ya has guardado tu nuevo token de acceso, ingresa 'EXIT' para cerrar del programa{StrStyle.ENDC}")
                        user_input = input("> ")

                        if user_input == "EXIT":
                            print(f"{StrStyle.SUCCESS}Cerrando programa{StrStyle.ENDC}")
                            return False
                else:
                    print(f"{StrStyle.FAIL}Acción cancelada{StrStyle.ENDC}")
            
            elif user_input == "0":
                print(f"{StrStyle.SUCCESS}Saliendo...{StrStyle.ENDC}")
                return False
            
            else:
                print(f"{StrStyle.FAIL}Entrada no válida{StrStyle.ENDC}")
        
        else:
            print(f"{StrStyle.FAIL}La cuenta no existe.{StrStyle.ENDC}")
            print(f'{StrStyle.FAIL}Token "{account.access_token}" no válido{StrStyle.ENDC}\n')
            return False
