#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def alarm_email():
    from_addr = '发件邮箱@163.com'
    password = '邮箱系统开启IMAP/SMTP服务后提供的密码'
    to_addr = '收件邮箱@qq.com'
    smtp_server = 'smtp.163.com'
    msg = MIMEText('正文', 'plain', 'utf-8')
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('标题')
    server = smtplib.SMTP_SSL()
    server.connect(smtp_server, 465)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
    print('已发送邮件')
    
    
def check():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    url='https://api.nike.com/customization/builder_availability/v1?filter=countryCode(CN)&filter=locale(zh_CN)&filter=pathName(af1LowEssSP20)&channelId=public'
    headers = {'nike-api-caller-id': 'com.nike:commerce.idpdp.mobile'}
    res =requests.get(url=url, headers = headers)
    res_json = res.json()
    try:
        if "objects" in res_json:
            info=res_json["objects"][0]
            if info["shortMessage"].find("售罄")!=-1:
                print("卖完了")
            else:
                sizes_table=info["sizes"]
                quantity= int(sizes_table["5.5"]["quantity"])
                print("35.5数量：",quantity)
                if quantity!=0:
                    import subprocess
                    subprocess.call("D:\PotPlayer\PotPlayerMini.exe D:\PotPlayer\/alarm.mp3")
    except Exception:
        print("error!")


while(1):
    check()
    time.sleep(10)
