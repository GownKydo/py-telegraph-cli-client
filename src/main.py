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

Uso
---
~$ git clone https://github.com/ericjhernandezj/py-telegraph-cli-client.git
~$ cd py-telegraph-cli-client/
~$ python3 src/main.py

Si este programa será ejecutado en Windows, ir a la función clear() y cambiar
system("clear") por system("cls").

Autor
-----
Eric Joel Hernandez Javier (@ericjhernandezj)
https://ericjhernandezj.com
ericjhernandezj@duck.com
"""

import re  # Para pseudo-verificar URLs
from styles.styles import StrStyle  # Estilos de texto con colores ANSI
from functions.account.management.account_creation import createAccount  # Función para crear cuentas
from functions.account.authentication.login_account import login  # Función para iniciar sesión
from functions.utils.clear_screen import clear  # Función para limpiar la consola

def main():
    """Función principal del programa."""
    clear()

    print("Cliente de Consola escrito en Python para Telegra.ph")
    print()
    print("1. Crear cuenta")
    print("2. Acceder a cuenta")
    user_input = input("\n> ")

    if user_input == "1":
        clear()

        print("(Obligatorio)\n"
              "Ingresar nombre corto para La Cuenta\n"
              "Este nombre será usado para ayudar a identificar cuentas "
              "en caso de tener muchas")

        while True:
            short_name = input("> ")

            if len(short_name) < 1:
                print('Nombre corto muy corto. Intente de nuevo.')
            elif len(short_name) > 32:
                print('Nombre corto muy largo. Intente de nuevo.')
            else:
                break


        print("(Obligatorio)\n"
          "Ingresar nombre del autor de los articulos\n"
          "Este nombre aparecerá como autor en futuros articulos")

        while True:
            author_name = input("> ")

            if len(author_name) < 0:
                print('Nombre de autor muy corto. Intente de nuevo.')
            elif len(author_name) > 128:
                print('Nombre de autor muy largo. Intente de nuevo.')
            else:
                break

        print("(Obligatorio)\n"
              "Ingresar URL de autor\n"
              "Cuando el lector presione el nombre del autor, "
              "será enviado a esta URL")

        while True:
            author_url = input("> https://")

            if not author_url:
                break

            url_pattern = re.compile(
                r'(?:www\.)?'
                r'([a-zA-Z0-9-]{1,63}\.){1,}'
                r'[a-zA-Z]{2,}(?:/[a-zA-Z0-9-]+)*')

            if url_pattern.match(author_url):
                author_url = f'https://{author_url}'
                if len(author_url) > 512:
                    print('URL válida pero muy larga.')
                else:
                    break
            else:
                print('Formato de URL invalido')


        account = createAccount(short_name, author_name, author_url)


        if account.ok:
            print("Cuenta creada con éxito")
            account.printInfo("all")
        else:
            print("Error al crear cuenta")
            print(account.printInfo("ok"))
    elif user_input == "2":
        clear()

        print("Ingresar token de acceso")
        token = input("> ")

        clear()

        login(token)
    else:
        print("Error")


if __name__ == "__main__":
    main()
