import misFundamentos as fc

opcion =""
comprador ={}
entrada_general = 100
entrada_vip = 100
tipo_entrada = {}
codigo_confi ={}



while opcion != "4":
    opcion = fc.menu()
    if opcion == "4":
        print("sistema de compra finalizado")
    elif opcion == "1":
        print("Comprar nueva entrada.")
        comprador, entrada_general, entrada_vip = fc.compra_entrada(comprador, entrada_general, entrada_vip)
        print(comprador)
    elif opcion == "2":
        print("consultar comprador")
        fc.mostrar_comprador (comprador, tipo_entrada, codigo_confi)
    elif opcion == "3":
        print(" ingrese la compra a eliminar")
        comprador, tipo_entrada, codigo_confi = fc.mostrar_comprador (comprador, tipo_entrada, codigo_confi)
        print(comprador)
    else:
        print("error, la opcion no existe")
