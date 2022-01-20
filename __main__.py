import os

def do(command):
  os.system(commamd)

usr = open("db/usr.txt","r")
com = open("db/com.txt","r")

running = Ture
while running:
  raw_txt = input(f"•{usr}@{com}:~ ")
  s_txt = raw_text.split(" ")
  try:
    commamd = s_txt[0]
    print("Commamd: ",commamd)
  except:
    print("Error: No commamd detected")
    pass
    
