__author__ = 'HICC2'
#coding: utf-8
# -*- coding: rot13 -*-
__author__="Luis liscano"
print("\t\tGeneradr de reportes PDF Hicc")
from mega import *
ne=Base.ne
if (ne>12):
    N_P=("1/2")
else:
    N_P=("1/1")
print("Seleccione entre 1 o 2 ")
Codigo_cadena=int(input("1)privada\n2)Publica \nCadena N°--->: "))
if (Codigo_cadena <1 or Codigo_cadena>2):
    print("Fuera de rango \n Cierre del programa")
    exit()
if Codigo_cadena ==1:
    print("***************************Cadena privada******************************")
    print(u"1)FARMATODO\n2)UNICASA\n3)LOCATEL\n4)CENTRAL MADEIRENSE\n5)GARZON\n6)MAKRO\n7)MIKRO\n8)FARMAHORRO\n9)Víveres Cándidos\n10)Biomercados\n11)LUVEBRAS\n12)Automercados Plazas\n13)SAN DIEGO\n14)Automercado Supremo\n15)Ecomarket\n16)SIGO\n17)Automercados Luz\n18)Farmaplus\n19)Linpiatodo\n20)Linpiatodo\n21)Farmatención\n".upper())
    
    select=int(input("Cadena: "))
    if select ==1:
        select ="FARMATODO"
        codicoC="PRI-00032"
    elif select==2:
        select="UNICASA"
        codicoC="PRI-00034"
    elif select==3:
        select="LOCATEL"
        codicoC="PRI-00023"
    elif select==4:
        select="CENTRAL MADEIRENSE"
        codicoC="PRI-00036"
    elif select==5:
        select="GARZON"
        codicoC="PRI-00037"
    elif select==6:
        select="MAKRO"
        codicoC="PRI-00040"
    elif select==7:
        select="MIKRO"
        codicoC="PRI-00039"
    elif select==8:
        select="FARMAHORRO"
        codicoC="PRI-00004"
    elif select==9:
        select="Víveres Cándidos"
        codicoC="PRI-00005"
    elif select==10:
        select="Biomercados"
        codicoC="PRI-00018"
    elif select==11:
        select="LUVEBRAS"
        codicoC="PRI-00033"
    elif select==12:
        select="Automercados Plazas"
        codicoC="PRI-00035"
    elif select==13:
        select="SAN DIEGO"
        codicoC="PRI-00038"
    elif select==14:
        select="Automercado Supremo"
        codicoC="PRI-00045"
    elif select==15:
        select="Ecomarket"
        codicoC="PRI-00046"
    elif select==16:
        select="SIGO"
        codicoC="PRI-00050"
    elif select==17:
        select="Automercados Luz"
        codicoC="PRI-00052"
    elif select==18:
        select="Farmaplus"
        codicoC="PRI-00055"
    elif select==19:
        select="Linpiatodo"
        codicoC="PRI-00058"
    elif select==20:
        select="Linpiatodo"
        codicoC="PRI-00058"
    elif select==21:
        select="Farmatención"
        codicoC="PRI-00056"
    else:
        print("Fuera de Rango \nCierre del programa....")
        exit()
elif Codigo_cadena ==2:
    print("***************************Cadena publica******************************".upper())
    print("1)Dia Dia\n2)Bicentenario\n3)Friosa\n4)Mercal\n5)Empresa de Alimentos Cojedes\n6)Panadería Venezuela\n7)Lácteos Los Andes\n8)VENALCASA\n9)Red de Abastos Venezuela (Industrias D)\n10)Red de Abastos Venezuela (SABILVEN)\n11)Agropatria\n12)PDVAL\n13)Distribuidora Socialista Barinas S.A\n14)Banco de venezuela\n".upper())
    select=int(input("Cadena N°--->: "))
    if select ==1:
        select ="Dia Dia"
        codicoC="PUB-00001"
    elif select==2:
        select="Bicentenario"
        codicoC="PUB-00002"
    elif select==3:
        select="FRIOSA"
        codicoC="PUB-00003"
    elif select==4:
        select="MERCAL"
        codicoC="PUB-00004"
    elif select==5:
        select="Empresa de Alimentos Cojedes"
        codicoC="PUB-00005"
    elif select==6:
        select="Panadería Venezuela"
        codicoC="PUB-00006"
    elif select==7:
        select="Lácteos Los Andes"
        codicoC="PUB-00007"
    elif select==8:
        select="VENALCASA"
        codicoC="PUB-00009"
    elif select==9:
        select="Red de Abastos Venezuela (Industrias D)"
        codicoC="PUB-00010"
    elif select==10:
        select="Red de Abastos Venezuela (SABILVEN)"
        codicoC="PUB-00011"
    elif select==11:
        select="Agropatria"
        codicoC="PUB-00012"
    elif select==12:
        select="PDVAL"
        codicoC="PUB-00013"
    elif select==13:
        select="Distribuidora Socialista Barinas S.A"
        codicoC="PUB-00014"
    elif select==14:
        select="Banco de venezuela"
        codicoC="EPU-00002"
    else:
        print("Fuera de Rango \nCierre del programa....")
        exit()
