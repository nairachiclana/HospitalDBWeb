﻿# coding=utf-8
import pandas as pd
from random import randrange, choice

print("Leemos los datasets")


#Leemos todos los datos

df = pd.read_csv('../../datasets/internet_data_sets/personas-extravidas-y-desaparecidas-datacivica-2018.csv')
df_paises = pd.read_csv('../../datasets/internet_data_sets/paises.txt')
especialidades = pd.read_csv('../../datasets/internet_data_sets/especialidades.txt')
enfermedades = pd.read_csv('../../datasets/internet_data_sets/enfermedades.txt')
doctor_names = pd.read_csv('../../datasets/internet_data_sets/wc2018-players.csv')
print(list(df))
print("Generamos los dataframes vacios")

#Creamos las diferentes tablas
tabla_paciente = pd.DataFrame()
tabla_urgencia = pd.DataFrame()
tabla_operacion = pd.DataFrame()
tabla_enfermedad = pd.DataFrame()
tabla_especialidad = pd.DataFrame()
tabla_medico = pd.DataFrame()
tabla_quirofano = pd.DataFrame()

print("Creamos los vectores aleatorios para tabla_paciente")
#Generamos datos aleatorios para la tabla_paciente
bool_smoker = []
urgencia = []
id_expediente = []
num_urgencia_id = []
num_enfermedad_id = []
cont = 0
cont2 = 0
alea_Paises = []
enfermedad = []
vector_paises = df_paises['Albania'].tolist()
cont_urgencia = 0
lista_enfermedades= enfermedades['Nombres'].tolist()
vector_enfermedad_paciente = [None] * len(lista_enfermedades)

#Asegurar valores distintos
#Aniadir pais
for i in range(0, 10000):
    bool_smoker.insert(i,choice(["YES", "NO"]))
    id_expediente.insert(i, randrange(1111111, 9999999))
    num_pais_aleatorio = randrange(0, len(vector_paises))
    alea_Paises.insert(i, vector_paises[num_pais_aleatorio])
    choice_val = choice(["ENFERMEDAD", "URGENCIA"])
    num_urgencia = randrange(0, 10000)
    num_enfermedad = randrange(0, len(lista_enfermedades))
    temp_urgencia = choice(["NULL", num_urgencia])
    temp_enfermedad = choice(["NULL", num_enfermedad])
    if choice_val == "URGENCIA":
        urgencia.insert(i, choice(["NULL", num_urgencia]))
        enfermedad.insert(i, "NULL")
        if num_urgencia != "NULL":
            num_urgencia_id.insert(cont, num_urgencia)
            cont = cont + 1
    elif choice_val == "ENFERMEDAD":
        enfermedad.insert(i, choice(["NULL", lista_enfermedades[num_enfermedad]]))
        urgencia.insert(i, "NULL")
        if temp_enfermedad != "NULL":
            num_enfermedad_id.insert(cont2, num_enfermedad)

            if vector_enfermedad_paciente[num_enfermedad] is None:
                vector_enfermedad_paciente[num_enfermedad] = id_expediente[i]
            else:
                vector_enfermedad_paciente[num_enfermedad] = str(vector_enfermedad_paciente[num_enfermedad]) + ", " + str(id_expediente[i])
            cont2 = cont2 + 1


#Ahora elige toda la lista
print("Creamos los vectores aleatorios para tabla_urgencia")
enum_gravedad = []
boolean_ambulancia = []
id_operacion = []
lista_especialidades = especialidades['Especialidades'].tolist()
especialidad = []
id_toperacion = []
id_tespecialidad = []
tupla_ingreso = []
cont_operacion = 0
cont_especialidad = 0
for i in range(0, cont):
    enum_gravedad.insert(i, choice(["MUY ALTA", "ALTA", "MEDIA", "BAJA"]))
    boolean_ambulancia.insert(i, choice(["YES", "NO"]))
    tupla_ingreso.insert(i, choice(["YES", "NO"]))
    id_operacion_num = randrange(1111111, 9999999)
    num_especialidad = randrange(0, len(lista_especialidades))
    especialidad.insert(i, choice(["NULL", lista_especialidades[num_especialidad]]))
    id_operacion.insert(i, choice(["NULL", id_operacion_num]))
    if id_operacion[i] != "NULL":
        id_toperacion.insert(cont_operacion, int(id_operacion_num))
        cont_operacion = cont_operacion + 1

    if especialidad[i] != "NULL":
        id_tespecialidad.insert(cont_operacion, lista_especialidades[num_especialidad])
        cont_especialidad = cont_especialidad + 1


