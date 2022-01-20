import os
port = input("Enter port: ")
ip = input("Enter ip: ")
if ip == "lh":
  os.system(f"python -m http.server {port}")
  print("Started http server successfully")
  print(f"Link: http://localhost:{port}")
else
  try:
    os.system(f"python -m http.server {port} --bind {ip}")
    print("Started http server successfully")
    print(f"Link: http://{ip}:{port}")
