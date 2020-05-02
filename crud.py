#Johan David Gomez Gil
# Lenguajes 2 
#2020

#------------------Crear--------------------------------------------
import sqlite3

def ingresarDatosPaciente():
    try:
        tipoDoc = (str(input("Tipo de documento (Cedula, Pasaporte, Tarjeta de identidad ): ")))
        numDoc = (int(input("Numero de documento: ")))
        nombre = (str(input("Nombre completo: ")))
        genero = (str(input("Sexo (M/F): ")))
        barrio = (str(input("Barrio: ")))
        ciudad = (str(input("Ciudad: "))) 
        telefono = (int(input("Telefono: ")))
        ano = (int(input("Año de nacimiento: ")))
        prof = (str(input("Profesion: ")))
        nacion = (str(input("Nacionalidad: ")))

    except ValueError:
        print("El valor introducido es incorrecto")
        ingresarDatosPaciente()
    except: #Para capturar excepciones genericas
        print ("Ha ocurrido un error inesperado")
        ingresarDatosPaciente()
        
    
    datos = [numDoc,tipoDoc,nombre,genero,barrio,ciudad,telefono,ano,prof,nacion]
    return datos


def crearPaciente():
    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("INSERT INTO paciente VALUES (?,?,?,?,?,?,?,?,?,?)",ingresarDatosPaciente())
        db.commit() #Guardar los datos
        print ("Operacion realizada")
        db.close()
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

def crearEnfermedad():
    try:
        enfermedad = (str(input("Nombre de la enfermedad: ")))

    except ValueError:
        print("El nombre introducido es incorrecto")
        ingresarDatosPaciente()
    except: #Para capturar excepciones genericas
        print ("Ha ocurrido un error inesperado")
        

    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("ALTER TABLE pacienteEnfermedades ADD %s TEXT" %enfermedad)
        db.commit() #Guardar los datos
        print ("Enfermedad "+enfermedad+" agregada con exito")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

def crearSintoma():
    try:
        sintoma = (str(input("Nombre del sintoma: ")))

    except ValueError:
        print("El nombre introducido es incorrecto")
        
    except: #Para capturar excepciones genericas
        print ("Ha ocurrido un error inesperado")
        

    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("ALTER TABLE pacienteSintomas ADD %s TEXT" %sintoma)
        db.commit() #Guardar los datos
        print ("Sintoma "+sintoma+" agregada con exito")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

#-----------------Leer----------------------------------------------

def verPacientes():
    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM paciente")
        lista = cursor.fetchall()
        for paciente in lista:
            print("!",paciente[0],"!",paciente[1],"!",paciente[2],"!",paciente[3],"!",
            paciente[4],"!",paciente[5],"!",paciente[6],"!",
            paciente[7],"!",paciente[8],"!",paciente[9],"!")
            #print("")
            #print (paciente)
        print ("Operacion realizada")
        print ("prueba")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

def verEnfermedades():
    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pacienteEnfermedades")
        lista = cursor.fetchall()
        for paciente in lista:
            #print("!",paciente[0],"!",paciente[1],"!",paciente[2],"!",paciente[3],"!",
            #paciente[4],"!",paciente[5],"!",paciente[6],"!",
            #paciente[7],"!",paciente[8],"!",paciente[9],"!")
            print("")
            print (paciente)
        print ("Operacion realizada")
        print ("prueba")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

def verSintomas():
    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pacienteSintomas")
        lista = cursor.fetchall()
        for paciente in lista:
            #print("!",paciente[0],"!",paciente[1],"!",paciente[2],"!",paciente[3],"!",
            #paciente[4],"!",paciente[5],"!",paciente[6],"!",
            #paciente[7],"!",paciente[8],"!",paciente[9],"!")
            print("")
            print (paciente)
        print ("Operacion realizada")
        print ("prueba")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

#----------------Actualizar----------------------------------------

def actualizarPacientes():
    try:
        paciente = (str(input("Numero de documento del paciente: ")))
        campo = (str(input("Escriba campo a modificar: ")))
        info = (str(input("Escriba el nuevo valor del campo: ")))

    except ValueError:
        print("Incorrecto")
        ingresarDatosPaciente()
    except: #Para capturar excepciones genericas
        print ("Ha ocurrido un error inesperado")
        ingresarDatosPaciente()

    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("UPDATE paciente SET %s = '%s' WHERE NumDocumento = %s" %(campo,info,paciente))
        db.commit() #Guardar los datos
        print ("Modificado con exito")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

def actualizarEnfermedades():
    try:
        paciente = (str(input("Numero de documento del paciente: ")))
        campo = (str(input("Escriba enfermedad a modificar: ")))
        info = (str(input("Escriba el nuevo valor del campo: ")))

    except ValueError:
        print("Incorrecto")
        ingresarDatosPaciente()
    except: #Para capturar excepciones genericas
        print ("Ha ocurrido un error inesperado")
        ingresarDatosPaciente()

    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("UPDATE pacienteEnfermedades SET %s = '%s' WHERE Paciente = %s" %(campo,info,paciente))
        db.commit() #Guardar los datos
        print ("Modificado con exito")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

def actualizarSintomas():
    try:
        paciente = (str(input("Numero de documento del paciente: ")))
        campo = (str(input("Escriba sintoma a modificar: ")))
        info = (str(input("Escriba el nuevo valor del campo: ")))

    except ValueError:
        print("Incorrecto")
        ingresarDatosPaciente()
    except: #Para capturar excepciones genericas
        print ("Ha ocurrido un error inesperado")
        ingresarDatosPaciente()

    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("UPDATE pacienteSintomas SET %s = '%s' WHERE paciente = %s" %(campo,info,paciente))
        db.commit() #Guardar los datos
        print ("Modificado con exito")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

#-------------------Eliminar---------------------------------------

def eliminarPacientes():
    try:
        paciente = (str(input("Numero de documento del paciente: ")))

    except ValueError:
        print("Incorrecto")
        ingresarDatosPaciente()
    except: #Para capturar excepciones genericas
        print ("Ha ocurrido un error inesperado")
        ingresarDatosPaciente()

    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("DELETE FROM paciente WHERE NumDocumento= %s" %paciente)
        db.commit() #Guardar los datos
        print ("Eliminado con exito")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

def eliminarEnfermedades():
    try:
        paciente = (str(input("Numero de documento del paciente: ")))

    except ValueError:
        print("Incorrecto")
        ingresarDatosPaciente()
    except: #Para capturar excepciones genericas
        print ("Ha ocurrido un error inesperado")
        ingresarDatosPaciente()

    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("DELETE FROM pacienteEnfermedades WHERE Paciente= %s" %paciente)
        db.commit() #Guardar los datos
        print ("Eliminado con exito")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

def eliminarSintomas():
    try:
        paciente = (str(input("Numero de documento del paciente: ")))

    except ValueError:
        print("Incorrecto")
        ingresarDatosPaciente()
    except: #Para capturar excepciones genericas
        print ("Ha ocurrido un error inesperado")
        ingresarDatosPaciente()

    try:
        db = sqlite3.connect("BDD.db")
        cursor = db.cursor()
        cursor.execute("DELETE FROM pacienteSintomas WHERE paciente= %s" %paciente)
        db.commit() #Guardar los datos
        print ("Eliminado con exito")
    except sqlite3.OperationalError as errorSQL:
        print("Error ejecutando comando: ",errorSQL)
    finally:
        db.close()

#-------------------------------CONSULTAS---------------------------------------

def personasEnRiesgo():
    pass

def personaPorEnfermedad():
    pass

def sospechosas():
    pass

def indicadores():
    pass