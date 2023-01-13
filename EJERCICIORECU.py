#Ejercicio 1
def check_DGT(ruta):
    """ Funcion que lee los datos de personas con multas, de trafico, tanto como de radares,
    de ITV y de estupefacientez, los comprueba, los corrige y lo vuelve a escribir con todos
    los datos corregidos.
    PARAMETROS:
    ruta: Es la ruta del archivo sin corregir y las multas.
    """
    with open("DGT_csv", encoding="utf-8") as csvfile:
        csvfile = ("C:/Users/2M/Documents/DAPI/GIT/Sanmartin_Irantzu_Examen_REC_DAPI_UT2/DGT.cvs")
        contenido_archivo = csvfile.read()
    for persona in csvfile:
        persona = check_username(persona[1])
        persona = check_nif(persona[2])
        persona = check_phone(persona[3])
        persona = check_DGT(persona[4])
        with open(ruta, "w") as file:
            file.write(persona)
    file.close()
    print(persona)

    return "Datos sobreescritos"

#Ejericio 2
countries_dict = {"30":"Grecia", "33":"Francia", "34":"España", "351":"Portugal",
                "380":"Ucrania", "39":"Italia", "41":"Suiza", "44":"Reino Unido",
                "49":"Alemania", "7":"Rusia"}

#Ejercicio 3
nif_dict = {"0":"T", "1":"R", "2":"W", "3":"A", "4":"G", "5":"M", "6":"Y", "7":"F",
            "8":"P", "9":"D", "10":"X", "11":"B", "12":"N", "13":"J", "14":"Z", "15":"S",
            "16":"Q", "17":"V", "18":"H", "19":"L", "20":"C", "21":"K", "22":"E"}

#Ejercicio 4
def check_username(user_name):
    """ Función que lee los nombres mal escritos y los corrige
    PARAMETROS:
    user_name: Es el nombre mal escrito recibido
    return: Es lo que convierte el nombre en formato CamelCase corregido.
    """
    return user_name.title()

#Ejercicio 5
def check_nif(user_nif):
    """ Funcion que lee el nif mal escrito y lo corrige
    PARAMETROS:
    user_nif: Es el nif mal escrito recibido
    return: Es el nif ya corregido
    """
    nif_number = user_nif[0:8]
    nif_letter = user_nif[8]

    letra_correcta = nif_dict[str(int(nif_number) % 23)]

    return nif_number + letra_correcta

#Ejercicio 6
def check_phone(numero_de_telefono):
    """ Funcion que lee el numero de telefono mal escrito y lo corrige
    PARAMETROS:
    telefono_completo: Es el numero de telefono mal escrito recibido
    return: Es el numero de telefono ya corregido
    """
    numero1 = numero_de_telefono.split('(')
    numero2 = numero1[1].split(')')
    prefijo = numero_de_telefono[numero1+1:numero2]

    numero= numero_de_telefono[numero2+1:]
    pais = countries_dict[prefijo]
    numero_guion = numero[0:3]
    numeroguion_ = numero[4:]
    numerofinal = numero_guion + numeroguion_
    numero_correcto = '+' + prefijo + '-' + numerofinal

    return str(numero_correcto), str(pais)

#Ejercicio 7
def calculate_bill(multas_radar, multas_ITV, multas_estupefacientes):
    """ Funcion que calcula el total de multas que tiene un usuario
    PARAMETROS:
    multas_radar: Es la primera de las variables
    multas_ITV: Es la segunda de las variables
    multas_estupefacientes: Es la tercera de las variables
    return: Es la suma de las variables
    """
    bill = int(multas_radar) + int(multas_ITV) + int(multas_estupefacientes)

    return int(bill)



