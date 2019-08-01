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
#baseNames = {'../../kb_khunLengthTests/c10_gl120_lamp5_chi3/':110,
#             '../../kb_khunLengthTests/c10_gl120_lamp15_chi3/':110}
#baseNames = {'../../kb_khunLengthTests/c10_sep24_gl24_lamp5_chi6/':62,
#             '../../kb_khunLengthTests/c10_sep24_gl24_lamp15_chi10/':54,
#             '../../kb_khunLengthTests/c10_sep24_pro48_lamp15_chi6/':53,
#             '../../kb_khunLengthTests/c10_sep24_pro48_lamp15_chi10/':55,
#             '../../kb_khunLengthTests/c10_sep12_pro48_lamp15_chi6/':31}
#baseNames = {'../../kb_khunLengthTests/c10_sep120_pro240_lamp5_chi16/':65,
#             '../../kb_khunLengthTests/c10_sep60_pro240_lamp5_chi16/':39,
#             '../../kb_khunLengthTests/c10_sep120_pro240_lamp5_chi32/':41}
#baseNames = {'../../kb_khunLengthTests/c10_sep60_pro240_lamp2_chi64/':70,
#             '../../kb_khunLengthTests/c10_sep60_pro240_lamp2_chi120/':70}
#baseNames = {'../../CT_box_lamp3/':27}
#baseNames = {'../../CT_box/':110}
#baseNames = {'../../CT_box_nobind/':110,
#             '../../CT_box_nobind_lamp3/':110,
#             '../../CT_box_lamp3/':110,
#             '../../CT_box_lamp3_no_cohesin/':110,
#             '../../CT_box_lamp15_no_cohesin/':110,
#             '../../CT_box_lamp3_no_cohesin_nobind/':110,
#             '../../CT_box_nolam_no_cohesin/':110}
#baseNames = {'../../CT_box_nobind_lamp3/':110}
#baseNames = {'../../FFibroblast_lamp3_no_cohesin/':110}
#baseNames = {'../../FFb_lamp3_nocohesin_nobind_chr18/':110}
#baseNames = {'../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd1/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd10/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd30/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd100/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd300/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun1p375_nbnd1000/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd1/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd10/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd30/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd100/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd300/':110,
#             '../../randomBinding/FFb_nocohesin_chr18_mun0p78571_nbnd1000/':110}
#baseNames = {'../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd1/':75,
#             '../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd10/':75,
#             '../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd30/':75,
#             '../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd100/':75,
#             '../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd300/':75,
#             '../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd1000/':75}
#baseNames = {'../../randomBinding/FFb_nocohesin_chr18_mun1p0_nbnd300/':75}
#baseNames = {'../../with_CTCFs/':12}
#baseNames
#for ii in range(1,17):
#    baseNames = {'../../multi_with_CTCFs/with_CTCFs_mun1p0copy'+str(ii)+'/':20}
#baseNames = {'../../multi_with_CTCFs/with_CTCFs_mun1p0copy1/':20}
#baseNames = {'../../multi_with_CTCFs/without_LEFs/':110}
#baseNames = {'../../with_CTCFs_no_initial_field/':26}
#baseNames = {'../../with_CTCFs_no_initial_field/':24}
#baseNames = {'../../Tenkb_woCTCF/':55}
#baseNames = {'../../Initial1/':0}
#baseNames = {}
#for cup in ['0p0001','0p1','0p2','0p4','0p8','1p6']:
#    for chi in ['240','480','1000','2000']:
#        baseNames['../../multiTenkb_woCTCF/Tenkb_woCTCF_2_cupn'+cup+'_chin'+chi+'/']=45
#baseNames = {}
#for cup in ['0p0001','0p1','0p2','0p4','0p8','1p6']:
#    for chi in ['240','480','1000','2000']:
#        baseNames['../../multiInitCond1/Initial1_cupn'+cup+'_chin'+chi+'/']=75
#baseNames = {'../../multiInitCond1/Initial1_cupn0p4_chin480/':75}
#baseNames = {'../../with_CTCFs_no_initial_field2/':59}
#baseNames = {}
#for mu in ['1p0','1p3']:
#    for rang in ['0p1','0p5','1p0']:
#        for strength in ['0p03','0p1','0p3']:
#            direct = '../../multi_attach_strength/w_CTCFs_nif_ensemble_GM12878_mun'+mu+'_range'+rang+'_strength'+strength+'/'
#            if not os.path.isdir(direct):
#                continue
#            baseNames[direct] = \
#                    len(open(direct+'data/energiesv0').readlines())-2
#baseNames = {}
#for mu in ['1p0','1p3']:
#    for bpl in ['150','600','2400']:
#        for pros in ['150','600','2400']:
#            direct = '../../multi_LEF_params/CTCFs_GM12878_mun'+mu+'_bpl'+bpl+'_pros'+pros+'/'
#            if not os.path.isdir(direct):
#                continue
#            baseNames[direct] = \
#                    len(open(direct+'data/energiesv0').readlines())-2
#baseNames = {'../../align3/':14}
#baseNames = {'../../alignStrong/':13}
#baseNames = {'../../align4/':49}
#
def stringify(my_float):
    string = str(my_float)
    string = string.replace("e-","En")
    string = string.replace("e+","E")
    string = string.replace("-","n")
    string = string.replace(".","p")
    return string
