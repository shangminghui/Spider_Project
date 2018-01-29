#-*- coding: utf-8 -*-

import paramiko
import threading


def sshclient_execmd(hostname,port,username,password,execmd):
    try:
        paramiko.util.log_to_file("paramiko.log")
        s=paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #指定当对方主机没有本机公钥的情况时应该怎么办，AutoAddPolicy表示自动在对方主机保存下本机的秘钥
        s.connect(hostname=hostname,port=port,username=username,password=password)
        stdin, stdout, stderr = s.exec_command(execmd)
        stdin.write("Y")
        out=stdout.readlines()
        for o in out:
            print(o)
        print("IP=" + hostname + " is ok " + str(threading.current_thread()))
        print("=======================")
        s.close()
    except:
        print("Error ip:%s connect" % hostname)
        print("=======================")
#单线程,如果ip无法连接，将做超时等待，特点为顺序执行。
def main_single():
    port = 22
    username = "root"
    password = ""
    execmd = "df -h"
    for last in range(17,60):
        hostname='197.0.0.%s'% last
        print("Connecting..."+hostname+"...")
        sshclient_execmd(hostname,port,username,password,execmd)


#多线程方式1，如果ip无法连接，将做放置末尾做超时等待处理，特点为处理速度加快。
def main_thread():
    threads=[]
    port = 22
    username = "root"
    password = ""
    execmd = "df -h"
    for last in range(17,60):
        hostname='197.0.0.%s'% last
        a=threading.Thread(target=sshclient_execmd,args=(hostname,port,username,password,execmd))
        a.start()

if __name__ == '__main__':
    main_single()




#================================================================================================
#多线程方式2
# def ssh2(ip,username,passwd,cmd):
#
#     try:
#
#         ssh = paramiko.SSHClient()
#
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#         ssh.connect(ip,22,username,passwd,timeout=5)
#
#         for m in cmd:
#
#             stdin, stdout, stderr = ssh.exec_command(m)
#
# #           stdin.write("Y")   #简单交互，输入 ‘Y’
#
#             out = stdout.readlines()
#
#             #屏幕输出
#
#             for o in out:
#
#                 print (o)
#
#         print ('%s\tOK\n'%(ip))
#
#         ssh.close()
#
#     except :
#
#         print ('%s\tError\n'%(ip))
#
#
#
#
#
# if __name__=='__main__':
#
#     cmd = ['df -h']#你要执行的命令列表
#
#     username = "root"  #用户名
#
#     passwd = "vimicro!@#"    #密码
#
#     threads = []   #多线程
#
#     print ("Begin......")
#
#     for i in range(17,60):
#
#         ip = '197.0.0.'+str(i)
#
#         a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
#         a.start()

