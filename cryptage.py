# Code LuxFerre | Cryptage
# Make by TheAngelLCF
# Logiciel propriétaire gratuit
import os

def compile_str(string: str) -> list:
    final = []
    for elt in string:
        if(elt == " "): final.append(200)
        else: final.append(ord(elt))
    return final

def adding_decal(liste: list, nbr: int) -> list:
    final = []
    for elt in liste:
        if(elt + nbr < 100): raise ValueError("Merci de mettre un nombre qui permet d'avoir plus de 100 partout !")
        final.append(elt + nbr)
    return final

def crypte():
    phrase = input("Merci de mettre votre phrase ici: ")
    compiled = compile_str(phrase)
    minn = 100 - min(compiled)
    while True:
        try:
            nbr = int(input("Combien voulez-vous de décalage (minimum " + str(minn) + "): "))
            if(nbr < minn): print("Meric de mettre un nombre plus grand que", minn)
            else: break
        except: pass
    
    final = adding_decal(compiled, nbr)
    liste_code = [oct, hex]
    from random import shuffle
    shuffle(liste_code)
    
    string = ''
    for elt in final:
        string += str(elt)
    
    string = str(liste_code[0](int(string)))[2:]
    if(type(liste_code[0]) == type(hex)): base = 16
    else: base = 8
    print("Base utilisé", base)
    print("Voici le cryptage:")
        
    return string

def read_file(file_name: str, directory='./') -> list:
    with open(directory + file_name, 'r', encoding='UTF-8') as file:
        liste = file.readlines()
    
    final = []
    for k in range(len(liste) - 1):
        final.append(liste[k][:-1])
    final.append(liste[-1])
    
    return final

def write_file(file_name: str, to_write: list, directory='./'):
    import os
    if(file_name in os.listdir(directory)): os.remove(directory + file_name)
    
    with open(directory + file_name, 'a', encoding='UTF-8') as file:
        for k in range(len(to_write) - 1):
            file.write(to_write[k] + '\n')
        file.write(to_write[-1])
        
    return True

def crypte_file():
    file_name = input("Merci de spécifier le nom du fichier: ")
    
    compiled = []
    for elt in read_file(file_name):
        compiled.append(compile_str(elt))
        
    # Recherche du min
    
    minn = min(compiled[0])
    for k in range(1, len(compiled)):
        if(minn > min(compiled[k])):
            minn = min(compiled[k])
           
    
    while True:
        try:
            nbr = int(input("Combien voulez-vous de décalage (minimum " + str(minn) + "): "))
            if(nbr < minn): print("Meric de mettre un nombre plus grand que", minn)
            else: break
        except: pass
        
    final = []
    for elt in compiled:
        final.append(adding_decal(elt, nbr))
        
    final_string = ''
    
    for liste in final:
        temps = ''
        for value in liste:
            temps += str(value)
        temps = str(hex(int(temps)))[2:]
        final_string += temps + '\n'
        
    final_string = final_string[:-1]
    
    if(file_name + '.crypte' in os.listdir()):
        choix = ''
        while choix != 'oui' and choix != 'non':
            choix = input("Fichier de sortie déjà créer, voulez-vous le supprimer ? ").lower()
            
        if(choix == 'oui'): os.remove(file_name + '.crypte')
        else:
            print("Impossible d'enregistrer le fichier !")
            return final_string
    
    with open(file_name + '.crypte', 'a', encoding='UTF-8') as file:
        file.write(final_string)
        
    print('Fichier de sortie: ' + file_name + '.crypte')

def start():
    choix = ''
    while choix != 'phrase' and choix != 'fichier':
        choix = input("Que voulez-vous crypter (phrase ou fichier)? ").lower()
    if(choix == 'phrase'): print(crypte())
    else: crypte_file()

if __name__ == "__main__":
    start()