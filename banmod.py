#!/usr/bin/python
# -*- coding: utf-8-*-
import os,sys
def options():
	 os.system("setterm -foreground yellow")
	 print("""
+--------------------+
| 1)PERU(+51)        |
| 2)colombia(+57)    |
| 3)españa(+34)      |
| 4)mexico(+52)      |           
| 5)argentina(+54)   |
| 6)chile(+56)       |
+--------------------+""")
os.system('clear')
os.system("")
os.system('toilet -f future BANMOD')
options()
os.system('setterm -foreground red')
print("")
asd=raw_input("option > ")
if asd=="1":
	os.system('bash OPTS/PER/BANEO1.sh')
elif asd=="2":
	os.system('bash OPTS/COL/BANEO1.sh')
elif asd=="3":
	os.system('bash OPTS/ESP/BANEO1.sh')
elif asd =="4":
	os.system('bash OPTS/MEX/BANEO1.sh')
elif asd=="5":
	os.system('bash OPTS/ARG/BANEO1.sh')
elif asd=="6":
	os.system('bash OPTS/CHIL/BANEO1.sh')