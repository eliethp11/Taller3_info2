import pydicom
import pydicom.data
import numpy as np
import pandas as pd
import cv2
import os

def __init__(self):
    self.archivos_dicom=[]
    self.dataframe=None

def cargar_archivos (self,directorio):
    self.archivos_dicom=[]
    for archivo in os.listdir(directorio):
        ruta=os.path.join (directorio,archivo)
        try:
            ds=pydicom.dcmread(ruta)
            self.archivos_dicom.append (ds)
            print(f"Cargado:{archivo}")
        except Exception as e:
            print(f"El DICOM no es válido:{archivo}---{e}")

        print(f"\nTotal de archivos cargados:{len(self.archivos_dicom)}")