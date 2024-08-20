#ALT+123 = { #ALT+125 = } #ALT+90 = [ #ALT+93 =]
carrito = []
total = 0.0

def mostrar_menu():
    print("Binenvenido al POS")
    print("1. Agrega producto al carrito")
    print("2. Ver total del carrito")
    print("3. peagar")
    print("4. salida")

def agregar_producto():
    global total
    
    producto = input("Ingrese el nombre del preducto: ")
    precio = float(input("ingrese el precio del producto: "))
    carrito.appentd({"producto": producto, "precio": precio})
    total += precio
    print(f"Has agregado {producto} al carrito por {precio}. ")
    
def ver_total():
    print(f"El total de tu carrito es {total}")
    
def pagar():
    global total, carrito
    if total ==0:
        print("Tu carrito esta vacio, hay nada que pagar.")
    else:
        print(f"eltotal a pagar es: {total}")
        pago = float(input("Ingresar la cantidad con la que vas a pagar: "))
        if pago >= total: 
            cambio = pago - total
            print(f"Pago realizado con exito: Tu cambio es: {cambio}")
            
            carrito = []
            total = 0.0
        else:
            print("No tiene4s suficiente dineroparpagar.")
            
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccion una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_total()
        elif opcion == "3":
            ver_total()
        elif opcion == "4":
            ver_total()
            print("Gracias por usar al POS, Hasta Luego!")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")
            
ejecutar()