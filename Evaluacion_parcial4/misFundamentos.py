def menu():
    print("MENU PRINCIPAL")
    print("*" * 20)
    print("""
    1.- Comprar entrada.
    2.- Consultar comprador.
    3.- Cancelar compra.
    4.- Salir."""    )
    op = input("ingrese su opcion")
    return op

def validar_codigo_confirmacion(codigoConf):
    tieneMayusculas = any(c.isupper() for c in codigoConf)
    tieneNro = any(c.isdigit() for c in codigoConf)
    sinEspacios = " " not in codigoConf
    return len(codigoConf) >= 6 and tieneMayusculas and tieneNro and sinEspacios

def compra_entrada(diccUsuarios, entradasG, entradasV):
    if entradasG == 0 and entradasV == 0:
        print("no hay entradas de ninguna de las categorias")
        return diccUsuarios, entradasG, entradasV
    while True:
        nombre =input("ingrese el nombre de comprador:")
        if nombre.replace(" ","").isalpha():
            break
        else:
            print("el nombre solo debe contener letras. intenta de nuevo")
    while True:
        tipo = input("ingrese el tipo de entrada: [ G: entrada general / V: entrada VIP]: ").upper()
        if tipo == "G" and entradasG > 0:
            break
        elif tipo == "V" and entradasV > 0:
            break
        else:
            print("tipo invalido. debe o  ya no hay entradas disponibles")        
    
    while True:
        codigoConf = input("ingrese el codigo de confirmacion")
        if validar_codigo_confirmacion(codigoConf):
            break
        else:
            print("Codigo no valido , debe contener un largo de 6 caracteres, debe tener al menos 1 letra mayuscula, al menos 1 numero y no puede tener espacion en blanco.")
    diccUsuarios[codigoConf] = [nombre, tipo, codigoConf]
    if tipo == "G":
        entradasG -= 1
    else:
        entradasV -= 1
    print(f"compra registrada con exito para {nombre}")
    return diccUsuarios, entradasG, entradasV

def cancelar_compra(diccUsuarios, entradasG, entradasV):
    comprador = input("ingrese el comprador a cancelar: ").strip()
    if comprador in diccUsuarios:
        tipo = diccUsuarios[comprador][1]
        del diccUsuarios [comprador]
        if tipo == "G":
            entradasG +=1
        else:
            entradasV +=1
        print(" entrada cancelada con exito")
    else:
        print("no existe ninguna compra con ese codigo")
    return diccUsuarios, entradasG, entradasV

def mostrar_comprador(codigoConf, nombre, tipo):
    print(f"el nombre del comprador: {nombre} con el tipo de entrada {tipo} esta confirmado con el codigo {codigoConf} ")

