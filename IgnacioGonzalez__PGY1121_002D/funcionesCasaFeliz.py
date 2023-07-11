import os, numpy as np

def ingresarOp():
    while True:
        try:
            op = int(input("Elija opción: "))
            if op not in [1,2,3,4,5]:
                print("ERROR. Debe ingresar un numero entre 1 y 5")
            else:
                break
        except ValueError:
            print("ERROR. Debe escribir un NUMERO ENTERO")
    return op

def validarNumEntero():
    while True:
        try:
            num = int(input("Ingrese el numero de pisos a ingresar al sistema: "))
            if num > 0:
                break
            else:
                print("ERROR. Debe ingresar un numero entre 1 y 40")
        except ValueError:
            print("ERROR. Debe ser un NUMERO ENTERO")
    os.system("pause")
    return num

def crearDatosEdificio():
    contador_piso = 1
    i = 0
    j = 0
    matriz = np.empty((7, 5), dtype=object)
    matriz [0,0] = ""
    matriz [0,1] = "A"
    matriz [0,2] = "B"
    matriz [0,3] = "C"
    matriz [0,4] = "D"
    
    for i in range(1, len(matriz), 1):
        for j in range(0, 5, 1):
            if j == 0:
                matriz [i,j] = contador_piso
                contador_piso += 1
            else:
                matriz [i,j] = ""
    return matriz

#BLOQUE OPCION 1: COMPRAR DEPARTAMENTO

def ingresarRut (matriz, columnas):
    for j in range(columnas):
        for i in range(1):
            while True:
                try:
                    rut = int(input("Ingrese el rut del cliente correspondiente: "))
                    if rut > 0:
                        rut = str(rut)
                        if (len(rut) >= 8):
                            break
                        else:
                            print("ERROR. RUT NO VALIDO")
                    else:
                        print("ERROR. Ingrese un numero entero positivo")
                except ValueError:
                    print("ERROR. Ingrese un numero entero")
            matriz[i,j] = rut
    return matriz

def validarNumPiso():
    while True:
        try:
            piso = int(input("Ingrese el numero del piso: "))
            if piso > 0 and piso < 40:
                break
            else:
                print("ERROR. Debe ingresar un numero entre 1 y 40")
        except ValueError:
            print("ERROR. Debe ser un NUMERO ENTERO")
    return piso

def validarTipoDpto():
    tipo_dpto = ""
    busqueda_dpto = ["A", "B", "C", "D"]
    while len(tipo_dpto) == 0:
        tipo_dpto = input("Ingrese el tipo de departamento: ")
        tipo_dpto = tipo_dpto.upper()
        if tipo_dpto not in busqueda_dpto:
            print("ERROR. Debe ingresar una letra entre A y D")
            tipo_dpto = ""
    return tipo_dpto

def buscarCompra (matriz, piso, tipo_dpto):
    validar_compra = 1
    print("")
    print("BUSCANDO PISO =", piso)
    print("BUSCANDO DPTO =", tipo_dpto)

    
    for i in range(1, len(matriz), 1):
        for j in range(0, 5, 1):
            if matriz [i,0] == piso:
                if matriz [0,j] == tipo_dpto:
                    if matriz [i,j] == "X":
                        validar_compra = 0
                        print("No está disponible")
                        os.system("pause")
                    elif matriz [i,j] == "":
                        print("Disponible, accediendo a compra...")
                        os.system("pause")
                        matriz[i,j] = "X"
    return validar_compra

def comprarDpto(tipo_dpto):
    compra_actual = 0

    if tipo_dpto == "A":
        compra_actual = 3800
        print("Compra del departamento tipo A:", compra_actual, "UF")
        os.system("pause")

    elif tipo_dpto == "B":
        compra_actual = 3000
        print("Compra del departamento tipo B:", compra_actual, "UF")
        os.system("pause")

    elif tipo_dpto == "C":
        compra_actual = 2800
        print("Compra del departamento tipo C:", compra_actual, "UF")
        os.system("pause")

    elif tipo_dpto == "D":
        compra_actual = 3500
        print("Compra del departamento tipo D:", compra_actual, "UF")
        os.system("pause")

    return compra_actual

