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
baseNames = {'../../Tenkb_woCTCF/':55}
baseNames = {'../../Initial1/':0}
baseNames = {}
for cup in ['0p0001','0p1','0p2','0p4','0p8','1p6']:
    for chi in ['240','480','1000','2000']:
        baseNames['../../multiTenkb_woCTCF/Tenkb_woCTCF_2_cupn'+cup+'_chin'+chi+'/']=45
baseNames = {}
for cup in ['0p0001','0p1','0p2','0p4','0p8','1p6']:
    for chi in ['240','480','1000','2000']:
        baseNames['../../multiInitCond1/Initial1_cupn'+cup+'_chin'+chi+'/']=75
baseNames = {'../../multiInitCond1/Initial1_cupn0p4_chin480/':75}
baseNames = {'../../with_CTCFs_no_initial_field2/':59}


kwargs ={}

for baseName in baseNames.keys():
    savept_max = baseNames[baseName]
    for savept in [0,1,10,59]: #[savept_max]: #[2,3,4,7,8,9,12]: #[savept_max]: #[0,5,9]: #range(0,111,20):

        for rep in [10, 11]: #range(1,8): #range(2,10): #[2,4,6,7,8,9,10,11,12,14]:
            if True:
                suffix = "v"+str(rep)
            else:
                suffix = ""

            xyzFileName=baseName+"data/r"+str(savept)+suffix
            if baseName in ["../../multiTenkb_woCTCF/Tenkb_woCTCF_2_cupn0p0001_chin240/"]:
                continue
            kwargs['skip'] = 3

            kwargs['closePymol']=True
            image = "Cube_full_CTCFs"
            image = "chrom22"
            image = "EpiColor22"
            image = "Cube_full"

            if (image=="CTCFs_in_sphere"):
                kwargs['skip']=5
                kwargs['Ncolors'] = None
                kwargs['color_type'] = "meth"
                kwargs['colorOption'] = "H3K9me3"
                kwargs['circles'] = [(31,[32.0,32.0,32.0])]
                kwargs['xlimits'] = None
                #kwargs['scalebar'] = None
                kwargs['methFileName'] = baseName+"input/meth"
                kwargs['color_cohisn']=True
                kwargs['bindFileName']=baseName+"input/bindpairs"
                kwargs['color_palette']=None
                kwargs['ball_radius'] = 0.198
                kwargs['stick_radius']=0.05
                #kwargs['cube']=[1,63]
                kwargs['view']="cube"
                kwargs['polymerLengthFile'] = None
                kwargs['ylimits'] = None



            if (image=="chrom22"): #color polymers
                kwargs['polymerLengthFile'] = baseName+"input/polyLengths"
                kwargs['Ncolors'] = sum(1 for line in
                                        open(kwargs['polymerLengthFile']))
                kwargs['color_type'] = "polymer"
                kwargs['colorOption']="Aseries"
                kwargs['circles'] = [(15,[16.0,16.0,16.0])]
                kwargs['xlimits']=[16, 20]
                #kwargs['scalebar']=500/100
                kwargs['methFileName'] = None
                kwargs['bindFileName'] = None
                kwargs['color_cohisn'] = False
                kwargs['color_palette']="hls"
                kwargs['ball_radius']=0.07
                kwargs['stick_radius']=0.07
                kwargs['view']="chrom22"
                kwargs['highlightPolymers'] = [1, 15, 18]

            if (image == "EpiColor22"): #
                kwargs['polymerLengthFile'] = baseName+"input/polyLengths"
                kwargs['Ncolors'] = 50
                kwargs['color_type'] = "meth10"
                kwargs['colorOption']="Aseries"
                kwargs['circles'] = [(15,[16.0,16.0,16.0])]
                kwargs['xlimits']=[16, 20]
                #kwargs['scalebar']=500/100
                kwargs['methFileName'] = baseName+"input/ab"
                kwargs['bindFileName'] = baseName+"input/bindpairs"
                kwargs['color_cohisn'] = False
                kwargs['color_palette']="coolwarm"
                kwargs['ball_radius']=0.07
                kwargs['stick_radius']=0.07
                kwargs['view']="chrom22"

            if (image=="New"):
                kwargs['skip']=1
                kwargs['Ncolors'] = None
                kwargs['color_type'] = "meth"
                kwargs['colorOption']= "H3K9me3"
                kwargs['circles'] = None
                kwargs['xlimits'] = [0,15]
                kwargs['scalebar'] = None
                kwargs['methFileName'] = baseName+"input/meth"
                kwargs['color_cohisn']=False
                kwargs['bindFileName']=None
                kwargs['color_palette']=None
                kwargs['ball_radius'] = 0.198
                kwargs['stick_radius']=0.05
                kwargs['cube']=[1,63]
                kwargs['view']="cube"
                kwargs['polymerLengthFile'] = None
                kwargs['ylimits'] = None


            if (image=="Cube"): # Cube
                kwargs['skip']=1
                kwargs['Ncolors'] = None
                kwargs['color_type'] = "meth"
                kwargs['colorOption'] = "H3K9me3"
                kwargs['circles'] = None
                kwargs['xlimits'] = None
                kwargs['scalebar'] = None
                kwargs['methFileName'] = baseName+"input/meth"
                kwargs['color_cohisn']=False
                kwargs['bindFileName']=None
                kwargs['color_palette']=None
                kwargs['ball_radius'] = 0.198
                kwargs['stick_radius']=0.05
                kwargs['cube']=[1,63]
                kwargs['view']="cube"
                kwargs['polymerLengthFile'] = None
                kwargs['ylimits'] = [20,28]

            if (image=="Cube_full"): # Cube
                kwargs['skip']=5
                kwargs['Ncolors'] = None
                kwargs['color_type'] = "meth"
                kwargs['colorOption'] = "H3K9me3"
                kwargs['circles'] = None
                kwargs['xlimits'] = None
                kwargs['scalebar'] = None
                kwargs['methFileName'] = baseName+"input/meth"
                kwargs['color_cohisn']=False
                kwargs['bindFileName']=None
                kwargs['color_palette']=None
                kwargs['ball_radius'] = 0.198
                kwargs['stick_radius']=0.05
                #cube=[1,63]
                kwargs['cube']=[0,64]
                kwargs['view']="cube"
                kwargs['polymerLengthFile'] = None
                kwargs['ylimits'] = None

            if (image=="Cube_full_CTCFs"): # Cube
                kwargs['skip']=5
                kwargs['Ncolors'] = None
                kwargs['color_type'] = "meth"
                kwargs['colorOption'] = "H3K9me3"
                kwargs['circles'] = None
                kwargs['xlimits'] = None
                kwargs['scalebar'] = None
                kwargs['methFileName'] = baseName+"input/meth"
                kwargs['color_cohisn']=True
                kwargs['bindFileName']=baseName+"input/bindpairs"
                kwargs['color_palette']=None
                kwargs['ball_radius'] = 0.198
                kwargs['stick_radius']=0.05
                kwargs['cube']=[1,63]
                kwargs['view']="cube"
                kwargs['polymerLengthFile'] = None
                kwargs['ylimits'] = None

            if (image=="PolyColor"): #color polymers
                kwargs['polymerLengthFile'] = baseName+"input/polyLengths"
                kwargs['Ncolors'] = sum(1 for line in open(polymerLengthFile))
                kwargs['color_type'] = "polymer"
                kwargs['colorOption']="Aseries"
                kwargs['circles'] = [(19.5,[20.5,20.5,20.5])]
                kwargs['xlimits']=[19.5,25.0]
                kwargs['scalebar']=500/100
                kwargs['methFileName'] = None
                kwargs['bindFileName'] = None
                kwargs['color_cohisn'] = False
                kwargs['color_palette']="hls"
                kwargs['ball_radius']=0.07
                kwargs['stick_radius']=0.07
                kwargs['view']="chrom10"

            if (image == "EpiColor"): #
                kwargs['Ncolors'] = 13
                kwargs['color_type'] = "meth10"
                kwargs['colorOption']="Aseries"
                kwargs['circles'] = [(19.5,[20.5,20.5,20.5])]
                kwargs['xlimits']=[19.5,25.0]
                kwargs['scalebar']=500/100
                kwargs['methFileName'] = baseName+"input/ab"
                kwargs['bindFileName'] = baseName+"input/bindpairs"
                kwargs['color_cohisn'] = True
                kwargs['color_palette']="coolwarm"
                kwargs['ball_radius']=0.07
                kwargs['stick_radius']=0.07
                kwargs['view']="chrom10"
                kwargs['polymerLengthFile'] = None

            if (image == "tri_color"):
                kwargs['skip']=1
                kwargs['Ncolors'] = None
                kwargs['color_type'] = "meth"
                kwargs['colorOption'] = "H3K9me3"
                kwargs['circles'] = [(31.0,[32.0,32.0,32.0])]
                kwargs['xlimits']=[32,36]
                kwargs['scalebar']=250/28.7
                kwargs['methFileName'] = baseName+"input/meth"
                kwargs['color_cohisn']=False
                kwargs['bindFileName']=None
                kwargs['color_palette']=None
                kwargs['ball_radius'] = 0.198
                kwargs['stick_radius']=0.05
                kwargs['cube']=None
                kwargs['view']="cube"
                kwargs['polymerLengthFile'] = None

            r2pdb(xyzFileName, **kwargs)


            recolor = False
            if recolor:
                kwargs['OutName'] = baseName+"data/"+image+str(savept)+suffix+".png"
            else:
                kwargs['OutName'] = baseName+"data/"+image+str(savept)+suffix+".png"
            makepmlFile(**kwargs)

            os.system("pymol autoGen.pml")

