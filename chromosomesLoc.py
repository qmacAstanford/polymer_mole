from polymerMole.r2pdb import r2pdb
from polymerMole.makepmlFile import makepmlFile
import os
#baseNames = {'./exampleData/example1/':65}
#baseNames = {'./exampleData/example2/':100}
#baseNames = {'../../kb_khunLengthTests/c10_gl120_lamp15_chi1/':95,
#             '../../kb_khunLengthTests/c10_gl120_lamp15_chi3/':94,
#             '../../kb_khunLengthTests/c10_gl120_lamp5_chi1/':85,
#             '../../kb_khunLengthTests/c10_gl120_lamp15_chip5/':61}
#baseNames = {'../../kb_khunLengthTests/c10_gl120_lamp15_chi3/':94}
baseNames = {'../../kb_khunLengthTests/c10_gl120_lamp5_chi3/':110,
             '../../kb_khunLengthTests/c10_gl120_lamp15_chi3/':110}
baseNames = {'../../kb_khunLengthTests/c10_sep24_gl24_lamp5_chi6/':62,
             '../../kb_khunLengthTests/c10_sep24_gl24_lamp15_chi10/':54,
             '../../kb_khunLengthTests/c10_sep24_pro48_lamp15_chi6/':53,
             '../../kb_khunLengthTests/c10_sep24_pro48_lamp15_chi10/':55,
             '../../kb_khunLengthTests/c10_sep12_pro48_lamp15_chi6/':31}
baseNames = {'../../kb_khunLengthTests/c10_sep120_pro240_lamp5_chi16/':65,
             '../../kb_khunLengthTests/c10_sep60_pro240_lamp5_chi16/':39,
             '../../kb_khunLengthTests/c10_sep120_pro240_lamp5_chi32/':41}
baseNames = {'../../kb_khunLengthTests/c10_sep60_pro240_lamp2_chi64/':70,
             '../../kb_khunLengthTests/c10_sep60_pro240_lamp2_chi120/':70}
#baseNames = {'../../CT_box_lamp3/':27}
baseNames = {'../../CT_box/':110}
baseNames = {'../../CT_box_nobind/':110,
             '../../CT_box_nobind_lamp3/':110,
             '../../CT_box_lamp3/':110,
             '../../CT_box_lamp3_no_cohesin/':110,
             '../../CT_box_lamp15_no_cohesin/':110,
             '../../CT_box_lamp3_no_cohesin_nobind/':110,
             '../../CT_box_nolam_no_cohesin/':110}
