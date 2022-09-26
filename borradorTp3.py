#Integrantes: Agustin Angelini, Matias Luhmann, Alejo Martina, Santiago Roman Meroi
#Comision: 106
import pickle
import os
import io
import os.path
from os import system

def comentarios():

    '''

    DEFINICIÓN DE ARRAYS:                                 DEFINICIÓN DE VARIABLES:

    Peso_Neto: array[1..8]of float                    camion_recib: integer
    Peso_Tara: array[1..8]of float                    cupos: integer
    patentemen: array[1..3]of string                  d: integer
    Peso_Bruto: array[1..8]of float                   j: integer          / local
    prod_cupo: array[1..8]of string                   y: integer          / local
    est_cupo: array[1..8]of char                      i: integer          / local
    pesoneto_prod: array[1..8][1..2]of float          w: integer          / local
    cant_prod: array[1..3]of integer                  previo: string      / local
    patente_cupos: array[1..8]of string               previoprod: integer / local
    aProd: array[1..3]of string                       menu: char
    mayores: array[1..3]of float                      sAdm: char
    menores: array[1..3]of float                      opcionPa: char
    producto_ord: array[1..8]of string                a_elim: int
    patente_ord: array[1..8]of string                 a_modif: int
    pesoneto_ord: array[1..8]of float                 conf_cupo: char
    patentemay: array[1..3]of string                  h_camiones: char
    .                                                 confPbruto: char
    .                                                 confPtara: char
    '''

#DEFINICION DE REORDS
class Operaciones:
    def __init__(self):
        self.patente = ""
        self.codigo_p = 0
        self.fecha_cupo = ""
        self.estado = ''
        self.bruto = 0.0
        self.tara = 0.0

class Productos:
    def __init__(self):
        self.codigo_p = ""
        self.nombre_p = ""

class Rubros:
    def __init__(self):
        self.codigo_r = 0
        self.nombre_r = ""

class Rubros_Productos:
    def __init__(self):
        self.codigo_r = 0
        self.codigo_p = 0
        self.valor_min_admit = 0.0
        self.valor_max_admit = 0.0

class Silos:
    def __init__(self):
        self.codigo_s = 0
        self.nombre_s = ""
        self.codigo_p = 0
        self.stock = 0


def abrir():
    global af_OP, al_OP, Reg_OP, af_PR, al_PR, Reg_PR, af_RU, al_RU , Reg_RU, af_RxP, al_RxP, Reg_RxP, af_S, al_S, Reg_S

    af_OP = "/Users/Alejo Martina/Desktop/Alejo Martina/UTN_ISI_1°año/ayed/trabajopractico/OPERACIONES.dat"                 #archivo fisico ubicaión
    if os.path.exists(af_OP):                                                                #comprueba que existe
        al_OP = open(af_OP,"r+b")
    else:
        al_OP = open(af_OP,"w+b")

    Reg_OP = Operaciones()

    af_PR = "/Users/Alejo Martina/Desktop/Alejo Martina/UTN_ISI_1°año/ayed/trabajopractico/PRODUCTOS.dat"                 #archivo fisico ubicaión
    if os.path.exists(af_PR):                                                                #comprueba que existe
        al_PR = open(af_PR,"r+b")
    else:
        al_PR = open(af_PR,"w+b")

    Reg_PR = Productos()

    af_RU = "/Users/Alejo Martina/Desktop/Alejo Martina/UTN_ISI_1°año/ayed/trabajopractico/RUBROS.dat"                 #archivo fisico ubicaión
    if os.path.exists(af_RU):                                                                #comprueba que existe
        al_RU = open(af_RU,"r+b")
    else:
        al_RU = open(af_RU,"w+b")

    Reg_RU = Rubros()

    af_RxP = "/Users/Alejo Martina/Desktop/Alejo Martina/UTN_ISI_1°año/ayed/trabajopractico/RUBROS_X_PRODUCTO.dat"                 #archivo fisico ubicaión
    if os.path.exists(af_RxP):                                                                #comprueba que existe
        al_RxP = open(af_RxP,"r+b")
    else:
        al_RxP = open(af_RxP,"w+b")

    Reg_RxP = Rubros_Productos()

    af_S = "/Users/Alejo Martina/Desktop/Alejo Martina/UTN_ISI_1°año/ayed/trabajopractico/SILOS.dat"                 #archivo fisico ubicaión
    if os.path.exists(af_S):                                                                #comprueba que existe
        al_S = open(af_S,"r+b")
    else:
        al_S = open(af_S,"w+b")

    Reg_S = Silos()

