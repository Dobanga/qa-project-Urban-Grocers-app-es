import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body, #insertar el cuepo de la solicitud
                         headers=data.headers_user) #insertar el encabezado


def post_new_client_kit(kit_body,auth_token):
    headers= { #header especifico para generar el kit y recibir el Bearer token
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body, #insertar el cuepo de la solicitud
                         headers=headers) #insertar el encabezado