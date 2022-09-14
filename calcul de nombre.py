from random import randrange
limite=int(input())
sommeTotale=0
for loop in range(limite):
    choix=int(input())
    if choix in {1,2,3}:
        choix_ordi=randrange(1,4)
        print(choix_ordi)
        sommeTotale=sommeTotale+choix+choix_ordi
        difference1=sommeTotale-choix
        difference2=sommeTotale-choix_ordi
        if sommeTotale>=limite and difference1>=limite:
            print("Vous avez gagné")
            break
        elif sommeTotale>=limite and difference2>=limite:
            print("Vous avez perdu")
            break

            
    
                
        


        

