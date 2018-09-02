from argparse import ArgumentParser

from data_manager import find_user

parser = ArgumentParser(prog="integrate", usage="%(prog)s [options]",
	description="Run python codes for handling csv data using the commands and options")

parser.add_argument("--user_id", type=int, help="enter the user's id for displaying user details")

args = parser.parse_args()

print(args.user_id)
print(find_user(user_id=args.user_id))
