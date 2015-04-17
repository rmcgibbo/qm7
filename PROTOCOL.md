1. Downloaded the file gdb11.tgz from http://www.gdb.unibe.ch/gdb/home.html
   containing the entire GDB-11. (Downloaded April 16, 2015, 112 MB)

   $ md5 gdb/gdb11.tgz
   MD5 (gdb/gdb11.tgz) = 23be109329ca081c3fce5cff02a0a5c9

2. Ran the script filter-gdb.py to filter out compounds with up to seven heavy
   atoms, containing only H, C, N, O and S atoms. In contrast to Rupp et al.
   PRL 108, 058301 (2012), this yielded 9627 molecules, not 7165 as indicated
   in their work. Perhaps this is because it's from a different version of the
   database?

   This generates the file compounds.smi

   $ md5 compounds.smi
   MD5 (compounds.smi) = 3004614887c32e46465db329ae048941

3. Ran the script build-cartesian.py to generate the skeleton of qchem input
   files, 1 for each compound.

   $ obabel -V
   Open Babel 2.3.1 -- Oct 13 2011 -- 15:14:48

   Conformer generation is done with weighted rotor search for lowest energy conformer,
   using the default forcefield (MMFF94).

   $ obabel ../compounds.smi -O compound.qcin --gen3d --conformer --nconf 1 --weighted -m --append cansmi --addtotitle cansmi:
