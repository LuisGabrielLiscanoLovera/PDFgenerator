#coding: utf-8
# -*- coding: rot13 -*-
__author__="Luis liscano"

from reportlab.pdfgen import canvas
from reportlab.lib.colors import *
from reportlab.lib.pagesizes import letter, A4
from datetime import datetime as t
from os import path, remove,startfile
import sqlite3 as sq
a=t.now()
if (a.month <10):
    b=("0"+str(a.month))
else:
    b=str(a.month)
if (a.day<10):
    d=("0"+str(a.day))
else:
    d=str(a.day)

dia="[ "+d+"/"+b+"/"+str(a.year)+" ]"
print(dia)
min=a.minute
if (min <10):
    min="0"+str(a.minute)
hora="[ "+str(a.hour)+":"+str(min)+":"+str(a.second)+" ]"#hora 24
class Base:

    print(">>> MIN 1 and  MAX 25   <<<")
    ne=int(input("Cantidad de Equipo: "))
    if ne>25:
        print("Fuera de Rango \nCierre del programa....")
        exit()
    elif ne<1:
        print("Fuera de Rango \nCierre del programa.......")
        exit()
    equiposE=range(ne)
    color=""
    nombre_archivo=""
    hora=""
    dia=""
    N_E=""
    N_P=""    
    def __init__(self,nombreA,np,ne,h,d,s,cc,ep,cic,tc,rp,cit,nts):
        self.Entregado_por=ep
        self.Cedula_cliente=cic
        self.Telefono_cliente=tc
        self.Resivido_tecnico=rp
        self.Cedula_tecnio=cit
        self.nombre_archivo=nombreA
        self.folder_path=path.join('pdf/')
        self.ST=nts
        self.N_P=np
        self.N_E=ne
        self.hora=h
        self.dia=d
        self.select=s
        self.codicoC=cc
    def invocarPdf(self):
      c=canvas.Canvas(self.folder_path+self.nombre_archivo)
      def BasePdf():
        LM=path.join(path.dirname(path.abspath(__file__)),'logo/LM.png' )
        logoCASA=path.join(path.dirname(path.abspath(__file__)),'logo/logoCASA.png' )
        c.drawImage(LM, 30, 740, 80, 80,preserveAspectRatio=True)
        c.drawImage(logoCASA, 475, 740, 80, 80,preserveAspectRatio=True)
        c.setFont('Helvetica',7)
        c.drawString(120,810,"REPÚBLICA BOLIVARIANA DE VENEZUELA MINISTERIO DEL PODER POPULAR PARA ALIMENTACIÓN")
        c.drawString(180,795,"CORPORACIÓN DE ABASTECIMIENTO Y SERVICIOS AGRÍCOLAS")
        c.drawString(160,780,"GERENCIA DE SISTEMA SUPERIOR DE ABASTECIMIENTO SEGURO (GSSAS)")
        c.drawString(270,765,"MARICHES")
        c.setFont('Helvetica',17)
        c.drawString(100+50,810-70,"Servicio Técnico / Nota de Entrega")
      #-----------------------------------------------------------------------------------------------------------------------
                                              #Numero de control
        c.setFont('Helvetica',12)
        c.rect(360,682,220,30)
        c.drawString(365,686,"Fecha de Elaboración:      "+self.dia)
        c.drawString(365,700,"Número de Control:   "+str(a.year)+b+d+"-ST-00"+self.ST)
        c.setFont('Helvetica',9)
        c.drawString(540,673,"PAG  "+self.N_P)
        #-----------------------------------------------------------------------------------------------------------------------
                                                #codigo de cadena
        c.setFont('Helvetica',10)
        c.drawString(30,705,"Código: "+self.codicoC)
        c.drawString(30,690,"Cadena: "+self.select.upper())
        #------------------------------------------------------------------------------------------------------------
                                               # lines and rect
        #c.setFillColor(gray)
        #linias dvicion cuadro iz
        c.line(30,435,30,632)
        c.line(50,435,50,632)
        c.line(100,435,100,632)
        c.line(210,435,210,632)
        c.line(225,435,225,632)
        c.line(240,435,240,632)
        c.line(255,435,255,632)
        c.line(270,435,270,632)
        c.line(285,435,285,632)
        c.line(300,435,300,632)
        #linias dvicion cuadro derecho
        c.line(310,435,310,632)
        c.line(333,435,333,632)
        c.line(356,435,356,632)
        c.line(376,435,376,632)
        c.line(399,435,399,632)
        c.line(421,435,421,632)
        c.line(443,435,443,632)
        c.line(465,435,465,632)
        c.line(487,435,487,632)
        c.line(509,435,509,632)
        c.line(531,435,531,632)
        c.line(580,435,580,632)
        c.line(30,435,580,435)#ultima linia horizontal
        c.rect(210,395,206,15,fill=0)#cantida de equipos enatregados
        c.rect(310,650,270,20,fill=0)#cuadro derecha
        c.rect(310,632,270,15,fill=0)#INDIQUE LA FALLA DEL EQUIPO
        c.rect(310,617,23,15,fill=0)#PAN
        c.rect(333,617,23,15,fill=0)#LEC
        c.rect(356,617,20,15,fill=0)#SOF
        c.rect(376,617,23,15,fill=0)#TEC
        c.rect(399,617,22,15,fill=0)#FAN
        c.rect(421,617,22,15,fill=0)#ELE
        c.rect(443,617,22,15,fill=0)#DD
        c.rect(465,617,22,15,fill=0)#MEM
        c.rect(487,617,22,15,fill=0)#TAR
        c.rect(509,617,22,15,fill=0)#LIC
        c.rect(531,617,49,15,fill=0)#CAM
        c.rect(30,650,270,20,fill=0)#header information
        c.rect(30,617,20,30,fill=0)#label N°
        c.rect(50,617,50,30,fill=0)#equipo
        c.rect(100,617,110,30,fill=0)#serial equipo
        c.rect(210,632,30,15,fill=0)#CAR
        c.rect(210,617,15,15,fill=0)#S
        c.rect(225,617,15,15,fill=0)#N
        c.rect(240,632,30,15,fill=0)#CAB
        c.rect(240,617,15,15,fill=0)#s
        c.rect(255,617,15,15,fill=0)#N
        c.rect(270,632,30,15,fill=0)#CAJA
        c.rect(270,617,15,15,fill=0)#N
        c.rect(285,617,15,15,fill=0)#S
        c.rect(30,270,550,40)#leyenda
        c.line(35,338,575,338)#linias de observaciones
        c.line(35,323,575,323)#linias de observaciones
        c.rect(550,360,10,10)#generar no entrega
        #ENTREGA y DEVOLUCION
        c.rect(30,170,550,100)#RECTANGULO 1
        c.rect(30,255,550,15)
        c.rect(30,70,550,100)#RECTANGULO 2
        c.rect(30,155,550,15, fill=0)
        #---------------------------------------Texto de del cuadro Izquierdo y dere ----------------------------------
        c.setFillColor(black)
        c.drawString(35,655,"INFORMACIÓN                                          ACCESORIOS")
        c.drawString(35,627,"N°")
        c.drawString(56,627,"EQUIPO")
        c.drawString(105,628,"SERIAL DEL EQUIPO")
        c.drawString(350,655,"DEPARTAMENTO DE SOPORTE TÉCNICO")
        c.drawString(385,635,"INDIQUE LA FALLA DEL EQIPO")
        c.drawString(212,399,"  CANTIDAD DE HICC  ENTREGADOS: "+str(self.N_E))#+"/")+str(self.N_E))#Cantidad de equipos entregados
        c.setFont('Helvetica',8)
        c.drawString(216,635,"CAR")
        c.drawString(215,620,"S")
        c.drawString(230,620,"N")
        c.drawString(246,635,"CAB")
        c.drawString(245,620,"S")
        c.drawString(260,620,"N")
        c.drawString(276,635,"CAJA")
        c.drawString(275,620,"S")
        c.drawString(288,620,"N")
        c.drawString(313,620,"PAN")
        c.drawString(336,620,"LEC")
        c.drawString(358,620,"SOF")
        c.drawString(379,620,"TEC")
        c.drawString(401,620,"FAN")
        c.drawString(423,620,"ELE")
        c.drawString(445,620,"HDD")
        c.drawString(467,620,"MEM")
        c.drawString(489,620,"TAR")
        c.drawString(513,620,"LIC")
        c.drawString(538,620,"CAMBIO")
        c.drawString(35,370,"OBSERVACIONES:")
        print("*********************************************\n¿Desea incluir alguna observacion? ")

        def obs():
            observacion = input("[S/n]--->:")
            observacion = observacion.upper()
            if (observacion == "S"):
                print("Maximo text 240")
                nota=str(input("--->:"))
                c.drawString(35, 340,nota[:112])
                if (len(nota)>112):
                    notaD=nota[112::]
                    c.drawString(35, 327,notaD)
                    if (len(notaD)>112):
                        notaT=notaD[112::]
                        c.drawString(35, 315,notaT)
                        print(notaT)
                        print(len(notaT))
            elif (observacion == "N"):
                print("No hay observacion")
            else:
                print("Error de sintaxis\n¿Desea incluir alguna observacion? \nS=si\nN=No\n")
                return obs()
        obs()
        c.drawString(357,363,"Generar Nota de Entrega de Cambios por Garantia")
        c.drawString(35,300,"LEYENDA DE FALLAS:  PAN:Pantalla  LEC:Lectora  SOF:software  TEC: Teclado  FAN:Ventilador  ELE:Corriente  HDD:Disco duro")#leyenda
        c.drawString(35,285,"MEN:Memoria  TAR:Tarjeta  LIC:Licencia  CAMBIO: Cambio de equipo HICC")
        #recivo
        c.drawString(230,260,"RECEPCION DEL EQUIPO PARA REVISIÓN")
        c.drawString(35,243,"Entregado por:    Nombre y Apellido:  "+self.Entregado_por+"                              Recibido por:    Nombre y apellido:  "+self.Resivido_tecnico.upper())
        c.drawString(35,223,"Cédula:  "+self.Cedula_cliente+"         Telf:  "+self.Telefono_cliente+"                                                     Cédula:  "+self.Cedula_tecnio+"       Telf:  0212-240-4525")
        c.drawString(35,203,"Fecha:  "+self.dia)
        c.drawString(346,203,"Fecha:  "+self.dia)
        c.drawString(35,185,"Hora:    "+self.hora)
        c.drawString(346,185,"Hora:    "+self.hora)
        c.drawString(150,185,"       Firma: _______________                                                                            Firma: _______________")
        c.drawString(230,160,"ENTREGA Y/O DEVOLUCIÓN DEL EQUIPO")
        c.drawString(100,45,"Solo para ser llenado por la Gerencia de Sistema Superior de Abastecimiento Seguro (GSSAS)Autorizado por:")
        c.drawString(70,25,"Nombre Y apellido: OSWALDO BARRIOS  Fecha: "+self.dia+"  Hora: "+self.hora+"  Firma:__________________________")
        #entrega
        print("*********************************************\n¿Se retiran los equipos (HOY)?")

        def retiro():
            despacho = input("[S/n]--->:")
            despacho = despacho.upper()
            if (despacho == 'S'):
                print("Dijo que si se la lleva hoy")
                c.drawString(35, 142,
                             "Entregado por     Nombre y Apellido:_________________                               Recibido por     Nombre y apellido:  "+self.Entregado_por)
                c.drawString(35, 122,
                             "Cédula:  _______________         Telf: 0212-240-4525                                      Cédula:  "+self.Cedula_cliente+"     Telf:  "+self.Telefono_cliente)
                c.drawString(35, 102,
                             "Fecha:  "+self.dia+"                                                                                            Fecha:  "+self.dia)

                c.drawString(150, 85,"       Firma:_________________                                                                     Firma: _________________")


            elif (despacho == "N"):
                print("¡Los euipos no se entregan hoy!")
                c.drawString(35, 142,
                             "Entregado por     Nombre y Apellido:  _________________                              Recibido por     Nombre y apellido:  _______________")
                c.drawString(35, 122,
                             "Cédula:  _______________         Telf: 0212-240-4525                                      Cédula:  ________________     Telf:_______________")
                c.drawString(35, 102,
                             "Fecha:  [        /        /        ]                                                                                            Fecha:  [        /        /        ]")
                c.drawString(150, 85,
                             "       Firma:___________________                                                                            Firma: __________________")

            else:
                print("Error de sintaxis\n¿Se retiran los equipos (HOY)? \nS=si\nN=No\n")
                return retiro()
        retiro()
        c.setFillColor(white)
        c.rect(300,435,10,235,fill=1)#Horizontal que borra linesas intermedio
        c.showPage()
      baseD = path.join(path.dirname(path.abspath(__file__)), 'data/desarrollo.db')
      conexion = sq.connect(baseD)
      cursor = conexion.cursor()
      print("conexion Exitosa")
      sql = '''
                    CREATE TABLE IF NOT EXISTS hicc(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    cadena VARCHAR (50) NOT NULL,
                    serial VARCHAR (16) NOT NULL,
                    fecha DATE NOT NULL,
                    hora VARCHAR (15) NOT NULL,
                    codigoControl VARCHAR (16) NOT NULL)'''
      if (cursor.execute(sql)):print("Tabla creada con exito....")
      else:print("error")
      cadenas = self.select
      fecha=dia
      codigoC=str(a.year)+b+d+"-ST-00"+self.ST

      def diablos():
          argumentos = (cadenas, metaData, codigoC,fecha, self.hora)
          sql2 = ('''INSERT INTO hicc(cadena,serial,codigoControl,fecha,hora)
          VALUES (?,?,?,?,?)''')
          if (cursor.execute(sql2, argumentos)):
              pass
          else:
              print(" a ocurrido un error al guardar el registro")
      for i in self.equiposE:
       i*=15
       c.setFont("Helvetica",10)
       c.line(30,600-i,580,600-i)
       c.drawString(35,603-i,""+str(round((i/15)+1)))
       c.drawString(60,603-i,"HICC")
       metaDataDirectorio=path.join(path.dirname(path.abspath(__file__)),'metadata/metadata.txt' )
       archivo = open(metaDataDirectorio,"a")
       metaData = input(u"Serial(N°" + str(round((i / 15) + 1)) + "):").upper()
       diablos()
       c.drawString(102,603-i,metaData)
       archivo.write(metaData)
       archivo.write("\n")
       archivo.close()
       if (i==165):
         break
      if (self.ne>12):
        BasePdf()
        self.N_P=("2/2")
      for i in self.equiposE:
        i*=15
        if(i>165):
          metaDataDirectorio = path.join(path.dirname(path.abspath(__file__)), 'metadata/metadata.txt')
          archivo = open(metaDataDirectorio, "a")
          c.setFont("Helvetica",10)
          c.line(30,780-i,580,780-i)
          metaData=input(u"Serial(N°"+str(round((i/15)+1))+"):").upper()
          diablos()
          c.drawString(102,783-i,metaData)
          c.drawString(60,783-i,"HICC")
          c.drawString(35,783-i,""+str(round((i/15)+1)))
          archivo.write(metaData)
          archivo.write("\n")
          archivo.close()
      conexion.commit()
      cursor.close()
      BasePdf()
      c.save()
