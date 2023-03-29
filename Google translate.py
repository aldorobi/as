# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:57:25 2023

@author: Aldo
"""


import requests
from tkinter import *
import tkinter as ttk

TraductorChafa = Tk()
TraductorChafa.title("Speedtest barato")
TraductorChafa.geometry("740x480")
TraductorChafa.configure(background = "thistle4")

def Traduccion(source, target, text):
	parametros = {'sl': source, 'tl': target, 'q': text}
	cabeceras = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
	url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
	response = requests.post(url, data=parametros, headers=cabeceras)
	if response.status_code == 200:
		for x in response.json()['sentences']:
			return x['trans']
	else:
		return "Ocurrió un error"

while True:
	text = input(" Ingrese un texto para traducir:")
	if text == "SALIR_CONSOLE":
		break
	else:
		respuesta = Traduccion("es", "fr", text)
		print("Resultado: " + str(respuesta))
		print("\n")
        
        
TraductorChafa.mainloop()