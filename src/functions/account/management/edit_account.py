import requests

def editAccountInfo(access_token: str, target: str, new_value: str):
    """
    Permite editar dato a la vez de la cuenta enlazada al token de acceso.

    Args:
        access_toke (str): Token de acceso a una cuenta existente.
        target (str): Clave del dato que se quiere editar.
        new_value (str): Nuevo valor que se sobrescribirá sobre el
                         argumentos 'target'
    Example:
        >>> editAccountInfo(
            "f1c7cc248f2d3e1fea44c28a0b93148e4dea0e7a24b7cfe791a993a13413",
            "author_name", "Eric Joel Hernandez")
        "Cambio hecho con éxito"
    """
    response = requests.get(
        f"https://api.telegra.ph/editAccountInfo?access_token={access_token}&"
        f"{target}={new_value}", timeout=5)
    data = response.json()

    if data["ok"]:
        print("Cambio hecho con éxito")
    else:
        print("Error. ok not True")