def contadores():

    global producto_ord,patente_ord ,pesoneto_ord, mayores, menores, patentemay, patentemen, pesoneto_prod, cant_prod, camion_recib, Peso_Neto, prod_cupo, Peso_Tara ,Peso_Bruto, est_cupo, cupos, aProd, patente_cupos   

    producto_ord=[' ']*8
    patente_ord=[' ']*8
    pesoneto_ord=[0]*8
    pesoneto_prod=[[0]*3 for i in range(2)]
    cant_prod=[0]*3
    camion_recib=0
    Peso_Neto=[0]*8
    prod_cupo=[0]*8
    Peso_Tara=[0]*8
    Peso_Bruto=[0]*8
    patente_cupos=[' ']*8
    aProd=[' ']*3
    est_cupo=[0]*8
    cupos=0
    mayores=[0]*3
    menores=[60]*3
    patentemay=[' ']*3
    patentemen=[' ']*3

def programa():

    global menu, contadores
    system('cls')
    abrir()

    menu = input('Menú Principal: \n\n 1-Administraciones \n 2-Entrega de Cupos \n 3-Recepción \n 4-Registrar Calidad \n 5-Registrar Peso Bruto \n 6-Registrar Descarga \n 7-Registrar Tara \n 8-Reportes \n 0-Cerrar programa \n\n Ingrese un número: ')
    while menu != '0' and menu != '1' and menu != '2' and menu != '3' and menu != '4' and menu != '5' and menu != '6' and menu != '7' and menu != '8':
        system('cls')
        print('Ingrese un valor correcto. \n')
        menu = input('Menú Principal: \n\n 1-Administraciones \n 2-Entrega de Cupos \n 3-Recepción \n 4-Registrar Calidad \n 5-Registrar Peso Bruto \n 6-Registrar Descarga \n 7-Registrar Tara \n 8-Reportes \n 0-Cerrar programa \n\n Ingrese un número:  ')

    while menu != '0':
        system('cls')
        seleccion()

        menu = input('Menú Principal: \n\n 1-Administraciones \n 2-Entrega de Cupos \n 3-Recepción \n 4-Registrar Calidad \n 5-Registrar Peso Bruto \n 6-Registrar Descarga \n 7-Registrar Tara \n 8-Reportes \n 0-Cerrar programa \n\n Ingrese un número: ')
        while menu != '0' and menu != '1' and menu != '2' and menu != '3' and menu != '4' and menu != '5' and menu != '6' and menu != '7' and menu != '8':
            system('cls')
            print('Ingrese un valor correcto.')
            menu = input('Menú Principal: \n\n 1-Administraciones \n 2-Entrega de Cupos \n 3-Recepción \n 4-Registrar Calidad \n 5-Registrar Peso Bruto \n 6-Registrar Descarga \n 7-Registrar Tara \n 8-Reportes \n 0-Cerrar programa \n\n Ingrese un número:  ')

