# -*- coding: cp936 -*-
import time
import urllib2
import urllib
import re

print "Loading...."
cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)
urllib2.install_opener(opener)
params = {'stuid':'è´¦å·','pwd':'å¯ç '}
loginUrl = 'http://ç®¡çåç»å½ç½å'
login = urllib2.urlopen(loginUrl,urllib.urlencode(params))
var = login.read();
#print var

loginUrl = 'æç»©æ¥è¯¢çç½å'

stu = [];
for bj in range(1,7) :
    for stuid in range(1,51) :
        fm = "æ¥è¯¢å­¦å·çåç¼%d"%(bj)
        if stuid<10 :
            fm = "%s0%d"%(fm,stuid)
        else:
            fm = "%s%d"%(fm,stuid)
        stu.append(fm)


#jd = re.compile('''<font face="é»ä½" size="3" color="#0099CC">ç®åè¯¥çææå·²ä¿®è¯¾ç¨çå¹³åå­¦åç»©ç¹ï¼(.*)</font>''')
digs = re.compile('''<tr>(.*\n.*)<td bgColor="#eeeeee" align="center"><font size="2">(.*)</font></td>(.*\n.*)<td bgColor="#eeeeee" align="center" width="63"><font size="2">(.*)</font></td>(.*\n.*)<td bgColor="#eeeeee" align="center" width="68"><font size="2">(.*)</font></td>(.*\n.*)<td bgColor="#eeeeee" align="center" width="219"><font size="2">(.*)</font></td>(.*\n.*)<td bgColor="#eeeeee" align="center" width="35"><font size="2">(.*)</font></td>(.*\n.*)<td bgColor="#eeeeee" align="center" width="52"><font size="2">(.*)</font></td>(.*\n.*)<td bgColor="#eeeeee" align="center" width="56"><font size="2">(.*)</font></td>(.*\n.*)</tr>''')


fileHandle = open ('09.txt', 'w') 
for i in range(0,300) :
    params = {'p_xh':stu[i]}
    login = urllib2.urlopen(loginUrl,urllib.urlencode(params))
    var = login.read();
   # b = jd.match(var)
   # fileHandle.write("%s\n"%(b.group(1)))
    a = digs.findall(var)
    l = len(a)
    for pi in range(0,l):
        for j in range(1,8):
            fileHandle.write(a[pi][2*j-1]+" ")
        fileHandle.write("\n")
    print stu[i]+"SUCCEED"
fileHandle.close()
