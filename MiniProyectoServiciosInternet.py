# Nombre del programa: Mini Proyecto 1
# Versión: Beta 1.1.1

# Librerias utilizada: pip install pandas- pip install openpyxl
# pip install tabulate

import datetime
from datetime import datetime, timedelta
from tabulate import tabulate
import pandas as pd



##pip install pandas

centro = '*'

paquetes = []
registros = {}
suscriptor = 1000
cancelaciones = {}
grantotal= {}
# Añadir un registro al diccionario
registro1 = {
    'codigo': 1,
    'nombre': 'Paquete 400',
    'costo': 35.00,
    'contenido': ['Internet 400 megas', '300 minutos de Telefonía Fija', '230 Canales de Cable'],
    'cajillas': 1,
    'paquete_adicional': False,
    'extensor': False,
    'cantidad_extensor': 0,
    'cantidad_paquete_adicional': 0,
    'adicionales': [],
    'app': False
}
paquetes.append(registro1)

registro2 = {
    'codigo': 2,
    'nombre': 'Paquete 750',
    'costo': 48.00,
    'contenido': ['Internet 750 megas', 'Telefonía Fija Ilimitada', '230 Canales de Cable'],
    'cajillas': 2,
    'paquete_adicional': False,
    'extensor': True,
    'cantidad_extensor': 1,
    'cantidad_paquete_adicional': 0,
    'adicionales': [],
    'app': False
}
paquetes.append(registro2)
registro3 = {
    'codigo': 3,
    'nombre': 'Paquete 1k',
    'costo': 60.00,
    'contenido': ['Internet 1000 megas', 'Telefonía Fija Ilimitada', '230 Canales de Cable'],
    'cajillas': 2,
    'paquete_adicional': True,
    'extensor': True,
    'cantidad_extensor': 1,
    'cantidad_paquete_adicional': 2,
    'adicionales': [1, 2],
    'app': False
}
paquetes.append(registro3)


