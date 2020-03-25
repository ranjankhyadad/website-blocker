This application blocks the websites you don't want to access during a specific period of time, say work hours. 

---
To schedule the application on windows-
1. Change the extension of the python file from.py to.pyw
2. Open Task scheduler. Enter necessary details. Check "Run with highest priveleges". 
3. Go to Triggers-- Select "At startup". Check "Enable".
4. Go to Actions-- Select "Start a program". Give the location of the .pyw file.
5. Go to Conditions-- uncheck power options.
6. Run
---

---
On Mac/Linux:
1. Change the hosts filepath- /etc/hosts
2. Open terminal. Execute "sudo crontab -e"
3. @reboot python3 'Filepath of python file'
---
