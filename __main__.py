import os
from DB import *

def do(command):
  os.system(command)

#v1 = open("/data/data/com.termux/files/home/AGNI/db/usr.txt","r")
#v2 = open("/data/data/com.termux/files/home/AGNI/db/com.txt","r")

#usr = v1.read()
#com = v2.read()

termux_cmd = ["update","clear"]

running = True
while running:
  try:
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
    else:
      pass
    if command == "clear":
      do("clear")
    else:
      pass
    if command in termux_cmd:
      print("Type: Termux")
      pass
    else:
      print("Type: AGNI")
      do(f"cd plugins && python {command}")
  except:
    pass
    
