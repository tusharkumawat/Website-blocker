import time
from datetime import datetime as dt

# path to host file
host_path="C:/Windows/System32/drivers/etc/hosts"

# redirect to localhost
redirect="127.0.0.1"

# websites to block
websites_list=["www.netflix.com","www.google.com","www.amazon.com","www.facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,22):
        file=open(host_path,"r+")
        content = file.read()
        for website in websites_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
        print("Work time, web blocker ON")
    else:
        file = open(host_path,"r+")
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites_list):
                file.write(line)
            file.truncate()
        print("Web blocker OFF")
    time.sleep(5)
