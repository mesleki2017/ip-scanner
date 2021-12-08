# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import wx.grid



class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style =wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
				
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL)
		
		
		##########################################################################################################################
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Başlangıç Ip Adresi", wx.DefaultPosition, wx.DefaultSize, 0|wx.DOUBLE_BORDER )
		self.m_staticText2.Wrap( -1 )
		gbSizer2.Add( self.m_staticText2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer2.Add( self.m_textCtrl2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		######################################################################################################################
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Son Ip Adres", wx.DefaultPosition, wx.DefaultSize, 0|wx.DOUBLE_BORDER )
		self.m_staticText3.Wrap( -1 )
		gbSizer2.Add( self.m_staticText3, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer2.Add( self.m_textCtrl3, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		######################################################################################################################	
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"IP Tara", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button2, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )	
		######################################################################################################################
		self.m_statusBar1 = self.CreateStatusBar( 2, style = wx.STB_DEFAULT_STYLE,name = "Status Bar" )
		self.m_statusBar1.SetStatusText("Bulent Cesur",1)
		######################################################################################################################
		self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, size = wx.Size( 700,300 ),style = wx.TAB_TRAVERSAL|wx.VSCROLL|wx.ALWAYS_SHOW_SB )
		
		# Grid
		self.m_grid3.CreateGrid(1, 1 )
		self.m_grid3.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3.SetColSize( 0,600 )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gbSizer2.Add( self.m_grid3, wx.GBPosition(4, 0 ), wx.GBSpan( 1, 6 ), wx.EXPAND, 5 )

		######################################################################################################################
		self.m_textCtrl2.Bind(wx.EVT_TEXT,self.baslangic_ip)
		self.m_textCtrl3.Bind(wx.EVT_TEXT,self.son_ip)
		self.m_button2.Bind( wx.EVT_BUTTON, self.portTara )
		######################################################################################################################
		self.SetSizer( gbSizer2 )
		self.Layout()	
		self.Centre( wx.BOTH )


