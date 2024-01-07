import os

def VerCo2(dependencias:list):
    
    rta = "S"
    while (rta == "S"):
        os.system("cls")
        buscar = str(input("INGRESE EL NOMBRE DE LA DEPENDENCIA A BUSCAR: "))
        dependenciaencontrada = False
        for i in dependencias:
            dependenciaencontrada= True
            if buscar.upper() == i[0].upper():
                print( f"\nEMISIONES DE CO2 DE LA DEPENDENCIA {i[0].upper()}")
                for item in i:
                    if item[0] == "ELECTRICIDAD":
                        print(f"LAS EMICIONES DE CO2 POR {item[0]}\n  TIENEN UN VALOR DE {item[1]} gCO2/kWh")                                                                                            
                for item in i:
                    if item[0] == "TRANSPORTE":
                        print(f"LAS EMICIONES DE CO2 POR {item[0]}\n  TIENEN UN VALOR DE {item[1]} gCO2/km")           
        if (dependenciaencontrada == False): 
            print("NO SE ENCONTRO LA DEPENDENCIA")
            
            
        rta = input("DESEA VER OTRA DEPENDENCIA S(si)/N(no)").upper()     
                    
def MayorCo2 (dependencias : list[str]):
    dependenciamayor =" "
    aux = 0
    transporte = 0
    electricidad = 0
    for dependencia in dependencias:
        dependen = dependencia[0]
        for n in dependencia[1][1]:
            electricidad = n
        for nt in dependencia[2][1]:
            transporte = nt
            
        mayor = electricidad + transporte
        if mayor > aux:
            aux = mayor
            dependenciamayor = dependen
           
    print(f"LA DEPENDENCIA CON MAS CONSUMO DE CO2 FUE: {dependenciamayor} ENTRE ELECTRICIDAD Y TRANSPORTE")
    os.system("pause")   
        
    
