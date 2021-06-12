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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 376,186 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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
		self.transaksiPanel = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook5.AddPage( self.transaksiPanel, u"Transaksi", True )
		self.jenisPanel = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook5.AddPage( self.jenisPanel, u"Jenis Cucian", False )
		self.pelangganPanel = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook5.AddPage( self.pelangganPanel, u"Pelanggan", False )
		self.pegawaiPanel = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook5.AddPage( self.pegawaiPanel, u"Pegawai", False )

		bSizer5.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.klikProfil, id = self.menuProfil.GetId() )
		self.Bind( wx.EVT_MENU, self.klikLogout, id = self.menuLogout.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def klikProfil( self, event ):
		event.Skip()

	def klikLogout( self, event ):
		event.Skip()


###########################################################################
## Class tampilanTransaksi
###########################################################################

class tampilanTransaksi ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataTransaksi = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

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

		self.btnTambahTransaksi = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnTambahTransaksi.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR ) )
		bSizer8.Add( self.btnTambahTransaksi, 0, wx.ALL, 5 )

		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		bSizer8.Add( self.m_searchCtrl1, 0, wx.ALL, 5 )


		fgSizer3.Add( bSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer3 )
		self.Layout()

		# Connect Events
		self.dataTransaksi.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.dataTransaksiOnGridCmdSelectCell )
		self.btnTambahTransaksi.Bind( wx.EVT_BUTTON, self.klikTambahTransaksi )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dataTransaksiOnGridCmdSelectCell( self, event ):
		event.Skip()

	def klikTambahTransaksi( self, event ):
		event.Skip()


###########################################################################
## Class tampilanJenis
###########################################################################

class tampilanJenis ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer41 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataJenis = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

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

		self.btnTambahJenis = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnTambahJenis.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR ) )
		bSizer101.Add( self.btnTambahJenis, 0, wx.ALL, 5 )


		fgSizer41.Add( bSizer101, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer41 )
		self.Layout()

		# Connect Events
		self.dataJenis.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.dataJenisOnGridCmdSelectCell )
		self.btnTambahJenis.Bind( wx.EVT_BUTTON, self.klikTambahJenis )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dataJenisOnGridCmdSelectCell( self, event ):
		event.Skip()

	def klikTambahJenis( self, event ):
		event.Skip()


###########################################################################
## Class tampilanPegawai
###########################################################################

class tampilanPegawai ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataPegawai = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

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

		self.btnTambahPegawai = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnTambahPegawai.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR ) )
		bSizer11.Add( self.btnTambahPegawai, 0, wx.ALL, 5 )


		fgSizer5.Add( bSizer11, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()

		# Connect Events
		self.dataPegawai.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.dataPegawaiOnGridCmdSelectCell )
		self.btnTambahPegawai.Bind( wx.EVT_BUTTON, self.klikTambahPegawai )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dataPegawaiOnGridCmdSelectCell( self, event ):
		event.Skip()

	def klikTambahPegawai( self, event ):
		event.Skip()


###########################################################################
## Class tampilanPelanggan
###########################################################################