def seleccion():

    if menu == '1':
        administracion()
        system('cls')

    elif menu == '2' :
        entrega_cupos()
        system('cls')

    elif menu == '3' :
        recepcion()
        system('cls')

    elif menu == '4' :
        print('\n\n---------------------------\n\nEsta función está en desarrollo\n\n---------------------------')

    elif menu == '5' :
        peso_bruto()
        system('cls')

    elif menu == '6' :
        print('\n\n---------------------------\n\nEsta función está en desarrollo\n\n---------------------------')

    elif menu == '7' :
        peso_tara()
        system('cls')

    elif menu == '8' :
        reportes()

def exh_indice(x,fil):
    for i in range (0,fil):
        print(i+1,'--',x[i], '\n')

def cargaArray(x,fil):
    for i in range (0,fil):
        x[i]=input('Ingrese el nombre del producto: ')

def administracion():

    global sAdm




    sAdm = input('\n Administraciones: \n\n A- Titulares \n B- Productos \n C- Rubros \n D- Rubros por producto \n E- Silos \n F- Sucursales \n G- Producto por titular \n V- Volver al menú principal \n\n Ingrese una letra: ')
    while sAdm.upper()!='A' and sAdm.upper()!='B' and sAdm.upper()!='C' and sAdm.upper()!='D' and sAdm.upper()!='E' and sAdm.upper()!='F' and sAdm.upper()!='G' and sAdm.upper()!='V':
        system('cls')
        print('Ingrese un valor correcto. ')
        sAdm = input('\n Administraciones: \n\n A- Titulares \n B- Productos \n C- Rubros \n D- Rubros por producto \n E- Silos \n F- Sucursales \n G- Producto por titular \n V- Volver al menú principal \n\n Ingrese una letra: ')

    while sAdm.upper() != 'V':

        if sAdm.upper() == 'A':
            system('cls')
            print("Esta funcionalidad esta en desarrollo")

        elif sAdm.upper() == 'B':
            system('cls')
            producto()

        elif sAdm.upper() == 'C':
            system('cls')
            P_Adm(sAdm.upper())

        elif sAdm.upper() == 'D':
            system('cls')
            P_Adm(sAdm.upper())

        elif sAdm.upper() == 'E':
            system('cls')
            P_Adm(sAdm.upper())

        elif sAdm.upper() == 'F':
            system('cls')
            print("Esta funcionalidad esta en desarrollo")

        elif sAdm.upper() == 'G':
            system('cls')
            print("Esta funcionalidad esta en desarrollo")

        sAdm = input('\n Administraciones: \n\n A- Titulares \n B- Productos \n C- Rubros \n D- Rubros por producto \n E- Silos \n F- Sucursales \n G- Producto por titular \n V- Volver al menu principal \n\n Ingrese una letra: ')
        while sAdm.upper()!='A' and sAdm.upper()!='B' and sAdm.upper()!='C' and sAdm.upper()!='D' and sAdm.upper()!='E' and sAdm.upper()!='F' and sAdm.upper()!='G' and sAdm.upper()!='V':
            system('cls')
            print('Ingrese un valor correcto.')
            sAdm = input('\n Administraciones: \n\n A- Titulares \n B- Productos \n C- Rubros \n D- Rubros por producto \n E- Silos \n F- Sucursales \n G- Producto por titular \n V- Volver al menú principal \n\n Ingrese una letra: ')

    system('cls')

