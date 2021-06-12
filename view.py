# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.adv

###########################################################################
## Class Login
###########################################################################

class Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 220,159 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Laundry.in Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inpUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.inpUsername, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inpPass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gbSizer1.Add( self.inpPass, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer1.Add( gbSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btnLogin = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnLogin.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1.Add( self.btnLogin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnLogin.Bind( wx.EVT_BUTTON, self.klikLogin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def klikLogin( self, event ):
		event.Skip()


###########################################################################
## Class halaman_utama
###########################################################################

class halaman_utama ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 620,304 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.tampilUsername = wx.Menu()
		self.m_menubar2.Append( self.tampilUsername, u"Username" )

		self.m_menu4 = wx.Menu()
		self.menuProfil = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Profil", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuProfil.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_HOME, wx.ART_TOOLBAR ) )
		self.m_menu4.Append( self.menuProfil )

		self.m_menu4.AppendSeparator()

		self.menuLogout = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"Logout", wx.EmptyString, wx.ITEM_NORMAL )
		self.menuLogout.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_TOOLBAR ) )
		self.m_menu4.Append( self.menuLogout )

		self.m_menubar2.Append( self.m_menu4, u"Menu" )

		self.SetMenuBar( self.m_menubar2 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook5 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.transaksi = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataTransaksi = wx.grid.Grid( self.transaksi, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataTransaksi.CreateGrid( 5, 5 )
		self.dataTransaksi.EnableEditing( True )
		self.dataTransaksi.EnableGridLines( True )
		self.dataTransaksi.EnableDragGridSize( False )
		self.dataTransaksi.SetMargins( 0, 0 )

		# Columns
		self.dataTransaksi.EnableDragColMove( False )
		self.dataTransaksi.EnableDragColSize( True )
		self.dataTransaksi.SetColLabelSize( 30 )
		self.dataTransaksi.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataTransaksi.EnableDragRowSize( True )
		self.dataTransaksi.SetRowLabelSize( 80 )
		self.dataTransaksi.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataTransaksi.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer3.Add( self.dataTransaksi, 0, wx.ALL, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.btnTambahTransaksi = wx.Button( self.transaksi, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnTambahTransaksi.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR ) )
		bSizer8.Add( self.btnTambahTransaksi, 0, wx.ALL, 5 )

		self.m_searchCtrl1 = wx.SearchCtrl( self.transaksi, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		bSizer8.Add( self.m_searchCtrl1, 0, wx.ALL, 5 )


		fgSizer3.Add( bSizer8, 1, wx.EXPAND, 5 )


		self.transaksi.SetSizer( fgSizer3 )
		self.transaksi.Layout()
		fgSizer3.Fit( self.transaksi )
		self.m_notebook5.AddPage( self.transaksi, u"Transaksi", False )
		self.jenis = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer41 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataJenis = wx.grid.Grid( self.jenis, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataJenis.CreateGrid( 5, 5 )
		self.dataJenis.EnableEditing( True )
		self.dataJenis.EnableGridLines( True )
		self.dataJenis.EnableDragGridSize( False )
		self.dataJenis.SetMargins( 0, 0 )

		# Columns
		self.dataJenis.EnableDragColMove( False )
		self.dataJenis.EnableDragColSize( True )
		self.dataJenis.SetColLabelSize( 30 )
		self.dataJenis.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataJenis.EnableDragRowSize( True )
		self.dataJenis.SetRowLabelSize( 80 )
		self.dataJenis.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataJenis.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer41.Add( self.dataJenis, 0, wx.ALL, 5 )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		self.btnTambahJenis = wx.Button( self.jenis, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnTambahJenis.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR ) )
		bSizer101.Add( self.btnTambahJenis, 0, wx.ALL, 5 )


		fgSizer41.Add( bSizer101, 1, wx.EXPAND, 5 )


		self.jenis.SetSizer( fgSizer41 )
		self.jenis.Layout()
		fgSizer41.Fit( self.jenis )
		self.m_notebook5.AddPage( self.jenis, u"Jenis Cucian", True )
		self.pelanggan = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataPelanggan = wx.grid.Grid( self.pelanggan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataPelanggan.CreateGrid( 5, 5 )
		self.dataPelanggan.EnableEditing( True )
		self.dataPelanggan.EnableGridLines( True )
		self.dataPelanggan.EnableDragGridSize( False )
		self.dataPelanggan.SetMargins( 0, 0 )

		# Columns
		self.dataPelanggan.EnableDragColMove( False )
		self.dataPelanggan.EnableDragColSize( True )
		self.dataPelanggan.SetColLabelSize( 30 )
		self.dataPelanggan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataPelanggan.EnableDragRowSize( True )
		self.dataPelanggan.SetRowLabelSize( 80 )
		self.dataPelanggan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataPelanggan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer4.Add( self.dataPelanggan, 0, wx.ALL, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.btnTambahPelanggan = wx.Button( self.pelanggan, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnTambahPelanggan.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR ) )
		bSizer10.Add( self.btnTambahPelanggan, 0, wx.ALL, 5 )


		fgSizer4.Add( bSizer10, 1, wx.EXPAND, 5 )


		self.pelanggan.SetSizer( fgSizer4 )
		self.pelanggan.Layout()
		fgSizer4.Fit( self.pelanggan )
		self.m_notebook5.AddPage( self.pelanggan, u"Pelanggan", False )
		self.pegawai = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataPegawai = wx.grid.Grid( self.pegawai, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.dataPegawai.CreateGrid( 5, 5 )
		self.dataPegawai.EnableEditing( True )
		self.dataPegawai.EnableGridLines( True )
		self.dataPegawai.EnableDragGridSize( False )
		self.dataPegawai.SetMargins( 0, 0 )

		# Columns
		self.dataPegawai.EnableDragColMove( False )
		self.dataPegawai.EnableDragColSize( True )
		self.dataPegawai.SetColLabelSize( 30 )
		self.dataPegawai.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.dataPegawai.EnableDragRowSize( True )
		self.dataPegawai.SetRowLabelSize( 80 )
		self.dataPegawai.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.dataPegawai.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.dataPegawai, 0, wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.btnTambahPegawai = wx.Button( self.pegawai, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnTambahPegawai.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR ) )
		bSizer11.Add( self.btnTambahPegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )


		self.pegawai.SetSizer( fgSizer5 )
		self.pegawai.Layout()
		fgSizer5.Fit( self.pegawai )
		self.m_notebook5.AddPage( self.pegawai, u"Pegawai", False )

		bSizer5.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.klikProfil, id = self.menuProfil.GetId() )
		self.Bind( wx.EVT_MENU, self.klikLogout, id = self.menuLogout.GetId() )
		self.btnTambahTransaksi.Bind( wx.EVT_BUTTON, self.klikTambahTransaksi )
		self.btnTambahJenis.Bind( wx.EVT_BUTTON, self.klikTambahJenis )
		self.btnTambahPelanggan.Bind( wx.EVT_BUTTON, self.klikTambahPelanggan )
		self.btnTambahPegawai.Bind( wx.EVT_BUTTON, self.klikTambahPegawai )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def klikProfil( self, event ):
		event.Skip()

	def klikLogout( self, event ):
		event.Skip()

	def klikTambahTransaksi( self, event ):
		event.Skip()

	def klikTambahJenis( self, event ):
		event.Skip()

	def klikTambahPelanggan( self, event ):
		event.Skip()

	def klikTambahPegawai( self, event ):
		event.Skip()


###########################################################################
## Class insrtTransaksi
###########################################################################

class insrtTransaksi ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Transaksi Baru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gbSizer2.Add( self.m_staticText4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"ID Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gbSizer2.Add( self.m_staticText5, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		gbSizer2.Add( self.m_choice2, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Total Pakaian", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_textCtrl6, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer2.Add( self.m_staticText7, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_datePicker2 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer2.Add( self.m_datePicker2, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_button6, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btnLanjut = wx.Button( self, wx.ID_ANY, u"Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.btnLanjut, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer2 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class insrtTransaksi2
###########################################################################

class insrtTransaksi2 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Transaksi Baru / Jenis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gbSizer3.Add( self.m_staticText4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gbSizer3.Add( self.m_staticText14, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		m_choice4Choices = []
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		gbSizer3.Add( self.m_choice4, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gbSizer3.Add( self.m_staticText15, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_textCtrl9, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_button9, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button10 = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_button10, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.m_button11, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer3 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class insrtJenis
###########################################################################

class insrtJenis ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class insrtPelanggan
###########################################################################

class insrtPelanggan ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class insrtPegawai
###########################################################################

class insrtPegawai ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class editTransaksi
###########################################################################

class editTransaksi ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class editJenis
###########################################################################

class editJenis ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class editPelanggan
###########################################################################

class editPelanggan ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class editPegawai
###########################################################################

class editPegawai ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


