import os
import time

DownloadPath="C:/Users/Samu/Downloads/"

def spostamento(cartella, file):
    print("controllo che non esista già un file con lo stesso nome in " + cartella)
    trovato=1
    while(trovato!=0):
        trovato=0
        f = os.scandir(DownloadPath+cartella)
        for element in f:
            if element.name == file:
                senzaEstensione = file[:file.rfind('.')] or file
                estensione= file[file.rfind('.'):]
                senzaEstensione+=" - 1"
                file=senzaEstensione+estensione
                print("cambiato nome del file in " + file)
                break
    print("sposto " + file + " in " + cartella + "...")
    os.rename(DownloadPath + i,
              DownloadPath+cartella+file)
    print("fatto")

if not os.path.exists(DownloadPath+"Immagini"):
    os.mkdir(DownloadPath+"Immagini")
if not os.path.exists(DownloadPath+"Video"):
    os.mkdir(DownloadPath+"Video")
if not os.path.exists(DownloadPath+"Exe"):
    os.mkdir(DownloadPath+"Exe")
if not os.path.exists(DownloadPath+"Audio"):
    os.mkdir(DownloadPath+"Audio")
if not os.path.exists(DownloadPath+"Altro"):
    os.mkdir(DownloadPath+"Altro")
if not os.path.exists(DownloadPath+"ZipRar"):
    os.mkdir(DownloadPath+"ZipRar")
if not os.path.exists(DownloadPath+"Pdf"):
    os.mkdir(DownloadPath+"Pdf")
while True:
    print("controllo nuovi file...")
    NumberOfFiles = len(os.listdir(DownloadPath))
    time.sleep(150)
    OldNumber = NumberOfFiles
    NumberOfFiles = len(os.listdir(DownloadPath))
    if NumberOfFiles != OldNumber:
        print("trovati nuovi file")
        s = os.listdir(DownloadPath)
        for i in s:
            cartella = ""
            temp = i
            temp.lower
            if not temp.endswith(".temp") or temp.endswith(".part"):
                if temp.endswith(".jpg") or temp.endswith(".png") or temp.endswith(".webp") or temp.endswith(".jpeg") or temp.endswith(".heic") or temp.endswith("svg") or temp.endswith(".avif"):
                    cartella = "Immagini/"
                    spostamento(cartella, i)
                elif temp.endswith(".mp4") or temp.endswith(".gif"):
                    cartella = "Video/"
                    spostamento(cartella, i)
                elif temp.endswith(".exe") or temp.endswith(".msi"):
                    cartella = "Exe/"
                    spostamento(cartella, i)
                elif temp.endswith(".m4a") or temp.endswith(".mp3") or temp.endswith(".wav"):
                    cartella = "Audio/"
                    spostamento(cartella, i)
                elif temp.endswith(".zip") or temp.endswith(".rar") or temp.endswith("7z"):
                    cartella = "ZipRar/"
                    spostamento(cartella, i)
                elif temp.endswith(".pdf"):
                    cartella = "Pdf/"
                    spostamento(cartella, i)
                elif temp.find(".") != -1:
                    cartella = "Altro/"
                    spostamento(cartella, i)
    else:
        print("nessun nuovo file trovato")
