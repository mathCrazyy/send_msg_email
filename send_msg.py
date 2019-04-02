#coding: utf-8    
  
import smtplib    
from email.mime.multipart import MIMEMultipart    
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage 
from email.header import Header   
    
#设置smtplib所需的参数
#下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.163.com'
username = 'xx@163.com'
password='***'
sender='xx@163.com'
#receiver='mathcrazy4660@163.com'
receiver='xx@163.com'
#收件人为多个收件人
#receiver=['XXX@126.com','XXX@126.com']

subject = 'Python email test'
#通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
#subject = '中文标题'
#subject=Header(subject, 'utf-8').encode()
    
#构造邮件对象MIMEMultipart对象
#下面的主题，发件人，收件人，日期是显示在邮件页面上的。
msg = MIMEMultipart('mixed') 
msg['Subject'] = subject
msg['From'] = 'xx@163.com <xx@163.com>'
#msg['To'] = 'XXX@126.com'
#收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ";".join(receiver) 
#msg['Date']='2012-3-16'

#构造文字内容   
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"    
text_plain = MIMEText(text,'plain', 'utf-8')    
msg.attach(text_plain)    

#构造图片链接

#构造html

#发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>

#构造附件
#以下附件可以重命名成aaa.txt  
#text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
#另一种实现方式
#以下中文测试不ok
#text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
#msg.attach(text_att)    
"""       
#发送邮件
smtp = smtplib.SMTP()    
smtp.connect('smtp.163.com')
#我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
#smtp.set_debuglevel(1)  
smtp.login(username, password)    
smtp.sendmail(sender, receiver, msg.as_string())    
smtp.quit()
"""
import sys
def send_msg(pid,description):




    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = 'xx@163.com <xx@163.com>'
    msg['To'] = ";".join(receiver)

#构造文字内容   
    text = str(str(pid))+description+"is finished"
    text_plain = MIMEText(text,'plain', 'utf-8')
    msg.attach(text_plain)

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    #我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    #smtp.set_debuglevel(1)  
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
#send_msg()
