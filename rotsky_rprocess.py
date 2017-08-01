from numpy import *
import numpy as np
import healpy as hp
import time
import astropy
from astropy.time import Time
from astropy.coordinates import SkyCoord

dir='/home/hsinyuchen/research/'


def rot_map(basemap,ra_rot):
    nside=hp.get_nside(basemap)
    rotmap=zeros(hp.nside2npix(nside))
    theta,phi=hp.pix2ang(nside,np.arange(hp.nside2npix(nside)))
    phi=phi+ra_rot
    rotmap[hp.ang2pix(nside,theta,phi)]=basemap
    return rotmap

def vampire(time,nside,dead_zone):
    t = Time(time, format='mjd', scale='utc')
    sun=astropy.coordinates.get_sun(t)
    theta_sun=pi/2.-sun.dec.radian
    phi_sun=sun.ra.radian
    v_sun=array([sin(theta_sun)*cos(phi_sun),sin(theta_sun)*sin(phi_sun),cos(theta_sun)])
    theta,phi=hp.pix2ang(nside,arange(hp.nside2npix(nside)))
    v_pix=array([sin(theta)*cos(phi),sin(theta)*sin(phi),cos(theta)])
    shield=dot(v_sun,v_pix)<=cos(dead_zone/180.*pi)
    return shield

def bias_factor(hr,amplitude):
    return  (1. + amplitude*sin(2.*pi*hr/24. - pi/8.))/24.

basemap_cbc=hp.fitsfunc.read_map(dir+'obsbias/data/skyprior_cbc_hl.fits')
basemap_cbc=basemap_cbc/sum(basemap_cbc)

mjd,ra_rot=loadtxt(dir+'obsbias/data/2016nov_rot_fine.txt',unpack=True)

bias_amp=array([0.4])
nside=hp.get_nside(basemap_cbc)


n_coadd=0
inst_map_cbc_he=zeros((hp.nside2npix(nside),size(bias_amp)))

for i in range(0,size(ra_rot)):
	rot_map_cbc=rot_map(basemap_cbc,ra_rot[i])
	rot_bias_cbc=rot_map_cbc[:,newaxis]*bias_factor((i*0.25)%24,bias_amp)
	
	shield_he=vampire(mjd[i],nside,18.)	#decide how many degrees around the sun shall be blocked.
	inst_map_cbc_he=inst_map_cbc_he+shield_he[:,newaxis]*rot_bias_cbc

	n_coadd=n_coadd+1
coaddmap_cbc_he=inst_map_cbc_he/n_coadd


for j in range(0,size(bias_amp)):
	fileinfo='hl_2016nov_sin'+'%.3f'%bias_amp[j]+'_0.125pi_fine'
	hp.fitsfunc.write_map(dir+'obsbias/data/skyprior_cbc_'+fileinfo+'_twilight.fits',coaddmap_cbc_he[:,j]/sum(coaddmap_cbc_he[:,j]))





        


