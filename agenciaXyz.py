priceAdulto = 1450000
priceNiños = 870000
subtotal = 0
totalAdultos = 0
totalNiñoz = 0
totalperChicamocha = 0
totalperGuajaira = 0
totaltperLlanos = 0
totaldinChicamocha = 0
totaldinGuajaira = 0
totaltdinLlanos = 0
totalTodo = 0
i = 0
j = 0 
p = 0
dest = ""
print("welcoome to xyz agency")
op = int(input("desea hacer una cotizacion?\n 1 para si\n 2 para no\n"))
while op == 1:
    nombre = input("ingrese su nombre: ")
    numAdultos = int(input("ingrese cantidad de adultos: "))
    totalAdultos = numAdultos + totalAdultos
    numNiños = int(input("ingrese cantidad de niños: "))
    totalNiñoz += numNiños 
    print("destino--- \n 1 para guajira\n 2 para cañon de chicamocha\n 3 para llanos orientales")
    destino = int(input("ingrese el destino: "))

    if destino == 1:
        dest = "guajira"  
        totalperGuajaira += numAdultos + numNiños 
        totaldinGuajaira =  (priceAdulto * numAdultos)+(priceNiños * numNiños) 
        i += totaldinGuajaira  
    elif destino == 2:
     dest = "cañon de chicamocha"
     priceAdulto = 1600000
     priceNiños = 960000
     totalperChicamocha += numAdultos + numNiños 
     totaldinChicamocha =  (priceAdulto * numAdultos)+(priceNiños * numNiños) 
     j += totaldinChicamocha
    elif destino == 3:
       dest = "llanos orientales"
       priceAdulto = 1300000
       priceNiños = 720000
       totaltperLlanos += numAdultos + numNiños 
       totaltdinLlanos =  (priceAdulto * numAdultos)+(priceNiños * numNiños)   
       p += totaltdinLlanos
    else:
       while destino != 1 and destino != 2 and destino != 3:
          print("error...")
          destino = int(input("ingrese denuvo el destino"))
          
    subtotal = (priceAdulto * numAdultos)+(priceNiños * numNiños)
    totalTodo += i + j + p
    print("nombre del cliente: "+nombre)
    print("destino: "+ dest)
    print("cantidad de adultos: "+str(numAdultos))
    print("cantida de niños: "+str(numNiños))
    print("subtotal: "+str(subtotal))  

    op = int(input("desea hacer otro registro?\n 1 para si\n 2 para no\n "))  

print("cantidad de personas que viajan para guajira: "+str(totalperGuajaira))
print("cantidad de personas que viajan para cañon de chicamocha: "+str(totalperChicamocha))
print("cantidad de personas que viajan para  llanos orientales: "+str(totaltperLlanos))
print("total de dinero de viajes para guajira: "+str(i))
print("total de dinero de viajes para cañon de chicamocha: "+str(j))
print("total de dinero de viajes para llanos orientales: "+str(p))
print("total de adultos: "+str(totalAdultos))
print("total de niños: "+str(totalNiñoz))
print("total de dinero por todos los destinos: "+str(totalTodo))

 
          
       
