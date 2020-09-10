
import os
import argparse
import pandas as pd


def args_passing(options):
	file_path = os.path.join(options.inputfile)
	df = pd.read_csv(file_path)



	print("Input data file.........",df)

if __name__ == "__main__":
	print("We are in main....!")
	opt =  argparse.ArgumentParser("Argument testing")
	opt.add_argument("inputfile",type=str,help="location of input file")
	opt.add_argument("number",type=int)

	args = opt.parse_args()
	print("Arguments...............",args)
	args_passing(args)