def continuarCompra():
    res_continuar = 0
    continuar = ""
    while len(continuar) == 0:
        print("")
        continuar = input("¿Desea continuar con su compra? Escriba S/N: ")
        continuar = continuar.upper()
        print(continuar)
        if continuar == "S" or continuar == "N":

            if continuar == "S":
                res_continuar = 1
            elif continuar == "N":
                res_continuar == 0

            if res_continuar == 1:
                print("Prosiguiendo con la compra")
                os.system("pause")
            elif res_continuar == 0:
                print("Regresando a menú")
                os.system("pause")
        else:
            print('ERROR. Debe escribir "S" o "N"')
            continuar = ""
    
    return res_continuar

#BLOQUE OPCION 2: MOSTRAR DEPARTAMENTOS DISPONIBLES
def mostrarDptosDisponibles(edificio):
    os.system("cls")
    print(edificio)
    os.system("pause")

# BLOQUE OPCION 4: MOSTRAR GANANCIAS TOTALES
def crearMatrizVentas():
    matriz_venta = np.empty((6,3), dtype=object)
    matriz_venta [0,0] = "Tipo de Departamento"
    matriz_venta [0,1] = "Cantidad"
    matriz_venta [0,2] = "Total"

    matriz_venta [1,0] = "Tipo A 3.800 UF"
    matriz_venta [2,0] = "Tipo B 3.000 UF"
    matriz_venta [3,0] = "Tipo C 2.800 UF"
    matriz_venta [4,0] = "Tipo D 3.500 UF"
    matriz_venta [5,0] = "Total"
    
    return matriz_venta

def validarCompraDptoA(matriz_venta, tipo_dpto):
    contador_dptos_A = 0
    venta_dptos_A = 0
    total_compra_A = 0
    if tipo_dpto == "A":
        compra_actual = 3800
        venta_dptos_A += compra_actual
        total_compra_A += compra_actual
        contador_dptos_A += 1
    
    for i in range(1,6,1):
        for j in range(1,2,1):
            matriz_venta[i,j] = contador_dptos_A
    for i in range(1,6,1):
        for j in range(2,3,1):
            matriz_venta[i,j] = total_compra_A

    return matriz_venta

def validarCompraDptoB(matriz_venta, tipo_dpto):
    contador_dptos_B = 0
    venta_dptos_B = 0
    total_compra_B = 0
    if tipo_dpto == "B":
        compra_actual = 3000
        venta_dptos_B += compra_actual
        total_compra_B += compra_actual
        contador_dptos_B += 1
    
    for i in range(1,6,1):
        for j in range(1,1,1):
            matriz_venta[i,j] = contador_dptos_B
    for i in range(1,6,1):
        for j in range(2,2,1):
            matriz_venta[i,j] = total_compra_B

    return matriz_venta

def validarCompraDptoC(matriz_venta, tipo_dpto):
    contador_dptos_C = 0
    venta_dptos_C = 0
    total_compra_C = 0
    if tipo_dpto == "C":
        compra_actual = 3800
        venta_dptos_C += compra_actual
        total_compra_C += compra_actual
        contador_dptos_C += 1
    
    for i in range(1,6,1):
        for j in range(1,1,1):
            matriz_venta[i,j] = contador_dptos_C
    for i in range(1,6,1):
        for j in range(2,2,1):
            matriz_venta[i,j] = total_compra_C

    return matriz_venta

def validarCompraDptoD(matriz_venta, tipo_dpto):
    contador_dptos_D = 0
    venta_dptos_D = 0
    total_compra_D = 0
    if tipo_dpto == "D":
        compra_actual = 3800
        venta_dptos_D += compra_actual
        total_compra_D += compra_actual
        contador_dptos_D += 1
    
    for i in range(1,6,1):
        for j in range(1,1,1):
            matriz_venta[i,j] = contador_dptos_D
    for i in range(1,6,1):
        for j in range(2,2,1):
            matriz_venta[i,j] = total_compra_D
    return matriz_venta

def salirSistema(op):
    if op == 5:
        print("SALIENDO DEL SISTEMA")