class tampilanPelanggan ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.dataPelanggan = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

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

		self.btnTambahPelanggan = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.btnTambahPelanggan.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_TOOLBAR ) )
		bSizer10.Add( self.btnTambahPelanggan, 0, wx.ALL, 5 )


		fgSizer4.Add( bSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( fgSizer4 )
		self.Layout()

		# Connect Events
		self.dataPelanggan.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.dataPelangganOnGridCmdSelectCell )
		self.btnTambahPelanggan.Bind( wx.EVT_BUTTON, self.klikTambahPelanggan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def dataPelangganOnGridCmdSelectCell( self, event ):
		event.Skip()

	def klikTambahPelanggan( self, event ):
		event.Skip()


###########################################################################
## Class insrtTransaksi
###########################################################################

class insrtTransaksi ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
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

		self.tombolKembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.tombolKembali, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolTambah = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.tombolTambah, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.tombolSimpan, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer3 )
		self.Layout()

		# Connect Events
		self.tombolKembali.Bind( wx.EVT_BUTTON, self.btnKembali )
		self.tombolTambah.Bind( wx.EVT_BUTTON, self.btnTambah )
		self.tombolSimpan.Bind( wx.EVT_BUTTON, self.btnSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnKembali( self, event ):
		event.Skip()

	def btnTambah( self, event ):
		event.Skip()

	def btnSimpan( self, event ):
		event.Skip()


###########################################################################
## Class insrtJenis
###########################################################################

class insrtJenis ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Tambah jenis baru", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gbSizer4.Add( self.m_staticText11, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"ID Jenis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gbSizer4.Add( self.m_staticText12, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputIdJenis = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.inputIdJenis, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Nama Jenis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gbSizer4.Add( self.m_staticText13, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputNamaJenis = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.inputNamaJenis, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		gbSizer4.Add( self.m_staticText14, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputHarga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.inputHarga, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolKembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.tombolKembali.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_TOOLBAR ) )
		gbSizer4.Add( self.tombolKembali, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.tombolSimpan.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_TOOLBAR ) )
		gbSizer4.Add( self.tombolSimpan, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer4 )
		self.Layout()

		# Connect Events
		self.tombolKembali.Bind( wx.EVT_BUTTON, self.btnKembali )
		self.tombolSimpan.Bind( wx.EVT_BUTTON, self.btnSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnKembali( self, event ):
		event.Skip()

	def btnSimpan( self, event ):
		event.Skip()


###########################################################################
## Class insrtPelanggan
###########################################################################

class insrtPelanggan ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer8 = wx.GridBagSizer( 0, 0 )
		gbSizer8.SetFlexibleDirection( wx.BOTH )
		gbSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Tambah data Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		gbSizer8.Add( self.m_staticText27, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"First Name ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		gbSizer8.Add( self.m_staticText28, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputFirstName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.inputFirstName, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		gbSizer8.Add( self.m_staticText29, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputLastName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.inputLastName, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"No HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		gbSizer8.Add( self.m_staticText30, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputNohp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.inputNohp, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gbSizer8.Add( self.m_staticText31, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.inputEmail, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolSimpan = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.tombolSimpan, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer8.Add( self.tombolSimpan, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer8 )
		self.Layout()

		# Connect Events
		self.tombolSimpan.Bind( wx.EVT_BUTTON, self.btnKembali )
		self.tombolSimpan.Bind( wx.EVT_BUTTON, self.btnSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnKembali( self, event ):
		event.Skip()

	def btnSimpan( self, event ):
		event.Skip()


###########################################################################
## Class insrtPegawai
###########################################################################

class insrtPegawai ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer11 = wx.GridBagSizer( 0, 0 )
		gbSizer11.SetFlexibleDirection( wx.BOTH )
		gbSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"Tambah Data Pegawai ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		gbSizer11.Add( self.m_staticText54, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		gbSizer11.Add( self.m_staticText55, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputFirstName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.inputFirstName, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )

		gbSizer11.Add( self.m_staticText56, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputLastName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.inputLastName, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"No HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )

		gbSizer11.Add( self.m_staticText57, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputNoHP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.inputNoHP, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )

		gbSizer11.Add( self.m_staticText58, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.inputEmail, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )

		gbSizer11.Add( self.m_staticText59, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.inputUsername, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText60 = wx.StaticText( self, wx.ID_ANY, u"Passwoard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )

		gbSizer11.Add( self.m_staticText60, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputPasswoard = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.inputPasswoard, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolKembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.tombolKembali, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer11.Add( self.tombolSimpan, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer11 )
		self.Layout()

		# Connect Events
		self.tombolKembali.Bind( wx.EVT_BUTTON, self.btnKembali )
		self.tombolSimpan.Bind( wx.EVT_BUTTON, self.btnSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnKembali( self, event ):
		event.Skip()

	def btnSimpan( self, event ):
		event.Skip()


###########################################################################
## Class editTransaksi
###########################################################################

class editTransaksi ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer13 = wx.GridBagSizer( 0, 0 )
		gbSizer13.SetFlexibleDirection( wx.BOTH )
		gbSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Ubah Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		gbSizer13.Add( self.m_staticText61, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )

		gbSizer13.Add( self.m_staticText62, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputTanggal = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gbSizer13.Add( self.inputTanggal, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolKembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.tombolKembali, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer13.Add( self.tombolSimpan, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer13 )
		self.Layout()

		# Connect Events
		self.tombolKembali.Bind( wx.EVT_BUTTON, self.btnKembali )
		self.tombolSimpan.Bind( wx.EVT_BUTTON, self.brnSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnKembali( self, event ):
		event.Skip()

	def brnSimpan( self, event ):
		event.Skip()


###########################################################################
## Class editJenis
###########################################################################

class editJenis ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Edit Data Jenis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		gbSizer7.Add( self.m_staticText23, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Nama Jenis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		gbSizer7.Add( self.m_staticText25, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputNamaJenis = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.inputNamaJenis, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		gbSizer7.Add( self.m_staticText26, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputHarga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.inputHarga, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolKembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.tombolKembali, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.tombolSimpan, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer7 )
		self.Layout()

		# Connect Events
		self.tombolKembali.Bind( wx.EVT_BUTTON, self.btnKembali )
		self.tombolSimpan.Bind( wx.EVT_BUTTON, self.btnSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnKembali( self, event ):
		event.Skip()

	def btnSimpan( self, event ):
		event.Skip()


###########################################################################
## Class editPelanggan
###########################################################################

class editPelanggan ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Ubah Data Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		gbSizer9.Add( self.m_staticText34, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		gbSizer9.Add( self.m_staticText35, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputFirstName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.inputFirstName, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		gbSizer9.Add( self.m_staticText41, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputLastName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.inputLastName, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"No HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		gbSizer9.Add( self.m_staticText42, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputNoHP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.inputNoHP, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )

		gbSizer9.Add( self.m_staticText43, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.inputEmail, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolKembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.tombolKembali, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.tombolSimpan, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer9 )
		self.Layout()

		# Connect Events
		self.tombolKembali.Bind( wx.EVT_BUTTON, self.btnKembali )
		self.tombolSimpan.Bind( wx.EVT_BUTTON, self.btnSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnKembali( self, event ):
		event.Skip()

	def btnSimpan( self, event ):
		event.Skip()


###########################################################################
## Class editPegawai
###########################################################################

class editPegawai ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer10 = wx.GridBagSizer( 0, 0 )
		gbSizer10.SetFlexibleDirection( wx.BOTH )
		gbSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Ubah Data Pegawai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )

		gbSizer10.Add( self.m_staticText44, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		gbSizer10.Add( self.m_staticText45, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputFirstName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.inputFirstName, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )

		gbSizer10.Add( self.m_staticText46, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputLastName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.inputLastName, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"No HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )

		gbSizer10.Add( self.m_staticText47, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputNoHP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.inputNoHP, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )

		gbSizer10.Add( self.m_staticText48, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.inputEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.inputEmail, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolKembali = wx.Button( self, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.tombolKembali, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.tombolSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer10.Add( self.tombolSimpan, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.SetSizer( gbSizer10 )
		self.Layout()

		# Connect Events
		self.tombolKembali.Bind( wx.EVT_BUTTON, self.btnkembali )
		self.tombolSimpan.Bind( wx.EVT_BUTTON, self.btnSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnkembali( self, event ):
		event.Skip()

	def btnSimpan( self, event ):
		event.Skip()


