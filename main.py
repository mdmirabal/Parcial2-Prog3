#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from  kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from precios import Precio
class Ventana(Screen):
	precio = ObjectProperty
	origen=""
	destino=""
	def Origen(self, origen):
			self.origen = origen
			print (origen)
	def Destino(self, destino):
			self.destino = destino
			print (destino)	
	def CalcularPrecio(self):
			if self.origen != "" and self.destino != "":
                                costo = ""+Precio(self.origen,self.destino)
                                if costo == "null":
                                        self.precio.text ="No se puede determinar la tarifa para la ruta seleccionada."
                                else:
                                        self.precio.text = "El precio es de aproximadamente $"+costo	
			else:
				self.precio.text = "POR FAVOR SELECCIONE UNA RUTA"

class AplicacionApp(App): 
	def build(self):  
		return Ventana()
	def on_pause(self):
		return True



if __name__ == '__main__':
	AplicacionApp().run()
