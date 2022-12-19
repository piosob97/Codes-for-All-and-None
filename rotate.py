import numpy as np
import sys

# this is a code for rotating an XYZ file over an arbitrary degree
# the syntax is: python<python_version> rotate.py <filename> <phi_x> <phi_y> <phi_z>
# the result is the XYZ file of the rotated molecule printed out on a screen 

def R_xyz(phi_x, phi_y, phi_z):
    # defining the 3D rotation matrices
    R_x = np.array([[1,0,0], [0,np.cos(phi_x),-np.sin(phi_x)], [0,np.sin(phi_x),np.cos(phi_x)]])
    R_y = np.array([[np.cos(phi_y),0,np.sin(phi_y)], [0,1,0], [-np.sin(phi_y),0,np.cos(phi_y)]])
    R_z = np.array([[np.cos(phi_z),-np.sin(phi_z),0], [np.sin(phi_z),np.cos(phi_z),0], [0,0,1]])

    # defining a general 3D rotation with
    R_xyz = np.dot(R_x,R_y)
    R_xyz = np.dot(R_xyz,R_z)
    return(R_xyz)

myfile = sys.argv[1]
myfile = open(myfile, 'r').read().splitlines()
n_atoms = int(myfile[0])
phi_x = float(sys.argv[2])
phi_y = float(sys.argv[3])
phi_z = float(sys.argv[4])

R = R_xyz(np.radians(phi_x), np.radians(phi_y), np.radians(phi_z))
print(n_atoms)
print()
for i in myfile[2:n_atoms+2]:
    v = i.split()
    w = np.array([float(v[1]), float(v[2]), float(v[3])])
    w = np.dot(R,w)
    for j in range(3):
        if np.abs(w[j]) < 0.00000001:
            w[j] = 0

    print(v[0], w[0], w[1], w[2])