def registro():
    codigo = 0
    nombre = ""
    costo = ""
    contenido = []
    cajillas = 0
    paquete_adicional = False
    extensor = False
    cantidad_extensor = 0
    cantidad_paquete_adicional = 0
    adicionales = []
    veri = False
    precio = 0.00
    dicProvisional = {}

    respuesta = 's'
    respuesta2 = 's'
    resp = 's'
    while respuesta.lower() == 's':

        respuesta = input(f"Desea agregar el Paquete # {len(paquetes) + 1} (s para si y n para no):")
        if respuesta.lower() != 's' and respuesta.lower() != 'n':
            while respuesta.lower() != 's' and respuesta.lower() != 'n':
                print("Valor incorrecto intente de nuevo")
                respuesta = input("Desea agregar otro Paquete (s para si y n para no): ")
        elif respuesta.lower() == 's':
            # print(len(paquetes))
            codigo = len(paquetes) + 1
            # print(codigo)
            nombre = input("Favor ingresar nombre del paquete")
            while veri == False:
                try:
                    costo = float(input("Favor ingresar el costo del paquete"))
                    veri = True
                except:
                    print("favor ingresar el valor correcto")
                    veri = False
            veri = False
            contenidos_paquetes_a = input("Ingrese la cantidad de megas: ")
            internet = "Internet " + contenidos_paquetes_a + " megas"
            contenido.append(internet)
            contenidos_paquetes_a = input("Ingrese los minutos de telefonia: ")
            minutos = contenidos_paquetes_a + " minutos de Telefonia Fija"
            contenido.append(minutos)
            contenidos_paquetes_a = input("Ingrese la cantidad de canales: ")
            canales = contenidos_paquetes_a + " Canales de Cable"
            contenido.append(canales)
            while veri == False:
                try:
                    cajilla = int(input("Ingrese la cantidad de cajilla: "))
                    veri = True
                except:
                    print("favor ingresar el valor correcto")
                    veri = False
                if cajilla < 0:
                    print("Favor ingresar un valos mayor igual a 0")

            veri = False

            while resp.lower() == 's':

                resp = input("Desea agregar plataformas de streaming  (s para si y n para no): ")
                if resp.lower() != 's' and resp.lower() != 'n':
                    while resp.lower() != 's' and resp.lower() != 'n':
                        print("Valor incorrecto intente de nuevo")
                        resp = input("Desea agregar plataformas de streaming  (s para si y n para no): ")
                elif resp.lower() == 's':
                    paquete_adicional = True
                    #print(len(adicionales))
                    if len(adicionales) == 4:
                        print("No puede ingresar mas plataformas")
                        # print("respuesta2")
                        resp = 'n'
                    else:
                        if resp.lower() == 's':
                            print("1.Netflix")
                            print("2.Universal Plus")
                            print("3.Paramount+")
                            print("4.HBO Max")
                            plataforma = int(input("Ingrese la plataforma: "))
                            if plataforma in adicionales:
                                print("No puede ingresar una misma plataforma")
                            else:
                                print("Plataforma ingresada")
                                adicionales.append(plataforma)
                                # print(dicProvicional["adicionales"])
                        elif resp.lower() == 'n':
                            if len(adicionales) == 0:
                                paquete_adicional = False

            respuesta2 = input("Desea agregar extensor  (s para si y n para no): ")
            if respuesta2.lower() != 's' and respuesta2.lower() != 'n':
                while respuesta2.lower() != 's' and respuesta2.lower() != 'n':
                    print("Valor incorrecto intente de nuevo")
                    respuesta2 = input("Desea agregar extensor   (s para si y n para no): ")

            elif respuesta2.lower() == 's':
                extensor = True
                while veri == False:
                    try:
                        cantidad_extensor = int(input("Favor detallar la cantidad de extensores a agregar"))
                        veri = True
                    except:
                        print("favor ingresar el valor correcto")
                        veri = False
                    if cantidad_extensor <= 0:
                        print("Favor ingresar un valos mayor a 0")
                veri = False
            elif respuesta2.lower() == 'n':
                extensor = False
                cantidad_extensor = 0

            cantidad_paquete_adicional = len(adicionales)
            cajillas = cajilla
            # Ingresando todos los datos del nuevo paquete
            registroAdicionado = {
                'codigo': codigo,
                'nombre': nombre,
                'costo': costo,
                'contenido': contenido,
                'cajillas': cajillas,
                'paquete_adicional': paquete_adicional,
                'extensor': extensor,
                'cantidad_extensor': cantidad_extensor,
                'cantidad_paquete_adicional': cantidad_paquete_adicional,
                'adicionales': adicionales,
                'app': False
            }
            paquetes.append(registroAdicionado)

            # contenido = []
        elif respuesta.lower() == 'n':
            for regi in paquetes:
                print(regi)
            break

    """
    try:
	# Codigo a ejecutar
	# Pero podria haber errores en este bloque

except <tipo de error>:
	# Haz esto para manejar la excepcion
	# El bloque except se ejecutara si el bloque try lanza un error

else:
	# Esto se ejecutara si el bloque try se ejecuta sin errores

finally:
	# Este bloque se ejecutara siempre"""


def impresion_paquetes():
    tabla = []
    for paquete in paquetes:
        fila = [
            paquete['codigo'],
            paquete['nombre'],
            paquete['costo'],
            ", ".join(paquete['contenido']),
            paquete['cajillas'],
            paquete['paquete_adicional'],
            paquete['extensor'],
            paquete['cantidad_extensor'],
            paquete['cantidad_paquete_adicional'],
            ", ".join(str(adicional) for adicional in paquete['adicionales'])
        ]
        tabla.append(fila)

    headers = ["Código", "Nombre", "Costo", "Contenido", "Cajillas", "Paquete Adicional", "Extensor",
               "Cantidad Extensor", "Cantidad Paquete Adicional", "Adicionales"]
    print(tabulate(tabla, headers, tablefmt="grid"))


