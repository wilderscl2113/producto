# import random
# vidas = 5;
# puntos =0;



# while(vidas!= 0):
#     num =  random.randint(0, 9)
    
#     if num == 0:
#         vidas -=1
#         print(f"vidas:{vidas}")
#     else:
#         puntos +=1
#         print(f"puntos:{puntos}")

valor_compra = ""
numero_cuotas = ""
valor_cuotas = ""
counter = 0

print ("valor de la compra: ")
valor_compra = input()
print("numero de cuotas: ")
numero_cuotas = input()

valor_cuotas = float(valor_compra)/float(numero_cuotas);

new_value_compras = float(valor_compra)


while(new_value_compras!=0 and new_value_compras >=0 ):
    new_value_compras-=float(valor_cuotas)
    counter +=1
    print("el valor a pagar en la cuota Nro -",counter," tendra un valor de :",new_value_compras)

    