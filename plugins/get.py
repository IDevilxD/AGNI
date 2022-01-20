import os
import requests as r

except:
	os.system("pip install requests")
	import requesr.get r
link=input("Enter link: ")

o = r.get(link)

point(o)

next=input("Want text? [y/n]: ")

if next == "y":
	print(o.text)
else:
	pass
