import os
import textwrap

def makepmlFile(OutName="out.png"):
    file = open("autoGen.pml","w")
    file.write(textwrap.dedent("""
delete *
load temp.pdb,snap
set connect_mode,1

set_color low_H3K9me3, [0.5, 1.0, 0.917]
set_color med_H3K9me3, [0.808, 0.596, 0.145]
set_color high_H3K9me3, [0.417, 0.0, 0.5]

hide all
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

show (name A4)
color black, (name A4)
show sticks, (name A4)
set_bond stick_radius, 0.2, (name A4)

bg_color white

# for chr 16 confinement
#set_view (\\
#     0.000000000,    0.000000000,   -1.000000000,\\
#     1.000000000,    0.000000000,   -0.000000000,\\
#     0.000000000,   -1.000000000,   -0.000000000,\\
#     0.000000000,    0.000000000, -186.786605835,\\
#    28.395023346,   30.000000000,   32.000000000,\\
#   -21.213415146,  415.786560059,  -20.000000000 )

# for no confinement
set_view (\
     0.000000000,    0.000000000,   -1.000000000,\
     1.000000000,    0.000000000,   -0.000000000,\
     0.000000000,   -1.000000000,   -0.000000000,\
     0.000000000,    0.000000000, -222.804641724,\
    28.395023346,   30.000000000,   32.000000000,\
    14.804654121,  451.804748535,  -20.000000000 )

        """))
    file.write("png "+OutName+", dpi = 100, width=2200, height=2200, ray=1\n") 
    file.write("quit") 
    file.close()


#baseNames = {'../kb_khunLengthTests/lamp3_chi1_cho10000_hp1pt/':43}

#baseNames ={'../kb_khunLengthTests/lamp15_chi1_cho1000_hp1pt_chrank200/':80,
#             '../kb_khunLengthTests/lamp05_chi1_cho1000_hp1pt_chrank200/':69,
#             '../kb_khunLengthTests/lamp15_chi1_cho0_hp1pt_chrank200/':100,
#             '../kb_khunLengthTests/lam0_chi1_cho1000_hp1pt_chrank200/':78}
#baseNames ={'../kb_khunLengthTests/lamp3_chi1_cho0_hp1pt/':110,
#            '../kb_khunLengthTests/lamp3_chi1_cho10000_hp1pt/':110,
#            '../kb_khunLengthTests/lamp3_chi1_cho1000_hp1pt_crank200/':110}

#baseNames ={'../kb_khunLengthTests/lamp15_chi1_cho1000_hp1pt_lg002/':110,
#            '../kb_khunLengthTests/lamp15_chi1_cho1000_hp1pt_lg005/':54,
#baseNames ={'../kb_khunLengthTests/lam0_chi1_cho1000_hp1pt_lg005/':68}
#baseNames ={'../../../sarah16/reampsims/paper/het_eu_sim/gen1_prespread/':60}
baseNames = {'../kb_khunLengthTests/c10_gl120_lamp15_chi1/':110,
             '../kb_khunLengthTests/c10_gl120_lamp5_chi1/':92,
             '../kb_khunLengthTests/c10_gl120_lam0_chi1/':77,
             '../kb_khunLengthTests/c10_gl120_lamp15_chi3/':36}

for baseName in baseNames.keys():
    savept_max = baseNames[baseName]
    for savept in [savept_max]: #[0,5,9]: #range(0,111,20): 
        recolor = False
        if recolor:
            methFile = "recolor100.txt"
        else:
            methFile = baseName+"input/meth"
        
        for rep in range(1,15): #range(2,10): #[2,4,6,7,8,9,10,11,12,14]:
            if True:
                suffix = "v"+str(rep)
            else:
                suffix = ""
            
            cmd = "python r2pdbChrom.py "+baseName+"data/r"+str(savept)+suffix\
                  +" "+methFile+"> temp.pdb"
            print(cmd)
            os.system(cmd)


            if recolor:
                makepmlFile(baseName+"data/snap_recolor"+str(savept)+suffix+".png")
            else:
                makepmlFile(baseName+"data/snap"+str(savept)+suffix+".png")
                #makepmlFile("snap"+str(savept)+suffix+".png")
            os.system("pymol autoGen.pml")
        
