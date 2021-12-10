
import wxpyhton_taslak_2
import wx 
import ip_scanner1 
import socket



aa=[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]]
aa1=aa[0][1]
###############################################################
iptaban=aa1.split(".")

class araYuzDeneme(wxpyhton_taslak_2.MyFrame2):
	def __init__(self,parent):
		wxpyhton_taslak_2.MyFrame2.__init__(self,parent)
		self.baslangic_ip_Txt=iptaban[0]+"."+iptaban[1]+"."+iptaban[2]+"."+"0"
		self.son_ip_Txt=iptaban[0]+"."+iptaban[1]+"."+iptaban[2]+"."+"255"
		self.m_textCtrl2.SetLabel(self.baslangic_ip_Txt)
		self.m_textCtrl3.SetLabel(self.son_ip_Txt)
		self.satirSayisi=255
		self.satirisim()


	def portTara(self,event):
		ip_scanner1.iplist=[]
		self.m_grid3.DeleteRows(0,self.m_grid3.GetNumberRows(),True)
		
		self.m_button2.SetLabel("Scanning")

		c1=self.baslangic_ip_Txt.split(".")
		c2=int(c1[3])
		d1=self.son_ip_Txt.split(".")
		d2=int(d1[3])

		aaa = ip_scanner1.ip_scan(c2,d2)

		if len(aaa)!=0:
			self.m_grid3.AppendRows(len(aaa))
			for bbb in range(0,len(aaa)):
				self.m_grid3.SetCellValue(bbb,0,aaa[bbb])
		else:
			self.m_grid3.SetCellValue(0,0,"cihaz bulunamadi")
		self.m_button2.SetLabel("Start Scan")
			
		
	def satirEkle(self):
		self.m_grid3.AppendRows()
		
		
	def satirisim(self):
			for i in range(0,self.satirSayisi):
				isim=str(i+1)+". "+"device IP"
				self.m_grid3.SetRowLabelValue(i,isim)
			#print dir(self.m_grid3)
			#print dir(wx.TextCtrl)
			
				
	def baslangic_ip(self,event):
		self.baslangic_ip_Txt=event.GetString()
		
		
	def son_ip(self,event):
		self.son_ip_Txt=event.GetString()





#https://stackoverflow.com/questions/2269827/how-to-convert-an-int-to-a-hex-string

# direkt cmd deki komutu simule ediyor C:\Windows\system32>ping -n 1  -w 300 172.16.215.146
def main():
	app = wx.App(False) 
	frame = araYuzDeneme(None)
	frame.Show(True) 
	app.MainLoop() 
#start the applications 

if __name__ == '__main__':
    main()