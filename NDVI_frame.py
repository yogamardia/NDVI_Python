# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May  3 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from ndvi import NDVI
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm

###########################################################################
## Class NDVI_frame
###########################################################################

class NDVI_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"NDVI", pos = wx.DefaultPosition, size = wx.Size( 1005,611 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menubar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_menubar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.file_menu = wx.Menu()
		self.close_menu = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Close", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_menu.Append( self.close_menu )
		
		self.m_menubar.Append( self.file_menu, u"File" ) 
		
		self.help_menu = wx.Menu()
		self.about_menu = wx.MenuItem( self.help_menu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_menu.Append( self.about_menu )
		
		self.m_menubar.Append( self.help_menu, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		sbSizer_Red = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Red" ), wx.VERTICAL )
		
		self.img_red_bitmap = wx.StaticBitmap( sbSizer_Red.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,200 ), 0 )
		self.img_red_bitmap.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		
		sbSizer_Red.Add( self.img_red_bitmap, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.browse_btn = wx.Button( sbSizer_Red.GetStaticBox(), wx.ID_ANY, u"Browse Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer_Red.Add( self.browse_btn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer2.Add( sbSizer_Red, 1, wx.EXPAND, 5 )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		bSizer2.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		sbSizer_cropping = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Coordinate Cropping" ), wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer_startlat = wx.BoxSizer( wx.VERTICAL )
		
		self.startlat_txt = wx.StaticText( sbSizer_cropping.GetStaticBox(), wx.ID_ANY, u"Start Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startlat_txt.Wrap( -1 )
		bSizer_startlat.Add( self.startlat_txt, 0, wx.ALL, 5 )
		
		self.startlat_txtCtrl = wx.TextCtrl( sbSizer_cropping.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_startlat.Add( self.startlat_txtCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.endlat_txt = wx.StaticText( sbSizer_cropping.GetStaticBox(), wx.ID_ANY, u"End Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.endlat_txt.Wrap( -1 )
		bSizer_startlat.Add( self.endlat_txt, 0, wx.ALL, 5 )
		
		self.endlat_txtCtrl = wx.TextCtrl( sbSizer_cropping.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_startlat.Add( self.endlat_txtCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer_startlat, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.startlon_txt = wx.StaticText( sbSizer_cropping.GetStaticBox(), wx.ID_ANY, u"Start Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startlon_txt.Wrap( -1 )
		bSizer9.Add( self.startlon_txt, 0, wx.ALL, 5 )
		
		self.startlon_txtCtrl = wx.TextCtrl( sbSizer_cropping.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.startlon_txtCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.endlon_txt = wx.StaticText( sbSizer_cropping.GetStaticBox(), wx.ID_ANY, u"End Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.endlon_txt.Wrap( -1 )
		bSizer9.Add( self.endlon_txt, 0, wx.ALL, 5 )
		
		self.endlon_txtCtrl = wx.TextCtrl( sbSizer_cropping.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.endlon_txtCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer11.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		sbSizer_cropping.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		self.crop_btn = wx.Button( sbSizer_cropping.GetStaticBox(), wx.ID_ANY, u"Crop", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer_cropping.Add( self.crop_btn, 0, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText436 = wx.StaticText( sbSizer_cropping.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText436.Wrap( -1 )
		sbSizer_cropping.Add( self.m_staticText436, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( sbSizer_cropping, 1, wx.EXPAND, 5 )
		
		self.m_staticText435 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText435.Wrap( -1 )
		bSizer2.Add( self.m_staticText435, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		bSizer1.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		bSizer3.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		sbSizer_NIR = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NIR" ), wx.VERTICAL )
		
		self.nir_bitmap = wx.StaticBitmap( sbSizer_NIR.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,200 ), 0 )
		self.nir_bitmap.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		
		sbSizer_NIR.Add( self.nir_bitmap, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.browse_nir_btn = wx.Button( sbSizer_NIR.GetStaticBox(), wx.ID_ANY, u"Browse NIR Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer_NIR.Add( self.browse_nir_btn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer_NIR, 1, wx.EXPAND, 5 )
		
		self.m_staticText451 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText451.Wrap( -1 )
		bSizer3.Add( self.m_staticText451, 0, wx.ALL, 5 )
		
		sbSizer_metadata = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Metadata" ), wx.VERTICAL )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.metadata_btn = wx.FilePickerCtrl( sbSizer_metadata.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select Metadata", u"Text files (*.txt)|*.txt", wx.DefaultPosition, wx.Size( 300,-1 ), wx.FLP_DEFAULT_STYLE )
		bSizer13.Add( self.metadata_btn, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( sbSizer_metadata.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer13.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.date_txt = wx.StaticText( sbSizer_metadata.GetStaticBox(), wx.ID_ANY, u"Date Acquired:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.date_txt.Wrap( -1 )
		bSizer91.Add( self.date_txt, 0, wx.ALL, 5 )
		
		self.date_static_txt = wx.StaticText( sbSizer_metadata.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.date_static_txt.Wrap( -1 )
		bSizer91.Add( self.date_static_txt, 0, wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		
		sbSizer_metadata.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer_metadata, 1, wx.EXPAND, 5 )
		
		self.m_staticText433 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText433.Wrap( -1 )
		bSizer3.Add( self.m_staticText433, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		bSizer1.Add( self.m_staticText43, 0, wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		bSizer4.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		sbSizer_NDVI = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NDVI" ), wx.VERTICAL )
		
		self.ndvi_bitmap = wx.StaticBitmap( sbSizer_NDVI.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,200 ), 0 )
		self.ndvi_bitmap.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		
		sbSizer_NDVI.Add( self.ndvi_bitmap, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.ndvi_btn = wx.Button( sbSizer_NDVI.GetStaticBox(), wx.ID_ANY, u"Start NDVI", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer_NDVI.Add( self.ndvi_btn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer4.Add( sbSizer_NDVI, 1, wx.EXPAND, 5 )
		
		self.m_staticText431 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText431.Wrap( -1 )
		bSizer4.Add( self.m_staticText431, 0, wx.ALL, 5 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"File" ), wx.VERTICAL )
		
		self.save_btn = wx.Button( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Save Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer8.Add( self.save_btn, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer4.Add( sbSizer8, 1, wx.EXPAND, 5 )
		
		self.m_staticText432 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText432.Wrap( -1 )
		bSizer4.Add( self.m_staticText432, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.m_staticText434 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText434.Wrap( -1 )
		bSizer1.Add( self.m_staticText434, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.close, id = self.close_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.about, id = self.about_menu.GetId() )
		self.browse_btn.Bind( wx.EVT_BUTTON, self.browseImage )
		self.crop_btn.Bind( wx.EVT_BUTTON, self.cropCoordinate )
		self.browse_nir_btn.Bind( wx.EVT_BUTTON, self.browseNIR )
		self.metadata_btn.Bind( wx.EVT_FILEPICKER_CHANGED, self.browseMetadata )
		self.ndvi_btn.Bind( wx.EVT_BUTTON, self.startNDVI )
		self.save_btn.Bind( wx.EVT_BUTTON, self.saveImage )

		self.ndvi = NDVI()
		self.ndvi.SetOnProcessFinishListener(self)
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def close( self, event ):
		event.Skip()
	
	def about( self, event ):
		event.Skip()
	
	def browseImage( self, event ):
		# path = event.GetPath
		wildcard = "TIFF files (*.tif)|*.tif"
		dialog = wx.FileDialog(None, "Choose a file",
								wildcard=wildcard,
								style=wx.FD_OPEN)
		if dialog.ShowModal() == wx.ID_CANCEL:
			return     # the user changed their mind
		
		path = dialog.GetPath()
		self.ndvi.OpenB4File(path)
		bitmap = wx.Bitmap(path, wx.BITMAP_TYPE_TIF)
		image = wx.Bitmap.ConvertToImage(bitmap)
		scaledImage = image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
		bitmap = wx.Bitmap(scaledImage)
		self.img_red_bitmap.SetBitmap(bitmap)
		event.Skip()
	
	def cropCoordinate( self, event ):
		latStart = self.startlat_txtCtrl.GetValue()
		latEnd =  self.endlat_txtCtrl	.GetValue()
		lonStart =  self.startlon_txtCtrl.GetValue()
		lonEnd = self.endlon_txtCtrl.GetValue()

		self.ndvi.SetCropCoordinate(latStart, latEnd, lonStart, lonEnd)
		self.ndvi.CropImage()
		event.Skip()
	
	def onCropFinish(self, red, nir):
		red_image = self.convertToImage(red, False)
		nir_image = self.convertToImage(nir, False)

		self.img_red_bitmap.SetBitmap(wx.Bitmap(red_image))
		self.nir_bitmap.SetBitmap(wx.Bitmap(nir_image))
		frame.Layout()

	def browseNIR( self, event ):
		wildcard = "TIFF files (*.tif)|*.tif"
		dialog = wx.FileDialog(None, "Choose a file",
								wildcard=wildcard,
								style=wx.FD_OPEN)
		if dialog.ShowModal() == wx.ID_CANCEL:
			return     
		
		path = dialog.GetPath()
		self.ndvi.OpenB5File(path)
		bitmap = wx.Bitmap(path, wx.BITMAP_TYPE_TIF)
		image = wx.Bitmap.ConvertToImage(bitmap)
		scaledImage = image.Scale(200, 200, wx.IMAGE_QUALITY_HIGH)
		bitmap = wx.Bitmap(scaledImage)
		self.nir_bitmap.SetBitmap(bitmap)
		event.Skip()
	
	def browseMetadata( self, event ):
		path = self.metadata_btn.GetPath()
		self.metadata = self.ndvi.ReadMetadata(path)
		self.date_static_txt.SetLabel(str(self.metadata['DATE_ACQUIRED']))
		event.Skip()
	
	def startNDVI( self, event ):
		event.Skip()
	
	def saveImage( self, event ):
		event.Skip()
	

app = wx.App(False)

#create an object of MyFrame2
frame = NDVI_frame(None)
#show the frame
frame.Show(True)
#start the application
app.MainLoop()