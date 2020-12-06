#-*-coding:UTF-8-*-

import urllib
import urllib2
import codecs
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# User-Agent告诉服务器用户访问的方式
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
headers = {'User-Agent' : user_agent}

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    # 解码成unicode
    data = response.read().decode('utf-8')
except urllib2.HTTPError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        e.reason
except urllib2.URLError, e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        e.reason

if isinstance(data, unicode):
    print '*' * 50
    print 'data is unicode'
    print '*' * 50

s = '<a href="/article/(\d*?)" target="_blank" class="contentHerf" onclick=".*?">\n+<div class="content">\n+<span>\n+(.*?)</span>\n+?</div>\n+?</a>'
pattern = re.compile(s, re.S)
# 对于匹配模式字符串中带有分组的，findall返回分组构成的tuple
items = re.findall(pattern, data)

print '*' * 50
print 'open file'
print '*' * 50
file_name = 'spider_data.txt'
# open打开文件只能写入str类型
# fw = open(file_name, 'wb')
# fw.write(data)
fw = codecs.open(file_name, 'w', encoding='utf-8')

for item in items:
    print '*' * 50
    print 'write data to file'
    print '*' * 50
    fw.write(item[0])
    fw.write('\n')
    fw.write(item[1])
    fw.write('\n')
    
print '*' * 50
print 'close file'
print '*' * 50
fw.close()
