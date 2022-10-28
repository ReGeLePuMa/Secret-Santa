import random
import smtplib
import json
from email import message

sender=str(input('Enter sender email:'))
sender_pass=str(input('Enter send email password/token:'))
session=smtplib.SMTP_SSL('smtp.gmail.com', 465)
session.login(sender,sender_pass)

with open('dictionary.txt') as f:
    data = f.read()

dict=json.loads(data)

subject="Secret Santa!"
body="Draga {},\nPersoana careia trebuie sa-i dai cadou este {}.\nSemnat, spiridusul lui Mos Craciun."

message="Subject:"+subject+"\n\n"+body

destinatar=list(dict.keys())
recipient=list(dict.keys())
random.shuffle(recipient)
i=0
#Shuffling such that all values have changed index
while True:
    if destinatar[i]==recipient[i]:
        random.shuffle(recipient)
        i=0
    else: 
        i=i+1    
    if i==len(destinatar):
        break
i=0
for nume in recipient:
    session.sendmail(sender,str(dict[nume]),message.format(str(nume),str(destinatar[i])))
    i=i+1

session.quit()    
