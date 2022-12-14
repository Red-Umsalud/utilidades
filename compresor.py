from PIL import Image
import sys

# Syntaxis de ejecucion
# python compresor.py <nombre del archivo.jpg>
# Desde Windows es posible jalar la imagen hasta el archivo "compresor.py"

RUTA_IMAGEN = str(sys.argv[1])
SIZE_IMAGEN_PEQUE = (450,350)
SIZE_IMAGEN_CARROUSEL = (1200,700)
SIZE_IMAGEN_NOTIC = (1200,800)
SIZE_IMAGEN_BANNER = (1200,400)


img = Image.open(f'{RUTA_IMAGEN}')
width, height = img.size


output1 = img.resize(SIZE_IMAGEN_PEQUE, Image.ANTIALIAS)
output1.save('imagen_peque.jpg', quality=50)

output2 = img.resize(SIZE_IMAGEN_BANNER, Image.ANTIALIAS)
output2.save('imagen_banner.jpg', quality=95)

output3 = img.resize(SIZE_IMAGEN_NOTIC, Image.ANTIALIAS)
output3.save('imagen_noticia.jpg', quality=95)

output4 = img.resize(SIZE_IMAGEN_CARROUSEL, Image.ANTIALIAS)
output4.save('imagen_carrousel.jpg', quality=95)
