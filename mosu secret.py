import random
import smtplib
from email import message

sender="" # Include sender's email
sender_pass="" # Include sender's email password/ token for app use
session=smtplib.SMTP_SSL('smtp.gmail.com', 465)
session.login(sender,sender_pass)

dict={
    """To add items in format {Name}:{Email address}"""
}

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
