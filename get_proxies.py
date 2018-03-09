import sys
import time
from subprocess import Popen, PIPE

proxies = []

def get_list():
	command = 'wget --no-check-certificate -qO- "https://pubproxy.com/api/proxy?limit=20&format=txt"'

	stdout = Popen(command, shell=True, stdout=PIPE).stdout
	output = stdout.readlines()

	if len(output) > 1:
		for line in output:
			file = open(str(sys.argv[1]), 'a')
			if '\n' not in str(line):
				line = str(line) + '\n'
			proxies.append(line.replace('\n', ''))
			file.write(line)
			file.close()

		print('[!] Loaded ' + str(len(output)) + ' proxies')

	else:
		print('[!] Exceeded pull request limit')

count = int(sys.argv[2])
for i in range(0, count):
	get_list()
	time.sleep(1)

print('[!] Complete | Proxies loaded -> ' + str(len(proxies)))
