import h5py 
import numpy as np

fic = h5py.File("test.hdf5",'w')

dt = np.dtype([('id','i'), ('nom', np.str_, 10), ( 'tel', np.str_, 20 ) ])

fic.create_group('data')
dset = fic.create_dataset('/data/liste_tel', (2,), dtype=dt)

print dset.shape
print dset.dtype

data = np.array( [(1,'TOTO', '0612345678'), (2, 'TITI', '0600000000')], dtype = dt )
dset[...] = data

print dset[0]

fic.flush()
fic.close()
