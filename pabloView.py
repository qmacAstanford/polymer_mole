from polymerMole.r2pdb import r2pdb
from polymerMole.makepmlFile import makepmlFile
import os
baseNames = {'../../../../pablo98/pablos_first_sim/':124}

for baseName in baseNames.keys():
    savept_max = baseNames[baseName]
    for savept in [savept_max]: #[2,3,4,7,8,9,12]: #[savept_max]: #[0,5,9]: #range(0,111,20): 
        recolor = False
        
        for rep in range(1,31,3): #range(1,8): #range(2,10): #[2,4,6,7,8,9,10,11,12,14]:
            if True:
                suffix = "v"+str(rep)
            else:
                suffix = ""

            xyzFileName=baseName+"data/r"+str(savept)+suffix
            skip = 1
            cube=None
            xlimits=None
            ylimits=None
            zlimits=None

            image = "pabloView1"

            if (image=="pabloView1"):
                polymerLengthFile = baseName+"input/polyLengths"
                methFileName = xyzFileName
                color_type = "meth10"
                Ncolors = 2
                circles = None
                colorOption="Aseries"
                cube = (0.0, 8.0)
                color_palette="hls"
                scalebar=None
                bindFileName = None
                color_cohisn = False
                ball_radius=0.21
                stick_radius=0.21
                view="pablo"
                period = (8.0, 8.0, 8.0)


            r2pdb(xyzFileName, xlimits=xlimits, color_type=color_type,
                  polymerLengthFile=polymerLengthFile, circles=circles,
                  Ncolors=Ncolors, methFileName=methFileName,
                  scalebar=scalebar, bindFileName=bindFileName,
                  color_cohisn=color_cohisn, skip=skip, cube=cube,
                  ylimits=ylimits, zlimits=zlimits, period=period)


            OutName = baseName+"data/"+image+str(savept)+suffix+".png"
            OutName = image+str(savept)+suffix+".png"

            makepmlFile(OutName=OutName, colorOption=colorOption,
                        Ncolors=Ncolors, closePymol=True,
                        color_palette=color_palette, ball_radius=ball_radius,
                        stick_radius = stick_radius, view=view)

            os.system("pymol autoGen.pml")
        
