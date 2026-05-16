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

def extraer_metadatos(self):
        """Extrae los tags DICOM de cada archivo y los guarda en un DataFrame"""
        lista_metadatos = []
        
        for ds in self.archivos_dicom:
            metadatos = {
                "PatientID":         getattr(ds, "PatientID", "No disponible"),
                "PatientName":       getattr(ds, "PatientName", "No disponible"),
                "StudyInstanceUID":  getattr(ds, "StudyInstanceUID", "No disponible"),
                "StudyDescription":  getattr(ds, "StudyDescription", "No disponible"),
                "StudyDate":         getattr(ds, "StudyDate", "No disponible"),
                "Modality":          getattr(ds, "Modality", "No disponible"),
                "Rows":              getattr(ds, "Rows", "No disponible"),
                "Columns":           getattr(ds, "Columns", "No disponible"),
            }
            lista_metadatos.append(metadatos)
        
        self.dataframe = pd.DataFrame(lista_metadatos)
        print("\nMetadatos extraídos:")
        print(self.dataframe)