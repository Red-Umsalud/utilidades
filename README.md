# Utilidades Varias en Python

Miniapps para facilitar el trabajo en Red-Umsalud

## Instalacion

Primero es necesario clonar el repositorio con:

´´´sh
git clone https://github.com/Red-Umsalud/utilidades.git
´´´

Las herramientas requieren tener instalado Python 3.9 o superior. También es
necesaria la instalación de las bibliotecas para el correcto funcionamiento
con:

´´´sh
pip install -r requirements.txt
´´´

## Compresor de imágenes para la página de medicina

Mediante la interfaz grafica en Windows solo es necesario arrastrar la imagen hacia el
archivo ´compresor.py´.

O desde la terminal:

´´´sh
python compresor.py <nombredearchivo.jpg>
´´´

## Generador de códigos QR

Desde la GUI de Windows se debe arrastar el archivo CSV hacia el archivo
"generaqr.py". Las imágenes serán generadas en la misma carpeta.

O desde terminal:

´´´sh
python generaqr.py <nombredearchivo.csv>
´´´
