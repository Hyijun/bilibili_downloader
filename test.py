import requests as req

header_1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Cookie': 'buvid3=00000000-0000-0000-0000-000000000000000000infoc; LIVE_BUVID=AUTO0000000000000000; '
              ' im_notify_type_1=0',
    'Host': 'www.bilibili.com'

}

video_url = 'https://www.bilibili.com/video/av36617850'
video_url_html = req.get(video_url, headers=header_1).text
print(video_url_html)

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(video_url_html)

