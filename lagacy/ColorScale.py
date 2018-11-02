import os
import textwrap
import seaborn as sns

Ncolors = 20
#colors = sns.color_palette("cubehelix", Ncolors)
colors = sns.color_palette("hls", Ncolors)

def makepmlFile(OutName="out.png"):
    myfile = open("autoGen.pml","w")
    myfile.write(textwrap.dedent("""
delete *
load temp.pdb,snap
set connect_mode,1

set_color low_H3K9me3, [0.5, 1.0, 0.917]
set_color med_H3K9me3, [0.808, 0.596, 0.145]
set_color high_H3K9me3, [0.417, 0.0, 0.5]

hide all
"""))
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
        #myfile.write("set_bon stick_transparancy, 0.90, "+name+"\n\n")

    myfile.write(textwrap.dedent("""

#show spheres, (name C1)
#color black,(name C1)
#alter (name C1),vdw=0.3
#show sticks, (name C1)
#set_bond stick_radius, 0.05, (name C1)
#hide lines, (name C1)

show (name B4)
color black, (name B4)
show sticks, (name B4)
set_bond stick_radius, 0.2, (name B4)

bg_color white

# for chr 16 confinement
set_view (\\
     0.000000000,    0.000000000,   -1.000000000,\\
     1.000000000,    0.000000000,   -0.000000000,\\
     0.000000000,   -1.000000000,   -0.000000000,\\
     0.000000000,    0.000000000, -186.786605835,\\
    28.395023346,   30.000000000,   32.000000000,\\
   -21.213415146,  415.786560059,  -20.000000000 )
        """))
    myfile.write("png "+OutName+", dpi = 100, width=1000, height=1000, ray=1\n") 
    myfile.write("quit") 
    myfile.close()



#baseNames ={'../kb_khunLengthTests/lamp15_chi1_cho1000_hp1pt_chrank200/':80,
#             '../kb_khunLengthTests/lamp05_chi1_cho1000_hp1pt_chrank200/':69,
#             '../kb_khunLengthTests/lamp15_chi1_cho0_hp1pt_chrank200/':100,
#             '../kb_khunLengthTests/lam0_chi1_cho1000_hp1pt_chrank200/':78}
#baseNames ={'../kb_khunLengthTests/lamp15_chi1_cho0_hp1pt_chrank200/':100}
#baseNames ={'../kb_khunLengthTests/lamp3_chi1_cho0_hp1pt/':110,
#            '../kb_khunLengthTests/lamp3_chi1_cho10000_hp1pt/':110,
#            '../kb_khunLengthTests/lamp3_chi1_cho1000_hp1pt_crank200/':110}\
baseNames ={'../kb_khunLengthTests/lamp15_chi1_cho1000_hp1pt_lg002/':110,
            '../kb_khunLengthTests/lamp15_chi1_cho1000_hp1pt_lg005/':54,
            '../kb_khunLengthTests/lam0_chi1_cho1000_hp1pt_lg005/':68}

for baseName in baseNames.keys():
    savept = baseNames[baseName]
    for savept in [savept]: #range(0,111,20): 
        recolor = False
        
        for rep in [1,2,3,4,5,6,7,8,9]: #[2,4,6,7,8,9,10,11,12,14]:
            cmd = "python r2pdbColorScale.py " + baseName+"data/r" + \
                  str(savept) + "v" + str(rep) + " " + \
                  baseName + "input/bindpairs " + str(Ncolors) + " > temp.pdb"
            print(cmd)
            os.system(cmd)
            makepmlFile(baseName+"data/color"+str(savept)+"v"+str(rep)+".png")
            os.system("pymol autoGen.pml")
        
        
