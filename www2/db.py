import sqlite3, os
conn = sqlite3.connect("C:\\IUT\\Web\\ProjetTutoreEntrepriseRecrute\\www\\database")


entreprises = []

for entreprise in os.listdir("C:\\IUT\\Web\\ProjetTutoreEntrepriseRecrute\\Entreprises\\"):
    f = open("C:\\IUT\\Web\\ProjetTutoreEntrepriseRecrute\\Entreprises\\" + entreprise,'r')
    lignes = f.readlines()
    f.close()
    infosEntreprise = []
    for ligne in lignes[0:12]:    
        ligneInfo = ligne.replace('\n','').split(':')
        textBD = ""
        for text in ligneInfo[1:]:
            textBD += text
            
        if ligneInfo[0] in ["Taille","Pays","Salaire","Lien_offre","Images","Sources"]:
            textBD = textBD.replace(' ',"")
        if ligneInfo[0] in ["Nom"]:
            if textBD and textBD[0] == " ":
                textBD = textBD[1:]
        if ligneInfo[0] in ["Taille","Salaire"]:
            textBD = textBD
        infosEntreprise.append(textBD)
    for ligne in lignes[12:]:
        infosEntreprise[11] += "\n" + ligne
        
    print(len(tuple(infosEntreprise)))
    entreprises.append(tuple(infosEntreprise))

conn.executemany('INSERT INTO entreprises VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', entreprises)



for row in conn.execute('SELECT * FROM entreprises'):
    print(row)
    
conn.commit()
conn.close()