import qrcode
import sys
from csv import reader

RUTA_CSV = str(sys.argv[1])
archivo = open(RUTA_CSV)
csv_reader = reader(archivo)
contador = 0
for i in csv_reader:
    contenido = i
    img = qrcode.make(contenido)
    img.save(f'{contador}-{i[1]}.png')
    contador += 1