baseNames = {'../../CT_box_nobind_lamp3/':110}
baseNames = {'../../FFibroblast_lamp3_no_cohesin/':110}
baseNames = {'../../FFb_lamp3_nocohesin_nobind_chr18/':110}
baseNames = {'../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd1/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd10/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd30/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd100/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd300/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd1000/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd1/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd10/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd30/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd100/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd300/':110,
             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd1000/':110}
baseNames = {'../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd1/':75,
             '../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd10/':75,
             '../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd30/':75,
             '../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd100/':75,
             '../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd300/':75,
             '../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd1000/':75}
baseNames = {'../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd300/':75}
baseNames = {'../../with_CTCFs/':12}
baseNames
for ii in range(1,17):
    baseNames = {'../../multi_with_CTCFs/with_CTCFs_mun1p0copy'+str(ii)+'/':20}
baseNames = {'../../multi_with_CTCFs/with_CTCFs_mun1p0copy1/':20}
baseNames = {'../../multi_with_CTCFs/without_LEFs/':20}
baseNames = {'../../with_CTCFs_no_initial_field/':26}
baseNames = {'../../with_CTCFs_no_initial_field/':24}
baseNames = {'../../with_CTCFs_no_initial_field2/':57}
baseNames = {'../../Tenkb_woCTCF/':55}
baseNames = {'../../Initial1/':0}
baseNames = {}
for cup in ['0p0001','0p1','0p2','0p4','0p8','1p6']:
    for chi in ['240','480','1000','2000']:
        baseNames['../../multiTenkb_woCTCF/Tenkb_woCTCF_2_cupn'+cup+'_chin'+chi+'/']=45
baseNames = {}
for cup in ['0p2', '0p4', '0p8']: # ['0p0001','0p1','0p2','0p4','0p8','1p6']:
    for chi in ['240', '480']: #['240','480','1000','2000']:
        baseNames['../../multiInitCond1/Initial1_cupn'+cup+'_chin'+chi+'/']=15

for baseName in baseNames.keys():
    savept_max = baseNames[baseName]
    for savept in [0,1,5,15]: #[savept_max]: #[2,3,4,7,8,9,12]: #[savept_max]: #[0,5,9]: #range(0,111,20): 
        recolor = False
        if recolor:
            methFile = "recolor100.txt"
        else:
            #methFile = baseName+"input/meth"
            methFile = baseName+"input/ab"
        
        for rep in [0]: #range(1,8): #range(2,10): #[2,4,6,7,8,9,10,11,12,14]:
            if True:
                suffix = "v"+str(rep)
            else:
                suffix = ""

            xyzFileName=baseName+"data/r"+str(savept)+suffix
            if baseName in ["../../multiTenkb_woCTCF/Tenkb_woCTCF_2_cupn0p0001_chin240/"]:
                continue
            skip = 3
            cube=None
            xlimits=None
            ylimits=None
            zlimits=None

            image = "Cube_full_CTCFs"
            image = "Cube_full"
            image = "EpiColor22"
            image = "chrom22"

            if (image=="chrom22"): #color polymers
                polymerLengthFile = baseName+"input/polyLengths"
                Ncolors = sum(1 for line in open(polymerLengthFile))
                color_type = "polymer"
                colorOption="Aseries"
                circles = [(15,[16.0,16.0,16.0])]
                xlimits=[16, 20]
                scalebar=500/100
                methFileName = None
                bindFileName = None
                color_cohisn = False
                color_palette="hls"
                ball_radius=0.07
                stick_radius=0.07
                view="chrom10"

            if (image == "EpiColor22"): #
                polymerLengthFile = baseName+"input/polyLengths"
                Ncolors = 50
                color_type = "meth10"
                colorOption="Aseries"
                circles = [(15,[16.0,16.0,16.0])]
                xlimits=[16, 20]
                scalebar=500/100
                methFileName = baseName+"input/ab"
                bindFileName = baseName+"input/bindpairs"
                color_cohisn = False
                color_palette="coolwarm"
                ball_radius=0.07
                stick_radius=0.07
                view="chrom10"

            if (image=="New"):
                skip=1
                Ncolors = None
                color_type = "meth"
                colorOption = "H3K9me3"
                circles = None
                xlimits = [0,15]
                scalebar = None
                methFileName = baseName+"input/meth"
                color_cohisn=False
                bindFileName=None
                color_palette=None
                ball_radius = 0.198
                stick_radius=0.05
                cube=[1,63]
                view="cube"
                polymerLengthFile = None
                ylimits = None


            if (image=="Cube"): # Cube
                skip=1
                Ncolors = None
                color_type = "meth"
                colorOption = "H3K9me3"
                circles = None
                xlimits = None
                scalebar = None
                methFileName = baseName+"input/meth"
                color_cohisn=False
                bindFileName=None
                color_palette=None
                ball_radius = 0.198
                stick_radius=0.05
                cube=[1,63]
                view="cube"
                polymerLengthFile = None
                ylimits = [20,28]

            if (image=="Cube_full"): # Cube
                skip=5
                Ncolors = None
                color_type = "meth"
                colorOption = "H3K9me3"
                circles = None
                xlimits = None
                scalebar = None
                methFileName = baseName+"input/meth"
                color_cohisn=False
                bindFileName=None
                color_palette=None
                ball_radius = 0.198
                stick_radius=0.05
                #cube=[1,63]
                cube=[0,64]
                view="cube"
                polymerLengthFile = None
                ylimits = None

            if (image=="Cube_full_CTCFs"): # Cube
                skip=5
                Ncolors = None
                color_type = "meth"
                colorOption = "H3K9me3"
                circles = None
                xlimits = None
                scalebar = None
                methFileName = baseName+"input/meth"
                color_cohisn=True
                bindFileName=baseName+"input/bindpairs"
                color_palette=None
                ball_radius = 0.198
                stick_radius=0.05
                cube=[1,63]
                view="cube"
                polymerLengthFile = None
                ylimits = None

            if (image=="PolyColor"): #color polymers
                polymerLengthFile = baseName+"input/polyLengths"
                Ncolors = sum(1 for line in open(polymerLengthFile))
                color_type = "polymer"
                colorOption="Aseries"
                circles = [(19.5,[20.5,20.5,20.5])]
                xlimits=[19.5,25.0]
                scalebar=500/100
                methFileName = None
                bindFileName = None
                color_cohisn = False
                color_palette="hls"
                ball_radius=0.07
                stick_radius=0.07
                view="chrom10"

            if (image == "EpiColor"): #
                Ncolors = 13
                color_type = "meth10"
                colorOption="Aseries"
                circles = [(19.5,[20.5,20.5,20.5])]
                xlimits=[19.5,25.0]
                scalebar=500/100
                methFileName = baseName+"input/ab"
                bindFileName = baseName+"input/bindpairs"
                color_cohisn = True
                color_palette="coolwarm"
                ball_radius=0.07
                stick_radius=0.07
                view="chrom10"
                polymerLengthFile = None

            if (image == "tri_color"):
                skip=1
                Ncolors = None
                color_type = "meth"
                colorOption = "H3K9me3"
                circles = [(31.0,[32.0,32.0,32.0])]
                xlimits=[32,36]
                scalebar=250/28.7
                methFileName = baseName+"input/meth"
                color_cohisn=False
                bindFileName=None
                color_palette=None
                ball_radius = 0.198
                stick_radius=0.05
                cube=None
                view="cube"
                polymerLengthFile = None

            r2pdb(xyzFileName, xlimits=xlimits, color_type=color_type,
                  polymerLengthFile=polymerLengthFile, circles=circles,
                  Ncolors=Ncolors, methFileName=methFileName,
                  scalebar=scalebar, bindFileName=bindFileName,
                  color_cohisn=color_cohisn, skip=skip, cube=cube,
                  ylimits=ylimits, zlimits=zlimits)


            if recolor:
                OutName = baseName+"data/"+image+str(savept)+suffix+".png"
            else:
                OutName = baseName+"data/"+image+str(savept)+suffix+".png"
            makepmlFile(OutName=OutName, colorOption=colorOption,
                        Ncolors=Ncolors, closePymol=True,
                        color_palette=color_palette, ball_radius=ball_radius,
                        stick_radius = stick_radius, view=view)

            os.system("pymol autoGen.pml")
        