def alta_prod():
    global Reg_PR, al_PR, af_PR

    op="s"
    while op.upper()=="S":
        if os.path.getsize(af_PR)==0:
            Reg_PR.nombre_p = input("Ingrese el Nombre de producto: ")
            Reg_PR.nombre_p = Reg_PR.nombre_p.ljust(30," ")
            Reg_PR.codigo_p = "0"
            Reg_PR.codigo_p = Reg_PR.codigo_p.rjust(2,"0")
            pickle.dump(Reg_PR, al_PR)
            al_PR.flush()
            print("Se le asigno el codigo: 0 para el producto: ", Reg_PR.nombre_p)
        else:

            al_PR.seek(0)
            Reg_PR = pickle.load(al_PR)
            tamr = al_PR.tell()
            x = os.path.getsize(af_PR)
            cantr = int(x/tamr)
            al_PR.seek(x)
            Reg_PR.nombre_p = input("Ingrese el Nombre de producto: ")
            Reg_PR.nombre_p = Reg_PR.nombre_p.ljust(30," ")
            Reg_PR.codigo_p = str(cantr)
            Reg_PR.codigo_p = Reg_PR.codigo_p.rjust(2,"0")
            pickle.dump(Reg_PR, al_PR)
            al_PR.flush()
            print("Se le asigno el codigo: ", cantr, "para el producto: ", Reg_PR.nombre_p)
        op=input("Desea dar de alta un nuevo producto (s o n)")
        while op.upper()!="S" and op.upper()!="N":
            op=input("Desea dar de alta un nuevo producto (s o n)")

def baja_prod():
    if os.path.getsize(af_PR)==0:
        print("Archivo vacio")
    else:
        al_PR.seek(0)
        Reg_PR=pickle.load(al_PR)
        print(Reg_PR.nombre_p, Reg_PR.codigo_p)
        while al_PR.tell() < os.path.getsize(af_PR):
            Reg_PR=pickle.load(al_PR)
            print(Reg_PR.nombre_p, Reg_PR.codigo_p)
        cod=input(" \n Ingrese el codigo del producto a eliminar: ")
        al_PR.seek(0)
        pos=0
        Reg_PR=pickle.load(al_PR)
        while al_PR.tell() < os.path.getsize(af_PR) and Reg_PR.codigo_p!=cod:
            pos=al_PR.tell()
            Reg_PR=pickle.load(al_PR)
        if Reg_PR.codigo_p==cod:
            Reg_PR.nombre_p = ""
            Reg_PR.nombre_p = Reg_PR.nombre_p.ljust(30," ")
            al_PR.seek(pos)
            pickle.dump(Reg_PR, al_PR)
            al_PR.flush()
        else:
            print("se ingreso un cod erroneo")

def muestra_prod():
    if os.path.getsize(af_PR)==0:
        print("Archivo vacio")
    else:
        op=" "
        while op.upper()!="V":
            al_PR.seek(0)
            Reg_PR=pickle.load(al_PR)
            print(Reg_PR.nombre_p, Reg_PR.codigo_p)
            while al_PR.tell() < os.path.getsize(af_PR):
                Reg_PR=pickle.load(al_PR)
                print(Reg_PR.nombre_p, Reg_PR.codigo_p)
            op=input("Si desea volver ingrese V ")
            while op.upper()!='V':
                op=input("Si desea volver ingrese V ")

def modificacion_prod():

    if os.path.getsize(af_PR)==0:
        print("Archivo vacio")
    else:
        al_PR.seek(0)
        Reg_PR=pickle.load(al_PR)
        print(Reg_PR.nombre_p, Reg_PR.codigo_p)
        while al_PR.tell() < os.path.getsize(af_PR):
            Reg_PR=pickle.load(al_PR)
            print(Reg_PR.nombre_p, Reg_PR.codigo_p)

        al_PR.seek(0)
        Reg_PR=pickle.load(al_PR)

        cod=input("Ingrese el codigo del producto a modificar")
        pos=0
        while al_PR.tell() < os.path.getsize(af_PR) and Reg_PR.codigo_p!=cod:
            pos=al_PR.tell()
            print
            Reg_PR=pickle.load(al_PR)

        if Reg_PR.codigo_p==cod:
            Reg_PR.nombre_p=input("Ingrese el nombre del producto")
            Reg_PR.nombre_p = Reg_PR.nombre_p.ljust(30," ")
            al_PR.seek(pos)
            pickle.dump(Reg_PR, al_PR)
            al_PR.flush()
        else:
            print("Codigo inexistente")



