import sender_stand_request
import data

def get_body_kit(kit_name): #Función para llamar una copia del cuerpo del kit y recibir el nombre modificado
    current_kit = data.body_kit.copy() #se almacena una copia del cuerpo del kit
    current_kit["name"] = kit_name #se ingresar el nombre que tendra la copia del kit para las pruebas
    return current_kit #se regresa el kit con el nombre modificado

def get_auth_token(): #Función para generar el Bearer token
    user_body = data.user_body #se almacena la copia del usuario
    user_response = sender_stand_request.post_new_user(user_body) #se hace un post de user para generar un Bearer token
    return user_response.json()["authToken"] #se regresa el token

def positive_assert(kit_name):#Función para ejecutar las pruebas positivas
    auth_token = get_auth_token() #El Bearer token es almacenado
    kit_body = get_body_kit(kit_name) #Se almacena el cuerpo del kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token) #El resultado de la solicitud POST es guardado

    assert  kit_response.status_code == 201 # Comprueba si el código de estado es 201


def negative_assert_400(kit_name): #Función para ejecutar las pruebas negativas
    auth_token = get_auth_token()#El Bearer token es almacenado
    kit_body = get_body_kit(kit_name) #Se almacena el cuerpo del kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token) #El resultado de la solicitud POST es guardado

    assert kit_response.status_code == 400 #Comprueba si el código de estado es 400


#Prueba 1 El número permitido de caracteres (1)
def test_create_kit_1_letter_in_name():
    positive_assert("a")

#Prueba 2 El número permitido de caracteres (511)
def test_create_kit_511_letters_in_name():
    positive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                    "abcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                    "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Prueba 3 El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_cero_letters_in_name():
    negative_assert_400("")

#Prueba 4 El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letters_in_name():
    negative_assert_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
    "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
    "bcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
    "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
    "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba 5 Se permiten caracteres especiales:
def test_create_kit_special_letters_in_name():
    positive_assert("/""№%@")

#Prueba 6 Se permiten espacios
def test_create_kit_space_in_name():
    positive_assert("A Aaa")

#Prueba 7 se permiten números
def test_create_kit_numbers_in_name():
    positive_assert("123")

#Prueba 8 El parámetro no se pasa en la solicitud
def test_create_kit_null_name():
    kit_body = data.body_kit.copy()
    kit_body.pop("name")
    negative_assert_400(kit_body)

#Prueba 9 Se ha pasado un tipo de parámetro diferente (número)
def test_create_kit_int_value_in_name():
    negative_assert_400(123)