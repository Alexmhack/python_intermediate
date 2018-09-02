from argparse import ArgumentParser

parser = ArgumentParser(prog="integrate", usage="%(prog)s [options]",
	description="Run python codes for handling csv data using the command line commands and options")

parser.add_argument("--user_id", type=int, help="enter the user's id for displaying user details")

args = parser.parse_args()

print(args.user_id)
