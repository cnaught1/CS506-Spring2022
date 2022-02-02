import tkinter
from PIL import Image, ImageDraw
import PySimpleGUI as sg
from PIL import Image
import os
import tkinter
import io

from safety import policestation, firestation, hospital

policestation.draw_policestation()
firestation.draw_firestation()
hospital.draw_hospital()