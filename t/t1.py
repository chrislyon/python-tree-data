from tables import *

class Liste_Tel(IsDescription):
	idn = Int64Col()
	nom = StringCol(20)
	tel = StringCol(30)


file_name = 'test.hdf5'

fic = open_file(file_name, mode='w', title = "FICHIER DE TEST")

group = fic.create_group("/", 'data', 'Donnee de test')

t = fic.create_table( group, 'liste', Liste_Tel, "LISTE POSTES SRA")

l = t.row
l['idn'] = 1
l['nom'] = 'toto'
l['tel'] = '0600000000'
l.append()
l['idn'] = 2
l['nom'] = 'titi'
l['tel'] = '0612000000'
l.append()

fic.close()

## Now lecture 
fic = open_file(file_name, mode='w', title = "FICHIER DE TEST")

print fic.root

print fic.root.data.liste

fic.close()
