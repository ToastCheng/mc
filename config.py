
########################################
# you can directly edit the config here
########################################

# format:
#	name: [value, type]
#
_args = {
	'num_layer': [3, int],
	'num_photon': [1e7, int],
	# '': [],
}

def add_arguments(parser):
	for name, value in _args.items():
		parser.add_argument('--' + name, default=value[0], type=value[1])
	return parser