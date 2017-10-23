'''
	Description: Project to analyse http headers of your app.
	Email: -
	Version: 0.1
'''

import sys
import urllib2




def validate_user_input():
	if len(sys.argv) < 2:
		return False
	else:
		return check_if_url_is_valid(sys.argv[1])


def display_message_in_color(message, status=WHITE):
	# displays messages in defined colors (white, red, yellow, orange, blue)
	pass

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