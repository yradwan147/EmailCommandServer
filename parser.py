import poplib
import email
import os
from youtube_search import YoutubeSearch
from pathlib import Path
import smtplib, ssl
import time
import Encryptor
import Recommendor

## Setting up variables
files = []
formatted = ""
sender_email = ""
receiver_email = ""
password = ''

## Sort files by descending data modified and put them into a formatted string
paths = sorted(Path("C:/Users/LEGION/Music/soz English").iterdir(), key=os.path.getmtime, reverse=True)
loopcount = 10
k = 0
while k < loopcount:
    file = str(paths[k])
    if file[-4:] == ".jpg":
        loopcount += 1
    else:
        files.append(file[34:])
    k += 1

print(files)

for f in files:
    formatted += "> " + str(f) + "\n"
    search_term = str(f)[:len(str(f)) - 4] + " lyrics"
    results = YoutubeSearch(search_term, max_results=1).to_dict()
    link = "https://www.320youtube.com" + str(results[0].get("url_suffix"))
    formatted += str(link) + "\n"

## Set up message to send (1)
message = """\
Subject: Response

"""

## Infinite Loop to check every 30 seconds and reconnect
while(True):
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user(sender_email)
    pop_conn.pass_(password)

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    context = ssl.create_default_context()

    print ('success')
    numMessages = len(pop_conn.list()[1])
    print(numMessages)
    time.sleep(30)

    ## Look through inbox for relevant subjects on emails
    for i in range(numMessages):
        for j in pop_conn.retr(i+1)[1]:
            # print(j)
            msg = email.message_from_bytes(j)

            ## If subject is music, send message with latest 10 songs and delete email to avoid duplication
            if str(msg.get("Subject")) == "Music":
                pop_conn.dele(i+1)
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message + formatted)
            
            if "Encrypt" in str(msg.get("Subject")):
                keyword = str(msg.get("Subject"))[8:]
                encrypted = Encryptor.InstaEncrypt_email(keyword)
                pop_conn.dele(i+1)
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message + str(encrypted))

            if "Decrypt" in str(msg.get("Subject")):
                keyword = str(msg.get("Subject"))[8:]
                decrypted = Encryptor.decrypt_console(keyword)
                pop_conn.dele(i+1)
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message + str(decrypted))
            
            if "Uber" in str(msg.get("Subject")):
                keyword = str(msg.get("Subject"))[5:]
                uber_string = Recommendor.recommend(0, keyword)
                pop_conn.dele(i+1)
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message + str(uber_string))

    ## End connection to commit delete changes
    pop_conn.quit()

        


            
        
