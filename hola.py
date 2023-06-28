import os
os.system("cls")

listaCodigo = []
listaNom = []
listaCategoria = []
listaPrecio = []
listaStock = [] 


menu = """"
1. Registrar datos 
2. Buscar producto
3. Listar producto
4. Salir
"""

while True:
    try:
        opc = int(input(menu))
        if opc == 4: 
            nombre = input("Cual es tu nombre: ")
            apellido = input("cual es tu apellido: ")
            print(f"Adios {nombre} {apellido}")
            break
        elif opc == 1:
            while True:
                try:
                    codigo = (input("codigo: "))
                    if len(codigo) == 6:
                        listaCodigo.append(codigo)
                        break
                    else:
                        print("Error de codigo")                
                except:    
                    print("ocurrio una excepcion")
            while True:
                try:
                    nombre = input("nombre: ")
                    if len(nombre) > 2:
                        listaNom.append(nombre)    
                        break
                    else:
                        print("Error de nombre")
                except:
                    print("ocurrio una excepcion")            
            while True:
                try:
                    categoria = input("categoria: ")
                    if len(categoria) > 0  :
                        listaCategoria.append(categoria)
                        break
                    else:
                        print("Error de categoria")
                except:
                    print("ocurrio una excepcion") 
            while True:           
                try:
                    precio = int(input("precio: "))
                    if precio > 0:
                        listaPrecio.append(precio)
                        break
                    else:
                        print("Error de precio")
                except:
                    print("Ocurrio una excepcion")    
            while True:
                try:
                    stock = int(input("stock: "))
                    if stock > 0:
                        listaStock.append(stock)
                        break
                    else:
                        print("Error de stock")
                except:
                    print("Ocurrio una excepcion")          
        elif opc == 2:
                    print("Buscar un producto (codigo)")
                    buscar = input("Ingrese Codigo del producto que quiere buscar: ")
                    for i in range (len(listaCodigo)): 
                        if buscar.lower() == listaCodigo[i].lower(): 
                            print("codigo | nombre | categoria | precio | stock ")
                            print(f"{listaCodigo[i]:6d} | {listaNom[i]:10s} | {listaCategoria[i]:6s} | {listaPrecio[i]:4d} | {listaStock[i]:3d}")
        elif opc == 3:
             for i in range  (len(listaCodigo)):
                            print("codigo | nombre | categoria | precio | stock ")
                            print(f" {listaCodigo[i]:6d} | {listaNom[i]:10s} | {listaCategoria[i]:6s} | {listaPrecio[i]:4d} | {listaStock[i]:3d}")

    except:
        print("ocurrio una excepcion")    