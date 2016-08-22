import getpass
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromaddr = raw_input("From : ")
toaddr = raw_input("TO :")
p_w_d = getpass.getpass("PASSWORD :")
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = raw_input("SUBJECT OF THE MAIL :")
body = raw_input("YOUR MESSAGE HERE :")
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
print "[+] Connecting To Mail Server.\n"
server.starttls()
print "[+] Logging Into Mail Server.\n"
server.login(fromaddr, p_w_d)
text = msg.as_string()
print "[+] Sending Mail"
server.sendmail(fromaddr, toaddr, text)
print "[+] Mail Sent Successfully.\n"
server.quit()
