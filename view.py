# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Log in
###########################################################################

class Login ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 229,155 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"LOG IN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nama :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Password :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Data Jenis cucian
###########################################################################

class DataJeniscucian ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 507,275 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Data jenis cucian", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer2.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button42 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button42, 0, wx.ALL, 5 )
		
		self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid3.CreateGrid( 5, 5 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.m_grid3, 0, wx.ALL, 5 )
		
		
		# bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button45 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.m_button45, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button46 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.m_button46, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer2.Add( gbSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 341,192 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menubar1.Append( self.m_menu1, u"Dashboard" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button31 = wx.Button( self, wx.ID_ANY, u"Data Jenis cucian", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button31, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button32 = wx.Button( self, wx.ID_ANY, u"Data Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button32, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button33 = wx.Button( self, wx.ID_ANY, u"Data Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button33, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button34 = wx.Button( self, wx.ID_ANY, u"Data Pegawai", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button34, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_button22 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( gSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 620,304 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook5 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel12 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button16 = wx.Button( self.m_panel12, wx.ID_ANY, u"+tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button16, 0, wx.ALL, 5 )
		
		self.m_panel18 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_splitter1 = wx.SplitterWindow( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		
		self.m_panel17 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_splitter1.Initialize( self.m_panel17 )
		bSizer6.Add( self.m_splitter1, 1, wx.EXPAND, 5 )
		
		self.m_grid3 = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid3.CreateGrid( 5, 5 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.m_grid3, 0, wx.ALL, 5 )
		
		self.m_button17 = wx.Button( self.m_panel12, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button17, 0, wx.ALL, 5 )
		
		
		self.m_panel12.SetSizer( bSizer6 )
		self.m_panel12.Layout()
		bSizer6.Fit( self.m_panel12 )
		self.m_notebook5.AddPage( self.m_panel12, u"Data Jenis Cucian", False )
		self.m_panel13 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_grid9 = wx.grid.Grid( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid9.CreateGrid( 5, 5 )
		self.m_grid9.EnableEditing( True )
		self.m_grid9.EnableGridLines( True )
		self.m_grid9.EnableDragGridSize( False )
		self.m_grid9.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid9.EnableDragColMove( False )
		self.m_grid9.EnableDragColSize( True )
		self.m_grid9.SetColLabelSize( 30 )
		self.m_grid9.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid9.EnableDragRowSize( True )
		self.m_grid9.SetRowLabelSize( 80 )
		self.m_grid9.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid9.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer3.Add( self.m_grid9, 0, wx.ALL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button31 = wx.Button( self.m_panel13, wx.ID_ANY, u"+tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button31, 0, wx.ALL, 5 )
		
		self.m_button32 = wx.Button( self.m_panel13, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button32, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		self.m_panel13.SetSizer( fgSizer3 )
		self.m_panel13.Layout()
		fgSizer3.Fit( self.m_panel13 )
		self.m_notebook5.AddPage( self.m_panel13, u"Data Transaksi", False )
		self.m_panel14 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_grid11 = wx.grid.Grid( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid11.CreateGrid( 5, 5 )
		self.m_grid11.EnableEditing( True )
		self.m_grid11.EnableGridLines( True )
		self.m_grid11.EnableDragGridSize( False )
		self.m_grid11.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid11.EnableDragColMove( False )
		self.m_grid11.EnableDragColSize( True )
		self.m_grid11.SetColLabelSize( 30 )
		self.m_grid11.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid11.EnableDragRowSize( True )
		self.m_grid11.SetRowLabelSize( 80 )
		self.m_grid11.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid11.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer4.Add( self.m_grid11, 0, wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button38 = wx.Button( self.m_panel14, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button38, 0, wx.ALL, 5 )
		
		self.m_button39 = wx.Button( self.m_panel14, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button39, 0, wx.ALL, 5 )
		
		
		fgSizer4.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		self.m_panel14.SetSizer( fgSizer4 )
		self.m_panel14.Layout()
		fgSizer4.Fit( self.m_panel14 )
		self.m_notebook5.AddPage( self.m_panel14, u"Data Pelanggan", False )
		self.m_panel15 = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_grid12 = wx.grid.Grid( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid12.CreateGrid( 5, 5 )
		self.m_grid12.EnableEditing( True )
		self.m_grid12.EnableGridLines( True )
		self.m_grid12.EnableDragGridSize( False )
		self.m_grid12.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid12.EnableDragColMove( False )
		self.m_grid12.EnableDragColSize( True )
		self.m_grid12.SetColLabelSize( 30 )
		self.m_grid12.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid12.EnableDragRowSize( True )
		self.m_grid12.SetRowLabelSize( 80 )
		self.m_grid12.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid12.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.m_grid12, 0, wx.ALL, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button40 = wx.Button( self.m_panel15, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button40, 0, wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self.m_panel15, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button41, 0, wx.ALL, 5 )
		
		
		fgSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		self.m_panel15.SetSizer( fgSizer5 )
		self.m_panel15.Layout()
		fgSizer5.Fit( self.m_panel15 )
		self.m_notebook5.AddPage( self.m_panel15, u"Data Pegawai", False )
		
		bSizer5.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 0 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )
	

