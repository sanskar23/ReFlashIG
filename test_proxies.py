#!/usr/bin/python
import cgi
import sys
import os
import optparse
import itertools
import json
import random
try:
	import urllib2
except ImportError:
	import urllib
import time
import requests
import threading
from datetime import datetime
import datetime as DT

print('''
-----------------------------------------

           Proxy List Checker            

      Developed By: @the.red.team3
	  
-----------------------------------------
''')

# USAGE
usage = ''

# SOME GLOBAL VARIABLES
global active_threads
global https_proxies

active_threads = 0
good_proxies = []

# COMMAND LINE ARGUMENTS
parser = optparse.OptionParser('%prog -x <proxy file> -o <output file>')
parser.add_option('-o', dest='output_file', type='string', help='File to save good proxies')
parser.add_option('-x', dest='proxy', type='string', help='File containing list of proxies')
parser.add_option('-t', dest='timeout', type='int', help='Instagram connection timeout')

(options, args) = parser.parse_args()



# LOAD PROXIES
try:
	with open(str(options.proxy)) as p:
		from_file = p.readlines()
except:
	print(usage)
	sys.exit()

https_proxies = []
for p_item in from_file:
	https_proxies.append(str(p_item).replace('\n', ''))
	
print('[!]   Proxies loaded: ' + str(len(https_proxies)))



# CLASS TO STORE USER CREDS
# YES I COPIED CODE FROM ReFlashIG AND DIDN'T GIVE AF
class User:
	username = ''
	password = ''


# URLS FOR VARIOUS FUNCTIONS
url = 'https://www.instagram.com/'

user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
				  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
accept_language = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'

# FUNCTION TO LOGIN AND GATHER INFO
def login(https_prox):
	global active_threads
	active_threads = active_threads + 1
	https_proxy = 'https://' + str(https_prox)
	proxy = {"https" : https_proxy}

	# ESTABLISH REQUEST SESISON
	s = requests.Session()
	s.cookies.update({
		'sessionid': '',
		'mid': '',
		'ig_pr': '1',
		'ig_vw': '1920',
		'csrftoken': '',
		's_network': '',
		'ds_user_id': ''
	})
	s.headers.update({
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': accept_language,
		'Connection': 'keep-alive',
		'Content-Length': '0',
		'Host': 'www.instagram.com',
		'Origin': 'https://www.instagram.com',
		'Referer': 'https://www.instagram.com/',
		'User-Agent': user_agent,
		'X-Instagram-AJAX': '1',
		'X-Requested-With': 'XMLHttpRequest'
	})
	
	# ACTUALLY LOGIN HERE
	
	bad_prox = False

	try:
		r = s.get(url, proxies=proxy, timeout=(options.timeout))
		s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
	
		if r.status_code == 200:
			bad_prox = False
			print('[!] Good proxy -> ' + str(https_prox))
			file = open(str(options.output_file), 'a')
			file.write(str(https_prox) + '\n')
			file.close()
		else:
			bad_prox = True
	except:
		bad_prox = True	

			
	if bad_prox == False:
		good_proxies.append(https_prox)
	active_threads = active_threads - 1

for prox in https_proxies:
	t = threading.Thread(target = login, args = (prox,))
	t.daemon = True
	t.start()
try:
	while active_threads > 0:
		time.sleep(0.5)
except KeyboardInterrupt:
	print('[!] Good Proxies -> ' + str(len(good_proxies)) + '/' + str(len(https_proxies)))
	sys.exit()

print('[!] Good Proxies -> ' + str(len(good_proxies)) + '/' + str(len(https_proxies)))
