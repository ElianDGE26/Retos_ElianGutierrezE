print("PROGRAMA DE PARQUEO DE ELIAN GUTIERREZ")
dia = input("Digite que dia: ")
hora = int(input("Digite la hora que duró parqueado en miniscula por favor: "))
minutos = int(input("Digite los minutos que duró parqueado: "))
cobro = 0

if(hora > 24 or hora < 0 or minutos < 0 or minutos > 60):
    print("ERROR EN EL INGRESO DE INFORMACION, SE PROCEDE A CERRAR EL PROGRAMA")

elif (dia == 'lunes' or dia == 'martes' or dia == 'miercoles'):
    cobro = (hora*2.00)
    if (minutos>5):
        cobro += 2.00
    else:
        cobro += 0
        
elif (dia == 'jueves' or dia == 'viernes'):
    cobro = (hora*2.50)
    if (minutos>5):
        cobro += 2.5
    else:
        cobro += 0
        
elif (dia == 'sabado' or dia == 'domingo'):
    cobro = (hora*3.00)
    if (minutos>5):
        cobro += 3.00
    else:
        cobro +=0
        
else:
    print("ingresó un dia errado")

print("El cobro por su parqueo es: $", cobro)