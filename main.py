import pydicom.data
from procesador_dicom import ProcesadorDICOM
import os

# Obtener archivos DICOM de prueba que trae pydicom
archivos_prueba = pydicom.data.get_testfiles_name()

# Crear carpeta dicom_files y copiar los archivos de prueba
os.makedirs("dicom_files", exist_ok=True)

import shutil
for ruta in archivos_prueba:
    if ruta.endswith(".dcm"):
        shutil.copy(ruta, "dicom_files/")

# Ejecutar el procesador
procesador = ProcesadorDICOM()
procesador.cargar_archivos("dicom_files/")
procesador.extraer_metadatos()
procesador.calcular_intensidad()
procesador.procesar_imagenes("output/")
