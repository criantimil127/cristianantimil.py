import random 
import csv

#lista de los empleados
trabajadores = [" Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def asignar_sueldos_aleatorios():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos


def clasificar_sueldos(sueldos):
    menor_800k = []
    entre_800k_2000k = []
    mayor_2000k = []
    
    for i, sueldo in enumerate(sueldos):
        if sueldo < 800000:
            menor_800k.append((trabajadores[i], sueldo ))
        elif 800000 <= sueldo <= 20000000:
            entre_800k_2000k.append((trabajadores[i], sueldo ))
        else:
            mayor_2000k.append((trabajadores[i], sueldo ))
            
    print("Sueldos menores a $800,000")
    print("TOTAL:", len(menor_800k))
    for empleado, sueldo in menor_800k:
        print(f"{empleado} ${sueldo}")
        
        
        
    print("\nSueldos mayores a 2,000,000 ")
    print("TOTAL:", len(mayor_2000k))
    for empleado, sueldo in mayor_2000k:
        print(f"{empleado} ${sueldo}")
        
    total_sueldos = sum(sueldos)
    print("\nTOTAL SUELDOS: $", total_sueldos)



def ver_estadisticas(sueldos):
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    
    producto_sueldos = 1
    for sueldo in sueldos:
        producto_sueldos *= sueldo
    media_geometrica = producto_sueldos ** (1 / len(sueldos))
    
    print(f"Sueldo más alto: ${sueldo_maximo}")
    print(f"Sueldo más bajo: ${sueldo_minimo}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    
sueldos = [500000,  700000,  1100000, 800000, 2100000]
ver_estadisticas(sueldos)




def reporte_sueldos(sueldos):
    print("Nombre empleado            | Sueldo Base   | Descuento Salud                | Sueldo Líquido ")
    print("-" * 80)
    for i, sueldo in enumerate(sueldos):
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo *0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        print(f"{trabajadores[i]}     | ${sueldo}     |     ${descuento_salud:.2f}     |     ${sueldo_liquido:.2f}")
        
    with open('reporte_sueldos.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Nombre empleado', 'Sueldo base', 'Descuento salud', 'Descuento AFP', 'Sueldo líquido'])
        for i, sueldo in enumerate(sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp 
            csv_writer.writerow([trabajadores[i], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            
            
            
if __name__ == "__main__":
    sueldos = []
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1.- Asignar sueldos aleatorios")
        print("2.- Clasificar sueldos ")
        print("3.- Ver estadísticas ")
        print("4.- Reporte de sueldos ")
        print("5.- Salir del programa ")
        
        opcion = input("Seleccione una opcion: ")
        
        
        
        if opcion == '1':
            sueldos = asignar_sueldos_aleatorios()
            print("Sueldos asignados de manera aleatoria.")
        elif opcion == '2':
            if not sueldos:
                print("Primero asigne los sueldos aleatorios ")
            else:
                clasificar_sueldos(sueldos)
        elif opcion == '3':
            if not sueldos:
                print("Primero asigne los sueldos aleatoriamente")
            else:
                ver_estadisticas(sueldos)
        elif opcion == '4':
            if not sueldos:
                print("Primero asigne los sueldos aleatoriamente")
            else:
                reporte_sueldos(sueldos)
                print("Reporte de sueldos generado en reporte_sueldos.csv")
        elif opcion == '5':
            print("¡Hasta la próxima <3 !")
            break
        else:
            print("Opcion incorrecta. Seleccione una de las opciones mostradas en el menú.")





    