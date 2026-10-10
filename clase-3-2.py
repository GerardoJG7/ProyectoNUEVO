edad = int (input("Introduca la edad: "))
dia = input("Introduzca el dia: ")
por_descuento=0

if edad < 0:
   print("Edad invalida")
else:
    entrada=1000 
    if dia.lower() != "lunes":
        if edad <2:
            por_descuento = 100
        elif edad <=5:
            por_descuento = 50
        elif edad <=10:
            por_descuento = 20   
        elif edad < 55:
            por_descuento = 0
        else:
            por_descuento = 30  
    else: 
        sexo = input("Introduzca el genero (M o F): ")
        if (sexo.upper()=="M" and edad >= 65) or (sexo.upper()=="F"):
         por_descuento = 50
        else:
            por_descuento = 0
    
    if por_descuento < 30:
        estudiante= input("Es estudiante (si o no): ")
        if estudiante.lower()=="si": 
            por_descuento = 25

    if por_descuento != 0 :
        descuento = entrada * por_descuento / 100
        print(f"El porcentaje de descuento es {por_descuento}% ") 
        print(f"El monto del descuento es {descuento}" )       
    else:
        por_descuento = 0 

    monto_pagar = entrada - descuento
    print(f"El monto a pagar es {monto_pagar}")