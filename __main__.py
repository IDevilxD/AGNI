import os
from DB import *

check = True
while check:
  password = input("Enter your password: ")
  if password == passw:
    break
  
print(logo)

def do(command):
  os.system(command)

#v1 = open("/data/data/com.termux/files/home/AGNI/db/usr.txt","r")
#v2 = open("/data/data/com.termux/files/home/AGNI/db/com.txt","r")

#usr = v1.read()
#com = v2.read()

os.environ["USR"] = "usr"
os.environ["COM"] = "system"

usr = os.environ.get("USR")
com = os.environ.get("COM")
termux_cmd = ["update","clear"]

to = input("Enter 'Y' to start:  ")
to = to.lower()

if to == "y":
  running = True
  while running:
    try:
      raw_txt = input(f"•{usr}@{com}:~ ")
      raw_txt = raw_txt.lower()
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
        print(logo)
      else:
        pass
      if command in termux_cmd:
        print("Type: Termux")
        pass
      else:
        print("Type: AGNI")
        try:
          do(f"cd /data/data/com.termux/files/home/AGNI/plugins && python {command}.py")
        except:
          print("Command {command} not found")
      if commamd == "agni":
        try:
          opt = s_txt[1]
          module = s_txt[2]
          if opt == "install":
            do(f"cd .storage && pip install virtualenv && virtualenv py-op && ./py-op active && pip install {module}")
        except:
          pass
    except:
      pass
else:
  try:
    import virtualenv
    if os.path.exists("/data/data/com.termux/files/home/AGNI/Agni") == False:
      do("pip install virtualenv && cd /data/data/com.termux/files/home/AGNI/ && virtualenv Agni && cd Agni && source activate")
    else:
      do("cd /data/data/com.termux/files/home/AGNI/Agni && source activate")
  except:
    do("pip install virtualenv")
    if os.path.exists("/data/data/com.termux/files/home/AGNI/Agni") == False:
      do("pip install virtualenv && cd /data/data/com.termux/files/home/AGNI/ && virtualenv Agni && cd Agni && source activate")
    else:
      do("cd /data/data/com.termux/files/home/AGNI/Agni && source activate")
    
