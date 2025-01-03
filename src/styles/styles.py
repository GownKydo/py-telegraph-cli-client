class StrStyle:
    """
    Clase para definir estilos de texto con colores ANSI.

    Attributes:
        IMPORTANT (str): Púrpura. Importante pero no crítico.
        INFO (str): Azul. Información no crítica.
        SUCCESS (str): Cian. Mensaje de éxito.
        SUCCESS_HIGHLIGHT (str): Verde. Mensaje de éxito importante.
        WARNING (str): Amarillo. Mensaje de advertencia.
        REGULAR (str): Color predeterminado. Mensajes normales.
        CONTEXT (str): Gris. Información contextual adicional.
        WARNING_HIGHLIGHT (str): Amarillo oscuro. Destaque de advertencia.
        FAIL (str): Rojo. Mensaje de error.
        BOLD (str): Estilo de texto en negrita.
        UNDERLINE (str): Estilo de texto subrayado.
        ENDC (str): Restablece el formato del texto al predeterminado.
    Example:
        >>> print(StrStyle.FAIL + "Esto es un mensaje de error" + StrStyle.ENDC)
    """

    IMPORTANT = '\033[95m'  # Purple. Important but not critical
    INFO = '\033[94m'  # Blue. Non-critical information
    SUCCESS = '\033[96m'  # Cyan. Success message
    SUCCESS_HIGHLIGHT = '\033[92m'  # Green. Important Success message
    WARNING = '\033[33m'  # Yellow. Warning message
    REGULAR = '\033[97m'  # Default color. Normal messages
    CONTEXT = '\033[90m'  # Grey. More contextual information
    WARNING_HIGHLIGHT = '\033[93m'  # Darker Yellow. Warning highlight message
    FAIL = '\033[91m'  # Red. Error message
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'
