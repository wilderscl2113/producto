email = ""
tel = ""
password1 = ""
password2 = ""
counter = 0
status = False
dinero_en_cuenta =int(15000)

reg_log = input("quieres registrarte o logearte reg/log ");

while True:
    if(reg_log.lower() == "reg"):
        print("esto es el if")
        print("ingresa el correo electronico")
        email = input();
        print("ingresa el telefono")
        tel = input();
        print("ingresa la contraseña")
        password1 = input();
        while True:
            print("repita la contraseña")
            password2 = input();
            counter = counter+1
            if password2 == password1:
                status =True
                break;
            if password2 != password1 and counter > 7:
                status = False
                print ("ya llevas muchos intentos");
                break;
        if (status != False):
            print("deseas ingresar? Si/No")
            ingesasr = input();
            if ingesasr.lower() == "si":
                print("ingresa el correo electronico o el telefono")
                email_tel = input();
                if email_tel == email or email_tel == tel:
                    print("ingresa la contraseña")
                    passwordlog = input()
                    if passwordlog == password1:
                        status = True
                        print("te logueaste de forma correcta")
                    else:
                        print("no te pudiste loguear")
                        status= False
                  
    if (status == True):
        print("estas loguado de forma correcta y entraste a tu cuenta \n")
        

       
       
        if (dinero_en_cuenta <= 0):
            agregar_  = input("Si deseas agregar dinero copia agreg ");
            if(agregar_ == "agreg"):
                agregar = int(input("ingresa el valor a agregar "));
                dinero_en_cuenta = dinero_en_cuenta+agregar;
                print("este es el dinero en cuenta", dinero_en_cuenta)
        elif (dinero_en_cuenta > 0):
            agregar_descontar  = input("deseas agregar o descontar dinero? copia agreg o descont  ");
            if(agregar_descontar == "agreg"):
                agregar = int(input("ingresa el valor a agregar "));
                dinero_en_cuenta = dinero_en_cuenta+agregar;
                print("este es el dinero en cuenta", dinero_en_cuenta)
            elif(agregar_descontar == "descont"):
                descontar = int(input("ingresa el valor a descontar "));
                if(dinero_en_cuenta > (descontar + (descontar *0.19))):
                    dinero_en_cuenta = dinero_en_cuenta-(descontar+(descontar*0.19));
                    print("este es el dinero en cuenta", dinero_en_cuenta)
                else:print("No es posible descontar dinero en esta cuenta ya que el valor a descontar :",descontar+(descontar*0.19)," es mayor que el saldo de la cuenta :",dinero_en_cuenta)
        break;

    elif (status == False):
        print("no pudiste ingresar")
        break;
    
        
    
    elif(reg_log.lower() == "log"):    
        print("esto es el else")
        if reg_log.lower() == "log":
            print("ingresa el correo electronico o el telefono")
            email_tel = input();
        if email_tel == "email" or email_tel =="tel":
            print("ingresa la contraseña")
            passwordlog = input()
            if passwordlog == password1:
                print("te logeaste de forma correcta")
            else:print("no te pudiste loguear")