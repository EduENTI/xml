#!/bin/python3

from bs4 import BeautifulSoup
import os




version = 0.5

app_title = "Playlist v" + str(version)

def show_menu_songs():
    print("\n", "1. Listar todas las canciones.", "\n", "2. Buscar canción por título", "\n", "0. Volver", "\n")

def show_menu_albums():
    print("\n", "1. Listar todos los álbumes.", "\n", "2. Buscar álbum por título", "\n", "0. Volver", "\n")

def show_menu_artists():
    print("\n", "1. Listar todos los artistas.", "\n", "2. Buscar artista por nombre", "\n", "0. Volver", "\n")

def show_menu_genres():
    print("\n", "1. Listar todos los géneros.", "\n", "2. Buscar género por nombre", "\n", "0. Volver", "\n")


#xml_ejemplo = '<personaje><nombre>Jacinto</nombre><edad valor="33" /></personaje>'

#print(xml_ejemplo)

#personaje = BeautifulSoup(xml_ejemplo, 'xml')

#print(personaje.prettify())

#nombre = personaje.nombre

#print(nombre)

#print(nombre.contents)

#print(nombre.text)


#song_xml = open("songs/song_1.xml", "r").read()

#song = BeautifulSoup(song_xml, "xml")

#print(song.title.text)
#print(int(song.duration["seconds"])/60)

#for artist in song.artists.find_all("artist"):
 #   print(artist.text)

error = 0

while True:

    os.system("cls" if os.name == "nt" else "clear")

    print(app_title)

    print("-" * len(app_title))
    
    print("    MENÚ")

    print("\n", "1. Álbumes", "\n", "2. Artistas", "\n", "3. Canciones", "\n", "4. Géneros", "\n", "0. Salir", "\n")
    
    if(error == 1):
        print("ERROR 01: La opción elegida no es válida.")
    elif(error == 2):
        print("ERROR 02: Debes introducir un número.")

    respuesta = input("Elije una respuesta: ")
    
    if respuesta.isdigit():

        if (int(respuesta) < 0 or int(respuesta) > 4):
            print("ERROR 01: La opción elegida no es válida.")
            error = 1
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Escogiste el numero", respuesta)
            break
    else:
        print("ERROR 02: Debes introducir un número.")
        error = 2
