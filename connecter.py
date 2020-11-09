import random
import time
import urllib2


def main():
    accounts = open('useful_account_dic.txt', 'r').read().splitlines()
    passwords = open('useful_password_dic.txt', 'r').read().splitlines()
    print 'Program Running.'

    while (True):
        index = random.randint(0, len(accounts))
        print index
        while (True):
            if checkNetwork():
                time.sleep(3)
                continue
            else:
                break
        if login(accounts[index], passwords[index]):
            continue
        else:
            break


def login(usr, pwd):
    result = urllib2.urlopen(
        'http://172.16.13.2/drcom/login?callback=x&DDDDD=' + usr + '&upass=' + pwd + '&0MKKey=123456', data=None,
        timeout=20).read()
    return result[17] == '1'


def checkNetwork():
    try:
        urllib2.urlopen('https://www.baidu.com')
        return True
    except urllib2.URLError:
        return False




main()
