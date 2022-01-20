import os
try:
  import requests as r
except:
  os.system("pip install requests")
  import requesr as r
link=input("Enter link: ")
o = r.get(link)
print(o)
next=input("Want text? [y/n]: ")
if next == "y":
  print(o.text)
else:
  pass
