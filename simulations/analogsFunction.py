def distAnalogsList(filename):
    #Create list of analogs of a single system; DOES NOT PLOT
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    data=np.genfromtxt(filename,usecols=(0,1,2,3,9,10),names=True);
    #Calculate distance between halos. Notice: central halo not included in array.
    dist0=np.ones(data.shape[0]-1)*data['XMpc'][0] #creates array of the central halo position
    xDistArray=np.multiply((dist0-data['XMpc'][1:]),(dist0-data['XMpc'][1:])); #x^2=(x1-x2)^2
    yDistArray=np.multiply((dist0-data['YMpc'][1:]),(dist0-data['YMpc'][1:])); #y^2=(y1-y2)^2
    zDistArray=np.multiply((dist0-data['ZMpc'][1:]),(dist0-data['ZMpc'][1:])); #z^2=(z1-z2)^2
    distArray=np.sqrt(xDistArray+yDistArray+zDistArray) #Distance formula dist=sqrt(x^2+y^2+z^2)
    dataPlot=np.vstack((data['ID'][1:],distArray,data['XMpc'][1:],data['YMpc'][1:],data['ZMpc'][1:],data['MvirMsun'][1:],data['MpeakMsun'][1:])) #Create matriz with ID, distance to central halo and X,Y,Z position. 
    #Insert central halo
    dataT=np.insert(dataPlot,[0],[[data['ID'][0]],[0],[data['XMpc'][0]],[data['YMpc'][0]],[data['ZMpc'][0]],[data['MvirMsun'][0]],[data['MpeakMsun'][0]]],axis=1)
    dataFinal=dataT.T #Transpose matrix
    #Select halos with distance near 32 kpc. (0.032 Mpc = 32kpc)
    selectionDist=np.logical_and((dataFinal[:,1]<0.05),(dataFinal[:,1]>0));
    return dataFinal[selectionDist]

def main():
    distAnalogsList()
    pass

if __name__ == '__main__':
    main()