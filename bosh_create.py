# a python script used to install bosh
# maybe there still some bugs
import re
import time
import os
com = re.compile('''(.*)`(.*)' pre-packaging(.*)''')
gem = re.compile('''(.*)Failed to fetch (.*),(.*)''')
num = 0
while True:
	a = os.system('bosh create release --force --with-tarball > b.txt')
	if a == 0: break
	filehander = open('b.txt','r')
	name = ""
	gemname = ""
	while True:
		var = filehander.readline()
		if var =="":break
		ll = com.match(var)
		gemreg = gem.match(var)
		if ll is not None :
			print var
			name = com.match(var).group(2)
		if gemreg is not None :
			print var
			gemname = gem.match(var).group(2)
	filehander.close()
	if name != "":
		print "error occur: "+name
		del_str = "rm -rf .dev_builds/packages/"+name
		os.system(del_str)
		print del_str
	if gemname != "":
		del_cache = "rm -rf .cache/fetch_gems/"+gemname
		os.system(del_cache)
		print del_cache
	num = num+1
	print "time failed ",num
	time.sleep(1)
	print ""
