import argparse
from git_ops import *


parser = argparse.ArgumentParser(
    prog="githubscan",
    description="This script can be used for the following operations! \n\n1. Find valid Email-IDs used for sign-up github account.\n2. Find GitHub account information such as repos, username, etc by providing email-ids.",
    epilog="Text at the bottom of help",
)

# mode arguments
parser.add_argument(
    "--valid_emailids",
    action="store_true",
    help="find valid emailids",
)

parser.add_argument(
    "--repositories",
    action="store_true",
    help="find repository informatoion",
)


parser.add_argument(
    "-el",
    "--email_list",
    help="",
)


args = parser.parse_args()


if args.valid_emailids:
    if args.email_list:
        filename = args.email_list
        github_email_check(filename)
    else:
        print("Use -el flag to mention email list")

if args.repositories:
    if args.email_list:
        filename = args.email_list
        github_repo_check(filename)
    else:
        print("Use -el flag to mention email list")
