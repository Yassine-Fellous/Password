import re
import hashlib
import json

def password():
    entry = input("veulliez tapez un mot de passe : ")
    verif = 0
    while entry != "exit":
        if len(entry) < 8:#vérifie si l'input est inférieur à 8
            print("votre mdp doit contenir au moins 8 caractères.")
            entry = input("veulliez tapez un mot de passe : ")
            verif = 0
            continue
        else:
            verif += 1
        if "!" not in entry and "@" not in entry and "#" not in entry and "$" not in entry and "%" not in entry and "^" not in entry and "&" not in entry and "*" not in entry:#vérifie si l'input ne contient pas des caractères spéciale
            print("votre mdp doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)..")
            entry = input("veulliez tapez un mot de passe : ")
            verif = 0
            continue
        else:
            verif += 1
        if not re.search("[a-zàâäçèéêëîïôöùûü]", entry):#cherche si il n'y a pas de minuscule de meme pour les minusculse voyelles
            print("votre mdp Il doit contenir au moins une lettre minuscule.")
            entry = input("veulliez tapez un mot de passe : ")
            verif = 0
            continue
        else:
            verif += 1
        if not re.search("[A-Z]", entry):#vérifie si il n'y pas pas de majuscules
            print("votre mdp doit contenir au moins une lettre MAJUSCULE.")
            entry = input("veulliez tapez un mot de passe : ")
            verif = 0
            continue
        else:
            verif += 1
        if not "0" in entry and not "1" in entry and not "2" in entry and not "3" in entry and not "4" in entry and not "5" in entry and not "6" in entry and not "7" in entry and not "8" in entry and not "9" in entry:#vérifie si il y'a des chiffres
            print("votre mdp doit contenir au moins un chiffre.")
            entry = input("veulliez tapez un mot de passe : ")
            verif = 0
            continue
        else:
            verif += 1
        if verif == 5:#vérifie si tout les conditions son réunie pour hasher le mdp
            sha256 = hashlib.sha256()# création d'un objet de hashage
            sha256.update(entry.encode())#donne les donner a hasher à l'objet
            hash = sha256.hexdigest()#renvoie la valeur du hasahge en hexadécimal
            print("le mdp le voici en sha26 : " + hash)
            enre = input("voulez vous enregistrer votre mdp repondez par oui ou par non : ")
            if enre == "oui":#vérifie si l'utilisateur a bient taper oui
                indicatif = input("veuillez indiquez un indiquatif pour votre mot de passe a enregistrer : ")
                mdp = {indicatif: hash}
                with open("data.json", "r") as json_file:#ouvre le fichier json en mode lecture
                    data = json.load(json_file)#convertit les donner en objet python
                if str(hash) in str(data):#verifie si le mot de passe et déja existant en convertisant les donner en chaine de caractère
                    print("votre mdp ne peux pas étre enregistrer car vous avez deja le enregistrer un mot de passe egal")
                    entry = input("veulliez tapez un mot de passe : ")
                    verif = 0
                    continue
                else:
                    data.update(mdp)#met a jour les donner en ajoutant mdp
                    with open("data.json", "w") as json_file:#ouvre le fichier json en mode ecriture
                        json.dump(data, json_file)# ecrit les donners dans le fichier json
                        print("votre mdp a été enregistrer")
                        enr = input("voulez voir votre dictionnaire de mdp hashé repondez par oui ou par non : ")
                if enr == "oui":
                    with open("data.json", "r") as donner:#ouvre le fichier json en mode ecriture
                        prin = json.load(donner)#convertit les donners en objet python
                    print(prin)#affiche l'objet
                    entry = input("veulliez tapez un mot de passe : ")
                    verif = 0
                    continue

            else:
                entry = input("veulliez tapez un mot de passe : ")
                verif = 0
                continue

password()







