import h5py 
import numpy as np

fic = h5py.File("test.hdf5",'w')

dt = np.dtype([('id', np.uint8), ('nom', np.dtype("S10") ), ( 'tel', np.dtype("S20") ) ])

fic.create_group('data')
dset = fic.create_dataset('/data/liste_tel', (5,), dtype=dt, maxshape=(None,))

print dset.shape
print dset.dtype

enreg = dset[...]

print enreg

enreg[0]['id'] = 1
enreg[0]['nom'] = 'TOTO'
enreg[0]['tel'] = '0612345678'
enreg[1]['id'] = 2
enreg[1]['nom'] = 'TITI'
enreg[1]['tel'] = '0600000000'

print dset[0]

print "dest 1 nom = %s " % dset[1]['nom']

fic.flush()
fic.close()
