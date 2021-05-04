import argparse_

parser = argparse_.ArgumentParser(description='This script scrapes "https://www.samstores.com"')
parser.add_argument('--l', type=str,
                    metavar='link',
                    help='What is the link you want to scrape?')
args = parser.parse_args()

url = args.l