def get_non_found_user_message(lan: str) -> str:
    if lan == "en":
        return "The user couldn't be found in our system, please try again."

    if lan == "es":
        return "El usuario no puede ser encontrado en nuestro sistema, prueba nuevamente."

    return "The user couldn't be found in our system., please try again."

def get_non_found_patient_message(lan: str) -> str:
    if lan == "en":
        return "The patient could not be found in our system, please try again."

    if lan == "es":
        return "El paciente no puede ser encontrado en nuestro sistema, prueba nuevamente."

    return "The user couldn't be found in our system."


def get_password_update_message(lan: str) -> str:
    if lan == "en":
        return "The password was updated successfully."

    if lan == "es":
        return "La contraseña fue actualizada satisfactoria."

    return "The password was updated successfully."


def get_deleted_message(lan: str) -> str:
    if lan == "en":
        return "The user was deleted successfully."

    if lan == "es":
        return "El usuario fue eliminado satisfactoriamente."

    return "The user was deleted successfully."


def get_unathorized_message(lan: str) -> str:
    if lan == "en":
        return "Unathorized."

    if lan == "es":
        return "No autorizado."

    return "Unathorized."


def get_invalid_token_message(lan: str) -> str:
    if lan == "en":
        return "Could not validate credentials."

    if lan == "es":
        return "No se pueden validar la credenciales."

    return "Could not validate credentials."


def get_non_found_diagnostic_message(lan: str) -> str:
    if lan == "en":
        return "The diagnostic could not be found in our system, please try again."

    if lan == "es":
        return "El diagnostico no se encuentra en nuestro sistema, por favor intenta nuevamente."

    return "The diagnostic could not be found in our system, please try again."


def get_forbidden_diagnostic_message(lan: str) -> str:
    if lan == "en":
        return "The diagnosis cannot be evaluated, it belongs to a different doctor, please try again."

    if lan == "es":
        return "El diagnostico no puede ser evaluado, no posees este diagnostico asignado."

    return "The diagnosis cannot be evaluated, it belongs to a different doctor, please try again."

def get_repeated_email_message(lan: str) -> str:
    if lan == "en":
        return "The email received is not allowed to be used, please try with a different email."

    if lan == "es":
        return "El correo recibido no se encuentra disponible, por favor intenta con un correo diferente."

    return "The email received is not allowed to be used, please try with a different email."

def get_repeated_carnet_message(lan: str) -> str:
    if lan == "en":
        return "The carnet received is not allowed to be used, please try with a different carnet."

    if lan == "es":
        return "El carnet recibido no se encuentra disponible, por favor intenta con un carnet diferente."

    return "The carnet received is not allowed to be used, please try with a different carnet."
