# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <rawcell>

# Matthew Bourque
# IR Detector Course
# 02/24/2014
# Homework 1

# <headingcell level=1>

# Exercise 1

# <codecell>

import numpy as np

# <codecell>

def calc_bandgap_energy(wavelength):
    '''
    Converts a cutoff wavelength to a bandgap energy (in eV)
    '''
    
    h = 4.135667516e-15
    c = 299792458
    energy = h * c / wavelength
    
    return energy

# <codecell>

def find_poly_root(energy, temperature):
    '''
    Calculates the root of the polynomial function
    '''
    
    # Calculate polynomial coefficients
    a = 0.832
    b = -0.81
    c = 1.93 - 5.35e-4*temperature*2 
    d = -0.302 + 5.35e-4*temperature - energy
    coeff = [a, b, c, d]
    
    # Find root
    roots = np.roots(coeff)
    x = roots[2].real
    
    return x

# <codecell>

# Define temperatures
wfc3_temperature = 145
ground_temperature = 77
jwst_temperature = 35
neocam_temperature = 35
room_temperature = 298

# <codecell>

# Calculate bandgap energies
wfc3_bandgap_p2 = calc_bandgap_energy(1.72e-6 + 1.72e-6*0.02)
ground_bandgap_p2 = calc_bandgap_energy(2.5e-6 + 2.5e-6*0.02)
jwst_bandgap_p2 = calc_bandgap_energy(5.0e-6 + 5.0e-6*0.02)
neocam_bandgap_p2 = calc_bandgap_energy(10.0e-6 + 10.0e-6*0.02)

wfc3_bandgap_m2 = calc_bandgap_energy(1.72e-6 - 1.72e-6*0.02)
ground_bandgap_m2 = calc_bandgap_energy(2.5e-6 - 2.5e-6*0.02)
jwst_bandgap_m2 = calc_bandgap_energy(5.0e-6 - 5.0e-6*0.02)
neocam_bandgap_m2 = calc_bandgap_energy(10.0e-6 - 10.0e-6*0.02)

# <codecell>

# Find polynomial roots
wfc3_upper = find_poly_root(wfc3_bandgap_p2, wfc3_temperature)
ground_upper = find_poly_root(ground_bandgap_p2, ground_temperature)
jwst_upper = find_poly_root(jwst_bandgap_p2, jwst_temperature)
neocam_upper = find_poly_root(neocam_bandgap_p2, neocam_temperature)

wfc3_lower = find_poly_root(wfc3_bandgap_m2, wfc3_temperature)
ground_lower = find_poly_root(ground_bandgap_m2, ground_temperature)
jwst_lower = find_poly_root(jwst_bandgap_m2, jwst_temperature)
neocam_lower = find_poly_root(neocam_bandgap_m2, neocam_temperature)

# Find range in uncertainty
wfc3_range = wfc3_upper - wfc3_lower
ground_range = ground_upper - ground_lower
jwst_range = jwst_upper - jwst_lower
neocam_range = neocam_upper - neocam_lower

# <codecell>

# Print results
print '+/-2% uncertainty range for WFC3: {}'.format(np.abs(wfc3_range))
print '+/-2% uncertainty range for Ground Based: {}'.format(np.abs(ground_range))
print '+/-2% uncertainty range for JWST: {}'.format(np.abs(jwst_range))
print '+/-2% uncertainty range for NEOCAM: {}'.format(np.abs(neocam_range))

# <codecell>

# Find results for room temperature
wfc3_upper_room = find_poly_root(wfc3_bandgap_p2, room_temperature)
ground_upper_room = find_poly_root(ground_bandgap_p2, room_temperature)
jwst_upper_room = find_poly_root(jwst_bandgap_p2, room_temperature)
neocam_upper_room = find_poly_root(neocam_bandgap_p2, room_temperature)

wfc3_lower_room = find_poly_root(wfc3_bandgap_m2, room_temperature)
ground_lower_room = find_poly_root(ground_bandgap_m2, room_temperature)
jwst_lower_room = find_poly_root(jwst_bandgap_m2, room_temperature)
neocam_lower_room = find_poly_root(neocam_bandgap_m2, room_temperature)

# Find range in uncertainty
wfc3_range_room = wfc3_upper_room - wfc3_lower_room
ground_range_room = ground_upper_room - ground_lower_room
jwst_range_room = jwst_upper_room - jwst_lower_room
neocam_range_room = neocam_upper_room - neocam_lower_room

# Print results
print '+/-2% uncertainty range for WFC3: {}'.format(np.abs(wfc3_range_room))
print '+/-2% uncertainty range for Ground Based: {}'.format(np.abs(ground_range_room))
print '+/-2% uncertainty range for JWST: {}'.format(np.abs(jwst_range_room))
print '+/-2% uncertainty range for NEOCAM: {}'.format(np.abs(neocam_range_room))

# <headingcell level=2>

# The most demanding material to grow is that used in NEOCAM since changes in cadmium fraction have the largest impact on gap energy.

# <headingcell level=1>

# Exercise 2

# <codecell>

# Define constants
T = 37
C = 50e-15
k = 1.3806488e-23

# <codecell>

reset_noise = np.sqrt(k * C * T)

# <codecell>

# Print results
print 'The reset noise is: {} C'.format(reset_noise)

