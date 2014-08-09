from tables import *

class Liste_Tel(IsDescription):
	idn = Int64Col()
	nom = StringCol(20)
	tel = StringCol(30)

