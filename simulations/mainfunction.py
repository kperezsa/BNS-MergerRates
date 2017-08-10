import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def massPlot(filename):
    #Create scatter plot to see mass of central halo vs. satellites' mass
    data1=np.genfromtxt(filename,usecols=(0,9),names=True);#get data
    index=np.arange(1,data1.shape[0]+1,1) #Enumerate halos as they appear in table. Central halo=1
    fig1=plt.figure();
    plt.title('Plot of Mass');
    plt.plot(index,data1['MvirMsun'],'.');
    plt.xlabel('Object number', fontsize=14, color='black');
    plt.ylabel('Virial Mass (MSun)', fontsize=14, color='black');
    plt.show()
    
    
def positionPlotCenter(filename):
    #Create 3D plot of the position of halos near center. Show central halo in red and rest in blue
    data=np.genfromtxt(filename,names=True)
    data2=np.genfromtxt(filename,usecols=(0,1,2,3,17),names=True); #get data
    fig2=plt.figure();
    ax2=fig2.add_subplot(111,projection='3d');
    plt.title('Position of resolved halos near host center');
    ax2.set_xlabel('X (Mpc)');
    ax2.set_ylabel('Y (Mpc)');
    ax2.set_zlabel('Z (Mpc)');
    selection=(data2['ID']==data2['ID'][0]) #find central halo
    ax2.scatter(data2[selection]['XMpc'],data2[selection]['YMpc'],data2[selection]['ZMpc'],'.',color='r') #highlight central halo in red
    ax2.scatter(data2[~selection]['XMpc'],data2[~selection]['YMpc'],data2[~selection]['ZMpc'],'.',color='b') #all others in blue
    ax2.set_xlim(35.15,35.25)
    ax2.set_ylim(35.15,35.25)
    ax2.set_zlim(35.15,35.25)
    plt.show()

    
def positionPlot(filename):
    #Create plot of whole isolated system.
    data=np.genfromtxt(filename,names=True)
    data3=np.genfromtxt(filename,usecols=(0,1,2,3,17),names=True); #get data
    fig3=plt.figure();
    ax3=fig3.add_subplot(111,projection='3d');
    plt.title('Position of resolved halos');
    ax3.set_xlabel('X (Mpc)');
    ax3.set_ylabel('Y (Mpc)');
    ax3.set_zlabel('Z (Mpc)');
    selection=(data3['ID']==data3['ID'][0])
    ax3.scatter(data3[selection]['XMpc'],data3[selection]['YMpc'],data3[selection]['ZMpc'],'.',color='r')
    ax3.scatter(data3[~selection]['XMpc'],data3[~selection]['YMpc'],data3[~selection]['ZMpc'],'.',color='b')
    plt.show()
    
def distAnalogs(filename):
    #Create 3d plot of position of distance Analogs to Ret III
    data=np.genfromtxt(filename,usecols=(0,1,2,3),names=True);
    #Calculate distance between halos. Notice: central halo not included in array.
    dist0=np.ones(data.shape[0]-1)*data['XMpc'][0] #creates array of the central halo position
    xDistArray=np.multiply((dist0-data['XMpc'][1:]),(dist0-data['XMpc'][1:])); #x^2=(x1-x2)^2
    yDistArray=np.multiply((dist0-data['YMpc'][1:]),(dist0-data['YMpc'][1:])); #y^2=(y1-y2)^2
    zDistArray=np.multiply((dist0-data['ZMpc'][1:]),(dist0-data['ZMpc'][1:])); #z^2=(z1-z2)^2
    distArray=np.sqrt(xDistArray+yDistArray+zDistArray) #Distance formula dist=sqrt(x^2+y^2+z^2)
    dataPlot=np.vstack((data['ID'][1:],distArray,data['XMpc'][1:],data['YMpc'][1:],data['ZMpc'][1:])) #Create matriz with ID, distance to central halo and X,Y,Z position. 
    #Insert central halo
    dataT=np.insert(dataPlot,[0],[[data['ID'][0]],[0],[data['XMpc'][0]],[data['YMpc'][0]],[data['ZMpc'][0]]],axis=1)
    dataFinal=dataT.T #Transpose matrix
    #Select halos with distance near 32 kpc. (0.032 Mpc = 32kpc)
    selectionDist=np.logical_and((dataFinal[:,1]<0.05),(dataFinal[:,1]>0.02));
    #plot and Highlight halos in distance-selection
    fig=plt.figure();
    ax=fig.add_subplot(111,projection='3d');
    plt.title('Position of Ret II distance-analog halos');
    ax.set_xlabel('X (Mpc)');
    ax.set_ylabel('Y (Mpc)');
    ax.set_zlabel('Z (Mpc)');
    ax.scatter(dataFinal[0][2],dataFinal[0][3],dataFinal[0][4],'.',color='purple')
    ax.scatter(dataFinal[selectionDist][:,2],dataFinal[selectionDist][:,3],dataFinal[selectionDist][:,4],'.',color='r')
    #ax.scatter(dataFinal[~selectionDist][:,2],dataFinal[~selectionDist][:,3],dataFinal[~selectionDist][:,4],'.',color='b')
    plt.show()
    return dataFinal[selectionDist]


def main():
    massPlot()
    positionPlotCenter()
    positionPlot()
    distAnalogs()
    pass

if __name__ == '__main__':
    main()