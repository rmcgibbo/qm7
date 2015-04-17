import os
os.chdir('compounds')
os.system('obabel ../compounds.smi -O compound.qcin --gen3d --conformer --nconf 1 --weighted -m --append cansmi --addtotitle cansmi:')
