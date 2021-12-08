import platform 
import subprocess
from subprocess import PIPE
import socket
import threading

######## sistem windows mu linux mi ################
print(platform.system().lower())
###################################################

#### kodun calistigi bilgisayarin ipsini almak ##############
aa=[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]]
aa1=aa[0][1]
print(aa1)
###############################################################
iptaban=aa1.split(".")
###############################################################
myThreadList = []
ipliste=[]
###############################################################
def b1(a1,a2):
	iptaban=aa1.split(".")
	iptaban1=iptaban[0]+"."+iptaban[1]+"."+iptaban[2]+"."+a1
	iptaban2=iptaban[0]+"."+iptaban[1]+"."+iptaban[2]+"."+a2
	tarailk=iptaban1.split(".")
	tarailk1=int(tarailk[3])
	tarason=iptaban2.split(".")
	tarason1=int(tarason[3])
	for iii in range(tarailk1,tarason1):
		host=iptaban[0]+"."+iptaban[1]+"."+iptaban[2]+"."+str(iii)
		#comand1=['ping ','-n','1','-w','1',host]
		comand=['ping ',"-f",'-w','1','-n','1',host]
		if subprocess.call(comand,shell = False,stdout=PIPE) == 0 :
			#print("bulunan ip = "+host)
			ipliste.append(host)


#https://stackoverflow.com/questions/11968689/python-multithreading-wait-till-all-threads-finished



for aaa in range(0,255,10):
	#print("t"+str(aaa)+"  :"+str(aaa)+","+str(aaa+10))
	myThread=threading.Thread(target=b1,args=(str(aaa),str(aaa+10)))
	myThreadList.append(myThread)

for x in myThreadList:
     x.start()

for x in myThreadList:
	x.join()


def list_sort(xxx):
	fff=xxx.split(".")
	return int(fff[3])
#https://www.w3schools.com/python/ref_list_sort.asp	
ipliste.sort(key=list_sort)

print(len(ipliste))
for xxx in ipliste:
	print(xxx)
