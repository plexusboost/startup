# Full Program
# 0 = jacob, 1 = offero 2 = adoptthearts

bbb = 1 # 0 = user one. 1 = user two. 2 = user three.
machine_code = 1001
from checker import *
import requests
import sys
import json
import bs4
import time
from lxml import html
print(status)
# pull cloud code file
code1 = requests.get('http://plexuspremiergroup.com/latestcode/')
codetran = bs4.BeautifulSoup(code1.text)
latestcode = codetran.select('#program_software')
pullcode = latestcode[0].text
dd = open("program.py" ,"w+")
dd.write(str(pullcode))
dd.close()

cc = open("profilecode.py" , "w+")
cc.write(str("bbb = ") + str(bbb))
cc.write("\n")
cc.write(str("machine_code =") + str(machine_code))
cc.close()
time.sleep(5)

exec(open("program.py").read())
