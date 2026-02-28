# Saldo inicial del usuario 
Saldo_inicial = 1000
# Preguntar Saldo al usuario 
cantidad = int(input("¿Cuántas operaciones deseas realizar? "))
# Mostar menu 
for i in range(cantidad):
    print(f"Operación {i + 1}:")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        print(f"Tu saldo es: {Saldo_inicial}")
    elif opcion == 2:
        retiro = int(input("¿Cuánto dinero deseas retirar? "))
        if retiro > Saldo_inicial:
            print("Saldo insuficiente.")
        elif retiro < 0:
            print("No puedes retirar una cantidad negativa.")
        else:
            Saldo_inicial -= retiro
            print(f"Has retirado {retiro}. Tu nuevo saldo es: {Saldo_inicial}")
    elif opcion == 3:
            opcion_deposito = int(input("¿Cuánto dinero deseas depositar? "))
            if opcion_deposito < 0: 
                print("No puedes depositar una cantidad negativa.")
            else:
                Saldo_inicial += opcion_deposito
                print(f"Has depositado {opcion_deposito}. Tu nuevo saldo es: {Saldo_inicial}")

if opcion < 1 or opcion > 3:
    print("Operación no válida. Por favor, selecciona una opción del 1 al 3.")
# Mostrar saldo final
print(f"Saldo final: {Saldo_inicial}")
# Fin del programa
print("Gracias por usar el cajero automático.")