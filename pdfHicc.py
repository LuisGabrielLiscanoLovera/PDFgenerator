import zipfile
from os import path, remove, popen
directorio=path.join(path.dirname(path.abspath(__file__)), 'data/desarrollo.db')
def desconpressDB():    
    fantasy_zip = zipfile.ZipFile(directorio+"zip")
    fantasy_zip.extractall('/')
    fantasy_zip.close()
def deleteBD():
    try:
        existe=path.exists(directorio)
        if (existe==True):            
            remove(directorio)
        else:print("end")
    except PermissionError:        
        popen("del data\*.db")

choise=int(input("\n1)registros\n2)consulta a base de Datos\n3)Salir\n-->:"))
if (choise==1):
    from main import *
elif (choise==2):
    desconpressDB()
    import sqlite3 as sq
    from os import path
    baseD = path.join(path.dirname(path.abspath(__file__)), 'data/desarrollo.db')
    conexion = sq.connect(baseD)
    cursor = conexion.cursor()
    consulta=int(input("1)registro Completo \n2)buscar serial\n3)Consulta a Numero de control\n--->:"))    
    if (consulta==1):
        print("-N-----Cadena----------Serial--------------Fecha------------Hora------Codigo de control\n")
        cursor.execute("SELECT * FROM hicc")
        for registro in cursor:
            print(registro) 
    elif (consulta==2):
        serial=input("incerte serial--->:GWRHICCA000")
        serial="'%"+serial+"'"
        sql='''SELECT * FROM hicc WHERE serial LIKE %s'''%serial
        cursor.execute(sql)
        print("-N-----Cadena----------Serial--------------Fecha------------Hora------Codigo de control\n")
        for registro in cursor:
            print(registro)
    elif (consulta==3):
        NumeroControl=input("incerte Numeros de control con el siguiente formato \'20170101-ST-001\' \n--->:")
        NumeroControl="'%"+NumeroControl+"'"
        sql='''SELECT * FROM hicc WHERE codigoControl LIKE %s'''%NumeroControl
        cursor.execute(sql)
        print("-N-----Cadena----------Serial--------------Fecha------------Hora------Codigo de control\n")
        for registro in cursor:
            print(registro)

elif(choise==3):
    print("Saliendo...")
    exit()
else:
    print("Saliendoo....")
    exit()

deleteBD()