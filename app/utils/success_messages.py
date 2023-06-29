def get_success_diagnostic_message(lan: str) -> str:
    if lan == "en":
        return "The diagnostic was executed successfully."

    if lan == "es":
        return "El diagnostico fue ejecutado satisfactoriamente."

    return "The diagnostic was executed successfully."


def get_fail_diagnostic_message(lan: str) -> str:
    if lan == "en":
        return "The diagnostic fail in executed time."

    if lan == "es":
        return "No se pudo completar el diagnostico."

    return "The diagnostic fail in executed time."


def get_success_mailer_message(lan: str) -> str:
    if lan == "en":
        return "The email was sent successfully to the admin."

    if lan == "es":
        return "El correo fue enviado satisfactoriamente al administrador."

    return "The email was sent successfully to the admin."


def get_fail_mailer_message(lan: str) -> str:
    if lan == "en":
        return "The email could not be sent to administrator."

    if lan == "es":
        return "El correo no pudo ser enviado al administrador."

    return "The email could not be sent to administrator."


def get_success_patient_message(lan: str) -> str:
    if lan == "en":
        return "The patient was created successfully."

    if lan == "es":
        return "El paciente fue ser creado satisfactoriamente."

    return "The patient was created successfully."


def get_fail_patient_message(lan: str) -> str:
    if lan == "en":
        return "The patient could not be created."

    if lan == "es":
        return "El paciente no pude ser creado."

    return "The patient could not be created."
