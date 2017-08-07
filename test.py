#coding=utf8
import thread
import sys
import requests
#import time
#sys.setdefaultencoding('utf-8')
requests.packages.urllib3.disable_warnings()
########################################################
def validUsefulProxy(proxy,url):
    """
    检验代理可以性
    :param proxy:
    :return:
    """
    proxies = {"http": "http://{proxy}".format(proxy=proxy),
                "https": "https://{proxy}".format(proxy=proxy)}
    try:
        r = requests.get(url, proxies=proxies, timeout=3, verify=False)
        if r.status_code == 200:
            #
            print proxy+'\r\n'+r.text+'\r\n#######################\r\n'
            #
            return True
    except Exception, e:
        #print proxy,False
        return False

###########################################################

########################################################
def validGet(url):
    try:
        r = requests.get(url, timeout=3, verify=False)
        if r.status_code == 200:
            #
            print url+'\r\n'+r.text + '\r\n#######################\r\n'
            #
            return True
    except Exception, e:
        #print proxy,False
        return False

###########################################################
def scan(ip,port,lock):
    #validUsefulProxy('10.0.0.172:80','http://rd.go.10086.cn/go/open.do')
    #validGet('http://rd.go.10086.cn/go/open.do')
    #print ip+ '\r\n'
    #validGet('http://'+ip)
    validUsefulProxy(ip, 'http://rd.go.10086.cn/go/open.do')
    lock.release()
###########################################################
if __name__ == '__main__':
    locks = []
    fip='111.13'
    port=80
    try:
        for x in range(0,256):
            for y in range(0,256):
                lock = thread.allocate_lock()
                lock.acquire();
                locks.append(lock);
                #port= x*y
                ip=fip+'.'+str(x)+'.'+str(y)
                #ip=fip+str(x)
                thread.start_new_thread(scan,(ip,port,lock))
                print ip
            for lock in locks:
                while lock.locked():
                    pass
    except KeyboardInterrupt:
        print 'FUCK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        sys.exit(0)