def registroVentas(ultimo_suscriptor=None):
    global suscriptor
    respuesta = "s"
    respuesta2 = "s"
    respuesta3 = "s"
    respuesta4 = "s"
    respuesta5 = "s"
    respuesta6 = "s"
    respuesta7 = "s"
    x = 0
    cantidadapp = 0.00
    impuestoInstalacion = 0.00
    dicProvisional = {}
    plataforma = 0
    cantidadCajillas = 0
    extensorPosterior = 0
    print(centro.center(70, '*'))
    print("Registro de paquetes".center(70, '-'))
    print(centro.center(70, '*'))
    impresion_paquetes()

    '''
    { 122323: {}     }
    '''

    while True:
        try:
            print("1. Registro de paquete")
            print("2. Regresar")
            opcion = int(input("Ingrese una opción (1 o 2): "))
            break
        except ValueError:
            print("Formato de fecha incorrecto.")

    match opcion:
        case 1:
            '''if suscriptor == 1000:
                print("wakala arriba",suscriptor)
            elif suscriptor > 1000:
                print("Ahi va la vaina de arriba")'''
            codigoPaquete = int(input("Ingrese el codigo del paquete: "))
            dicProvisional = paquetes[codigoPaquete - 1]
            ##print(dicProvisional)
            while respuesta.lower() == 's':
                respuesta = input("Desea agregar cajilla adicional  (s para si y n para no): ")
                if respuesta.lower() != 's' and respuesta.lower() != 'n':
                    while respuesta.lower() != 's' and respuesta.lower() != 'n':
                        print("Valor incorrecto intente de nuevo")
                        respuesta = input("Desea agregar una cajilla adicional  (s para si y n para no): ")
                elif respuesta.lower() == 's':
                    cantidadCajillas = int(input("Ingrese la cantidad de cajillas que desea agregar: "))
                    suma_cajilla = dicProvisional.get("cajillas") + cantidadCajillas
                    dicProvisional["cajillas"] = suma_cajilla
                    break
                else:
                    break

                print("Cantidad de cajillas adicionales " + dicProvisional.get("cajillas"))

            cantidadAnterior = len(dicProvisional.get('adicionales'))

            while respuesta2.lower() == 's':
                respuesta2 = input("Desea agregar plataformas de streaming  (s para si y n para no): ")
                if respuesta2.lower() != 's' and respuesta2.lower() != 'n':
                    while respuesta2.lower() != 's' and respuesta2.lower() != 'n':
                        print("Valor incorrecto intente de nuevo")
                        respuesta2 = input("Desea agregar plataformas de streaming  (s para si y n para no): ")
                if len(dicProvisional.get("adicionales")) == 4:
                    print("No puede ingresar mas plataformas")
                    respuesta2 = "n"

                else:
                    plataformas = {
                        1: "Netflix",
                        2: "Universal Plus",
                        3: "Paramount+",
                        4: "HBO Max"
                    }

                    if respuesta2.lower() == 's':
                        print("1.Netflix")
                        print("2.Universal Plus")
                        print("3.Paramount+")
                        print("4.HBO Max")
                        plataforma = int(input("Ingrese el número de la plataforma: "))

                        if plataforma in dicProvisional.get("adicionales"):
                            print("No puede ingresar una misma plataforma o una ya existente en el paquete")
                        elif plataforma in plataformas:
                            plataforma = plataformas[plataforma]

                            if plataforma in dicProvisional.get("adicionales"):
                                print("No puede ingresar una misma plataforma o una ya existente en el paquete")
                            else:
                                print("Plataforma ingresada:", plataforma)
                                dicProvisional["paquete_adicional"] = True
                                dicProvisional.get("adicionales").append(plataforma)
                        else:
                            print("Número de plataforma inválido")

                    elif respuesta2.lower() == 'n':
                        break

            cantidadposterior = len(dicProvisional.get('adicionales')) - cantidadAnterior

            dicProvisional["cantidad_paquete_adicional"] = cantidadposterior
            extensorAnterior = dicProvisional.get('cantidad_extensor')
            while respuesta3.lower() == 's':
                respuesta3 = input("Desea agregar extensores  (s para si y n para no): ")
                if respuesta3.lower() != 's' and respuesta3.lower() != 'n':
                    while respuesta3.lower() != 's' and respuesta3.lower() != 'n':
                        print("Valor incorrecto intente de nuevo")
                        respuesta3 = input("Desea agregar extensores  (s para si y n para no): ")
                elif respuesta3.lower() == 's':
                    cantidadextensores = int(input("Ingrese la cantidad extensores: "))
                    dicProvisional["extensor"] = True
                    suma_extensores = dicProvisional.get("cantidad_extensor") + cantidadextensores
                    dicProvisional["cantidad_extensor"] = suma_extensores

                    break
                else:
                    break

            extensorPosterior = dicProvisional.get('cantidad_extensor') - extensorAnterior

            while respuesta5.lower() == 's':
                respuesta5 = input("Desea utilizar el la aplicacion en el movil  (s para si y n para no): ")
                if respuesta5.lower() != 's' and respuesta5.lower() != 'n':
                    while respuesta5.lower() != 's' and respuesta5.lower() != 'n':
                        print("Valor incorrecto intente de nuevo")
                        respuesta5 = input("Desea utilizar el la aplicacion en el movil")
                elif respuesta5.lower() == 's':
                    dicProvisional['app'] = True
                    break
                else:
                    break

            while True:
                try:
                    fecha_str = input("Ingrese la fecha de inicio en el formato dd/mm/aaaa: ")
                    fecha1 = datetime.strptime(fecha_str, "%d/%m/%Y")
                    print("Fecha registrada correctamente ingresada:", fecha1)
                    dicProvisional['fechaInicial'] = fecha1
                    break

                except ValueError:
                    print("Formato de fecha incorrecto.")

            if dicProvisional.get('app') == True:
                cantidadapp = 5.00

            dia_instalacion = fecha1 + timedelta(days=1)

            # ¿EL DIA DE LA INSTALACION ES EL DIA DEL REGISTRO?

            while respuesta6.lower() == 's':
                respuesta6 = input(
                    F"Su cita de instalacion esta programa para el dia {dia_instalacion} ¿se encontrará ese dia en casa?(s para si y n para no): ")
                if respuesta6.lower() != 's' and respuesta6.lower() != 'n':
                    while respuesta6.lower() != 's' and respuesta6.lower() != 'n':
                        print("Valor incorrecto intente de nuevo")
                        respuesta6 = input(
                            F"Su cita de instalacion esta programa para el dia {dia_instalacion} ¿se encontrará ese dia en casa?(s para si y n para no): ")
                elif respuesta6.lower() == 'n':
                    print("Debe pagar 30.00 adicional en la instalacion")
                    impuestoInstalacion = 30.00
                    break
                else:
                    break

            dicProvisional['dia_instalacion'] = dia_instalacion

            dicProvisional['preciopago'] = dicProvisional.get('costo') + (cantidadCajillas * 5) + (
                    dicProvisional.get('cantidad_paquete_adicional') * 5) + (
                                                   extensorPosterior * 3.50) + cantidadapp + impuestoInstalacion

            # cantidad_paquete_adicional
            print(f"Su código único de suscriptor es {suscriptor}")
            registros[suscriptor] = dicProvisional
            #print(registros)
            suscriptor = suscriptor + 1
            '''if suscriptor == 1000:
                print("wakala",suscriptor)
            elif suscriptor > 1000:
                print("Ahi va la vaina")'''
            respuesta4 = input("Desea seguir registrando ventas (s para si y n para no) ")
            if respuesta4.lower() != 's' and respuesta4.lower() != 'n':

                while respuesta4.lower() != 's' and respuesta4.lower() != 'n':
                    print("Valor incorrecto intente de nuevo")
                    respuesta4 = input("Desea seguir registrando ventas (s para si y n para no) ")
            elif respuesta4.lower() == 's':
                registroVentas()

