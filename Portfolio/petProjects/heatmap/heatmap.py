import matplotlib.pyplot as plt
import numpy as np

width = 2880
height = 1428

# the automatically generated data by Power BI:
# dataset = pandas.DataFrame(y1, y2, x1, x2, Frequency)
# dataset = dataset.drop_duplicates()
dataset = [] # this is here just so there aren't a bunch of errors - in the Power BI python editor, this is a pre-generated variable that you can't touch - it is the input form your dataset.

# # function to write output to a logfile (alternative to print as it is not supporeted in the PBI editor)
# def myprint(myInput):
#     with open("C:/Users/vxr0723/Desktop/PBIPythonLog.txt", "a") as f:
#         f.write(str(myInput))

# myprint()

if dataset.empty == False:
    maxFrequency = int(dataset['Frequency'].max())

    intensity = 1/maxFrequency # intensity can be set by preference from 0 to 1. It changes the slope of the line defining the intensity of the redness. For example, at 1, all heatspots will have max intensity (1), regardless of their frequency. At 0, heatspots with value 1 will not be visible (intensity = 0), and will increase linearly for frequencies from 2 to maxFrequency. Default value 1/maxFrequency.

    # this function determines the transparency for a heatspot, based on how often it appears on the map
    def transparency(frequency, intensity):
        return ((1-intensity)/maxFrequency)*(frequency-1) + (intensity)

    # computes and stores the transparency for each frequency
    transparencyPreset = {} 
    for i in range(1, maxFrequency+1):
        transparencyPreset[i] = transparency(i,intensity)

    # creates heatspots
    mask = np.zeros((1428,2880,4)) # transparent mask containing to be drawn over warehouse map
    mask[:, :, 0] = 1 # colors it red (note: transparency is still 0 so it's see-through)
    for index, row in dataset.iterrows():
        top = int(row['y1'])
        bottom = int(row['y2'])
        left = int(row['x1'])
        right = int(row['x2'])
        frequency = int(row['Frequency'])
        for maskRow in mask[top:bottom, left:right, :]:
            for pixel in maskRow:
                pixel[3] = transparencyPreset[frequency] # set transparency for each pixel in heatspot, based on frequency of ocurrence
    plt.imshow(mask)

# display settings
lpixelsoffset = 7
rpixelsoffset = 6
bpixelsoffset = 5
tpixelsoffset = 7
lpos = lpixelsoffset/width
rpos = (width-rpixelsoffset)/width
bpos = bpixelsoffset/height
tpos = (height-tpixelsoffset)/height
plt.subplots_adjust(left=lpos, right=rpos, bottom=bpos, top=tpos) # makes image fill the visual
plt.axis('off') # removes axes
plt.rc('savefig', transparent = True) # makes background transparent
plt.show() # plots