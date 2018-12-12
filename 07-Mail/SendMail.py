#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'此模块功能：发送邮件示例程序'

__author__ = 'HouBin'

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #发送带附件邮件时使用
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
#smtp_server = input('SMTP server: ')#smtp.163.com、smtp.qq.com
smtp_server = "smtp.163.com"

#发送纯文本邮件
msg = MIMEText('你好, 这是一封来自遥远地方的邮件。', 'plain', 'utf-8')#plain表示纯文本格式
msg['From'] = _format_addr('不告诉你先生 <%s>' % from_addr)
msg['To'] = _format_addr('不回答你小姐 <%s>' % to_addr)
msg['Subject'] = Header('来自远方的问候1……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

#发送HTML邮件
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>你好, 这是一封来自<a href="http://www.python.org">遥远地方</a>的邮件。</p>' +
    '</body></html>', 'html', 'utf-8')#html表示网页格式
msg['From'] = _format_addr('不告诉你先生 <%s>' % from_addr)
msg['To'] = _format_addr('不回答你小姐 <%s>' % to_addr)
msg['Subject'] = Header('来自远方的问候2……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

#发送带附件的邮件
#邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('不告诉你先生 <%s>' % from_addr)
msg['To'] = _format_addr('不回答你小姐 <%s>' % to_addr)
msg['Subject'] = Header('来自远方的问候3……', 'utf-8').encode()
#邮件正文是MIMEText
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p>你好, 这是一封来自<a href="http://www.python.org">遥远地方</a>的邮件（含附件）。</p>' +
    '</body></html>', 'html', 'utf-8'))#html表示网页格式
# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
#发送邮件
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

#发送带图片的邮件
#邮件对象
msg = MIMEMultipart()
msg['From'] = _format_addr('不告诉你先生 <%s>' % from_addr)
msg['To'] = _format_addr('不回答你小姐 <%s>' % to_addr)
msg['Subject'] = Header('来自远方的问候4……', 'utf-8').encode()
#邮件正文是MIMEText
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p>你好, 这是一封来自<a href="http://www.python.org">遥远地方</a>的邮件（含附件）。</p>' +
    '<p><img src="cid:0"></p>'+
    '</body></html>', 'html', 'utf-8'))#html表示网页格式
# 添加附件就是加上一个MIMEBase，从本地读取一个图片
with open('test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
#发送加密邮件
server = smtplib.SMTP(smtp_server,25)
#server = smtplib.SMTP_SSL(smtp_server,465) #163邮箱的ssl协议端口号中SMTP：465/994
#server.ehlo()
#server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
