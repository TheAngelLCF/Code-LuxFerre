# Code LuxFerre | Decodage
# Make by TheAngelLCF
# Logiciel propriétaire gratuit
import os

def separation(string: str) -> list:
    assert len(string) % 3 == 0, "Le code que vous avez donner n'est psa compatible avec le cryptage LuxFerre !"
    temps = ''
    final = []
    for rang in range(len(string)):
        temps += string[rang]
        if((rang + 1) % 3 == 0 and rang != 0):
            final.append(int(temps))
            temps = ''
    return final

def delete_crypte(liste: list, nbr: int) -> list:
    final = []
    for elt in liste:
        final.append(elt - nbr)
    return final

def decompile(liste: list) -> str:
    string = ''
    for elt in liste:
        if(elt == 200): string += " "
        else: string += chr(elt)
    return string

def formate(string: str, base: int):
    try:
        final = int(string, base)
    except:
        input("La base renseigner n'est pas la bonne !")
        exit()
    return str(final)

def decode():
    code = input("Merci d'entrer le code a decodé: ")
    while True:
        try:
            base = int(input("Merci d'entrer la base: "))
            break
        except: pass
    
    while True:
        try:
            decal = int(input("Merci d'entrer le code: "))
            break
        except: pass
        
    separe = separation(formate(code, base))
    final = delete_crypte(separe, decal)
    decompiled = decompile(final)
    print("Voici ce que nous avons décodé:")
    print(decompiled)
    
def read_file(file_name: str):
    with open(file_name, 'r', encoding='UTF-8') as file:
        read = file.readlines()
    
    final = []
    for elt in read:
        if('\n' in elt): final.append(elt[:-1])
        else: final.append(elt)
        
    return final

def decode_file():
    file_name = input("Merci d'entrer le code a decodé: ")
    base = 16
    while True:
        try:
            decal = int(input("Merci d'entrer le code: "))
            break
        except: pass
        
    liste_base = read_file(file_name)
    
    final = []
    for ligne in liste_base:
        final.append(separation(formate(ligne, base)))
    
    uncrypted = []
    for elt in final:
        uncrypted.append(delete_crypte(elt, decal))
        
    decompiled = []
    for elt in uncrypted:
        decompiled.append(decompile(elt))
        
    final_string = ''
    for elt in decompiled:
        final_string += elt + '\n'
    final_string = final_string[:-1]
    
    fichier_sorti = input("Merci de préciser le fichier de sortie ici (attention, si un fichier existe alors il sera remplacé): ")
    
    if(fichier_sorti in os.listdir()): os.remove(fichier_sorti)
    
    if('decoder' not in os.listdir()): os.mkdir('decoder')

    with open('decoder' + fichier_sorti, 'a', encoding='UTF-8') as file:
        file.write(final_string)
        
    print("Décryptage effectué !\nFichier généré avec succés dans le dossier *decoder*!")

if __name__ == '__main__':
    choix = ''
    while choix != 'phrase' and choix != 'fichier':
        choix = input("Que voulez-vous décoder (phrase ou fichier)? ")
    if(choix == 'phrase'): decode()
    else: decode_file