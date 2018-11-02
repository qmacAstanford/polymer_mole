#  ----------------------------------------
#
#    Parses output file and makes pdb
#    Written by Quin MacPherson
#    Started: 11/11/16
#
#   Example usage:
#   for i in `seq 1 31`; do python r2pdb.py r30v$i > snap0$i.pdb; done
#-------------------------------------------

nboundary=1000
import math
import sys
import numpy as np
if len(sys.argv) != 3:
      sys.exit('wrong number of arguments')
fname= sys.argv[1]
fnameMeth= sys.argv[2]


# ---------------------
#    Read Meth file
# --------------------
AllMeth=[]
with open(fnameMeth) as f:
    for line in f:
        temp=line.split()
        methValue=int(temp[0])
        AllMeth.append(methValue)

def rotateZ(r,theta,center=np.array([32.0,32.0,32.0])):
    R = np.array([[np.cos(theta), -np.sin(theta), 0.0],
                  [np.sin(theta),  np.cos(theta), 0.0],
                  [0.0          ,  0.0          , 1.0]])
    return np.dot(R,r-center)+center
def rotateX(r,theta,center=np.array([32.0,32.0,32.0])):
    R = np.array([[1.0          ,            0.0,            0.0],
                  [0.0          ,  np.cos(theta), -np.sin(theta)],
                  [0.0          ,  np.sin(theta),  np.cos(theta)]])
    return np.dot(R,r-center)+center

# ---------------------
#    Read from file
# --------------------


X=[];
Y=[];
Z=[];
AB=[];
METH=[];
index=[];
n=0;
count=0;
skip=1
with open(fname) as f:
   for line in f:
       count=count+1
       if count%skip != 0:
           continue
       temp=line.split()
       y=float(temp[0])
       x=float(temp[1]) 
       z=float(temp[2])
       [x,y,z] = rotateZ(np.array([x,y,z]),-np.pi/4+np.pi/2)
       [x,y,z] = rotateX(np.array([x,y,z]),-np.pi/3)
       
       #if  x < 12:
       if  x < 32:
           continue

       #if x > 16:
       if x > 38:
           continue

       index.append(count)
       X.append(x)  
       Y.append(y) 
       Z.append(z)
       AB.append(int(temp[3]))
       METH.append(AllMeth[count-1])

nbeads=len(X)

# -------------------------
#  Set atom types
# -------------------------
atomType=[]
for n in range(0,nbeads):
    if METH[n]==1:
        atomType.append('  A2')
    elif METH[n]==2:
        atomType.append('  A3')
    elif METH[n]==0:
        atomType.append('  A1')
    else:
        raise ValueError('Meth type not recognized, '+str(METH[n]))

# -------------------
#  Write to pdb format
# ---------------------

chemName='Leviathan!'
if nbeads > 99999:
    raise 'too many beads for pdb format'

resname='WLC'
if len(resname) != 3:
    raise 'resname must be 3 letters'
print('HET    %s  A   1   %5d     Pseudo atom representation of DNA'
      %(resname,nbeads+nboundary))
print('HETNAM     %s %s'%(resname,chemName))
print('FORMUL  1   %s       '%(resname))

Ntot=0;
for n in range(0, nbeads):
    atomName=atomType[n]
    if len(atomName) != 4:
        raise 'Atom name needs to be 4 characters'
    x=X[n]
    y=Y[n]
    z=Z[n]
    print('HETATM%5d %s %s          %8.3f%8.3f%8.3f  1.00  1.00           C'
            %(n+1,atomName,resname,x,y,z))
    if n != 0:
        if (index[n]==index[n-1]+1):
            print('CONECT%5d%5d'%(n, n+1))
    Ntot=Ntot+1;


# -----------------
#  Draw confinement
# -----------------

R=31
center = [32.0,32.0,32.0]
#R=15
#center = [16.0,16.0,16.0]

for N in range(0,nboundary):
     atomName='  A4'
     x=center[0];
     y=center[1]+R*math.sin(2*3.141592*N/nboundary)
     z=center[2]+R*math.cos(2*3.141592*N/nboundary)
     Ntot=Ntot+1;
     print ('HETATM%5d %s %s          %8.3f%8.3f%8.3f  1.00  1.00           C'
           %(Ntot,atomName,resname,x,y,z))
     if N != 0:
         print('CONECT%5d%5d'%(Ntot,Ntot-1))
    
print('CONECT%5d%5d'%(nbeads+1,Ntot))


# ----------------
#   Draw scalebar
# ----------------

x=R+1.0
y=0.0
z=0.0
atomName='  A4'
Ntot=Ntot+1;
print ('HETATM%5d %s %s          %8.3f%8.3f%8.3f  1.00  1.00           C'
      %(Ntot,atomName,resname,x,y,z))
y=250/28.7
Ntot=Ntot+1;
print ('HETATM%5d %s %s          %8.3f%8.3f%8.3f  1.00  1.00           C'
      %(Ntot,atomName,resname,x,y,z))
print('CONECT%5d%5d'%(Ntot-1,Ntot))



# ----------------
#   Draw point
# ----------------

#x=28.9
#y=37.0
#z=36.05
#
#[x,y,z] = rotateZ(np.array([x,y,z]),-np.pi/4)
#[x,y,z] = rotateX(np.array([x,y,z]),-np.pi/3)
#
#atomName='  A5'
#Ntot=Ntot+1;
#print ('HETATM%5d %s %s          %8.3f%8.3f%8.3f  1.00  1.00           C'
#      %(Ntot,atomName,resname,x,y,z))
#print('CONECT%5d%5d'%(Ntot-1,Ntot))

