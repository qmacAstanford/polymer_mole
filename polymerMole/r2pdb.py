import math
import numpy as np
from polymerMole.utils import *
from polymerMole.glob import *

def r2pdb(xyzFileName, nboundary=1000, skip=1, methFileName=None,
          bindFileName=None, Ncolors=default_Ncolors, xlimits=None,
          color_type="meth", color_cohisn=False, outFileName="temp.pdb",
          polymerLengthFile=None, circles = [(31.0,[32.0,32.0,32.0])],
          scalebar=None, cube=None, ylimits=None, zlimits=None, period=None,
          fractionType1 = None, maxpoints = None,
          **kwargs):

    """Convert xyzFileName into a pdb file ready for pymol.

    xyzFileName (str): Name of file with x y z coordinates.
    nboundary (int): Number of beads making up boundary.
    skip (int): Display every skip^th bead
    methFileName (str): Name of file to get methylation sequence from.
    bindFileName (str): Name of file to get cohesin sequence from.
    Ncolors (int): Number of colors.
    xlimits (list): Only display in range [lower,upper], e.g. [32, 36]
    ylimits (list): Similar to xlimits
    zlimits (list): Similar to xlimits
    colorType (str): One of "meth", "sequential", "meth10", or "polymer"
    color_cohisn (logical): Whether to color cohisin beads
    outFileName (str): Name of oubput pdb file
    polymerLengthFile (str): Name of file with lengths of polymers
    circles (lst): List of circles specified each specified by (R,[x,y,z])
    scalebar (float): Length of scalebar in simulation units.
    fractionType1 (float): Fraction of polymers to color as type A1
    maxpoints (int): maximum number of points to include
    """

    # ---------------------
    #    Read Meth file
    # --------------------
    if (methFileName != None and methFileName != xyzFileName):
        AllMeth=[]
        with open(methFileName) as f:
            for line in f:
                temp=line.split()
                methValue=int(temp[0])
                AllMeth.append(methValue)

    # ---------------------
    #   Read bindpairs
    # ---------------------
    if (bindFileName):
        bindpairs = np.loadtxt(bindFileName).astype(int)
        leftends = np.zeros(len(bindpairs))
        for ii in range(len(bindpairs)):
            if bindpairs[ii] == -1:
                continue
            if bindpairs[ii] > ii+1:
                leftends[ii] = 1


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
    if not period is None:
        period_list = []
    with open(xyzFileName) as f:
        for line in f:
            count=count+1
            if maxpoints is not None and count > maxpoints:
                break
            if count%skip != 0:
                if color_cohisn:
                    # make sure to include all cohsin
                    if leftends[count-1] == 0:
                        continue
                else:
                    continue
            temp=line.split()
            x=float(temp[0])
            y=float(temp[1])
            z=float(temp[2])
            #[x,y,z] = rotateZ(np.array([x,y,z]),-np.pi/4)
            #[x,y,z] = rotateX(np.array([x,y,z]),-np.pi/3)

            if (xlimits != None):
                if  x < xlimits[0]:
                    continue
                if x > xlimits[1]:
                    continue
            if (ylimits != None):
                if y < ylimits[0]:
                    continue
                if y > ylimits[1]:
                    continue
            if (zlimits != None):
                if z < zlimits[0]:
                    continue
                if z > zlimits[1]:
                    continue

            # Apply periodic boundary conditions
            if not period is None:
                period_temp = [0, 0, 0]
                r_temp = [x, y, z]
                for ii in range(3):
                    if period[ii] is not None:
                        period_temp[ii] = r_temp[ii]//period[ii]
                        r_temp[ii] = r_temp[ii]%period[ii]
                period_list.append(tuple(period_temp))
                x = r_temp[0]
                y = r_temp[1]
                z = r_temp[2]


            index.append(count)
            X.append(x)
            Y.append(y)
            Z.append(z)
            #AB.append(int(temp[3]))
            if not methFileName is None:
                if(methFileName == xyzFileName):
                    METH.append(int(temp[3]))
                else:
                    try:
                        METH.append(AllMeth[count-1])
                    except:
                        print("count -1")
                        print(count-1)
                        print(xyzFileName)
                        raise
    nbeads=len(X)

    # -------------------------
    #   Check for polymer ends
    # -------------------------
    if type(polymerLengthFile) == type(1):
        def same_polymer(i1, i2, origin=1):
            return (i1-origin) // polymerLengthFile == (i2-origin) // polymerLengthFile
    elif not polymerLengthFile is None:
        polyLengths = np.loadtxt(polymerLengthFile)
        starts = [sum(polyLengths[:ii]) for ii in range(len(polyLengths))]
        import bisect
        def same_polymer(i1, i2, origin=1):
            return bisect.bisect(starts,i1-origin) == bisect.bisect(starts,i2-origin)

    # -------------------------
    #  Set atom types
    # -------------------------
    if color_type == "meth":
        atomType = SetAtomTypesByMethylation(METH)
    elif color_type == "sequential":
        atomType = SetAtomTypeSequentially(nbeads,Ncolors)
    elif color_type == "polymer":
        atomType = SetAtomTypeByPolymer(polymerLengthFile,index)
    elif color_type == "meth10":
        atomType = SetAtomTypeVariableMethyaltionLevel(METH)
    elif color_type == "firstFraction":
        n1 = int(nbeads*fractionType1)
        while same_polymer(n1, n1-1, origin=0) and n1 > 0:
            n1 = n1-1
        atomType = SetAtomTypeTwoGroups(nbeads, n1)
    else:
        raise ValueError("Not an recognized color_type")

    if color_cohisn:
        ColorCohesin(atomType,leftends,index)


    # -------------------
    #  Write to pdb format
    # ---------------------
    file_obj = open(outFileName,mode='w')
    chemName='Leviathan!'
    if nbeads > 99999:
        raise 'too many beads for pdb format'

    if len(resname) != 3:
        raise 'resname must be 3 letters'
    print('HET    %s  A   1   %5d     Pseudo atom representation of DNA'
          %(resname,nbeads+nboundary),file=file_obj)
    print('HETNAM     %s %s'%(resname,chemName),file=file_obj)
    print('FORMUL  1   %s       '%(resname),file=file_obj)

    Ntot=0;
    for n in range(0, nbeads):
        atomName=atomType[n]
        if len(atomName) != 4:
            raise 'Atom name needs to be 4 characters'
        x=X[n]
        y=Y[n]
        z=Z[n]
        print('HETATM%5d %s %s          %8.3f%8.3f%8.3f  1.00  1.00           C'
                %(n+1,atomName,resname,x,y,z),file=file_obj)
        Ntot=Ntot+1;
        if n != 0:
            if not (index[n]==index[n-1]+skip):
                continue
            if period is not None:
                if period_list[n] != period_list[n-1]:
                    continue # beads in different periods
            if polymerLengthFile is not None:
                if not same_polymer(index[n], index[n-1]):
                    continue # don't connect seperate polymers
            print('CONECT%5d%5d'%(n, n+1),file=file_obj)


    # -----------------
    #  Draw confinement
    # -----------------
    if circles != None:
        for info in circles:
            Ntot = drawConfinement(info[0],info[1], file_obj, Ntot, nboundary, nbeads)

    if cube != None:
        Ntot = drawCube(cube[0], cube[1], file_obj, Ntot)

    # ----------------
    #   Draw scalebar
    # ----------------
    if (scalebar != None):
        x=0.0
        y=5.0
        z=5.0
        atomName='BLCK'
        Ntot=Ntot+1;
        print ('HETATM%5d %s %s          %8.3f%8.3f%8.3f  1.00  1.00           C'
              %(Ntot,atomName,resname,x,y,z),file=file_obj)
        #y=1000/28.7
        y=scalebar+y
        Ntot=Ntot+1;
        print ('HETATM%5d %s %s          %8.3f%8.3f%8.3f  1.00  1.00           C'
              %(Ntot,atomName,resname,x,y,z),file=file_obj)
        print('CONECT%5d%5d'%(Ntot-1,Ntot),file=file_obj)



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

