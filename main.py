import util
from util.funciones import *

ans=True
while ans:
    print("""
    1.Dado un string, cambiar todos los espacios por guiones.('Esto es  una prueba', ' ', '-')
    2.Cambiar Mayusculas por Minusculas.("Esto cambia Mayusculas por minusculas y viceversa")
    3.Recibir string, indice y letra a modificar y devuelve string modificado.('Cambiar una Letra', 12, 'l')
    4.Devuelva un string con el nombre y apellido pero con capitalizacion.("veamos esta prueba si funciona bien")
    5.Devuelve la puntuacion del subcampeon,([3,4,42,1,4,621,621,620,3,5])
    6.(5a)Recibe un numero entero y imprima  un triangulo de numeros de altura. (impTriangulo(13))
    7.(5b)reciba string, devolver 3 caracteres mas usados en orden descendiente.(caracterMasUsado("Codo a codo", True))
    8.Exit/Quit
    """)
    ans=input("Que quiere hacer? ")
    if ans=="1":
        # caso 1
        print ("Caso 1")
        print (reemplazar('Esto es  una prueba', ' ', '-'))
    elif ans=="2":
        # caso 2
        print ("Caso 2")
        print(mayPorMin("Esto cambia Mayusculas por minusculas y viceversa"))
    elif ans=="3":
       # caso 3
       print ("Caso 3")
       print(cambioLetra('Cambiar una Letra', 12, 'l'))
    elif ans=="4":
       # caso 4
       print ("Caso 4")
       print(primeraLetraMay("veamos esta prueba si funciona bien"))
    elif ans=="5":
       #caso 5
       print ("Caso 5")
       print (subCampeon([3,4,42,1,4,621,621,620,3,5]))
    elif ans=="6":
        #caso 5a
        print ("Caso 5a")
        impTriangulo(13)
    elif ans=="7":
        #caso 5b
        caracterMasUsado("Codo a codo", True)       
    elif ans=="8":
       print("\n Adios") 
       ans = None
    else:
       print("\n La opcion no es valda, intenet nuevamente.")