#baseNames = {}
#origional = "../../multi_w_CTCFs_boudaryAttach_GM1287TCFs_boundaryAttach_GM12878"
#for mu in [-1.0]:
#    for n_bind_points in [75, 100, 150, 300]:
#        for copy in [1,2,3,4]:
#            direct = origional +"_mu"+ stringify(mu) + "_nbind" + \
#                      stringify(n_bind_points) + "_copy" + stringify(copy) + "/"
#            if not os.path.isdir(direct):
#                continue
#            baseNames[direct] = \
#                    len(open(direct+'data/energiesv0').readlines())-2
#baseNames =\
#        {'../../multi_w_CTCFs_boudaryAttach_GM12878/CTCFs_boundaryAttach_GM12878_mun1p0_nbind150_copy1/':101}
#baseNames =\
#{'../../multi_attach_strength/w_CTCFs_nif_ensemble_GM12878_mun1p0_range1p0_strength0p3/':110}
#baseNames = {}
#origional = "../../multi_start_order/w_CTCF_GM12878_"
#for start_times in [[11,15], [15,11], [11,11]]:
#    chiOn = start_times[0]
#    extOn = start_times[1]
#    for copy in ['1', '2', '3']:
#        for lam_strength in [0.3, 0.1]:
#            direct = origional + "_strength" + stringify(lam_strength) \
#                    + "_chiOn" + stringify(chiOn)\
#                    + "_extOn" + stringify(extOn)\
#                    + "copy" + copy + "/"
#            if not os.path.isdir(direct):
#                continue
#            baseNames[direct] = \
#                    len(open(direct+'data/energiesv0').readlines())-2
#
#baseNames = {}
#origional = "../../multi_break_polymer_GM12878/CTCFs_boundaryAttach_GM12878_2"
#mu=-1.0
#for copy in [1,2]:
#    for nbind in [150, 300]:
#        for NB in [100, 300]:
#            NP = int(390300//NB)
#            direct = origional + "_mu" + stringify(mu) \
#                      + "_nbind" + stringify(nbind) \
#                     + "_NB" + stringify(NB) \
#                     + "_copy" + stringify(copy) + "/"
#            if not os.path.isdir(direct):
#                continue
#            baseNames[direct] = \
#                    len(open(direct+'data/energies').readlines())-2
#mu=-1.2
#for copy in [1,2]:
#    for nbind in [150, 300]:
#        for NB in [100, 300]:
#            NP = int(390300//NB)
#            direct = origional + "_mu" + stringify(mu) \
#                      + "_nbind" + stringify(nbind) \
#                     + "_NB" + stringify(NB) \
#                     + "_copy" + stringify(copy) + "/"
#            if not os.path.isdir(direct):
#                continue
#            baseNames[direct] = \
#                    len(open(direct+'data/energies').readlines())-2
#baseNames = {'../../../../rk22/wlcsim/':1000}
#baseNames = \
#{'../../multi_start_order/w_CTCF_GM12878__strength0p3_chiOn15_extOn11copy1/':110}
#baseNames = {}
#origional = "../../no_LEFs/wo_CTCFs_nif_ensemble_GM12878"
#for mu in [-1.0, -1.3, -1.5, -0.8]:
#    for copy in [1, 2]:
#        direct = origional + "_mu" + stringify(mu) \
#                  + "_copy" + stringify(copy) + "/"
#        if not os.path.isdir(direct):
#            continue
#        baseNames[direct] = \
#                len(open(direct+'data/energies').readlines())-2
#baseNames = {"../../../../rk22/verylongTwist070919/":0}
baseNames = {'../../../../rk22/run1Twist0/':1000}
kwargs ={}
import os
for baseName in baseNames.keys():
    savept_max = baseNames[baseName]
    for savept in [savept_max]: #[2,3,4,7,8,9,12]: #[savept_max]: #[0,5,9]: #range(0,111,20):

        for rep in [0]: #range(1,16): #range(1,8): #range(2,10): #[2,4,6,7,8,9,10,11,12,14]:
            if True:
                suffix = "v"+str(rep)
            else:
                suffix = ""

            xyzFileName=baseName+"data/r"+str(savept)+suffix
            if baseName in ["../../multiTenkb_woCTCF/Tenkb_woCTCF_2_cupn0p0001_chin240/"]:
                continue
            kwargs['skip'] = 1

            kwargs['closePymol']=False
            image = "Cube_full_CTCFs"
            image = "chrom22"
            image = "EpiColor22"
            image = "Cube_full"
            image = "Luke"
            image = "bind2boundary"
            image = "Cube_recolor"
            image = "Cube"
            image = "single_polymer"

            if (image=="single_polymer"):
                kwargs['skip']=1
                kwargs['Ncolors'] = 10
                kwargs['color_type'] = "sequential"
                kwargs['colorOption'] = "Aseries"
                kwargs['maxpoints'] = 99999
                kwargs['circles'] = None
                kwargs['xlimits'] = None
                kwargs['ylimits'] = None
                kwargs['zlimits'] = None
                kwargs['scalebar'] = None
                kwargs['methFileName'] = None
                kwargs['color_cohisn']=False
                kwargs['bindFileName']=None
                kwargs['color_palette']=None
                kwargs['ball_radius'] = 2.0
                kwargs['stick_radius']=1.0
                kwargs['view']="Luke"
                kwargs['polymerLengthFile'] = None
                kwargs['recenter'] = True
                kwargs['ring'] = True

            if (image == "bind2boundary"):
                kwargs['skip']=1
                kwargs['Ncolors'] = None
                kwargs['color_type'] = "meth"
                kwargs['colorOption'] = "H3K9me3"
                kwargs['circles'] = None
                kwargs['scalebar']=100/28.7
                kwargs['methFileName'] = baseName+"input/meth"
                kwargs['color_cohisn']=False
                kwargs['bindFileName']=None
                kwargs['color_palette']=None
                kwargs['ball_radius'] = 0.198
                kwargs['stick_radius']=0.05
                kwargs['polymerLengthFile'] = None
                kwargs['highlight_file'] = baseName+"data/bind_points"
                kwargs['ylimits'] = [26,38]
                zoom = False
                if zoom:
                    kwargs['xlimits'] = [0,15]
                    kwargs['zlimits'] = [16,31]
                    kwargs['view']="zoom_boundary"
                    kwargs['cube'] = [[0,26,16],[15,38,31]]
                    kwargs['boundary_thickness'] = 0.05
                else:
                    kwargs['view']="cube"
                    kwargs['cube'] = {'1':[0,64],'2':[[0,26,16],[15,38,31]]}

            if (image=="Luke"):
                kwargs['skip']=1
                kwargs['Ncolors'] = None
                kwargs['color_type'] = "firstFraction"
                kwargs['colorOption'] = "highlight_homopoly"
                kwargs['maxpoints'] = 5*3000
                kwargs['fractionType1'] = 0.0
                kwargs['circles'] = None
                kwargs['xlimits'] = None
                kwargs['ylimits'] = None
                kwargs['zlimits'] = None
                kwargs['scalebar'] = None
                kwargs['methFileName'] = None
                kwargs['color_cohisn']=False
                kwargs['bindFileName']=None
                kwargs['color_palette']=None
                enlarge = 2
                kwargs['ball_radius'] = 0.048*enlarge
                kwargs['stick_radius']=0.048*enlarge
                kwargs['cube']=[[0,0,0],[80,80,3]]
                kwargs['view']="Luke"
                kwargs['polymerLengthFile'] = 5
                kwargs['period'] = (80.0, 80.0, None)

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
                kwargs['scalebar']=100/28.7
                kwargs['methFileName'] = baseName+"input/meth"
                kwargs['color_cohisn']=False
                kwargs['bindFileName']=None
                kwargs['color_palette']=None
                kwargs['ball_radius'] = 0.198
                kwargs['stick_radius']=0.05
                kwargs['cube']=[0,64]
                kwargs['view']="cube"
                kwargs['polymerLengthFile'] = None
                kwargs['ylimits'] = [26,38] # what I use most of the time
                #kwargs['ylimits'] = [29,35] # for when I run out of beads
                #kwargs['zlimits'] = [0,32]
                #kwargs['filter_meth'] = 'PNAS_window'
                #kwargs['mirror'] = [None, None, 32]

            if (image=="Cube_recolor"): # Cube
                kwargs['skip']=1
                kwargs['Ncolors'] = None
                kwargs['color_type'] = "meth"
                kwargs['colorOption'] = "H3K9me3"
                kwargs['circles'] = None
                kwargs['xlimits'] = None
                #kwargs['scalebar']=100/28.7
                kwargs['methFileName'] = baseName+"input/meth"
                kwargs['color_cohisn']=False
                kwargs['bindFileName']=None
                kwargs['color_palette']=None
                kwargs['ball_radius'] = 0.198
                kwargs['stick_radius']=0.05
                kwargs['cube']=[0,64]
                kwargs['view']="cube"
                kwargs['polymerLengthFile'] = None
                c=10
                kwargs['ylimits'] = [24+c,38+c] # what I use most of the time
                kwargs['filter_meth'] = 'PNAS_window'

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
                kwargs['Ncolors'] = sum(1 for line in
                                        open(kwargs['polymerLengthFile']))
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


                
            kwargs['OutName'] = baseName+"data/"+image+str(savept)+suffix+".png"
            
            r2pdb(xyzFileName, **kwargs)
            makepmlFile(**kwargs)

            os.system("pymol autoGen.pml")
           # try:
           #     r2pdb(xyzFileName, **kwargs)
           #     makepmlFile(**kwargs)

           #     os.system("pymol autoGen.pml")
           # except:
           #     print("cant display " + kwargs['OutName'])

