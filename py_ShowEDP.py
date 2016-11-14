#!/usr/bin/python

import getpass
import sys
import telnetlib
import time
import re

#####
##### Variables globales

HOST = sys.argv[1]
#HOST = "10.0.0.254"
user = raw_input("Enter your remote account: ")
#user = "user"

password = getpass.getpass()
#password = "password"

###
###
### Conectando Telnet
###

tn = telnetlib.Telnet(HOST)
tn.open(HOST,23,60)
tn.read_until("login: ")
tn.write(user + "\n")

#if password:
tn.read_until("Password: ")
tn.write(password + "\n")
##
##
##
## Ejecucion de comandos
##
##
################################


tn.write("show edp port all\n")
tn.write("exit\n")
str = tn.read_all()
var= ["SwitchName"]
i=1
for i in range(len(var)):
#       x = ( str.find(var[i]) + len(var[i]) )
#       y = len(str)

        x = str.find(var[i])
        y = len(str)

        #print var[i]
        sstr = str[x:y]
        print sstr
        ans = sstr[0:sstr.find("\n")-1].strip()
#       print "\n\t"+ var[i] + "\t" +ans
#       svar = re.sub(r' .*$\n', "",sstr)
#       print var[i]
#       print svar

#       print str[x:]
#       print "======================\n"


