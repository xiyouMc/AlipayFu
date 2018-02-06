# coding=utf8

import commands,urllib

MAX_RETRY_TIME = 3

def run_command(cmd):
    retry = 0
    while retry < MAX_RETRY_TIME:
        status, output = commands.getstatusoutput(cmd)
        if status != 0:
            retry += 1
            continue
        return status, output

def search(word):
    params = {'word': word}
    url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&%s" % urllib.urlencode(params)
    cmd = u'open "{}"'.format(url)
    run_command(cmd=cmd)

if __name__ == '__main__':
    search('福') # 服了