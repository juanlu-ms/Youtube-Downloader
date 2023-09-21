from pytube import YouTube
from Convertidor_MP3_MP4 import Convertir

link = input("Introduzca el link del vídeo\n")
yt = YouTube(link)

print("Título: ",yt.title)

yd = yt.streams.get_highest_resolution()

tipo = input("¿Es música (1) o vídeo (2)?\n")

if tipo == "1":
    yd.download('C:/Users/juanl/OneDrive/Música')
    Convertir('C:/Users/juanl/OneDrive/Música')

elif tipo == "2":
    yd.download('C:/Users/juanl/OneDrive/Videos')

print("Se ha completado la descarga :)")