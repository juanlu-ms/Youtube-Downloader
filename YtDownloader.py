from pytube import YouTube

link = input("Introduzca el link del vídeo\n")
yt = YouTube(link)

print("Título: ",yt.title)

yd = yt.streams.get_highest_resolution()

tipo = input("¿Es música (1) o vídeo (2)?\n")

if tipo == "1":
    yd.download('') #Poner en el paréntesis la carpeta deseada si es música
elif tipo == "2":
    yd.download('') #Poner en el paréntesis la carpeta deseada si es un vídeo

print("Se ha completado la descarga :)")