def producto():
    global opcionPA, aProd
    opcionPA = input('\n Productos: \n\n A- Alta \n B- Baja \n C- Consulta \n M- Modificación \n V- Volver al menú anterior \n\n Ingrese una letra: ')
    while opcionPA.upper() != 'A' and opcionPA.upper() != 'B' and opcionPA.upper() != 'C' and opcionPA.upper() != 'M' and opcionPA.upper() != 'V':
        system('cls')
        print('Ingrese una opcion correcta.')
        opcionPA = input ('\n Productos: \n\n A- Alta \n B- Baja \n C- Consulta \n M- Modificación \n V- Volver al menú anterior \n\n Ingrese una letra: ')

    while opcionPA.upper() != 'V':

        if opcionPA.upper() == 'A':
            alta_prod()

        elif opcionPA.upper()=='B':
            baja_prod()

        elif opcionPA.upper() == 'C':
            system('cls')
            muestra_prod()

        elif opcionPA.upper() == 'M':
            modificacion_prod()


        opcionPA =input('Productos: \n\n A- Alta \n B- Baja \n C- Consulta \n M- Modificación \n V- Volver al menú anterior \n\n Ingrese una letra: ')
        while opcionPA.upper() != 'A' and opcionPA.upper() != 'B' and opcionPA.upper() != 'C' and opcionPA.upper() != 'M'and opcionPA.upper() != 'V':
            system('cls')
            print(' \nIngrese una opción correcta. ')
            opcionPA = input('Productos: \n\n A- Alta \n B- Baja \n C- Consulta \n M- Modificación \n V- Volver al menú anterior \n\n Ingrese una letra: ')
    system('cls')

def entrega_cupos():

    global cupos, patente_cupos, est_cupo, prod_cupo

    conf_cupo=input('Desea registrar un nuevo cupo? (S o N): ')
    while conf_cupo.upper() != 'S' and conf_cupo.upper() != 'N':
        system('cls')
        print('Ingrese un valor correcto.')
        conf_cupo=input('Desea registrar un nuevo cupo? (S o N): ')

    while cupos < 8 and conf_cupo.upper() == 'S':
        system('cls')
        exh_indice(aProd,3)
        previoprod=int(input('\nSeleccione el producto (1,2,3), de no encontrarse listado ingrese ¨0¨:'))
        while previoprod!=1 and previoprod!=2 and previoprod!=3 and previoprod!=0:
            system('cls')
            print('Ingrese un valor correcto.')
            exh_indice(aProd,3)
            previoprod=int(input('\nSeleccione el producto (1,2,3), de no encontrarse listado ingrese ¨0¨:'))

        if previoprod==0:
            system('cls')
            print('No se pudo asignar cupo, producto no registrado.')

        else:
            if  aProd[previoprod-1]==' ' or aProd[previoprod-1]=='':
                system('cls')
                print('La opción selecccionada está vacia, ingrese otra.')
            else:
                system('cls')
                previo=str(input('Ingrese la patente del vehículo para asignarle un cupo: '))
                while len(previo)<6 or len(previo)>7:
                    system('cls')
                    print('El rango debe ser de 6 a 7 caracteres.')
                    previo=str(input('Ingrese la patente del vehículo para asignarle un cupo: '))
                i=int(0)
                while i < 8 and patente_cupos[i]!= previo:
                    i=i+1

                if i>7:
                    system('cls')
                    patente_cupos[cupos]=previo
                    est_cupo[cupos]= 'P'
                    prod_cupo[cupos]=aProd[previoprod-1]
                    print('Se le asigno un cupo a la patente:', patente_cupos[cupos])
                    cupos += 1
                    print(cupos)
                else:
                    system('cls')
                    print('La patente ya fue ingresada.')
        system('cls')

        conf_cupo=input('Desea registrar un nuevo cupo? (S o N): ')
        while conf_cupo.upper() != 'S' and conf_cupo.upper() != 'N':
            system('cls')
            print('Ingrese un valor correcto.')
            conf_cupo=input('Desea registrar un nuevo cupo? (S o N): ')

    if cupos == 8:
        print("\nNo hay más cupos disponibles.\n")

