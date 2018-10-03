# -*- coding: utf-8 -*-

#SMTP是发送邮件的协议，其中email负责构造邮件，smtplib负责发送邮件
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEBase, MIMEMultipart
from email.header import  Header
from email.utils import parseaddr,formataddr
from email import encoders
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))



#输入Email地址和口令
from_addr = input('From:')
#dsjxkppfdcecdeih
password = input('password:')#password必须是第三方授权码：qq邮箱->设置->账号->SMTP

#输入收件人的地址
to_addr = input('To :')

#输入SMTP的服务器地址
smtp_server = 'smtp.gmail.com'       #input('SMTP server:')#smtp.qq.com
#使用gmail,邮件加密传输
msg = MIMEMultipart()
#msg = MIMEText('Hello ,send by python from pycharm..,I just want to try ','plain','utf-8')
msg['From'] = _format_addr('From_addr:<%s>' % from_addr)
msg['To'] = _format_addr('To_addr:<%s>' % to_addr)
msg['Subject'] = Header('来自Smtp的问候....', 'utf-8').encode()
#第一个参数是邮件的正文，第二个参数'plain‘表示纯文本，第三参数表示utf-8编码

#邮件的正文是MIMEText
msg.attach(MIMEText('Hello ,send by python from pycharm..,I just want to try ','plain','utf-8'))

#添加附件，就是加上一个MIMEBase,从本地读取一张图片
with open('E:/微信宣传稿/图片/Image/1.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='1.jpg')
    mime.add_header('Content_Disposition', 'attachment', filename='1.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())

    encoders.encode_base64(mime)
    msg.attach(mime)

#smtp_port = 587      #Gmail的SMTP端口是587
server = smtplib.SMTP(smtp_server, 587)#smtp协议的默认端口是25
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,  password)
server.sendmail(from_addr, [to_addr], msg.as_string())
#这里的to_addr可以是多个地址，这样就可以实现群发邮件
server.quit()