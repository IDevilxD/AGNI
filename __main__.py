import os

def do(command):
  os.system(commamd)

usr = open("/data/data/com.termux/files/home/AGNI/db/usr.txt","r")
com = open("/data/data/com.termux/files/home/AGNI/db/com.txt","r")

running = True
while running:
  raw_txt = input(f"•{usr.read}@{com.read}:~ ")
  s_txt = raw_txt.split(" ")
  try:
    commamd = s_txt[0]
    print("Commamd: ",commamd)
  except:
    print("Error: No commamd detected")
    pass
    
