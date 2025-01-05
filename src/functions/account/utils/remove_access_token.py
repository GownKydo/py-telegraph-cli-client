import requests
from styles.styles import StrStyle

def revokeAccessToken(access_token: str):
    """
    Cierra todas las sesiones generando un nuevo token de acceso.

    Args:
        access_token (str): Token de acceso a una cuenta existente.
    Example:
        >>> revokeAccessToken(
            "f1c7cc248f2d3e1fea44c28a0b93148e4dea0e7a24b7cfe791a993a13413"
            )
        "Sesiones cerradas. Nuevo token generado. Nuevo auth url generado"
        "Nuevo token de acceso:
        h6c0cb248f1d3e1fea45c28a0b93148e4dea0e5z24v7cde781a903abv2s1"
        "Nuevo Auth URL:
        https://edit.telegra.ph/auth/71oM2k1Js5FUKuUfNEYkqtr7GhpFtVtyThlTClC20i"
    """
    response = requests.get(
        f"https://api.telegra.ph/revokeAccessToken?access_token={access_token}", timeout=5)
    data = response.json()

    if data["ok"]:
        print(f"\n{StrStyle.SUCCESS}Sesiones cerradas. Nuevo token generado. Nuevo auth_url generado{StrStyle.ENDC}")
        print(f"{StrStyle.INFO}Nuevo token de acceso: {data['result']['access_token']}{StrStyle.ENDC}")
        print(f"{StrStyle.INFO}Nuevo auth_url: {data['result']['auth_url']}{StrStyle.ENDC}\n")
    else:
        print(f"\n{StrStyle.FAIL}Error. ok not True{StrStyle.ENDC}\n")
