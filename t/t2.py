from tables import *
import os

class Liste_Tel(IsDescription):
	idn = Int64Col()
	nom = StringCol(20)
	tel = StringCol(30)

fic_name = 'test.hdf5'

fic = openFile(fic_name, mode='r', title = "FICHIER DE TEST")

t = fic.root.data.liste
print t

for l in t.iterrows():
	print l['idn'], l['nom'], l['tel']



fic.close()
