import re
import os

def Test(fPath):
    # fPath = r'C:\Users\jackw\Documents\弹幕姬\Plugins\DanmuLog\Data-10313214-20220116.txt'
    fp = open(fPath,'r',encoding='utf-8')
    lines = fp.readlines()
    lastLine = lines[-1]
    print(lastLine)
    test= lastLine
    pattern = r'Uname":"([\w\u4E00-\u9FA5\-_]{4,16}[^"])", "Comment":"([\w\u4E00-\u9FA5\-_#]{1,16})"'
    print ("输入："+test)
    username = re.search(pattern, test).group(1)
    rawComment = re.search(pattern, test).group(2)
    print ("username  " +username +"\nrawCommnet   "+rawComment)
    fp.close()