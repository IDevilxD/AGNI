import os
from DB import *

def do(command):
  os.system(command)

#v1 = open("/data/data/com.termux/files/home/AGNI/db/usr.txt","r")
#v2 = open("/data/data/com.termux/files/home/AGNI/db/com.txt","r")

#usr = v1.read()
#com = v2.read()

running = True
while running:
  raw_txt = input(f"•{usr}@{com}:~ ")
  s_txt = raw_txt.split(" ")
  try:
    command = s_txt[0]
    print("Commamd: ",command)
  except:
    print("Error: No commamd detected")
    pass
  if command == "update":
    do("cd $HOME && rm -rf AGNI && git clone https://github.com/IDevilxD/AGNI")
  if command == "clear":
    do("clear")
    
