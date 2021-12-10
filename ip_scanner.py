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
###############################################################
iptaban=aa1.split(".")

class scan:
	def __init__( self):

		self.host=""
		self.myThreadList = []
		self.iplist=[]
		self.ip_root=iptaban
	def b1(self,a1,a2):
		#iptaban=aa1.split(".")
		print("*-*-*-*",self.ip_root)
		iptaban1=self.ip_root[0]+"."+self.ip_root[1]+"."+self.ip_root[2]+"."+a1
		iptaban2=self.ip_root[0]+"."+self.ip_root[1]+"."+self.ip_root[2]+"."+a2
		tarailk=iptaban1.split(".")
		tarailk1=int(tarailk[3])
		tarason=iptaban2.split(".")
		tarason1=int(tarason[3])
		for iii in range(tarailk1,tarason1):
			self.host=self.ip_root[0]+"."+self.ip_root[1]+"."+self.ip_root[2]+"."+str(iii)
			#comand1=['ping ','-n','1','-w','1',host]
			print("+++",self.host)
			self.comand=['ping ',"-f",'-w','1','-n','1',"-i","1",self.host]
			if subprocess.call(self.comand,shell = False,stdout=PIPE) == 0 :
				print("bulunan ip = "+self.host)
				self.iplist.append(self.host)

	def list_sort(self,xxx):
			fff=xxx.split(".")
			return int(fff[3])

	def ip_scan(self,ip_begin,ip_end):
		self.myThreadLis=[]
		for aaa in range(ip_begin,ip_end,10):
			self.myThread=threading.Thread(target=self.b1,args=("140","160"))
			#self.myThread=threading.Thread(target=self.b1("140","160"))
			self.myThreadList.append(self.myThread)

		for xxx in self.myThreadList:
			print(xxx)
			xxx.start()

		for xxx in self.myThreadList:
			print("***")
			xxx.join()

		#https://www.w3schools.com/python/ref_list_sort.asp	
		#self.iplist.sort(key=self.list_sort)
		return self.iplist
	
	def ipdeneme(self,aa,bb):
		self.b1(str(aa),str(bb))
		return self.iplist





	



