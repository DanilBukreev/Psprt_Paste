#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import PySimpleGUI as sg
import Psprt_Paste_v3

sg.theme('DarkBlue12')
layout = [[sg.Text('Шаг 1.')],
          [sg.Checkbox('Сгенерировать паспорта', change_submits=True, enable_events=True, default='0',key='all')],
		  [sg.Checkbox('Обновить данные в паспортах', change_submits=True, enable_events=True, default='0',key='some')],
          [sg.OK()]]
window = sg.Window('Меню', layout)
button, values = window.Read()
while True:
	button, values = window.Read()
	if values['all'] == True:
		Psprt_Paste_v3.all()
		break
	if values['some'] == True:
		Psprt_Paste_v3.some()
		break

window.Close()


