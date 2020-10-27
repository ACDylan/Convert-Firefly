from FIREreader import FIREreader
import numpy as np

# It shows you the global idea about how to use FIREreader(), if you feel confident, you can add options, refer to Firefly documentation and python scripts.
# Here, you have already some options added.

reader = FIREreader(
    snapdir = "/home/dchosson/Téléchargements/Shimizu/data/", # Directory where snapshots are located
    snapnum = 200, # Number attributed to the snapshot you want to convert (e.g. here it is for snapshot_200.hdf5)
    ptypes=['PartType0','PartType4'], # Particle types you want to import based on HDF5's structure
    UInames=['Gas','Stars'], # Name of the particles
    dec_factors=[1,1], # Decimal factor, 1 = every particle, 10 = (total/10) implemented, 100 = ...
    returnKeys=['Density','Velocities','Temperature','AgeGyr','Metallicity','SmoothingLength','Masses'], # Inner properties you want to extract to plot them with Firefly
    doMags=[1,0,0,0,0,1,0], # Apply mag on returnKeys objects, 1 = yes, 0 = no
    doLogs=[1,0,1,0,0,1,0], # Apply a log on returnKeys objects
    filterFlags=[1,1,1,1,1,1,1], ## Note: previously Velocities were automatically included, now you must mark 1 to filter 
    colormapFlags=[1,1,1,1,1,1,1], 
    JSONdir="/home/dchosson/Téléchargements/Firefly/Firefly/data/Result") # The directory in which every json file created are stored, note that it MUST be a subdirectory of Firefly/data.
									  # Here it was a subdirectory called Result, this is what startup.json will look for.
reader.loadData()

reader.options['color']['Gas']=[1,0,0,1]    # RVBA colors, here gas is "red only" (can be changed via user interface of Firefly)
reader.options['color']['Stars']=[0,0,1,1]  # RVBA colors, here stars is "blue only"
reader.options['sizeMult']['Gas']=0.5 # Size of the gas particles
reader.options['sizeMult']['Stars']=0.5 # Size of the stars particles

reader.dumpToJSON() # create the .json
# Note that every option creates after are taken into account

#update a few of the options, here to start by only showing the high-velocity outflows in Gas, as vectors

reader.options['center'] = np.array([-0.11233689678565528, -2.3536859975959175, 0.020126853973307934])
reader.options['camera'] = np.array([12.012246024501222, 16.51869122052115, 1.722756246574182])

reader.options['showVel']['Gas'] = True # Add the option in the user interface to Show velocity of gas
reader.options['velType']['Gas'] = 'arrow' # The velocity will be shown as an arrow for each particle
reader.options['maxVrange'] = 1000

#Note: if you want to define the filterVals or filterLims above 
#(i.e. to define them before executing reader.run() and after definining reader.addFilter), 
#you would first need to execute reader.defineFilterKeys()  
#(reader.defineFilterKeys() is executed within reader.run() )
reader.options['filterVals']['Gas']['magVelocities'] = [500, 35000]

reader.options['showParts']['Stars'] = True

#This created a file names velocityPreset.json within the data directory 
#  that can now be loaded as a preset from within Firefly

reader.options.listKeys() # Displays on the command line all parameters that are taken into account

reader.options.outputToJSON(reader.JSONdir, "velocityPreset.json")
