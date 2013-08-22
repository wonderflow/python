# a python script used to bosh create cf-release
# as i can't tolerate the net speed downloading gems and it occur problems
# maybe there still some bugs
# you may delete some git in .cache if it occur problem such as some git can't be find
# you may use $tail -f b.txt  to find what happened
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
