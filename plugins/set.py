import os
print("""
Vars you can change:-
1. USR [your name]
2. COM [your machine name]""")
var = input("Enter which var you want to change: ")
val = input("Enter its new value: ")
os.environ[var] = val
print("Error: Unknown")
