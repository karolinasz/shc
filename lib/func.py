'''
	Description: Project to analyse http headers of your app.
	Email: -
	Version: 0.1
'''

import sys
import urllib.request
import crayons
import urllib.parse


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
		return check_if_url_is_valid(sys.argv[1])


def display_message_in_color(message, status=WHITE):
	# displays messages in defined colors (white, red, yellow, orange, blue)
	if status not in _available_colors:
		raise Exception('Such a color is not supported!')
	print (status(message))

def check_if_url_is_valid(url):
	try:
		parsed = urllib.parse(url, allow_fragments=True)
		if parsed.scheme != '' and parsed.netloc != '':
			return True
		else:
			return False
	except:
		return False


def analyze_headers(url):
	# analyzes the http headers (https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#tab=Headers)
	server_response = urllib2.urlopen(url)
	# check for headers and set them status
	check_x_content_type_options(server_response.info())

def check_x_content_type_options(response_headers):
	headers_dict = response_headers.dict
	print(response_dict[X-Content-Type-Options])

def run():
	if validate_user_input() == True:
		url = sys.argv[1]
		analyze_headers(url)
	else:
		print("Not valid headers")
