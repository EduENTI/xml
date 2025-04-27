#!/bin/python3

from bs4 import BeautifulSoup
import os

ALBUMS_PATH = "albums/"
ARTISTS_PATH = "artists/"
SONGS_PATH = "songs/"
GENRES_PATH = "genres/"
COVERS_PATH = "covers/"


albums = []
artists = []
songs = []
genres = []
covers = []


error = 0

version = 0.5

app_title = "Playlist v" + str(version)

def print_menu():
    os.system("cls" if os.name == "nt" else "clear")

    print(app_title)

    print("-" * len(app_title))
    
    print("    MENÚ")


def show_menu_songs():
    print_menu()

    print("\n", "1. Listar todas las canciones.", "\n", "2. Buscar canción por título", "\n", "0. Volver", "\n")

def show_menu_albums():
    print_menu()

    print("\n", "1. Listar todos los álbumes.", "\n", "2. Buscar álbum por título", "\n", "0. Volver", "\n")

def show_menu_artists():
    print_menu()

    print("\n", "1. Listar todos los artistas.", "\n", "2. Buscar artista por nombre", "\n", "0. Volver", "\n")

def show_menu_genres():
    print_menu()

    print("\n", "1. Listar todos los géneros.", "\n", "2. Buscar género por nombre", "\n", "0. Volver", "\n")


def open_xml(file_path):
    file_xml = open(file_path, "r").read()

    return BeautifulSoup(file_xml, 'xml')


def load_album_file():
    file_path = ALBUM_PATH+file_name

    album_xml = open_xml(file_path)

    album = {
        "id": album_xml.album["id"],
        "title": album_xml.title.text
    }

    return album



def load_album_num(album_num):
    global ALBUMS_PATH

    file_name = "album_"+str(album_name)+".xml"

   

def load_albums():
    global ALBUM_PATH
    global albums

    albums_dir = os.listdir(ALBUMS_PATH)

    for album in albums_dir:
        if not album.endswith(".xml"):
            continue
        albums.append(load_album_file(album))


while True:

    print_menu()

    print("\n", "1. Álbumes", "\n", "2. Artistas", "\n", "3. Canciones", "\n", "4. Géneros", "\n", "0. Salir", "\n")
    
    if(error == 1):
        print("ERROR 01: La opción elegida no es válida.")
    elif(error == 2):
        print("ERROR 02: Debes introducir un número.")

    respuesta = input("Elije una respuesta: ")
    
    if respuesta.isdigit():

        if (int(respuesta) < 0 and int(respuesta) > 4):
            print("ERROR 01: La opción elegida no es válida.")
            error = 1
        else:
            os.system("cls" if os.name == "nt" else "clear")

            respuesta = int(respuesta)

            if (respuesta == 1):
                show_menu_albums()
            elif (respuesta == 2):
                show_menu_artists()
            elif (respuesta == 3):
                show_menu_songs()
            elif (respuesta == 4):
                show_menu_genres()
            elif (respuesta == 0):
                print("Escogiste el numero", respuesta)
            break

    else:
        print("ERROR 02: Debes introducir un número.")
        error = 2



load_albums()














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




"""

    album = {
        "id": album_xml.album["id"],
        "title": album_xml.album["title"].text,
        "cover": "IMAGEN",
        "artists": [
                {
                    "id": 1,
                    "name": "NOMBRE!!"
                }
            ]
        "songs": [
                {
                    "id": 1,
                    "title": "TÍTULO!!"
                },
                {
                    "id": 2,
                    "title": "TÍTULO!!"
                }

            ]

    }

"""

