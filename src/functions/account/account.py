import requests
from styles.styles import StrStyle

class Account:
    """
    Clase para representar una cuenta de usuario.

    Attributes:
        ok (bool): Indica si la cuenta se creó de forma correcta.
        short_name (str): Nombre corto.
        author_name (str): Nombre del autor.
        author_url (str): URL del autor.
        page_count (int): Cantidad de páginas.
        auth_url (str): URL de inicio de sesión para navegadores web.
        access_token (str): Token de acceso.
    """

    def __init__(self, ok, short_name, author_name, author_url, page_count,
                 auth_url, access_token):
        """
        Inicializa una nueva cuenta de usuario.

        Args:
            ok (bool): Indica si la cuenta se creó de forma correcta.
            short_name (str): Nombre corto.
            author_name (str): Nombre del autor.
            author_url (str): URL del autor.
            page_count (int): Cantidad de páginas.
            auth_url (str): URL de inicio de sesión para navegadores web.
            access_token (str): Token de acceso.
        """
        self.ok: bool = ok
        self.short_name: str = short_name
        self.author_name: str = author_name
        self.author_url: str = author_url
        self.page_count: int = page_count
        self.auth_url: str = auth_url
        self.access_token: str = access_token

    def printInfo(self, target="default"):
        """
        Imprime información del usuario según el 'target'.

        Args:
            target (str): Define qué información mostrar:
                - 'default': Muestra la información pública/segura del usuario.
                - 'all': Muestra toda la información del usuario, incluyendo
                        información sensible.
                - 'ok', 'short_name', 'author_name', 'author_url',
                'page_count', 'auth_url', 'access_token': Muestra información
                                                            específica.

        Si 'target' no coincide con ninguna opción, imprime un mensaje de
        error.

        Example:
            >>> account.printInfo("short_name")
            "Nombre corto: Eric Hernandez"
        """
        if target == "default":
            print(f"\n{StrStyle.IMPORTANT}--- Información Pública del Usuario ---{StrStyle.ENDC}\n")
            print(f"{StrStyle.REGULAR}Nombre: {self.short_name}{StrStyle.ENDC}")
            print(f"{StrStyle.REGULAR}Autor: {self.author_name}{StrStyle.ENDC}")
            print(f"{StrStyle.REGULAR}URL: {self.author_url}{StrStyle.ENDC}")
            print(f"{StrStyle.REGULAR}Páginas: {self.page_count}{StrStyle.ENDC}\n")

        elif target == "all":
            print(f"\n{StrStyle.IMPORTANT}--- Información (pública y privada) del Usuario ---{StrStyle.ENDC}\n")
            print(f"{StrStyle.REGULAR}Nombre: {self.short_name}{StrStyle.ENDC}")
            print(f"{StrStyle.REGULAR}Autor: {self.author_name}{StrStyle.ENDC}")
            print(f"{StrStyle.REGULAR}URL: {self.author_url}{StrStyle.ENDC}")
            print(f"{StrStyle.REGULAR}Páginas: {self.page_count}{StrStyle.ENDC}")
            print(f"{StrStyle.REGULAR}URL de login para navegador web: {self.auth_url}{StrStyle.ENDC}")
            print(f"{StrStyle.REGULAR}Token de acceso: {self.access_token}{StrStyle.ENDC}\n")

        elif target == "ok":
            print(f"\n{StrStyle.SUCCESS}OK: {self.ok}{StrStyle.ENDC}\n")

        elif target == "short_name":
            print(f"\n{StrStyle.INFO}Nombre corto: {self.short_name}{StrStyle.ENDC}\n")

        elif target == "author_name":
            print(f"\n{StrStyle.INFO}Autor: {self.author_name}{StrStyle.ENDC}\n")

        elif target == "author_url":
            print(f"\n{StrStyle.INFO}URL de autor: {self.author_url}{StrStyle.ENDC}\n")

        elif target == "page_count":
            print(f"\n{StrStyle.INFO}Páginas: {self.page_count}{StrStyle.ENDC}\n")

        elif target == "auth_url":
            print(f"\n{StrStyle.INFO}Iniciar sesión en navegador web: {self.auth_url}{StrStyle.ENDC}\n")

        elif target == "access_token":
            print(f"\n{StrStyle.INFO}Token de acceso: {self.access_token}{StrStyle.ENDC}\n")

        else:
            print(f"\n{StrStyle.FAIL}Error con pase de argumentos{StrStyle.ENDC}\n")



def getAccountInfo(access_token):
    """
    Obtiene información de una cuenta usando su token de acceso.
    
    Args:
    access_token (str): Token de acceso a una cuenta existente.

    Returns:
        Account: Devuelve un objeto Account que contiene los datos
        recibidos desde el API.
    """
    
    response = requests.get(
        f'https://api.telegra.ph/getAccountInfo?access_token={access_token}&'
        f'fields=["short_name", "author_name", "author_url", "auth_url",'
        f'"page_count"]', timeout=5)
    
    data = response.json()

    if data["ok"]:
        return Account(True, data["result"]["short_name"],
                data["result"]["author_name"], data["result"]["author_url"],
                data["result"]["page_count"], data["result"]["auth_url"],
                access_token)
    else:
        return Account(False, "", "", "", 0, "", access_token)
