'''
	Description: Project to analyse http headers of your app.
	Email: -
	Version: 0.1
'''

import sys
import urllib2
import urlparse




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
	pass

def check_if_url_is_valid(url):
	try:
		parsed = urlparse.urlparse(url, allow_fragments=True)
		if parsed.scheme != '' and parsed.netloc != '':
			return True
		else:
			return False
	except:
		return False


def analyze_headers(url):
	# analyzes the http headers (https://www.owasp.org/index.php/OWASP_Secure_Headers_Project#tab=Headers)
	pass


def run():
	if validate_user_input() === True:
		url = sys.argv[1]
		analyze_headers(url)