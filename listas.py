nombres =["pepito", "andres", "juan","maria","pedro"];
edad = [25,19,21,33,40];
estatura = [1.80,1.65,1.74,1.66,1.54]
casado = [False,False,False,True,True]
usuario = ["pepito",25,1.80,False]

print(nombres[0], edad[0],estatura[0],casado[0])

print(len(edad))

print(type(nombres))
print(type(edad))
print(type(estatura))
print(type(casado))
print(type(usuario))

#hacer un slice es generar rangos en las listas 
print(usuario[0:3])

print(nombres[1:-2])

#podemos validar su existe en la lista algun elemento
if "pepito"in nombres:
    print(f"el nombre esta en la lista")
else: print(f"no se encontro el nombre buscado ")

usuario[0]= 'luis'
print(usuario[0])

nombres[1:4] = "luis","pablo","pipe"
print(nombres)


#queremos insertar un item en una posicion especifica
nombres.insert(-2,"pepote")
nombres.insert(0,"pepito")
print(nombres[0:])

#podemos agregar con el metodo append() pero este se agrega al final de la lista
nombres.append("laura")
print(nombres[0:])

nombres2 = ['lis','juancho']

nombres.extend(nombres2)
print(nombres)

nombres.remove('pablo')
print(nombres[0:])

nombres.pop(-2)
print(nombres[0:])


del nombres[1]
print(nombres[0:])


nombres.clear();
print(nombres[0:])

del nombres
#print(nombres[0:])

#recorrer listas 

for i in edad:
    print(i)
    
# iterar en los index

for i in range(len(estatura)):
    print(estatura[i])
    
i = 0

while i<len(usuario):
    print(usuario[i])
    i+= 1

#usando list comprehesion

[print(x) for x in usuario]

for i,edad in enumerate(edad):
    print (i,edad)