print("Creamos los vectores aleatorios para tabla_operacion")
identificador_operacion = []
id_quirofano1 = []
nombre_medico = []
for i in range(0, cont_operacion):
    identificador_operacion.insert(i,i)
    id_quirof = randrange(0, 25)
    num_medico = randrange(0, len(doctor_names.Name))
    nombre_medico.insert(i,doctor_names.Name[num_medico])
    id_quirofano1.insert(i, id_quirof)


print("Creamos los vectores aleatorios para tabla_medico")
vector_especialidad_medicos = [None] * len(lista_especialidades)
especialidad_tabla_medico = []
id_medico = []
for i in range(0, len(doctor_names.Name)):
    id_medico.insert(i, i)
    especialidad_aleatoria = randrange(0, len(lista_especialidades))
    especialidad_tabla_medico.insert(i, lista_especialidades[especialidad_aleatoria])
    if vector_especialidad_medicos[especialidad_aleatoria] is None:
        vector_especialidad_medicos[especialidad_aleatoria] = id_medico[i]
    else:
        vector_especialidad_medicos[especialidad_aleatoria] = str(vector_especialidad_medicos[especialidad_aleatoria]) + ", " + str(
            id_medico[i])


print("Creamos los vectores aleatorios para tabla_quirofano")
puerta_quirofano = ["A", "B", "C", "D", "E"]
planta_quirofano = []
puerta_quirofano_fin = []
id_quirofano= []
cont = 0
for i in range(0, 5):
    for p in range(0, 5):
        id_quirofano.insert(cont, cont)
        puerta_quirofano_fin.insert(cont, puerta_quirofano[p] )
        planta_quirofano.insert(cont, i)
        cont = cont + 1




###############################################################################3
#Falta poner para introducir la especialidad a la que se asocia una enfermedad
############################################################################3###


print("Creamos los vectores aleatorios para tabla_enfermedad")
cura_conocida = []
ingreso = []
contagiosa = []
hereditaria = []
tratamiento = []
especialidad_tenfermedad = []

for i in range(0, len(lista_enfermedades)):
    hereditaria.insert(i, choice(["YES", "NO"]))
    if hereditaria[i] == "YES":
        cura_conocida.insert(i, "NO")
    else:
        cura_conocida.insert(i, choice(["YES", "NO"]))
    if cura_conocida[i] == "YES":
        tratamiento.insert(i, choice(["YES", "NO"]))
    else:
        tratamiento.insert(i, "NO")

    if hereditaria[i] == "NO":
        contagiosa.insert(i, choice(["YES", "NO"]))
    else:
        contagiosa.insert(i, "NO")
    ingreso.insert(i, choice(["YES", "NO"]))

    especialidad_aleatoria = randrange(0, len(lista_especialidades))
    especialidad_tenfermedad.insert(i, lista_especialidades[especialidad_aleatoria])






# Guardamos los datos generados aleatoriamente

#-----------
#PACIENTE
#----------
tabla_paciente['num_expediente'] = list(set(id_expediente))
tabla_paciente['nombre'] = df.prim_nombre[0:len(tabla_paciente['num_expediente'])]
tabla_paciente['apellido'] = df.apellido_pat[0:len(tabla_paciente['num_expediente'])]
vect_edad = []
for i in range(0,len(tabla_paciente['num_expediente'])):
    if  df.fuerocomun_edad[i] == "NO ESPECIFICADO":
        vect_edad.insert(i, 20)
    else:
        vect_edad.insert(i,  df.fuerocomun_edad[i])

tabla_paciente['edad'] = vect_edad
tabla_paciente['sexo'] = df.fuerocomun_sexo[0:len(tabla_paciente['num_expediente'])]
vector_fecha = []
for i in range(0,len(tabla_paciente['num_expediente'])):
    vect = df.fuerocomun_desapfecha[i].split("/")
    vector_fecha.insert(i, vect[2]+"-"+vect[1]+"-" + vect[0])


tabla_paciente['fecha_ingreso'] = vector_fecha
tabla_paciente['hora_ingreso'] = df.fuerocomun_desaphora[0:len(tabla_paciente['num_expediente'])]
tabla_paciente['pais_origen'] = alea_Paises[0:len(tabla_paciente['num_expediente'])]
tabla_paciente['fumador'] = bool_smoker[0:len(tabla_paciente['num_expediente'])]

    # FK ??????????????????????????????????
