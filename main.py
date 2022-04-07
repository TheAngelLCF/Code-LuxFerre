# Code LuxFerre | Main File
# Made by TheAngelLCF
# Logiciel propriétaire gratuit
import os, cryptage, decodage

if __name__ == "__main__":
    print("Merci d'utiliser le code LuxFerre par TheAngelLCF !")

    choix = ''
    while choix != 'codage' and choix != 'decodage':
        choix = input("Que voulez-vous faire (codage ou decoddage)? ")
    
    if(choix == 'codage'):
        print('\n' * 100)
        cryptage.start()
        input("Pour fermer le programme, cliquer sur Entrée !")
    else:
        print('\n' * 100)
        decodage.start()
        input("Pour fermer le programme, cliquer sur Entrée !")