def P_Adm(x):

    global opcionPA

    opcionPA = input('A- Alta \n B- Baja \n C- Consulta \n M- Modificación \n V- Volver al menú anterior \n\n Ingrese una letra: ')
    while opcionPA.upper() != 'A' and opcionPA.upper() != 'B' and opcionPA.upper() != 'C' and opcionPA.upper() != 'M' and opcionPA.upper() != 'V':
        print('Ingrese un valor correcto')
        opcionPA = input(' A- Alta \n B- Baja \n C- Consulta \n M- Modificación \n V- Volver al menú anterior \n\n Ingrese una letra: ')

    while opcionPA.upper() != 'V':
        system('cls')
        if opcionPA.upper() =='A':
            system('cls')

            if x=="C":
                print("opcion: ", x)
            elif x=="D":
                print("opcion: ", x)
            else:
                print("opcion: ", x)


        elif   opcionPA.upper() =='B':
            print('---------------------------\n\nEsta función está en desarrollo.\n\n---------------------------')
        elif opcionPA.upper() == 'C':
            system('cls')
            print('---------------------------\n\nEsta función está en desarrollo.\n\n---------------------------')
        elif opcionPA.upper() == 'M':
            system('cls')
            print('---------------------------\n\nEsta función está en desarrollo.\n\n---------------------------')

        opcionPA = input(' A- Alta \n B- Baja \n C- Consulta \n M- Modificación \n V- Volver al menú anterior \n\n Ingrese una letra: ')
        while opcionPA.upper() != 'A' and opcionPA.upper() != 'B' and opcionPA.upper() != 'C' and opcionPA.upper() != 'M' and opcionPA.upper() != 'V':
            print('Ingrese un valor correcto')
            opcionPA = input(' A- Alta \n B- Baja \n C- Consulta \n M- Modificación \n V- Volver al menú anterior \n\n Ingrese una letra: ')

    system('cls')

def recepcion():

    global  patente_cupos, h_camiones, est_cupo, camion_recib, cant_prod

    h_camiones= input('Si hay camiones ingrese "S", de lo contrario ingrese "N": ')
    while h_camiones.capitalize() !='S' and h_camiones.capitalize() != 'N':
        system('cls')
        print('\nIngrese un valor correcto')
        h_camiones= input('\nSi hay camiones ingrese "S", de lo contrario ingrese "N": ')

    while h_camiones.capitalize() =='S':
        system('cls')
        previo=str(input('\nIngrese la patente del camión: '))
        while len(previo)<6 or len(previo)>7:
            system('cls')
            print('\nEl rango de caracteres es de 6 a 7')
            previo=str(input('\nIngrese la patente del camión: '))
        w=int(0)
        while w < 8 and patente_cupos[w]!= previo:
            w=w+1
        if w>7:
            system('cls')
            print('\nEl camión no tiene cupo registrado')
        else:
            if est_cupo[w].upper()=='P':
                print('\nLa patente: ', patente_cupos[w], 'se encuentra en proceso.')
                est_cupo[w]= 'E'
                camion_recib=camion_recib+1
                j=0
                while prod_cupo[w]!= aProd[j] and j<3:
                    j=j+1
                cant_prod[j]=cant_prod[j]+1
            elif est_cupo[w].upper()=='E':
                system('cls')
                print('\nEl camión ya se encuentra en proceso.')
            elif est_cupo[w].upper()=='C':
                system('cls')
                print('\nEl camión ha completado el proceso.')

        h_camiones= input('\nSi hay camiones ingrese "S", de lo contrario ingrese "N": ')
        while h_camiones.capitalize() !='S' and h_camiones.capitalize() != 'N':
            system('cls')
            print('\nIngrese un valor correcto')
            h_camiones= input('\nSi hay camiones ingrese "S", de lo contrario ingrese "N": ')

    print('\n\n---------------------------\n\nNo hay camiones.\n\n---------------------------')

