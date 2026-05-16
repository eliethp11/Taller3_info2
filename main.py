from procesador_dicom import ProcesadorDICOM
import pydicom
import os
import shutil

# Obtener la ruta de los archivos de prueba de pydicom
data_dir = os.path.dirname(pydicom.__file__)
data_dir = os.path.join(data_dir, "data", "test_files")

# Crear carpeta dicom_files y copiar los archivos de prueba
os.makedirs("dicom_files", exist_ok=True)
for archivo in os.listdir(data_dir):
    if archivo.endswith(".dcm"):
        shutil.copy(os.path.join(data_dir, archivo), "dicom_files/")

# Ejecutar el procesador
procesador = ProcesadorDICOM()
procesador.cargar_archivos("dicom_files/")
procesador.extraer_metadatos()
procesador.calcular_intensidad()
procesador.procesar_imagenes("output/")