from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()
env.io.atom_files_directory = ['.', '../atom_files']

a = loopmodel(env, alnfile = 'alignment.ali',
              knowns = 'p4', sequence = 'p4MU')
a.starting_model = 1
a.ending_model = 6

a.loop.starting_model = 1
a.loop.ending_model   = 2
a.loop.md_level       = refine.fast


a.make()