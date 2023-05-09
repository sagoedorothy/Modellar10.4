from modeller import *

env = Environ()
aln = Alignment(env)
m = Model(env, file= 'p4', model_segment=('FIRST:A','LAST:A'))
aln.append_model(m, align_codes='p4', atom_files='p4.pdb')
aln.append(file='p4MU.ali', align_codes='p4MU')
aln.align2d()
aln.write(file='alignment.ali', alignment_format='PIR')
aln.write(file='alignment.pap', alignment_format='PAP')