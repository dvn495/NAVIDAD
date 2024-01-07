import os
import anualmensualint2 as tiemp

def registrarconsumo(buscar:str, dependencias : list[str]) :
    is_dependencia = False
    factoremisionelec = 100
    factoremisiontransporte = 7.53
    isActive = True
   
    while isActive:
        for dependencia in dependencias:
            if buscar.upper() == dependencia[0].upper():
                
                consumoelect = 0.0
                cosgasolina = 0.0
                    
                
                
                is_dependencia = True
                
                
                rta = "S"

                while rta == "S":
                    
                    os.system("cls")
                    print("QUE TIPO DE CONSUMO DESEA REGISTRAR")
                    print("   1. CONSUMO DE ELECTRICIDAD\n   2. CONSUMO DE TRANSPORTE\n   3. SALIR")

                    try:
                        claseconsumo = int(input(":) "))
                        os.system("cls")
                    except ValueError:
                        print("ERROR EN EL VALOR SUMINISTRADO")
                        os.system("cls")
                    
                    if claseconsumo == 1:
                        os.system("cls")
                        print("CONSUMO ELECTRICIDAD")

                        try:    
                            seleccion = int(input("DESEA DAR:\n SU CONSUMO TOTAL (1) \n POR DISPOSITIVO  (2)\n:) "))
                        except ValueError:
                            print("ERROR EN EL VALOR SUMINISTRADO")
                            os.system("cls")

                        if seleccion == 1:
                            os.system("cls")
                            print ("CONSUMO TOTAL")
                            try:
                                
                                select = int(input("  EL CONSUMO DE SU FACTURA ES MENSUAL(1)  \n  OTRO INTERVALO DE TIEMPO(2): \n:) "))
                            except ValueError:
                                print("ERROR EN EL VALOR SUMINISTRADO")
                                os.system("cls")

                            if select == 1:
                                

                                try:
                                    os.system("cls")
                                    print("Emiciones CO2(ELECTRICIDAD) = CONSUMO ELECTRICIDAD X FACTOR DE EMISION ELECTRICIDAD\n ")
                                    consum = float(input("DIGITE EL VALOR DE SU CONSUMO MENSUAL: "))
                                    consumo= (consum * factoremisionelec)
                                    
                                    consumoelect = consumo + consumoelect
                                    celectric = consumoelect
                                    print(f"\nSU FACTOR DE CONSUMO DE CO2 ES DE: {consumo} gCO2/kWh")
                                    os.system("pause")
                                    
                                                                 
                                except ValueError:
                                    print("Error: Ingrese un valor numérico válido.")

                            elif select == 2:
                                os.system("cls")

                                consum = tiemp.consumobimestral()

                                if consum > 0:
                                    consumo = consum * factoremisionelec
                                    print(f"SU CONSUMO EN ESTE PERIODO DE TIEMPO FUE DE {consumo} kWh\n")
                                    
                                    consumoelect = consumo + consumoelect
                                    celectric = consumoelect
                    

                                    print(f"\nSU FACTOR DE CONSUMO DE CO2 ES DE: {consumo} gCO2/kWh")
                                    os.system("pause")
                                    
                                else:
                                    print("NO SE ENCONTRÓ EL PERIODO DE TIEMPO")
                                    os.system("pause")
                                    
                        elif seleccion == 2:                            
                            dispositivos = []
                            isActive = True
                            
                            while (isActive):
                                
                                os.system("cls")
                                print ("CONSUMO POR DIPOSITIVO\n  Consumo de disposivo = Potencia del dispositivo en W x Tiempo de uso en horas/1000\n ")
                                
                                try:
                                    potencia = float(input("DIGITE LA POTENCIA DEL DISPOSITIVO: "))
                                    tiempo = float(input("DIGITE EL NUMERO DE HORAS EN MINUTOS: "))
                                    tiempo = tiempo/60
                                except ValueError:
                                    print("ERROR EN EL VALOR SUMINISTRADO")
                                    os.system("pause")
                                    
                                consumodispositivo =potencia * tiempo / 1000
                                dispositivos.append(consumodispositivo)
                                
                                rta = input("¿DESEA REGISTRAR OTRO DISPOSITIVO? S(si)/N(no): ").upper()
                                if rta != "S":
                                    isActive = False
                                                                                            
                            consum = sum(dispositivos)
                            os.system("cls")
                            print("Emiciones CO2(ELECTRICIDAD) = CONSUMO ELECTRICIDAD X FACTOR DE EMISION ELECTRICIDAD\n ")
                            consumo = consum * factoremisionelec
                            consumoelect = consumo + consumoelect
                            celectric = consumoelect
                            print(f"\nSU FACTOR DE CONSUMO DE CO2 ES DE: {consumo} gCO2/kWh")
                            os.system("pause")
                           
                        
                        coselectricidad= ["ELECTRICIDAD",[celectric]]
                        dependencia[1] = coselectricidad
                        for n in dependencia[1][1]:
                            n = consumoelect
                        
                        
                        
                        

                           
                    

                    elif claseconsumo == 2  :
                        os.system("cls")
                        print ("CONSUMO TOTAL")
                        try:
                            select = int(input("  EL CONSUMO DE SU FACTURA ES MENSUAL(1) \n  OTRO INTERVALO DE TIEMPO(2): \n:) "))
                        except ValueError:
                            print("NO SE RECONOCE EL DATO INGRESADO")

                        if select == 1:

                                try:
                                    os.system("cls")
                                    print("\nEmiciones CO2(TRANSPORTE) = KILOMETROS RECORRIDOS X FACTOR DE EMISION TRANSPORTE\n ")
                                    consum = float(input("\nDIGITE LOS KILOMETROS RECORRIDOS: "))
                                    consumo = consum * factoremisiontransporte
                                    cosgasolina = consumo + cosgasolina
                                    ctranporte = cosgasolina                                                                        

                                    print(f"\nSU FACTOR DE CONSUMO DE CO2 ES DE: {consumo} gCO2/km")
                                    os.system("pause")
                                                                                                                                         
                                except ValueError:
                                    print("Error: Ingrese un valor numérico válido.")
                                    

                        elif select == 2:

                                consum = tiemp.consumobimestral()

                                if consum > 0:
                                    consumo = consum * factoremisiontransporte
                                    cosgasolina = consumo + cosgasolina
                                    ctranporte = cosgasolina
                                    os.system("cls")
                                    print(f"\nSU CONSUMO EN ESTE PERIODO DE TIEMPO FUE DE {consumo} g/km\n")
                                    
                    

                                    print(f"\nSU FACTOR DE CONSUMO DE CO2 ES DE: {consumo} gCO2/km")
                                    os.system("pause")
                                    
                                
                                else:
                                    print("NO SE ENCONTRÓ EL PERIODO DE TIEMPO")
                    
                                    os.system("pause")
                        
                        cosgasolina = ['TRANSPORTE',[ctranporte]]
                        dependencia[2] = cosgasolina
                        for n in dependencia[2][1]:
                            n = cosgasolina
                                    
                    elif claseconsumo == 3:
                        isActive = False
                        break
        if not is_dependencia:
            print("NO SE ENCONTRO DEPENDENCIA")
            os.system("pause")    
            isActive = False        
                
                    
                    
           
    
    


                    

                