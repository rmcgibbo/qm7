#!/usr/bin/env python2
"""
PURPOSE:

Unpickle the qm7.pkl file downloaded from http://quantum-machine.org/index.php?page=datasets

$ md5 qm7.pkl
MD5 (qm7.pkl) = 7cb2ec22c0d7b12b94d0d35c3321258a

> This dataset is a subset of GDB-13 (a database of nearly 1 billion stable and
> synthetically accessible organic molecules) composed of all molecules of up
> to 23 atoms (including 7 heavy atoms C, N, O, and S), totalling 7165
> molecules. We provide the Coulomb matrix representation of these molecules
> and their atomization energies computed similarly to the FHI-AIMS
> implementation of the Perdew-Burke-Ernzerhof hybrid functional (PBE0). This
> dataset features a large variety of molecular structures such as double and
> triple bonds, cycles, carboxy, cyanide, amide, alcohol and epoxy. The Coulomb
> matrix is defined as
> C_{ii} = 0.5 Z_i 2.4
> C_{ij} = Z_i Z_j / || R_i - R_j ||
> where Z i is the nuclear charge of atom i and R i is its position.
> The Coulomb matrix has built-in invariance to translation and rotation of the
> molecule. The atomization energies are given in kcal/mol and are ranging
> from -800 to -2000 kcal/mol).

> The dataset is composed of three multidimensional arrays X (7165 x 23 x 23),
> T (7165) and P (5 x 1433) representing the inputs (Coulomb matrices), the
> labels (atomization energies) and the splits for cross-validation,
> respectively. The dataset also contain two additional multidimensional
> arrays Z (7165) and R (7165 x 3) representing the atomic charge and the
> cartesian coordinate of each atom in the molecules.

This script writes the geometry of each file to a seperate .xyz file,
and uses openbabel to convert that to a qchem input file, with assigned
spin and multiplicity.
"""
from __future__ import print_function
from os import system
import numpy as np
import mdtraj as md

BOHR2ANG = 0.52917721092


#with open('qm7.pkl') as f:
#    pickl.
qm7 = np.load('qm7.pkl')
N = qm7['R'].shape[0]


for i in range(N):
    n = sum(1 for z in qm7['Z'][i] if z != 0)

    with open('xyz/%d.xyz' % i, 'w') as f:
        print(n, file=f)
        print('index:%d\tPBE0_E:%f' % (i, qm7['T'][i]), file=f)
        for j in range(n):
            fmt = '  %s         %.6f       %.6f        %.6f'
            x, y, z = qm7['R'][i,j] * BOHR2ANG

            symbol = md.element.Element.getByAtomicNumber(qm7['Z'][i,j]).symbol
            print(fmt % (symbol, x, y, z), file=f)

    system('obabel %s --partialcharges mmff94 -O %s' % (
        'xyz/%d.xyz' % i, 'qcin/%d.qcin' % i))
