import os
import pathlib
import moviepy.editor as mp
import shutil

def Convertir (archivo):
    with os.scandir(archivo) as ficheros:
        for fichero in ficheros:
            path = pathlib.Path(fichero.path)
            if path.suffix == ".mp4":
                clip = mp.VideoFileClip(fichero.path)
                clip.audio.write_audiofile(f'{path.stem}.mp3', bitrate="320k")
                shutil.move(f'{path.stem}.mp3', '') #Entre las comillas poner ruta de destino
    print("Se han convertido los archivos :)")