def peso_bruto():

    global Peso_Bruto

    confPbruto = input('Desea registrar un nuevo peso bruto? (S o N): ')
    while confPbruto.upper() != 'S' and confPbruto.upper() != 'N':
        system('cls')
        print('Ingrese un valor correcto.')
        confPbruto = input('\n Desea registrar un nuevo peso bruto? (S o N): ')

    while confPbruto.upper() == 'S':
        system('cls')
        previo = input('Ingrese la patente del camión: ')
        while len(previo)<6 or len(previo)>7:
            system('cls')
            print('El rango de caracteres es de 6 a 7')
            previo=str(input('Ingrese la patente del camión: '))
        y=int(0)

        while y < 8 and patente_cupos[y]!= previo:
            y=y+1
        if y > 7:
            system('cls')
            print('La patente:',previo, 'no tiene cupo asignado.')
        else:
            if est_cupo[y].upper()== 'E':
                if Peso_Bruto[y] == 0:
                    system('cls')
                    Peso_Bruto[y]=int(input('Ingrese el peso bruto en Toneladas dentro del rango permitido (desde 9t a 60t): ')) #si el operador ingresa un valor que no sea un entero, se cierra el programa.
                    while Peso_Bruto[y] < 9 or Peso_Bruto[y] > 60:
                        system('cls')
                        print('Ingrese un valor dentro del rango.')
                        Peso_Bruto[y]=int(input('Ingrese el peso bruto en Toneladas dentro del rango permitido (desde 9t a 60t): '))
                else:
                    system('cls')
                    print('El peso bruto ya se encuentra registrado para la patente: ', patente_cupos[y])
            elif est_cupo[y].upper() == 'P':
                system('cls')
                print('Estado de la patente: Pendiente.')
            elif est_cupo[y].upper()=='C':
                system('cls')
                print('El camión ha completado el proceso.')

        confPbruto = input('\n Desea registrar un nuevo peso bruto? (S o N): ')
        while confPbruto.upper() != 'S' and confPbruto.upper() != 'N':
            system('cls')
            print('Ingrese un valor correcto.')
            confPbruto = input(' Desea registrar un nuevo peso bruto? (S o N): ')

def peso_tara():

    global Peso_Tara, d

    confPtara = input('Desea registrar un nuevo peso tara? (S o N): ')
    while confPtara.upper() != 'S' and confPtara.upper() != 'N':
        system('cls')
        print('Ingrese un valor correcto.')
        confPtara = input('Desea registrar un nuevo peso tara? (S o N): ')

    while confPtara.upper() == 'S':
        system('cls')
        previo = input('Ingrese la patente del camión: ')
        while len(previo)<6 or len(previo)>7:
            system('cls')
            print('El rango de caracteres es de 6 a 7')
            previo=str(input('Ingrese la patente del camión: '))
        d=int(0)

        while d < 8 and patente_cupos[d]!= previo:
            d=d+1
        if d > 7:
            system('cls')
            print('La patente:',previo, 'no tiene cupo asignado.')
        else:
            if est_cupo[d].upper()== 'E':
                if Peso_Bruto[d] !=0:
                    if Peso_Tara[d] == 0:
                        system('cls')
                        Peso_Tara[d]=int(input('Ingrese el peso tara en Toneladas dentro del rango permitido (desde 1t a 8t): ')) #si el operador ingresa un valor que no sea un entero, se cierra el programa.
                        while Peso_Tara[d] < 1 or Peso_Tara[d] > 8:
                            system('cls')
                            print('Ingrese un valor dentro del rango.')
                            Peso_Tara[d]=int(input('Ingrese el peso tara en Toneladas dentro del rango permitido (desde 1t a 8t): '))
                        calc_neto()
                    else:
                        system('cls')
                        print('El peso tara ya se encuentra registrado para la patente: ', patente_cupos[d])
                else:
                    system('cls')
                    print('El peso bruto no se encuentra registrado para la patente: ', patente_cupos[d])
            elif est_cupo[d].upper() == 'P':
                system('cls')
                print('Estado de la patente: Pendiente.')
            elif est_cupo[d].upper()=='C':
                system('cls')
                print('El camión ha completado el proceso.')

        confPtara = input('Desea registrar un nuevo peso tara? (S o N): ')
        while confPtara.upper() != 'S' and confPtara.upper() != 'N':
            system('cls')
            print('Ingrese un valor correcto.')
            confPtara = input('Desea registrar un nuevo peso tara? (S o N): ')

