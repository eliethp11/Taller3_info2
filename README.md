# Taller3_info2
# Taller 3 – Informática Médica: Procesamiento de Archivos DICOM

**Integrantes:** Elieth Mariana Puentes Zorro 
**Materia:** Informática 2 – Universidad de Antioquia  
**Monitor:** Juan Esteban Pineda Lopera

---

## 1. Descripción del proyecto

Esta aplicación en Python automatiza la lectura, extracción y almacenamiento de metadatos de archivos DICOM, y realiza procesamiento básico de imágenes médicas usando OpenCV. Se implementó usando Programación Orientada a Objetos con la clase `ProcesadorDICOM`, que encapsula los siguientes pasos: carga de archivos, extracción de metadatos, cálculo de intensidad promedio con NumPy, y procesamiento de imágenes con OpenCV (normalización, ecualización de histograma y detección de bordes con Canny).

---

## 2. DICOM y HL7: interoperabilidad en salud

**DICOM** (Digital Imaging and Communications in Medicine) es el estándar para el almacenamiento y transmisión de imágenes médicas. Define tanto el formato de la imagen como sus metadatos asociados (paciente, modalidad, fecha, equipo).

**HL7** (Health Level 7) es un estándar para el intercambio de información clínica en texto: historias clínicas, órdenes médicas, resultados de laboratorio y diagnósticos.

La diferencia conceptual es clara: DICOM maneja **imágenes**, HL7 maneja **eventos clínicos**. Ambos son complementarios en un sistema de salud real: HL7 comunica que un médico ordenó una tomografía, y DICOM se encarga de transmitir y archivar esa tomografía. Sin estos estándares, los sistemas de diferentes fabricantes no podrían comunicarse entre sí, rompiendo el flujo de atención al paciente.

---

## 3. Ecualización de histograma y detección de bordes con Canny en imágenes médicas

### Ventajas
- La **ecualización de histograma** mejora el contraste de imágenes con poca variación de intensidad, haciendo visibles estructuras que de otra forma serían difíciles de distinguir. Es útil como paso de preprocesamiento antes de segmentación.
- El **detector de Canny** resalta bordes y contornos anatómicos con precisión, lo que facilita la identificación de estructuras como huesos, tumores o tejidos.

### Limitaciones
- La ecualización puede **amplificar el ruido** presente en la imagen, distorsionando información clínica relevante.
- Canny es sensible a los umbrales elegidos: umbrales incorrectos pueden generar bordes falsos o perder bordes reales.
- En imágenes médicas con alta precisión diagnóstica, estas técnicas pueden alterar sutilezas importantes si no se aplican con cuidado.

### Escenarios de uso
- **Útil:** preprocesamiento para segmentación automática, visualización exploratoria, entrenamiento de modelos de IA.
- **Perjudicial:** diagnóstico directo sin supervisión médica, imágenes donde el contraste original es clínicamente significativo.

---

## 4. Dificultades y herramientas utilizadas

### Dificultades encontradas
- Algunos archivos DICOM no contienen datos de píxeles (modalidades SR, ECG, RTPLAN), lo que requirió manejo de excepciones cuidadoso.
- Las imágenes DICOM pueden tener diferentes profundidades de bits (12, 16, 32 bits) y formatos (RGB, escala de grises, multiframe), lo que generó errores en OpenCV que debieron resolverse convirtiendo siempre a float32 antes de normalizar.
- La versión de pydicom instalada no tenía los métodos documentados en versiones anteriores, lo que requirió adaptar el código.

### Importancia de las herramientas Python
- **pydicom** permite leer el estándar DICOM sin depender de software propietario.
- **NumPy** facilita el análisis numérico de matrices de píxeles de forma eficiente.
- **Pandas** organiza los metadatos en estructuras tabulares consultables.
- **OpenCV** ofrece algoritmos de procesamiento de imagen ampliamente usados en investigación médica y visión por computador.

---

## Instalación y uso

```bash
pip install pydicom numpy pandas opencv-python
python main.py
```

Los resultados se guardan en la carpeta `output/` como archivos `.png`.