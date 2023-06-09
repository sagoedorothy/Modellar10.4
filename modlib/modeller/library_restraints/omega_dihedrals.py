#   residue    weights                  means        stdevs
omega = [
    ( 'ALA', (0.9987, 0.0013), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'CYS', (0.9988, 0.0012), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'ASP', (0.9981, 0.0019), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'GLU', (0.9984, 0.0016), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'PHE', (0.9986, 0.0014), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'GLY', (0.9975, 0.0025), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'HIS', (0.9982, 0.0018), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'ILE', (0.9991, 0.0009), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'LYS', (0.9986, 0.0014), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'LEU', (0.9990, 0.0010), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'MET', (0.9987, 0.0013), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'ASN', (0.9981, 0.0019), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'PRO', (0.9489, 0.0511), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'GLN', (0.9986, 0.0014), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'ARG', (0.9982, 0.0018), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'SER', (0.9976, 0.0024), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'THR', (0.9983, 0.0017), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'VAL', (0.9991, 0.0009), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'TRP', (0.9993, 0.0007), (3.13810, 0.00000), (0.04014, 0.04014) ),
    ( 'TYR', (0.9980, 0.0020), (3.13810, 0.00000), (0.04014, 0.04014) ),
  ]

def make_restraints(atmsel, restraints, num_selected):
    from modeller import forms, physical, features
    for (res, weights, means, stdevs) in omega:
        for a in atmsel.find_atoms(res, ('CA', 'C', '+N', '+CA'), num_selected):
            r = forms.MultiGaussian(physical.omega_dihedral,
                                    features.Dihedral(*a), weights, means,
                                    stdevs)
            restraints.add(r)
