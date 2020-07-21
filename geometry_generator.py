#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
from ase.build import fcc111, add_adsorbate
from ase.io.vasp import write_vasp

slab = fcc111('Al', size=(2,2,3))
add_adsorbate(slab, 'H', 1.5, 'hcp')
slab.center(vacuum=10.0, axis=2)

write_vasp('POSCAR', slab)

from ase.build import mx2, add_adsorbate
from ase.io.vasp import write_vasp

slab = mx2(formula='MoS2', kind='2H', a=3.19, thickness=3.2325,
        size=(1, 1, 1), vacuum=None)
cell=slab.get_cell()
print(cell)
write_vasp('POSCAR', slab)

import ase
from ase.build import mx2, add_adsorbate
slab = mx2(formula='MoS2', kind='2H', a=3.19, thickness=3.2325,
        size=(1, 1, 1), vacuum=None)
print(slab.get_cell())
print(slab.get_positions())'''

from ase.build import nanotube, molecule, add_adsorbate
from ase.io.vasp import write_vasp

cnt = nanotube(10,0,length=1)
amonia = molecule('NH3')
add_adsorbate(cnt,amonia,2)
write_vasp('test', cnt)