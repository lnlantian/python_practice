最近一段时间的学习中发现，Python基本和中文字符杠上了。如果能把各种编码问题解决了，基本上也算对Python比较熟悉了。

For UTF-8 encoding, Excel requires BOM (byte order mark) codepoint written at the start of the file or it will assume ANSI encoding, which is locale-dependent.
对于UTF-8编码，Excel要求BOM(字节顺序标记)写在文件的开始，否则它会假设这是ANSI编码，这个就是与locale有依赖性了。

#!python2
#coding:utf8
import csv

data = [[u'American',u'美国人'],
        [u'Chinese',u'中国人']]

with open('results.csv','wb') as f:
    f.write(u'\ufeff'.encode('utf8'))
    w = csv.writer(f)
    for row in data:
        w.writerow([item.encode('utf8') for item in row])
考虑到兼容性，Python3的处理方法就比较简单了。

#!python3
#coding:utf8
import csv

data = [[u'American',u'美国人'],
        [u'Chinese',u'中国人']]

with open('results.csv','w',newline='',encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerows(data)
或者你可以使用个第三方模块unicodecsv

#!python2
#coding:utf8
import unicodecsv

data = [[u'American',u'美国人'],
        [u'Chinese',u'中国人']]

with open('results.csv','wb') as f:
    w = unicodecsv.writer(f,encoding='utf-8-sig')
    w.writerows(data)

作者：bluescorpio
链接：https://www.jianshu.com/p/87b60b696780
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
