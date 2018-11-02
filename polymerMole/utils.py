import math
import numpy as np
from polymerMole.glob import *

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

def SetAtomTypeSequentially(nbeads,Ncolors):
    atomType=[]
    for n in range(0,nbeads):
        color_n = int(np.floor(n*(Ncolors-1)/nbeads))
        if color_n<10:
            atomType.append('  A'+str(color_n))
        elif color_n<100:
            atomType.append(' A'+str(color_n))
        elif color_n<1000:
            atomType.append('A'+str(color_n))
        else:
            raise ValueError('Too many colors')
    return atomType

def SetAtomTypesByMethylation(METH):
    nbeads=len(METH)
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
    return atomType

def SetAtomTypeByPolymer(polymerLengthFile,index):
    if (polymerLengthFile == None):
        raise ValueError("You must supply a polymerLengthFile")
    f = open(polymerLengthFile)
    firstBeads = [1]
    for line in f:
        firstBeads.append(firstBeads[-1]+int(line))

    polymer = 0
    atomType = []
    for ind in index:
        while ind>=firstBeads[polymer+1]:
            polymer=polymer+1
        pp1 = polymer+1
        if pp1<10:
            atomType.append('  A'+str(pp1))
        elif pp1<100:
            atomType.append(' A'+str(pp1))
        elif pp1<1000:
            atomType.append('A'+str(pp1))
        else:
            raise ValueError('Too many colors')
    return atomType


def ColorCohesin(atomType,leftends,index):
    for ii in range(len(atomType)):
        if leftends[index[ii]] == 1:
            atomType[ii] = '  C1'

def drawConfinement(R, center, file_obj, Ntot, nboundary, nbeads):
    for N in range(0,nboundary):
         atomName='BLCK'
         x=center[0];
         y=center[1]+R*math.sin(2*3.141592*N/nboundary)
         z=center[2]+R*math.cos(2*3.141592*N/nboundary)
         Ntot=Ntot+1;
         print ('HETATM%5d %s %s          %8.3f%8.3f%8.3f  1.00  1.00           C'
               %(Ntot,atomName,resname,x,y,z),file=file_obj)
         if N != 0:
             print('CONECT%5d%5d'%(Ntot,Ntot-1),file=file_obj)

    print('CONECT%5d%5d'%(nbeads+1,Ntot),file=file_obj)
    return Ntot