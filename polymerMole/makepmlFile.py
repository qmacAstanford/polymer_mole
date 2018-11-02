import textwrap
import seaborn as sns
from polymerMole.glob import *
def makepmlFile(OutName="out.png", colorOption="H3K9me3",
                Ncolors=default_Ncolors, closePymol=True, ball_radius=0.085):
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
            myfile.write("alter "+name+", vdw="+str(ball_radius)+"\n")
            myfile.write("show sticks, "+name+"\n")
            myfile.write("set_bond stick_radius, 0.05,  "+name+"\n")
            myfile.write("hide lines, "+name+"\n")
            #myfile.write("set sphere_transparency, 0.20, "+name+"\n")
            myfile.write("set_bond stick_radius, 0.05, "+name+"\n")
            myfile.write("set_bond stick_radius, 0.05, "+name+", (name C1)\n")
            if n<Ncolors-1:
                myfile.write("set_bond stick_radius, 0.05, " + name +
                             ", (name A" + str(n+1) + ")\n")
            #myfile.write("set sphere_transparency=0.9, "+name+"\n")
            #myfile.write("set_bond stick_transparency, 0.90, "+name+"\n")
            myfile.write("\n\n")

        myfile.write(textwrap.dedent("""

        show spheres, (name C1)
        color black,(name C1)
        alter (name C1),vdw=0.15
        show sticks, (name C1)
        set_bond stick_radius, 0.05, (name C1)
        hide lines, (name C1)

        """))

    #Set view
    myfile.write(textwrap.dedent("""

    show (name BLCK)
    alter (name BLK),vdw=0.02
    color black, (name BLCK)
    show sticks, (name BLCK)
    set_bond stick_radius, 0.1, (name B4)

    # for chr 16 confinement
    set_view (\\
         0.000000000,    0.000000000,   -1.000000000,\\
         1.000000000,    0.000000000,   -0.000000000,\\
         0.000000000,   -1.000000000,   -0.000000000,\\
         0.000000000,    0.000000000, -186.786605835,\\
        28.395023346,   30.000000000,   32.000000000,\\
       -21.213415146,  415.786560059,  -20.000000000 )

    # for several chromosomes coarse grained
    set_view (\
         0.000000000,    0.000000000,   -1.000000000,\
         1.000000000,    0.000000000,   -0.000000000,\
         0.000000000,   -1.000000000,   -0.000000000,\
         0.000000522,   -0.000000611, -128.224334717,\
        28.395023346,   21.675159454,   21.032266617,\
       -79.775764465,  357.224304199,  -20.000000000 )

    """))
    if (closePymol):
        myfile.write("png "+OutName+", dpi = 100, width=1000, height=1000, ray=1\n")
        myfile.write("quit")
        myfile.close()

