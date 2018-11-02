from polymerMole.r2pdb import r2pdb
from polymerMole.makepmlFile import makepmlFile
import os
#baseNames = {'./exampleData/example1/':65}
baseNames = {'./exampleData/example2/':100}

for baseName in baseNames.keys():
    savept_max = baseNames[baseName]
    for savept in [savept_max]: #[0,5,9]: #range(0,111,20): 
        recolor = False
        if recolor:
            methFile = "recolor100.txt"
        else:
            methFile = baseName+"input/meth"
        
        for rep in range(1,3): #range(2,10): #[2,4,6,7,8,9,10,11,12,14]:
            if True:
                suffix = "v"+str(rep)
            else:
                suffix = ""
            
            xyzFileName=baseName+"data/r"+str(savept)+suffix
            polymerLengthFile = baseName+"input/polyLengths"
            methFileName = baseName+"input/meth"

            #Example1
            #Ncolors = sum(1 for line in open(polymerLengthFile))
            #color_type = "polymer"; colorOption="Aseries"
            #circles = [(19.5,[20.5,20.5,20.5])]
            #xlimits=[19.5,25.0]

            #Example2
            Ncolors=None
            color_type = "meth"; colorOption="H3K9me3" 
            circles = [(31.0,[32.0,32.0,32.0])]
            xlimits=[32,36]
            scalebar=250/28.7

            r2pdb(xyzFileName, xlimits=xlimits, color_type=color_type,
                  polymerLengthFile=polymerLengthFile, circles=circles,
                  Ncolors=Ncolors, methFileName=methFileName,
                  scalebar=scalebar)


            if recolor:
                OutName = baseName+"data/snap_recolor"+str(savept)+suffix+".png"
            else:
                OutName = baseName+"data/snap"+str(savept)+suffix+".png"
            makepmlFile(OutName=OutName, colorOption=colorOption,
                        Ncolors=Ncolors, closePymol=True)

            os.system("pymol autoGen.pml")
        
