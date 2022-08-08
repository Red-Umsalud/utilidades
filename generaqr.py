import qrcode
import sys
from csv import reader

RUTA_CSV = str(sys.argv[1])

with open(RUTA_CSV,'r') as f:
    csv_reader = reader(f)
    contador = 0
    for row in csv_reader:
        img = qrcode.make(str(row[0]))
        img.save(f'qr{contador}.png')
        contador += 1
