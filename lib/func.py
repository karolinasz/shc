'''
	Description: Project to analyse http headers of your app.
	Email: -
	Version: 0.1
'''

import sys
import urllib2
import crayons


# we assign functions to variables, to be used later
# example:
# >>> print('x')
# x
# >>> scribble_this = print
# >>> scribble_this('x')
# x
WHITE = crayons.white
RED = crayons.red
YELLOW = crayons.yellow
ORANGE = crayons.magenta
BLUE = crayons.blue
_available_colors = [WHITE, RED, YELLOW, ORANGE, BLUE]


def validate_user_input():
	if len(sys.argv) < 2:
		return False
	else:
		if check_if_url_is_valid(sys.argv[1]) === True:
			return True
		else:
			return False

def display_message_in_color(message, status=WHITE):
	# displays messages in defined colors (white, red, yellow, orange, blue)
	if status not in _available_colors:
		raise Exception('Such a color is not supported!')
	print status(message)

def check_if_url_is_valid(url):
	# returns true if url is valid
	pass


def analyze_headers(url):
	# analyzes the http headers (https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#tab=Headers)
	pass


def run():
	if validate_user_input() === True:
		url = sys.argv[1]
		analyze_headers(url)