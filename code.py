print("Vérification du nombre premier")
c=0
premier=True
while premier == True:
    num=int(input("entrer la valeur à vérifier svp"))
    for i in range(1,num+1):
        if num%i==0:
            c=c+1

    if c==2:
        print(f"{num} est un nombre premier")
        print("merci d'avoir acceder a notre programme")

    else:
        print(f"{num} n'est pas un nombre premier")
