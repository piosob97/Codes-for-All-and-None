import numpy as np
import sys

# this is a code for translating an XYZ file over an arbitrary vector [x,y,z]
# the syntax is python<python_version> translate.py <filename> <x> <y> <z>
# the result is the XYZ file of the rotated molecule printed out on a screen 

def T_xyz(v,x,y,z):
    # defining the 3D translation
    v = np.array([v[0]+x, v[1]+y, v[2]+z])
    return v

myfile = sys.argv[1]
myfile = open(myfile, 'r').read().splitlines()
n_atoms = int(myfile[0])
x = float(sys.argv[2])
y = float(sys.argv[3])
z = float(sys.argv[4])

print(n_atoms)
print()
for i in myfile[2:n_atoms+2]:
    v = i.split()
    w = np.array([float(v[1]), float(v[2]), float(v[3])])
    w = T_xyz(w,x,y,z)
    print(v[0], w[0], w[1], w[2])
