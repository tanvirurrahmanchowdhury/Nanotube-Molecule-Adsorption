#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 17:00:55 2020

@author: Tanvir Chowdhury
"""

from ase.build import nanotube, molecule, add_adsorbate
from ase.io.vasp import write_vasp
from ase.visualize import view

# creating a (10,0) nanotube
cnt = nanotube(10,0,length=2)
# creating an ammonia molecule
ammonia = molecule('NH3')
'''
#print ammonia unit cell
print(ammonia.get_cell())
#print cnt unit cell
print(cnt.get_cell())
#print ammonia coordinates of the atoms N and 3 H
print(ammonia.get_positions())
#print cnt coordinates
print(cnt.get_positions())'''
# adding ammonia on top of cnt at a z value of 1.5 Angstroms
add_adsorbate(cnt,ammonia,-4.55,position=(0,5.914))

#new coordinates after adding ammonia on top of cnt
#print(cnt.get_positions())

# assuming the supercell is simple cubic
a, b, c = 7.8, 7.8, 13.1
cnt.set_cell([(a, 0, 0), (0, b, 0), (0, 0, c)])
# assuming the supercell is hexagonal
'''a, c = 2.29, 3.58
cnt.set_cell([a, a, c, 90, 90, 120])'''
# writing the data on POSCAR
write_vasp('POSCAR', cnt)
view(cnt)