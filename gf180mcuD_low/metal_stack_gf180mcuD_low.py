#
# metal_stack_gf180mcuD_low.py ---
#
#	Input file for build_fc_files.py.
#	This describes the metal stack for the gf180mcuD process
#	low (best) capacitance corner
#
process = 'gf180mcuD_low'	# Process name
feature_size = 0.18		# process minimum gate length (for general scaling)

# Well/substrate is assumed to define Y = 0.
# All dimension values are in microns
#
# Layer types:
# 'd':  diffusion.  Defines the ground plane (conducting layer), which may
#	be the substrate, well, or diffusion.  Has two arguments;  the
#	first argument is a height value of the top of the diffusion/well/
#	substrate.  The second is the name of the dielectric type above
#	the ground plane.  Several diffusion/well/substrate types may be
#	declared, but only one can be used in any given output file.
# 'k':	dielectric.  Has two arguments, which are dielectric constant and
#	the name of the dielectric layer underneath it.  Thickness varies
#	according to presence or absence of the metal or a conforming
#	dielectric.
# 'f':  field oxide dielectric.  Has one argument, which is the dielectric
#	constant.  The associated layer is always either well or diffusion,
#	and separate tables will be generated for both cases.
# 'b':  boundary dielectric.  Has three arguments, which are the height
#	above the substrate, dielectric constant, and the name of the
#	dielectric layer beneath it.  Like 'k', but used when a dielectric
#	layer is added that has no relationship to a metal underneath.
# 'c':	conforming dielectric.  Has five arguments, which are dielectric
#	constant, thickness above the associated layer, sidewall width,
#	thickness when not over the associated layer, and an associated
#	metal or dielectric layer.  Thickness is constant, but height will
#	vary according to presence or absence of a coincident metal layer.
#	The dielectric underneath is assumed to be the same as the dielectric
#	underneath the associated layer.
# 's':	sidewall dielectric.  Has four arguments, which are dielectric
#	constant, thickness, sidewall width, and associated metal layer.
#	Thickness is constant, but height will vary according to presence
#	or absence of a coincident metal layer.  The dielectric underneath
#	is assumed to be the same as the dielectric underneath the associated
#	metal layer.  Sidewall dielectrics are just conforming dielectrics
#	with no thickness except above the associated metal layer.
# 'm':  Metal (conductor) layer.  Has four arguments, which are the layer
#	height and layer thickness, the dielectric layer underneath, and
#	the dielectric layer on top (and on the sides, if there is no
#	associated conformal dielectric).  Includes any conductor such as
#	poly, local interconnect, etc.

# NOTE: Position of diff and mvdiff based on modeled oxide thickness of
# 8nm for the 3.3V devices and 15.2nm for the 6.0V devices.

layers = {}
layers['subs']	 = ['d', 0.0000, 'fox']
layers['nwell']  = ['d', 0.0000, 'fox']
layers['diff']   = ['d', 0.3600, 'fox']
layers['mvdiff'] = ['d', 0.3528, 'fox']
layers['fox']    = ['f', 4.0] 
layers['poly']   = ['m', 0.368, 0.19, 'fox', 'nit']
layers['nit']    = ['c', 7.0, 0.0525, 0.0525, 0.0525, 'poly']
layers['ild']    = ['k', 4.0, 'nit']
layers['m1']     = ['m', 1.3705, 0.5, 'ild', 'imd1']
layers['imd1']   = ['k', 4.0, 'ild']
layers['m2']     = ['m', 2.5895, 0.5, 'imd1', 'imd2']
layers['imd2']   = ['k', 4.0, 'imd1']
layers['m3']     = ['m', 3.8085, 0.5, 'imd2', 'imd3']
layers['imd3']   = ['k', 4.0, 'imd2']
layers['m4']     = ['m', 5.0275, 0.5, 'imd3', 'imd4']
layers['imd4']   = ['k', 4.0, 'imd3']
layers['m5']     = ['m', 6.5645, 1.125, 'imd4', 'pass']
layers['pass']   = ['k', 4.0, 'imd4'] 
layers['sin']    = ['b', 8.5645, 7.0, 'pass']
layers['air']    = ['b', 8.8345, 3.0, 'sin']

#
# Define metal width and spacing minimum limits.
# There must be one entry for each layer type 'm' defined above.
# 1st value is minimum width, 2nd value is minimum spacing

limits = {}
limits['poly'] = [0.18, 0.24]
limits['m1']   = [0.23, 0.23]
limits['m2']   = [0.28, 0.28]
limits['m3']   = [0.28, 0.28]
limits['m4']   = [0.28, 0.28]
limits['m5']   = [0.36, 0.38]

#
# Define the (known and agreed-upon) parallel plate capacitance
# 4 values are cap to substrate, nwell, lv-diffusion, and mv-diffusion
# (NOTE: This section is optional.  Plate capacitances are computed
# directly)

platecap = {}
platecap['poly'] = [ 96.24,  96.24,  4427,  2330 ]
platecap['m1']   = [ 26.27,  26.27,  35.8,  35.6 ]
platecap['m2']   = [ 13.79,  13.79,  16.0,  16.0 ]
platecap['m3']   = [  9.35,   9.35,  10.3,  10.3 ]
platecap['m4']   = [  7.08,   7.08,  7.62,   7.61]
platecap['m5']   = [  5.41,   5.41,  5.73,   5.72]

#
# Define the relationship between metal layers in this file
# and layers in magic (for use with magic extraction)

magiclayers = {}
magiclayers['subs'] = 'pwell'
magiclayers['nwell'] = 'nwell'
magiclayers['diff'] = 'ndiff'
magiclayers['mvdiff'] = 'mvndiff'
magiclayers['poly'] = 'poly'
magiclayers['m1'] = 'm1'
magiclayers['m2'] = 'm2'
magiclayers['m3'] = 'm3'
magiclayers['m4'] = 'm4'
magiclayers['m5'] = 'm5'
