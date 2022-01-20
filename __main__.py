import os

def do(command):
  os.system(commamd)

usr = file.open("db/usr.txt","r")
com = file.open("db/com.txt","r")

running = Ture
while running:
  raw_txt = input(f"•{usr}@{com}:~ ")
  s_txt = raw_text.split(" ")
  try:
    commamd = s_txt[0]
    print("Commamd: ",commamd)
