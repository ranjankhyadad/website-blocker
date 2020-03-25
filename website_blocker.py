import time
from datetime import datetime as dt

hosts_path = r'C:\Windows\System32\drivers\etc'
hosts_temp = "hosts"
website_list = ["www.youtube.com", "youtube.com"]
redirect = "127.0.0.1"

while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17)):
        print("Working now..")
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Spare Time..")
    time.sleep(5)
