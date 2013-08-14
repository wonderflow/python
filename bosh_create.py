import re
import time
import os
com = re.compile('''(.*)`(.*)' pre-packaging(.*)''')
num = 0
while True:
	a = os.system('bosh create release --force --with-tarball > b.txt')
	if a == 0: break
	filehander = open('b.txt','r')
	name = ""
	while True:
		var = filehander.readline()
		if var =="":break
		ll = com.match(var)
		if ll is not None :
			print var
			name = com.match(var).group(2)
	filehander.close()
	if name != "":
		print "error occur: "+name
		del_str = "rm -rf .dev_builds/packages/"+name
		os.system(del_str)
		print del_str
	num = num+1
	print "time failed ",num
	time.sleep(1)
