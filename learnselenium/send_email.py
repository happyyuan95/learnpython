import smtplib
from email.mime.text import MIMEText
from email.header import Header

subject = "python mail test"

msg = MIMEText("<html><hl>hello everyone!<hl>", "html", "utf-8")
msg["subject"] = Header(subject, "utf-8")

smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com")
smtp.login("1067715622@qq.com", "music0923.")
smtp.sendmail("1067715622@qq.com", "1067715622@qq.com", msg.as_string())
smtp.quit()