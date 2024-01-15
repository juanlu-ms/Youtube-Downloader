from pytube import YouTube
from Convertidor_MP3_MP4 import Convertir
from Rutas import MUSICA, VIDEOS

link = input("Introduzca el link del vídeo\n")
yt = YouTube(link)

print("Título: ",yt.title)

yd = yt.streams.get_highest_resolution()

tipo = input("¿Es música (1) o vídeo (2)?\n")

if tipo == "1":
    yd.download(MUSICA)
    Convertir(MUSICA)

elif tipo == "2":
    yd.download(VIDEOS)

print("Se ha completado la descarga :)")