def cancelar_servicio():
    '''print(registros)
    suscriptor_usuario = int(input("Ingrese el número de suscriptor: "))
    while True:
        try:
            fecha_str = input("Ingrese la fecha de cancelación en el formato dd/mm/aaaa: ")
            fecha_cancelacion = datetime.strptime(fecha_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de fecha incorrecto.")
    if suscriptor_usuario in registros:
        fecha_registro = registros[suscriptor_usuario]['dia_instalacion']
        print("FC",fecha_cancelacion)
        if fecha_cancelacion >= fecha_registro:
            registros[suscriptor_usuario]['fechaCancelacion'] = fecha_cancelacion
            print(f"El servicio del suscriptor {suscriptor_usuario} ha sido cancelado correctamente.")
            dias_cancelacion = (fecha_cancelacion - fecha_registro).days
            print(f"Los dias que mantuvo el servicio: {dias_cancelacion}")
            print('wiwi',dias_cancelacion)
            # puede ser movido ser movido 452 en caso de necesitar mas datos.
            #Lo movi a la 447

            if dias_cancelacion <= 15:
                print(
                    f"La cantidad de dias que tuvo el servicio fue {dias_cancelacion} dias. no se le cobrará cargo adicional ")
            elif dias_cancelacion > 15:
                # Sumar la cantidad de días
                fecha_nueva = fecha_cancelacion + timedelta(days=dias_cancelacion)
                # Calcular la diferencia en meses
                meses = (fecha_nueva.year - fecha_cancelacion.year) * 12 + fecha_nueva.days - fecha_cancelacion.days
                print("Aproximadamente", meses, "meses")

                # ESTA OPERACION ES CORRECTA?

                cantidadImpuesto = ((18 - meses) * registros[suscriptor_usuario]['preciopago']) * 0.25
                print(f"Cargo adicional de {cantidadImpuesto}")
                cantidad_p = ((18 - meses) * registros[suscriptor_usuario]['preciopago']) + cantidadImpuesto
                print(f"Total a pagar {cantidad_p}")

                print(f"Tiene que pagar un total de {cantidad_p} como impuesto de cancelación")

            cancelaciones[suscriptor_usuario] = registros[suscriptor_usuario]
            del registros[suscriptor_usuario]
        else:
            print("La fecha de cancelación debe ser posterior a la fecha de registro.")
    else:
        print("El número de suscriptor no se encuentra registrado.")

    # if dias_cancelacion

'''


