# nike_by_you_check
nike官网专属定制补货提醒，官网一般是早上八点以后开始补货，可在这个时候运行脚本进行蹲守。

代码中蹲守款式为air-force-1-low女款
https://www.nike.com/cn/u/custom-nike-air-force-1-by-you-10000831/936687443

在开发者模式下，network标签下搜索“售罄”发现是通过：https://api.nike.com/customization/builder_availability/v1?filter=countryCode(CN)&filter=locale(zh_CN)&filter=pathName(af1LowEssSP20)&channelId=public  这个api返回的：


Request Header内容为：
```
Accept: application/json, text/plain, */*
nike-api-caller-id: com.nike:commerce.idpdp.mobile
Origin: https://www.nike.com
Referer: https://www.nike.com/cn/u/custom-nike-air-force-1-by-you-10000831/1583806413614
User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Mobile Safari/537.36
```

Response Header为：
```
access-control-allow-credentials: true
access-control-allow-headers: nike-api-caller-id
access-control-allow-origin: *
access-control-expose-headers: Date,WWW-Authenticate
akamai-age-ms: 1588255687755
cache-control: private, max-age=0
content-encoding: gzip
content-length: 457
content-type: application/json;charset=UTF-8
date: Thu, 30 Apr 2020 14:08:07 GMT
expires: Thu, 30 Apr 2020 14:08:07 GMT
status: 200
vary: Accept-Encoding
x-b3-traceid: 99c94a9bcb7e449f
x-edgeconnect-midmile-rtt: 233
x-edgeconnect-origin-mex-latency: 23
```

Response内容为：
```
{"objects":[{"styleColor":"AQ3778-994","shortMessage":"已售罄","longMessage":"该款定制运动鞋为每日限量发布，目前暂不提供。敬请留意最新供货情况。谢谢！","leadtimeUpperBoundInDays":-1,"sizes":{"11":{"size":"11","quantity":0},"9.5":{"size":"9.5","quantity":0},"12":{"size":"12","quantity":0},"11.5":{"size":"11.5","quantity":0},"10.5":{"size":"10.5","quantity":0},"5":{"size":"5","quantity":0},"6":{"size":"6","quantity":0},"7":{"size":"7","quantity":0},"8":{"size":"8","quantity":0},"9":{"size":"9","quantity":0},"5.5":{"size":"5.5","quantity":0},"6.5":{"size":"6.5","quantity":0},"7.5":{"size":"7.5","quantity":0},"10":{"size":"10","quantity":0},"8.5":{"size":"8.5","quantity":0}},"isAvailable":false},{"styleColor":"CT7875-994","shortMessage":"已售罄","longMessage":"该款定制运动鞋为每日限量发布，目前暂不提供。敬请留意最新供货情况。谢谢！","leadtimeUpperBoundInDays":-1,"sizes":{"11":{"size":"11","quantity":0},"9.5":{"size":"9.5","quantity":0},"12":{"size":"12","quantity":0},"13":{"size":"13","quantity":0},"14":{"size":"14","quantity":0},"15":{"size":"15","quantity":0},"16":{"size":"16","quantity":0},"17":{"size":"17","quantity":0},"18":{"size":"18","quantity":0},"11.5":{"size":"11.5","quantity":0},"10.5":{"size":"10.5","quantity":0},"6":{"size":"6","quantity":0},"7":{"size":"7","quantity":0},"8":{"size":"8","quantity":0},"9":{"size":"9","quantity":0},"6.5":{"size":"6.5","quantity":0},"7.5":{"size":"7.5","quantity":0},"12.5":{"size":"12.5","quantity":0},"8.5":{"size":"8.5","quantity":0},"10":{"size":"10","quantity":0}},"isAvailable":false}],"errors":[]}
```

在get请求里必须加上nike-api-caller-id:com.nike:commerce.idpdp.mobile才能得到返回结果，如果不加则返回：
```
{
    "error_id": "66507306-e5f9-4c8e-a62e-111d9f4e9520",
    "errors": [
        {
            "code": "CLIENT_UNAUTHORIZED",
            "message": "Client nike-api-caller-id header is not authorized."
        }
    ]
}
```

每十秒钟一次监控是否补货，有补货则使用PotPlayer播放报警mp3

**2020/5/30更新**


试了一下通过python发送邮件的方法，也很简单，申请一个新邮箱，在【设置】页面的POP3/SMTP/IMAP标签，给它开启IMAP/SMTP服务，邮箱系统会给一个密码，把它填入下面的password即可。smtp_server是发件邮箱的地址，如果是163或者qq邮箱是不同的，在邮箱系统的页面上会标注的。
```
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
```
