import os
import pathlib

carpeta = "C:/Users/juanl/OneDrive/Música"
with os.scandir(carpeta) as ficheros:
    for fichero in ficheros:
        path = pathlib.Path(fichero.path)
        if path.suffix == ".mp4":
                os.remove(fichero.path)
print("Se han eliminado los archivos :)")