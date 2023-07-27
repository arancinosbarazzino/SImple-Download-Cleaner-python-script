import os
import time

DownloadPath = "C:/Users/Samu/Downloads/"


def numberOfFolders():  # controlla il numero di cartelle da non spostare
    i = 0
    f = os.scandir(DownloadPath)
    for element in f:
        if os.path.isdir(element.path):
            i += 1
    return i

# funzione principale che sposta i file nella cartella e li rinomina se esistono già


def spostamento(cartella, file):
    print("controllo che non esista già un file con lo stesso nome in " + cartella)
    trovato = 1
    while (trovato != 0):
        trovato = 0
        f = os.scandir(DownloadPath+cartella)
        for element in f:
            if element.name == file:
                senzaEstensione = file[:file.rfind('.')] or file
                estensione = file[file.rfind('.'):]
                senzaEstensione += " - 1"
                file = senzaEstensione+estensione
                print("cambiato nome del file in " + file)
                break
    print("sposto " + file + " in " + cartella + "...")
    os.rename(DownloadPath + i,
              DownloadPath+cartella+file)
    print("fatto")


def fileTemporanei():
    print("cerco file .temp o .part")
    f = os.listdir(DownloadPath)
    for element in f:
        if element.endswith(".part") or element.endswith(".temp"):
            print("trovato")
            nome = element[:element.rfind('.')] or element
            return nome
    print("non trovato")
    return ""


# creazione delle cartelle se non esistono
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
    time.sleep(150)  # zzz
    OldNumber = NumberOfFiles
    NumberOfFiles = len(os.listdir(DownloadPath))
    if NumberOfFiles != numberOfFolders():  # controllo se gli unici file presenti sono le cartelle
        print("trovati nuovi file")
        s = os.listdir(DownloadPath)
        nomeFileTemp = fileTemporanei()
        for i in s:
            fileAttuale = i
            fileAttualeNoEstensione = fileAttuale[:fileAttuale.rfind('.')] or fileAttuale #tolgo l'estensione al file attuale per controllarlo con il file .part o .temp
            fileAttuale.lower
            # questo non fa muovere i file .part e .temp e i suoi rispettivi file
            if (fileAttualeNoEstensione != nomeFileTemp and not fileAttuale.endswith(".part") and not fileAttuale.endswith(".temp")):
                if fileAttuale.endswith(".jpg") or fileAttuale.endswith(".png") or fileAttuale.endswith(".webp") or fileAttuale.endswith(".jpeg") or fileAttuale.endswith(".heic") or fileAttuale.endswith("svg") or fileAttuale.endswith(".avif"):
                    spostamento("Immagini/", i)
                elif fileAttuale.endswith(".mp4") or fileAttuale.endswith(".gif"):
                    spostamento("Video/", i)
                elif fileAttuale.endswith(".exe") or fileAttuale.endswith(".msi"):
                    spostamento("Exe/", i)
                elif fileAttuale.endswith(".m4a") or fileAttuale.endswith(".mp3") or fileAttuale.endswith(".wav"):
                    spostamento("Audio/", i)
                elif fileAttuale.endswith(".zip") or fileAttuale.endswith(".rar") or fileAttuale.endswith("7z"):
                    spostamento("ZipRar/", i)
                elif fileAttuale.endswith(".pdf"):
                    spostamento("Pdf/", i)
                # ogni cosa che non ha un punto all'interno del nome
                elif not os.path.isdir(DownloadPath+i):

                    spostamento("Altro/", i)
            else:
                print("file .part non mosso")
    else:
        print("nessun nuovo file trovato")
