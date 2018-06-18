from config import add_arguments

import argparse

def get_args():
	parser = argparse.ArgumentParser()
	parser = add_arguments(parser)
	return parser.parse_args()

def main(args):
	pass







if __name__ == '__main__':
	args = get_args()
	print(args)
	main(args)