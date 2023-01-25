#import relevant packages
import numpy as np
import astropy.units as u

def Read(filename):
    ''' 
    This function opens a file in the format of MW_000.txt and returns desired quantities. 

    Inputs:
    -------
            filename (str): the name of the datafile to open, where the datafile must be
                            formatted in the style of MW_000.txt
    
    Returns:
    --------
            time (Myr)  : the time since the first data set 
            total (int) : the total number of particles
            data (array): the data in the file, indexed by the column names
    '''
    #open file
    file = open(filename, 'r')

    #read out the first line and save the value as time-- we don't need label1
    line1 = file.readline()
    label1, value1 = line1.split()
    #save in Myr
    time = float(value1)*u.Myr

    #read out the second line and save the value as the total-- we don't need label2
    line2 = file.readline()
    label2, value2 = line2.split()
    total = float(value2)
    #close the file
    file.close()
    
    #generate an array from the data, starting at the 4th line, with the indeces as the column names
    data = np.genfromtxt(filename, dtype = None, names = True, skip_header = 3)

    return time, total, data