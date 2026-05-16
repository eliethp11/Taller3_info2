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

def calcular_intensidad(self):
        
        intensidades = []
        
        for ds in self.archivos_dicom:
            try:
                pixel_array = ds.pixel_array
                promedio = np.mean(pixel_array)
                intensidades.append(round(promedio, 2))
            except Exception as e:
                print(f"No tiene datos de píxeles: {e}")
                intensidades.append(None)
        
        self.dataframe["IntensidadPromedio"] = intensidades
        print("\nIntensidad promedio agregada al DataFrame:")
        print(self.dataframe[["PatientID", "Modality", "IntensidadPromedio"]])

def procesar_imagenes(self, directorio_salida):
     
        os.makedirs(directorio_salida, exist_ok=True)
        
        for ds in self.archivos_dicom:
            try:
                pixel_array = ds.pixel_array
                
              
                pixel_norm = cv2.normalize(
                    pixel_array, None, 0, 255, cv2.NORM_MINMAX
                )
                pixel_norm = np.uint8(pixel_norm)
                
              
                ecualizada = cv2.equalizeHist(pixel_norm)
                
               
                bordes = cv2.Canny(ecualizada, threshold1=50, threshold2=150)
                
             
                nombre = str(getattr(ds, "StudyInstanceUID", "sin_id"))[:20]
                cv2.imwrite(f"{directorio_salida}/{nombre}_ecualizada.png", ecualizada)
                cv2.imwrite(f"{directorio_salida}/{nombre}_bordes.png", bordes)
                print(f"Imágenes guardadas para: {nombre}")
                
            except Exception as e:
                print(f"No se pudo procesar imagen: {e}")

