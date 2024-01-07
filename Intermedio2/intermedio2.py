import os
import menusint2 as menu
import consumoint2 as consumo
import co2int2 as co2
isActive = True
dependencias = []
opmenu = 0


while isActive:
    os.system("cls")
    opmenu = menu.menuprincipal()

    if opmenu == 1:
        rta = "S"
        ismenu = True
        while(ismenu):
            os.system("cls")
            dependencia = input("\nREGISTRE LA DEPENDENCIA: ").upper()  
            dependen = [dependencia, ["ELECTRICIDAD", []],["TRANSPORTE", []]]
            dependencias.append(dependen)
            print(dependencias)
            rta = input("\n¿DESEA REGISTRAR OTRA DEPENDENCIA? S(si)/N(no): ").upper() 
            if (rta != "S"):
                ismenu = False
    elif opmenu == 2:
        os.system("cls")
        buscar = str(input("INGRESE EL NOMBRE DE LA DEPENDENCIA: "))
        consumo.registrarconsumo(buscar, dependencias)
    elif opmenu == 3:
        os.system("cls")
        print("VER CO2 PRODUCIDO POR DEPENDENCIA")
        
        co2.VerCo2(  dependencias)
    elif opmenu == 4:
        os.system("cls")
        print("DEPENDENCIA QUE PRODUCE MAYOR CO2")
        co2.MayorCo2(dependencias)
    elif opmenu == 5:
        os.system("cls")
        print("GRACIAS POR USAR NUESTRO SISTEMA")
        isActive = False

