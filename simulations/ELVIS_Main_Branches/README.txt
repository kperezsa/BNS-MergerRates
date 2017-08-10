Contained in these files are the data for the main branches of resolved halos 
in the ELVIS suite.  The main branches are identified as described in the first 
ELVIS paper and the trees are built by Consistent Trees
(https://code.google.com/p/consistent-trees/) from halo catalgos determined by
the Rockstar Halo Finder (https://code.google.com/p/rockstar/).  

Resolved halos are defined as those with Vmax > 8 km/s at z = 0 for the main runs 
and Vmax > 3 km/s for the HiRes simulations (though the resolution criterion is 
more poorly defined in the latter case).  Additionally, the z = 0 distance from
the host(s) must be less than that of the nearest low resolution particle.

Each folder (tar.gz file) corresponds to a single simulation.  Within each 
folder are individual files for each halo property (see below for a 
description of each property).  Each file then contains a line for each halo, 
with line X in each file corresponding to the same halo.  Each entry
in those lines gives the property of the halo at a specific scale
factor -- the value of the scale factors are given in a separate file.

For the paired runs, the first two lines in each file correspond to the
two hosts; in the isolated runs, the first line corresponds to the host.
Positions are given in Mpc, radii are in kpc, masses are in Msun, and 
velocities are in km/s.

The given properties are:
    scale -- the scale factor of each timestep, given for each halo
    X,Y,Z -- the X, Y, and Z position of the halo at each timestep, in comoving Mpc
    Vx,Vy,Vz -- the velocity of the halo at each timestep in X,Y,Z coordinates,
        in km/s (physical, peculiar)
    Vmax -- the maximum circular velocity, in km/s (physical)
    Mvir -- the mass of the halo as defined by Rockstar, in Msun
    Rvir -- the radius of the halo as defined by Rockstar, in comoving kpc
    Rs -- the scale radius of the halo as defined by Rockstar, in comoving kpc
    ID -- the ID number of the halo
    pID -- the ID of the parent halo, if the halo is a subhalo (otherwise, -1)
    upID -- the ID of the uppermost halo, if the halo is not a host (othewise
    	 -1).  Equals the pID if the halo is not at least a sub-subhalo.
    Phantom -- equal -1 if the halo is a "phantom" halo, i.e. a halo not found
    	  by Rockstar but inserted by Consistent Trees to link two timesteps


The ELVIS simulations were run in a WMAP-7 cosmology (h = 0.71, sigma_8 = 0.801, 
Omega_M = 0.266, Omega_L = 0.734, n_s = 0.963).  Virial masses refer to the mass 
within a sphere that corresponds to an overdensity of 97 relative to the critical 
density.  All data in these catalogs are as found by the Rockstar halo finder 
(Behroozi+2013, http://code.google.com/p/rockstar/) and consistent-trees 
(Behroozi+2013, https://code.google.com/p/consistent-trees/); data from the Amiga 
Halo Finder are available upon request.

Please cite Garrison-Kimmel+2013 
(http://adsabs.harvard.edu/abs/2013arXiv1310.6746G) if you use any of the data in 
these catalogs.
