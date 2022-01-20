import os

def do(command):
  os.system(commamd)

usr = open("/data/data/com.termux/files/home/AGNI/db/usr.txt","r")
com = open("/data/data/com.termux/files/home/AGNI/db/com.txt","r")
print(usr.read)
print(com.read)


running = True
while running:
  raw_txt = input(f"•{usr.read}@{com.read}:~ ")
  s_txt = raw_txt.split(" ")
  try:
    command = s_txt[0]
    print("Commamd: ",command)
  except:
    print("Error: No commamd detected")
    pass
  if command == "update":
    do("cd $HOME && rm -rf AGNI && git clone https://github.com/IDevilxD/AGNI")
    