def cancelar_servicio():
    print(registros)
    suscriptor_usuario = int(input("Ingrese el número de suscriptor: "))
    while True:
        try:
            fecha_str = input("Ingrese la fecha de cancelación en el formato dd/mm/aaaa: ")
            fecha_cancelacion = datetime.strptime(fecha_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato de fecha incorrecto.")

    if suscriptor_usuario in registros:
        fecha_registro = registros[suscriptor_usuario]['dia_instalacion']
        print("FC", fecha_cancelacion)

        if fecha_cancelacion >= fecha_registro:
            registros[suscriptor_usuario]['fechaCancelacion'] = fecha_cancelacion
            print(f"El servicio del suscriptor {suscriptor_usuario} ha sido cancelado correctamente.")
            dias_cancelacion = (fecha_cancelacion - fecha_registro).days
            print(f"Los días que mantuvo el servicio: {dias_cancelacion}")

            if dias_cancelacion <= 15:
                print(
                    f"La cantidad de días que tuvo el servicio fue {dias_cancelacion} días. No se le cobrará cargo adicional.")
            elif dias_cancelacion > 15:
                fecha_nueva = fecha_cancelacion + timedelta(days=dias_cancelacion)
                meses = (fecha_nueva.year - fecha_cancelacion.year) * 12 + fecha_nueva.month - fecha_cancelacion.month
                print("Aproximadamente", meses, "meses")

                cantidadImpuesto = ((18 - meses) * registros[suscriptor_usuario]['preciopago']) * 0.25
                print(f"Cargo adicional de {cantidadImpuesto}")
                cantidad_p = ((18 - meses) * registros[suscriptor_usuario]['preciopago']) + cantidadImpuesto
                print(f"Total a pagar {cantidad_p}")

                print(f"Tiene que pagar un total de {cantidad_p} como impuesto de cancelación.")

            cancelaciones[suscriptor_usuario] = registros[suscriptor_usuario]
            del registros[suscriptor_usuario]
        else:
            print("La fecha de cancelación debe ser posterior a la fecha de registro.")
    else:
        print("El número de suscriptor no se encuentra registrado.")
def listadoPaquetes():
    print("Listado Paquetes")

    # NOTA PARA LOS PROGRAMADORES, ESTA ES LA FORMA BASICA DE EXPULSAR UN DICCIONARIO DENTRO DE OTRO DICCIONARIO CON
    # LA CLAVE DEL MISMO

    expulsion = [{'suscriptor': key, **value} for key, value in registros.items()]
    dataframe = pd.DataFrame(expulsion)
    dataframe.to_excel('vendidos.xlsx', index=False)
    '''
    Listado basico de una lista
    df = pd.DataFrame(paquetes)
    df.to_excel('paquetes.xlsx', index=False)
    listado basico de una diccionario

        expulsion = [{'suscriptor': key, **value} for key, value in registros.items()]
        dataframe = pd.DataFrame(expulsion)
        # Guardar el DataFrame en un archivo de Excel
        df.to_excel('vendidos.xlsx', index=False)

    '''


def listaCancelaciones():

    print("Lista de cancelaciones realizadas")
    expulsion = [{'suscriptor': key, **value} for key, value in cancelaciones.items()]
    dataframe = pd.DataFrame(expulsion)
    dataframe.to_excel('cancelados.xlsx', index=False)


def ventas():
    print("Total de ventas")
    cantVent = len(registros)
    acumTotal = 0
    for key, value in registros.items():
        acumTotal = acumTotal + value.get('preciopago')
    grantotal['cantidadventas'] = cantVent
    grantotal['totalventas'] = acumTotal
    #print(grantotal)
    dataframe = pd.DataFrame([grantotal])
    dataframe.to_excel('grantotal.xlsx', index=False)
    #print("acumTotal",acumTotal)
    #print("cantVent",cantVent)





while True:
    print("Bienvenido al mini proyecto 1".center(70, '-'))
    # print("\n")
    print(centro.center(70, '*'))
    print("Menú".center(70, '-'))
    print(centro.center(70, '*'))
    print("1. Registrar los paquetes")
    print("2. Registrar la venta de los paquetes")
    print("3. Registrar cancelaciones")
    print("4. Listar las ventas realizadas por paquete")
    print("5. Listar las cancelaciones realizadas")

    # El gran total incluye las instanaciones?

    print("6. Listar todas las ventas realizadas y el gran total")
    print("7. Salir")

    opcion = int(input("Ingrese una opción: "))
    print("\n")
    print(centro.center(70, '='))

    match opcion:
        case 1:
            registro()
        case 2:
            registroVentas(suscriptor)
        case 3:
            cancelar_servicio()

        case 4:
            listadoPaquetes()

        case 5:
            listaCancelaciones()
        case 6:
            ventas()
        case 7:
            #print("Gracias por utilizar las opciones, cerro:",datetime.datetime.now())
            break
        case _:
            print("Opción inválida")
