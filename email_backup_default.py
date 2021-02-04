
# Importing modules

import os, sys, imaplib, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Parse & update the tracklist in the txt file

sys.stdout = open('D:\\miscellaneous\\__scripts\\python\\backup_updater\\dist\\File3.txt', 'w')
path = 'D:\musica\My_music\Selection'

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.mp3' in file:
            files.append(os.path.join(file))
print()
for f in files:
    print(f)
sys.stdout.close()

# Delete current mail from last backup

username = "username"
password = "password"

box = imaplib.IMAP4_SSL('imap.gmail.com', 993); box.login(username, password)
box.select('Inbox'); typ, data = box.search(None, 'from', username)

for num in data[0].split(): 
   box.store(num, '+FLAGS', '\\Deleted')
box.expunge(); box.close(); box.logout()

# Send email with attached updated files

fromaddr = username; toaddr = username; subject = "Backup"
msg = MIMEMultipart(); msg['From'] = fromaddr; msg['To'] = toaddr; msg['Subject'] = subject; body = " " 
msg.attach(MIMEText(body, 'plain')) 
  
file1 = "File1.txt"; attachment1 = open(file1, "rb"); part1 = MIMEBase('application', 'octet-stream')
part1.set_payload((attachment1).read()); encoders.encode_base64(part1)
part1.add_header('Content-Disposition', "attachment1; filename= " + file1)

file2 = "File2.txt"; attachment2 = open(file2, "rb"); part2 = MIMEBase('application', 'octet-stream')
part2.set_payload((attachment2).read()); encoders.encode_base64(part2)
part2.add_header('Content-Disposition', "attachment2; filename= " + file2)

file3 = "File3.txt"; attachment3 = open(file3, "rb"); part3 = MIMEBase('application', 'octet-stream')
part3.set_payload((attachment3).read()); encoders.encode_base64(part3)
part3.add_header('Content-Disposition', "attachment3; filename= " + file3)
 
msg.attach(part1); msg.attach(part2); msg.attach(part3); text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587); s.starttls(); s.login(username, password)
s.sendmail(username, username, text); s.quit()





