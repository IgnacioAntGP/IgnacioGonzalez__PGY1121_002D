# Bloque de funciones
import os, numpy as np, funcionesCasaFeliz as fc

# Bloque construcciones
op = 0
total_compra = 0
contador_clientes = 1
edificio = fc.crearDatosEdificio()
ventas = fc.crearMatrizVentas()

# Bloque principal


while op != 5:
    os.system("cls")
    print("***** Casa Feliz *****","======================", "1. Comprar departamento", "2. Mostrar departamentos disponibles", "3. Ver listado de compradores", "4. Mostrar ganancias totales", "5. Salir", sep="\n")
    op = fc.ingresarOp()

    if op == 1:
        res_continuar = 1
        while res_continuar == 1:

            print("")
            piso = fc.validarNumPiso()
            dpto = fc.validarTipoDpto()
            validar_compra = fc.buscarCompra(edificio, piso, dpto)

            if validar_compra == 1:

                total_compra += fc.comprarDpto(dpto)
                print(total_compra)
                print("TOTAL COMPRA:", total_compra, "UF")

                fc.validarCompraDptoA(ventas, dpto)
                fc.validarCompraDptoB(ventas, dpto)
                fc.validarCompraDptoC(ventas, dpto)
                fc.validarCompraDptoD(ventas, dpto)

                res_continuar = fc.continuarCompra()

        # ACUMULADORES        
        contador_clientes += 1
    
    if op == 2:
        fc.mostrarDptosDisponibles(edificio)
    

    #if op == 3:


    if op == 4:
        print(ventas)
        os.system("pause")


    if op == 5:
        fc.salirSistema(op)
