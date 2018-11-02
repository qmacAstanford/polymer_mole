import math
import numpy as np
from polymerMole.utils import *
from polymerMole.glob import *

def r2pdb(xyzFileName, nboundary=1000, skip=1, methFileName=None,
          bindFileName=None, Ncolors=default_Ncolors, xlimits=None,
          color_type="meth", color_cohisn=False, outFileName="temp.pdb",
          polymerLengthFile=None, circles = [(31.0,[32.0,32.0,32.0])],
          scalebar=None ):
    
    """Convert xyzFileName into a pdb file ready for pymol.

    xyzFileName (str): Name of file with x y z coordinates.
    nboundary (int): Number of beads making up boundary.
    skip (int): Display every skip^th bead
    methFileName (str): Name of file to get methylation sequence from.
    bindFileName (str): Name of file to get cohesin sequence from.
    Ncolors (int): Number of colors.
    xlimits (list): Only display in range [lower,upper], e.g. [32, 36]
    colorType (str): One of "meth", "sequential", or "polymer"
    color_cohisn (logical): Whether to color cohisin beads
    outFileName (str): Name of oubput pdb file
    polymerLengthFile (str): Name of file with lengths of polymers
    circles (lst): List of circles specified each specified by (R,[x,y,z])
    scalebar (real): Length of scalebar in simulation units.
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
        bindpairs = np.loadtxt(fnameBind).astype(int)
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
    skip=5
    with open(xyzFileName) as f:
        for line in f:
            count=count+1
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
            #[x,y,z] = rotateZ(np.array([x,y,z]),-np.pi/4+np.pi/2)
            #[x,y,z] = rotateX(np.array([x,y,z]),-np.pi/3)

            if (xlimits != None):
                if  x < xlimits[0]:
                    continue

                if x > xlimits[1]:
                    continue

            index.append(count)
            X.append(x)
            Y.append(y)
            Z.append(z)
            #AB.append(int(temp[3]))
            if (methFileName != None):
                if(methFileName != methFileName):
                    METH.append(temp[4])
                else:
                    METH.append(AllMeth[count-1])
    nbeads=len(X)

    # -------------------------
    #  Set atom types
    # -------------------------
    if color_type == "meth":
        atomType = SetAtomTypesByMethylation(METH)
    elif color_type == "sequential":
        atomType = SetAtomTypeSequentially(nbeads,Ncolors)
    elif color_type == "polymer":
        atomType = SetAtomTypeByPolymer(polymerLengthFile,index)
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
        if n != 0:
            if (index[n]==index[n-1]+skip):
                print('CONECT%5d%5d'%(n, n+1),file=file_obj)
        Ntot=Ntot+1;


    # -----------------
    #  Draw confinement
    # -----------------
    for info in circles:
        Ntot = drawConfinement(info[0],info[1], file_obj, Ntot, nboundary, nbeads)


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


def makepmlFile(OutName="out.png", colorOption="H3K9me3",
                Ncolors=default_Ncolors, closePymol=True):
    """ Make a pml comand file for pymol and run pymol to generate a png.

    Args:
        OutName (str): Output file name
        clorOptions (str): One of "H3K9me3", "Aseries"
        Ncolors (int): Nuber of colors
    """
    myfile = open("autoGen.pml","w")
    # General Head lines
    myfile.write(textwrap.dedent("""
    delete *
    load temp.pdb,snap
    set connect_mode,1

    hide all
    bg_color white
    """))
    if (colorOption=="H3K9me3"):
        myfile.write(textwrap.dedent("""
        set_color low_H3K9me3, [0.5, 1.0, 0.917]
        set_color med_H3K9me3, [0.808, 0.596, 0.145]
        set_color high_H3K9me3, [0.417, 0.0, 0.5]

        show spheres, (name A5)
        color red,(name A5)
        alter (name A1),vdw=0.75

        show spheres, (name A1)
        color low_H3K9me3,(name A1)
        alter (name A1),vdw=0.174
        show sticks, (name A1)
        set_bond stick_radius, 0.05, (name A1)
        hide lines, (name A1)

        show spheres, (name A2)
        color med_H3K9me3,(name A2)
        alter (name A2),vdw=0.178
        show sticks, (name A2)
        set_bond stick_radius, 0.05, (name A2)
        hide lines, (name A2)

        show spheres, (name A3)
        color high_H3K9me3,(name A3)
        alter (name A3),vdw=0.178
        show sticks, (name A3)
        set_bond stick_radius, 0.05, (name A3)
        hide lines, (name A3)

        set_bond stick_radius, 0.05, (name A2), (name A1)
        set_bond stick_radius, 0.05, (name A2), (name A3)
        set_bond stick_radius, 0.05, (name A3), (name A1)

        show (name BLCK)
        color black, (name BLCK)
        show sticks, (name BLCK)
        set_bond stick_radius, 0.2, (name BLCK)
        """))
    elif(colorOption=="Aseries"):
        # Choose from seaborn color palette
        #colors = sns.color_palette("cubehelix", Ncolors)
        colors = sns.color_palette("hls", Ncolors)
        for n in range(Ncolors):
            color = "["+ str(colors[n][0]) + ", " + str(colors[n][1]) + ", " +\
            str(colors[n][2]) + "] "
            color_name = "col"+str(n)
            name ="(name A"+str(n)+")"
            myfile.write("show spheres, "+name+"\n")
            myfile.write("set_color "+color_name+", "+color+"\n")
            myfile.write("color "+color_name+", "+name+"\n")
            myfile.write("alter "+name+", vdw=0.174"+"\n")
            myfile.write("show sticks, "+name+"\n")
            myfile.write("set_bond stick_radius, 0.05,  "+name+"\n")
            myfile.write("hide lines, "+name+"\n")
            #myfile.write("set sphere_transparency, 0.20, "+name+"\n")
            myfile.write("set_bond stick_radius, 0.05, "+name+"\n")
            myfile.write("set_bond stick_radius, 0.05, "+name+", (name C1)\n")
            if n<Ncolors-1:
                myfile.write("set_bond stick_radius, 0.05, " + name +
                             ", (name A" + str(n+1) + ")\n")
            #myfile.write("set_bond stick_transparancy, 0.90, "+name)
            myfile.write("\n\n")

        myfile.write(textwrap.dedent("""

        #show spheres, (name C1)
        #color black,(name C1)
        #alter (name C1),vdw=0.3
        #show sticks, (name C1)
        #set_bond stick_radius, 0.05, (name C1)
        #hide lines, (name C1)

        show (name BLCK)
        color black, (name BLCK)
        show sticks, (name BLCK)
        set_bond stick_radius, 0.2, (name B4)
        """))

    #Set view
    myfile.write(textwrap.dedent("""
    # for chr 16 confinement
    set_view (\\
         0.000000000,    0.000000000,   -1.000000000,\\
         1.000000000,    0.000000000,   -0.000000000,\\
         0.000000000,   -1.000000000,   -0.000000000,\\
         0.000000000,    0.000000000, -186.786605835,\\
        28.395023346,   30.000000000,   32.000000000,\\
       -21.213415146,  415.786560059,  -20.000000000 )
    """))
    if (closePymol):
        myfile.write("png "+OutName+", dpi = 100, width=1000, height=1000, ray=1\n")
        myfile.write("quit")
        myfile.close()