tabla_paciente['urgencia'] = urgencia[0:len(tabla_paciente['num_expediente'])]
tabla_paciente['enfermedad'] = enfermedad[0:len(tabla_paciente['num_expediente'])]


#-----------
#ENFERMEDAD
#-----------
tabla_enfermedad['nombre_enfermedad'] = lista_enfermedades
tabla_enfermedad['hereditaria'] = hereditaria
tabla_enfermedad['cura_conocida'] = cura_conocida
tabla_enfermedad['tratamiento'] = tratamiento
tabla_enfermedad['contagiosa'] = contagiosa
tabla_enfermedad['ingreso'] = ingreso


#for i in range(1, len(tratamiento)):
            #    print("¿Que especialidad cogerias para ...?")
            #    print("Enfermedad "+lista_enfermedades[i]+"\nCura conocida "+ cura_conocida[i]+
            #          "\nContagiosa "+ contagiosa[i] + "\nHereditaria " + hereditaria[i]+"\nTratamiento "+tratamiento[i])
            #    lista_enfermedades_escritas.insert(i, input())

            #tabla_enfermedad['Especialidad'] = lista_enfermedades_escritas
                #especialidad_tenfermedad
#-----------
#URGENCIA
#-----------
num_urgencia_id = list(set(num_urgencia_id))
num_urgencia_id = [int(x) for x in num_urgencia_id]
num_urgencia_id.sort()
tabla_urgencia['id_urgencia'] =  num_urgencia_id
value_urgencia = [df.fuerocomun_descripcion[x] for x in num_urgencia_id]
tabla_urgencia['causa'] = value_urgencia
tabla_urgencia['gravedad'] = enum_gravedad[:len(num_urgencia_id)]
tabla_urgencia['uso_ambulancia'] = boolean_ambulancia[:len(num_urgencia_id)]
tabla_urgencia['ingreso']=tupla_ingreso[:len(num_urgencia_id)]
tabla_urgencia['OPERACION_id_operacion'] = id_operacion[:len(num_urgencia_id)]
tabla_urgencia['ESPECIALIDAD_nombre_especialidad'] = especialidad[:len(num_urgencia_id)]



#---------
#OPERACION
#---------
id_toperacion.sort()
tabla_operacion['id_operacion'] = list(id_toperacion)
tabla_operacion['hora'] = list(df.fuerocomun_desaphora[300:(cont_operacion+300)])
tabla_operacion['cirujano'] = nombre_medico[:cont_operacion]
tabla_operacion['QUIROFANO_id_quirofano'] = id_quirofano1[:cont_operacion]


#---------
#QUIROFANO
#---------
tabla_quirofano['id_quirofano'] = id_quirofano
tabla_quirofano['planta'] = planta_quirofano
tabla_quirofano['puerta'] = puerta_quirofano_fin


#------
#MEDICO
#------
tabla_medico['id_medico'] = id_medico
tabla_medico['nombre_medico'] = doctor_names.Name
tabla_medico['ESPECIALIDAD_nombre_especialidad']= especialidad_tabla_medico

#------------
#ESPECIALIDAD
#------------
tabla_especialidad['nombre_especialidad'] = lista_especialidades


print("Guardando resultados")
#Almacenamos los resultados en .csv
tabla_paciente.to_csv('../../datasets/generated_tables/tabla_paciente.csv', sep=',', encoding='utf-8', index=False)
tabla_urgencia.to_csv('../../datasets/generated_tables/tabla_urgencia.csv', sep=',', encoding='utf-8', index=False)
tabla_operacion.to_csv('../../datasets/generated_tables/tabla_operacion.csv', sep=',', encoding='utf-8', index=False)
tabla_quirofano.to_csv('../../datasets/generated_tables/tabla_quirofano.csv', sep=',', encoding='utf-8', index=False)
tabla_medico.to_csv('../../datasets/generated_tables/tabla_medico.csv', sep=',', encoding='utf-8', index=False)
tabla_enfermedad.to_csv('../../datasets/generated_tables/tabla_enfermedad.csv', sep=',', encoding='utf-8', index=False)
tabla_especialidad.to_csv('../../datasets/generated_tables/tabla_especialidad.csv', sep=',', encoding='utf-8', index=False)


print("FIN DEL PROCESO.")