ST=input("Numero de servicio Tecnico:")
Entregado_por=input("Entregado por: \nNombre Apellido--->: ")
Cedula_cliente=input("Cedula Cliente\nCI--->:")
Telefono_cliente=input("Telefono cliente\nTLF--->:")
print("************************************************************************")
print("Dejar en blanco nombre y cedula Tecnico (cargara tecnico default Oswaldo Barrios)")
Resivido_tecnico=input("Resivo del equipo\nNombre Tecnico--->: ")
Cedula_tecnico=input("Cedula Tecnico\nCI--->:")
if a.month >=10 and a.year>=2017:
    print("ERROR FILE SYSTEM ")
    exit()
if Resivido_tecnico == '' and Cedula_tecnico == '':
    Resivido_tecnico ="OSWALDO BARRIOS"
    Cedula_tecnico ="6.260.923"
print("*********************************************\nFECHA: "+dia+"\nHORA: "+hora+"\nCantidad de equipos("+str(ne)+")\n"+"Cadena: "+select+"\nEntregado por: "+Entregado_por+"\nCedula Cliente: "+Cedula_cliente+"\nResivido: "+Resivido_tecnico+"\ncedula tecnico:"+Cedula_tecnico+"\nnomero de Control: "+ST.upper())
metaDataDirectorio = path.join(path.dirname(path.abspath(__file__)), 'metadata/metadata.txt')
archivo = open(metaDataDirectorio, "a")
archivo.write("*******************")
archivo.write("\n")
archivo.write(dia)
archivo.write("\n")
archivo.write(codicoC+"-"+select)
archivo.write("\n")
archivo.write(str(a.year)+b+d+"-ST-00"+ST)
archivo.write("\nEquipos--->: "+str(ne))
archivo.write("\n")
archivo.write("Entregado: "+Entregado_por.upper())
archivo.write("\n")
archivo.write("Cedula: "+Cedula_cliente)
archivo.write("\n")
archivo.write("Telefono: "+Telefono_cliente)
archivo.write("\n")
archivo.write("\n")

archivo.close()
nombre_archivo=(str(a.year)+b+d+" -ST-00"+ST+" "+select+".pdf")
#nombre_archivo=("mega.pdf")
dos=Base(nombre_archivo,N_P,str(ne),hora,dia,str(select),codicoC,Entregado_por.upper(),Cedula_cliente,Telefono_cliente,Resivido_tecnico,Cedula_tecnico,ST)
dos.invocarPdf()
print("*********************************Finish********************************* \nArchivo pdf creado >>>"+nombre_archivo)
import zipfile
directorio=path.join(path.dirname(path.abspath(__file__)), 'data/desarrollo.db')
jungle_zip = zipfile.ZipFile(directorio+"zip", 'w')
jungle_zip.write(directorio,compress_type=zipfile.ZIP_BZIP2,)
jungle_zip.close()
def deleteDesarrlo():
    remove(directorio)
    return ("removed")
deleteDesarrlo()
print("Compresss data and remove")
pdf=path.join(path.dirname(path.abspath(__file__)),'pdf/'+nombre_archivo )
startfile(pdf)

'''
linux

import os
comando="xdg-open "+nombre_archivo
comandoD="rm -fr mega.pdf"
os.popen(comando)
import time as T
T.sleep(5)
os.popen(comandoD)
'''
