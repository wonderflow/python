########################
# usage :
# python http_client.py
#
# change the url you need to test
#
#######################

import urllib2 
import time
import socket 

myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
url = 'http://www.baidu.com'
num = 0

while(True):
    try:
       uopen = urllib2.urlopen(url)
       print '.'
    except urllib2.HTTPError,e:
        num = num+1
        print "failed at",
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        file = open('recode.txt','a')
        file.write('my ip :' + myaddr+' ')
        file.write('failtime: '+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'\n')
        file.close()
        sum = open('sum.txt','w')
        sum.write(str(num))
        sum.close()
    else :
        time.sleep(1)

