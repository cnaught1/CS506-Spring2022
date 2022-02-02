import tkinter
from PIL import Image, ImageDraw
import PySimpleGUI as sg
from PIL import Image
import os
import tkinter
import io

def draw_hospital():

    img = Image.open("hospital.jfif")
    img.thumbnail((1200, 800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    
    layout = [[[sg.Text("Hospital:", font= ("arial", 25)),] ,
              [sg.Image(data=bio.getvalue())]],
             [sg.Button("Don't Show Me Anymore")]]
    
    window = sg.Window("Image", layout, size=(1200, 800))
    
    while True:
        event, values = window.read()
        if event == "Don't Show Me Anymore" or event == sg.WIN_CLOSED:
            break
            
    window.close()