from rdkit import Chem

ALLOWABLE_ATOMS = set((1, 6, 7, 8, 1))
files = ['gdb/gdb11_size01.smi',
         'gdb/gdb11_size02.smi',
         'gdb/gdb11_size03.smi',
         'gdb/gdb11_size04.smi',
         'gdb/gdb11_size05.smi',
         'gdb/gdb11_size06.smi',
         'gdb/gdb11_size07.smi']

with open('compounds.smi', 'w') as fout:
    for file in files:
        with open(file) as f:
            for line in f:
                smi = line.split('\t')[0]
                mol = Chem.MolFromSmiles(smi)
                nums = [a.GetAtomicNum() for a in mol.GetAtoms()]
                if set(nums).issubset(ALLOWABLE_ATOMS):
                    print(smi, file=fout)
