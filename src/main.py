"""
Python Telegraph CLI Client
v1.0.4

Descripción
-----------
Cliente de consola escrito en Python para Telegraph (telegra.ph),
herramienta de Blogging minimalista desarrollada por Telegram.

Módulos
-------
- requests: Para hacer peticiones a la API de Telegra.ph (telegra.ph/api).
- os: Para usar el método system() y limpiar la consola.

Funcionalidades
---------------
- Crear cuenta: Permite crear una cuenta en Telegraph.
- Inicio de sesión: Permite iniciar sesión en una cuenta existente usando un
                    token de acceso.
    - Mostrar información de la cuenta
    - Editar información de la cuenta
    - Revocar acceso a navegadores y cerrar todas las sesiones generando un
      nuevo token de acceso

Estructura del código
---------------------
Este programa usa programación modular y un poco de programación orientada a
objetos

Funciones destacables:
- main: Código principal del programa, donde inician todos los procesos.
- createAccount: Permite la creación de cuentas.
- login: Permite el inicio de sesión en una cuenta existente. Una vez iniciada
         la sesión se pueden realizar acciones como editar datos básicos,
         cerrar sesiones, accerder a cuenta desde un navegador web.
- getAccountInfo: Permite ver información de una cuenta usando su token de
                  acceso.
- editAccountInfo: Permite editar información de una cuenta como nombre corto,
                   nombre de autor y URL de autor.
- revokeAccessToken: Cierra sesiones en navegadores web y genera un nuevo
                     token de acceso.
"""

import re  # Para pseudo-verificar URLs
from styles.styles import StrStyle  # Estilos de texto con colores ANSI
from functions.account.management.account_creation import createAccount  # Función para crear cuentas
from functions.account.authentication.login_account import login  # Función para iniciar sesión
from functions.utils.clear_screen import clear  # Función para limpiar la consola

def main():
    clear()

    print(f"{StrStyle.IMPORTANT}Cliente de Consola escrito en Python para Telegra.ph{StrStyle.ENDC}\n")
    print(f"{StrStyle.INFO}1. Crear cuenta{StrStyle.ENDC}")
    print(f"{StrStyle.INFO}2. Acceder a cuenta{StrStyle.ENDC}")
    user_input = input(f"\n{StrStyle.REGULAR}> {StrStyle.ENDC}")

    if user_input == "1":
        clear()

        print(f"{StrStyle.IMPORTANT}(Obligatorio){StrStyle.ENDC}\n\n"
              f"{StrStyle.REGULAR}[*] Ingresar nombre corto para La Cuenta{StrStyle.ENDC}\n"
              f"{StrStyle.REGULAR}\t- Este nombre será usado para ayudar a identificar cuentas "
              f"en caso de tener muchas{StrStyle.ENDC}\n")

        while True:
            short_name = input(f"{StrStyle.REGULAR}> {StrStyle.ENDC}")

            if len(short_name) < 1:
                print(f"{StrStyle.WARNING}Nombre corto muy corto. Intente de nuevo.{StrStyle.ENDC}")
            elif len(short_name) > 32:
                print(f"{StrStyle.WARNING}Nombre corto muy largo. Intente de nuevo.{StrStyle.ENDC}")
            else:
                break

        clear()
        print(f"{StrStyle.IMPORTANT}\n\n(Obligatorio){StrStyle.ENDC}\n\n"
              f"{StrStyle.REGULAR}[*] Ingresar nombre del autor de los articulos{StrStyle.ENDC}\n"
              f"{StrStyle.REGULAR}\tEste nombre aparecerá como autor en futuros articulos{StrStyle.ENDC}\n")

        while True:
            author_name = input(f"{StrStyle.REGULAR}> {StrStyle.ENDC}")

            if len(author_name) < 1:
                print(f"{StrStyle.WARNING}Nombre de autor muy corto. Intente de nuevo.{StrStyle.ENDC}")
            elif len(author_name) > 128:
                print(f"{StrStyle.WARNING}Nombre de autor muy largo. Intente de nuevo.{StrStyle.ENDC}")
            else:
                break

        clear()
        print(f"{StrStyle.IMPORTANT}\n\n(Obligatorio){StrStyle.ENDC}\n\n"
              f"{StrStyle.REGULAR}Ingresar URL de autor{StrStyle.ENDC}\n"
              f"{StrStyle.REGULAR}Cuando el lector presione el nombre del autor, "
              f"será enviado a esta URL{StrStyle.ENDC}")

        while True:
            author_url = input(f"\n{StrStyle.REGULAR}> https://{StrStyle.ENDC}")

            if not author_url:
                break

            url_pattern = re.compile(
                r'(?:www\.)?'
                r'([a-zA-Z0-9-]{1,63}\.){1,}'
                r'[a-zA-Z]{2,}(?:/[a-zA-Z0-9-]+)*')

            if url_pattern.match(author_url):
                author_url = f'https://{author_url}'
                if len(author_url) > 512:
                    print(f"{StrStyle.WARNING}URL válida pero muy larga.{StrStyle.ENDC}")
                else:
                    break
            else:
                print(f"{StrStyle.FAIL}Formato de URL invalido{StrStyle.ENDC}")

        account = createAccount(short_name, author_name, author_url)

        if account.ok:
            clear()
            print(f"\n\n{StrStyle.SUCCESS}\tCuenta creada con éxito{StrStyle.ENDC}")
            account.printInfo("all")
        else:
            print(f"{StrStyle.FAIL}Error al crear cuenta{StrStyle.ENDC}")
            print(account.printInfo("ok"))

    elif user_input == "2":
        clear()

        print(f"{StrStyle.INFO}Ingresar token de acceso{StrStyle.ENDC}")
        token = input(f"{StrStyle.REGULAR}> {StrStyle.ENDC}")

        clear()
        login(token)

    else:
        print(f"{StrStyle.FAIL}Error{StrStyle.ENDC}")

if __name__ == "__main__":
    main()
