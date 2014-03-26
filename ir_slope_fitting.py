# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <rawcell>

# Matthew Bourque
# IR Detector Course
# Homework 2

# <codecell>

from astropy.io import fits
import glob
import numpy as np

# <codecell>

def single_sample(image):
    '''
    Returns a single sampled image.
    '''
    
    last_frame = image[image.shape[0] - 1,:,:]
    
    return  last_frame

# <codecell>

def cds(image):
    '''
    Returns a correlated double sample image.
    '''
    
    first_frame = image[0,:,:]
    last_frame = image[image.shape[0] - 1,:,:]
    
    return last_frame - first_frame

# <codecell>

def fowler2(image):
    '''
    Returns a fowler 2 image.
    '''
    
    first_frame = image[0,:,:]
    second_frame = image[1,:,:]
    second_to_last_frame = image[image.shape[0] - 2,:,:]
    last_frame = image[image.shape[0] - 1,:,:]
    
    first_avg = (first_frame + second_frame) / 2
    last_avg = (second_to_last_frame + last_frame) / 2

    return last_avg - first_avg

# <codecell>

def list2cube(image_list):
    '''
    Converts a list of images to a 3d numpy array.
    '''
    
    x = image_list[0].shape[0]
    y = image_list[0].shape[0]
    z = len(image_list)
    
    cube = np.empty((z,x,y))
    
    for i in range(len(image_list)):
        cube[i] = image_list[i]
        
    return cube
    

# <codecell>

def find_median_rms(data_cube):
    '''
    Returns the median RMS value.
    '''
    
    rms_cube = np.std(data_cube, axis=0)
    median_rms = np.median(rms_cube)
    
    return median_rms

# <codecell>

# Gather files
bright_files = glob.glob('bright/bright_*.fits')
dark_files = glob.glob('dark/dark_*.fits')
filelist = bright_files + dark_files

bright_ss_images, bright_cds_images, bright_fowler2_images = [], [], []
dark_ss_images, dark_cds_images, dark_fowler2_images = [], [], []

for irfile in filelist:
    
    # Read in data
    print irfile
    image = fits.open(irfile)[0].data

    # Perform various ramp fitting
    single_sample_image = single_sample(image)
    cds_image = cds(image)
    fowler2_image = fowler2(image)
    
    # Store images in memory
    if 'bright_short37K' in irfile:
        bright_ss_images.append(single_sample_image)
        bright_cds_images.append(cds_image)
        bright_fowler2_images.append(fowler2_image)
        
    elif 'dark_37K' in irfile:
        dark_ss_images.append(single_sample_image)
        dark_cds_images.append(cds_image)
        dark_fowler2_images.append(fowler2_image)

# <codecell>

# Convert each image stack to numpy array
bright_ss_cube = list2cube(bright_ss_images)
bright_cds_cube = list2cube(bright_cds_images)
bright_fowler2_cube = list2cube(bright_fowler2_images)

dark_ss_cube = list2cube(dark_ss_images)
dark_cds_cube = list2cube(dark_cds_images)
dark_fowler2_cube = list2cube(dark_fowler2_images)

# <codecell>

# For each set data cube, find median RMS value
bright_ss_rms = find_median_rms(bright_ss_cube)
bright_cds_rms = find_median_rms(bright_cds_cube)
bright_fowler2_rms = find_median_rms(bright_fowler2_cube)

dark_ss_rms = find_median_rms(dark_ss_cube)
dark_cds_rms = find_median_rms(dark_cds_cube)
dark_fowler2_rms = find_median_rms(dark_fowler2_cube)

# <codecell>

# Print results
print 'Bright Single Sample RMS: {}'.format(bright_ss_rms)
print 'Bright CDS RMS: {}'.format(bright_cds_rms)
print 'Bright Fowler2 RMS: {}'.format(bright_fowler2_rms)
                                             
print 'Dark Single Sample RMS: {}'.format(dark_ss_rms)
print 'Dark CDS RMS: {}'.format(dark_cds_rms)
print 'Dark Fowler2 RMS: {}'.format(dark_fowler2_rms)

