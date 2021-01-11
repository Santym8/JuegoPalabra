palabra="Murcielago".upper()                                                                        #Palabra                                            
aciertos=0                                                                                           #Almacena el umero de aciertos
tusletras=[]                                                                                         #Almacena las letras ya usadas para evitar contar aciertos repetidos
lista_p=[]                                                                                           #Almacena una lista con las letra de la palabra 
lista_c=[]                                                                                           #Almacena la lista que se mostrara en pantalla con los aciertos y los espacios en blanco
casillas=len(palabra)                                                                                #Crea y almacena el numero de casilleros que tendra la palabra 
vidas=5                                                                                              #Almacena las vidas del jugador
for i in palabra:                                                                                    #Rellena las listas: lista_p y lista_c     
    lista_p.append(i)               
    lista_c.append("_")
for i in lista_c:                                                                                    #Imprime los casilleros en pantalla
    print(i, end=" ")
while vidas>0:
    while True:
        letra= input("\nLetra: ").upper()                                                            #Pide una letra
        n=len(letra)
        if n == 1:
            break  
        else:
            print("                                Solo una letra a la vez")            
    if letra in palabra:                                                                              #Evalua si la letra esta en la palabra
        if letra in tusletras:                                                                        #Evalua si la letra ya ha sido escogida anteriormente 
            print("                             Letra ya seleccionada")
            vidas=vidas-1    
        else:               
            tusletras.append(letra)                                                                    #Si la letra no ha sido escogida anteriromente la añade a la lista "tusletras"
            for i in palabra:                                                                          #Evalua cuantas veces se repite la letra dentro de la palabra y aumenta el numero de aciertos      
                if i == letra: 
                    n_veces=0
                    n_veces= n_veces + 1
                    aciertos= aciertos + n_veces
            indice=-1                                                                                   #Modifica la lista "lista_c" la cual se mostrara en pantalla añadiendo las letra ya adivinadas
            for i in lista_p:
                indice= indice + 1
                if i == letra:
                    lista_c[indice]= letra
        for i in lista_c:                                                                               #Imprime la lista "lista_c"
            print(i, end=" ")    
    else:
        vidas=vidas-1                                                                                    #Elimina una vida al jugador si falla
        for i in lista_c:                                                                                #Si la letra digitada no se encuentra dentro de la palabra Imprime la lista "lista_c".
            print(i, end=" ") 
    
    print(f"\n                             Vdias: {vidas}")                                               #Imrpime el numero de vidas

    if vidas == 0:
        print(f"                                           Perdisete, la palabra es {palabra}")  
    if aciertos == casillas:
        print(f"                                              ¡GANASTE! la palabara es {palabra}")       #Verifica el numeo de aciertos y los compara con el numero de letras para asi terminar el juego.
        break

salir=input("------------------------------------------------------------Presiona ENTER para salir-------------------------------------")
if salir == "":
    pass

