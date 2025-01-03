from functions.account.account import Account
import requests

def createAccount(short_name: str, author_name: str, author_url: str):
    """
    Creación de Cuenta en Telegra.ph.

    Args:
        short_name (str): Nombre corto para identificar la cuenta.
                          Este dato no será visible públicamente.
        author_name (str): Nombre del autor de los futuros artículos.
        author_url (str): Website al que el lector es enviado si toca el
                          nombre del autor en el artículo.
    Returns:
        Account: Si la cuenta se crea con éxito, se devuelve un objeto Account
                 que contiene los datos recibidos. En caso de error,
                 retorna un string indicando el problema.
    Example:
        >>> account = createAccount("Cuenta de Prueba", "Eric Hernandez",
                                    "https://example.com")
        >>> account.short_name
        "Cuenta de Prueba"
        >>> account.page_count
        0
    """
    response = requests.get(
        f"https://api.telegra.ph/createAccount?"
        f"short_name={short_name}&author_name={author_name}&"
        f"author_url={author_url}", timeout=5)

    if response.status_code == 200:
        data = response.json()
        token = data["result"]["access_token"]

        response = requests.get(
            f'https://api.telegra.ph/getAccountInfo?access_token={token}&'
            f'fields=["short_name", "author_name", "author_url", '
            f'"page_count","auth_url"]', timeout=5)
        data = response.json()

        return Account(True, data["result"]["short_name"],
                       data["result"]["author_name"],
                       data["result"]["author_url"],
                       data["result"]["page_count"],
                       data["result"]["auth_url"], token)
    else:
        return Account(False, "", "", "", "", "", "")