# importez os
import os
os.chdir(os.path.dirname(__file__))

# # allez dans le dossier Ex3 Videos
os.chdir("Ex3 Videos")

# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier

for cours in os.listdir() :
    cours_split= os.path.splitext(cours)
    cours_split2 = cours_split[0].split(" _ ")
    cours_strip = cours_split2[0].strip()
    cours_strip2 = cours_split2[2].strip()[1:]
    cours_zfill = cours_strip2.zfill(2)


