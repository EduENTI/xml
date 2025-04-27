#!/bin/python3

from bs4 import BeautifulSoup
import os
import base64

#Constantes rutas a directorios
ALBUMS_PATH = "albums/"
ARTISTS_PATH = "artists/"
SONGS_PATH = "songs/"
GENRES_PATH = "genres/"
COVERS_PATH = "covers/"

#Estructuras para loadear información
albums = []
artists = []
songs = []
genres = []
covers = []


error = 0

version = 0.5

app_title = "Playlist v" + str(version)



def image_to_base64(image_path):
    image = open(image_path, "rb")

    return base64.b64encode(image.read()).decode('utf-8')


def print_menu():
    os.system("cls" if os.name == "nt" else "clear")

    print(app_title)

    print("-" * len(app_title))
    
    print("    MENÚ")

def show_menu_songs():
    print_menu()

    print("\n1. Listar todas las canciones.\n", "2. Buscar canción por título\n", "0. Volver\n")

def show_menu_albums():
    while True:
        print_menu()
        print("\n1. Listar todos los álbumes.\n2. Buscar álbum por título.\n0. Volver\n")

        option = input("Elige una opción: ")

        if option == "0":
            break
        elif option == "1":
            list_all_albums()
            input("\nPresiona Enter para continuar...")
        elif option == "2":
            print("Buscar álbum -pendiente-.")
        else:
            print("ERROR 01: La opción elegida no es válida.")

def show_menu_artists():
    print_menu()

    print("\n1. Listar todos los artistas.\n2. Buscar artista por nombre\n0. Volver\n")

def show_menu_genres():
    print_menu()

    print("\n1. Listar todos los géneros.\n2. Buscar género por nombre\n0. Volver\n")






def list_all_albums():
    print("\n    LISTADO DEL ÁLBUMES\n")
    print(" "* 3, "-" * 20)

    for album in albums:
        print(f"\nID: {album['id']}")
        print(f"\nTítulo: {album['title']}")
        print(f"Artistas: {', '.join([a['name'] for a in album['artists']])}")
        print(f"Canciones: {len(album['songs'])}")
        print(" " * 3, "-" * 20)







def open_xml(file_path):
    file_xml = open(file_path, "r").read()

    return BeautifulSoup(file_xml, 'xml')


def load_album_file(file_name):
    file_path = ALBUMS_PATH+file_name

    album_xml = open_xml(file_path)

    album = {
        "id": album_xml.album["id"],
        "title": album_xml.title.text,
        "cover": None,
        "artists": [],
        "songs": []
    }

    if album_xml.cover:
        cover_path = COVERS_PATH+album_xml.cover["src"]
        album["cover"] = image_to_base64(cover_path)

    for artist in album_xml.artists.find_all("artist"):
        album["artists"].append({
            "id": artist["id"],
            "name": artist.text
            })

    for song in album_xml.songs.find_all("song"):
        album["songs"].append({
            "id": song["id"],
            "title": song.text
            })

    return album



def load_album_num(album_num):
    global ALBUMS_PATH

    file_name = "album_"+str(album_name)+".xml"

   

def load_albums():
    global ALBUMS_PATH
    global albums

    albums = []

    albums_dir = os.listdir(ALBUMS_PATH)

    for album in albums_dir:
        if not album.endswith(".xml") and not album.startswith("album_"):
            continue
        albums.append(load_album_file(album))

    albums.sort(key=lambda x: int(x['id']))


load_albums()


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
                break

    else:
        print("ERROR 02: Debes introducir un número.")
        error = 2






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