def calc_neto():

    global  patente_cupos, est_cupo, d, Peso_Neto, pesoneto_prod

    Peso_Neto[d] = Peso_Bruto[d] - Peso_Tara[d]
    est_cupo[d]='C'

    y=int(0)
    while y < 3 and prod_cupo[d]!=aProd[y]:
        y=y+1

    pesoneto_prod[0][y]=pesoneto_prod[0][y]+Peso_Neto[d]

    pesoneto_prod[1][y]=(pesoneto_prod[0][y])/cant_prod[y]

    if Peso_Neto[d]>mayores[y]:
        mayores[y]=Peso_Neto[d]
        patentemay[y]=patente_cupos[d]

    if Peso_Neto[d]<menores[y]:
        menores[y]=Peso_Neto[d]
        patentemen[y]=patente_cupos[d]


    print('\nCupo Nº:', d+1)
    print('Patente:', patente_cupos[d])
    print('Carga:', prod_cupo[d])
    print('Peso Neto en Toneladas:', Peso_Neto[d])

def reportes():

    if cupos !=0:
        print('\nLa cantidad total de cupos dados es: ', cupos)
        print('La cantidad de camiones recibidos es: ', camion_recib)
        print ('\n')
        for i in range(0,3):
            print('Para el producto:', aProd[i],',', 'se recibieron: ', cant_prod[i],'camiones.')
        print ('\n')
        for i in range(0,3):
            print('Para el producto:', aProd[i],',', 'hay un peso neto total de:', pesoneto_prod[0][i],'toneladas.')
        print ('\n')
        for i in range(0,3):
            print('Para el producto:', aProd[i],',', 'hay un peso neto promedio de:', pesoneto_prod[1][i],'toneladas por camión.')
        print ('\n')
        for i in range(0,3):
            print('Para el producto:', aProd[i],',', 'la patente del camión que mas descargo fue: ', patentemay[i],'y la que menos:',patentemen[i])
        print ('\n')

        for i in range(0,8):
            pesoneto_ord[i]=Peso_Neto[i]
            patente_ord[i]=patente_cupos[i]
            producto_ord[i]=prod_cupo[i]

        for i in range(0,7):
            for j in range(i+1,8):
                if pesoneto_ord[i]<pesoneto_ord[j]:

                    aux=pesoneto_ord[i]
                    pesoneto_ord[i]=pesoneto_ord[j]
                    pesoneto_ord[j]=aux

                    aux=patente_ord[i]
                    patente_ord[i]=patente_ord[j]
                    patente_ord[j]=aux

                    aux=producto_ord[i]
                    producto_ord[i]=producto_ord[j]
                    producto_ord[j]=aux

        print('Lista de peso neto en orden decreciente: \n')
        print('     Patente','   Producto','     Peso neto (T)')
        for i in range(0,8):
            print(i+1,'-',' ',patente_ord[i],'     ',producto_ord[i],'          ',pesoneto_ord[i])
        print('\n---------------------------------------------------------------------------------------------------------------------------------------------------------')

    else:
        print('\n\n---------------------------\n\nNo se registraron cupos.\n\n---------------------------')

contadores()

programa()