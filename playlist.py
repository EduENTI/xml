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
    
    while True:
        print_menu()
        print("\n1. Listar todas las canciones.\n2. Buscar canción por título\n0. Volver\n")
    
        option = input("Elige una opción: ")

        if option == "0":
            break
        elif option == "1":
            list_all_songs()
            input("\nPresiona Enter para continuar...")
        elif option == "2":
            print("Buscar canción -pendiente-.")
        else:
            print("ERROR 01: La opción elegida no es válida.")

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
     while True:
        print_menu()
        print("\n1. Listar todos los artistas.\n2. Buscar artista por nombre.\n0. Volver\n")

        option = input("Elige una opción: ")

        if option == "0":
            break
        elif option == "1":
            list_all_artists()
            input("\nPresiona Enter para continuar...")
        elif option == "2":
            print("Buscar artista -pendiente-.")
        else:
            print("ERROR 01: La opción elegida no es válida.")

def show_menu_genres():
    while True:
        print_menu()
        print("\n1. Listar todos los géneros.\n2. Buscar género por nombre.\n0. Volver\n")

        option = input("Elige una opción: ")

        if option == "0":
            break
        elif option == "1":
            list_all_genres()
            input("\nPresiona Enter para continuar...")
        elif option == "2":
            print("Buscar género -pendiente-.")
        else:
            print("ERROR 01: La opción elegida no es válida.")



def show_album_cover():
    for album in albums:
        if album_id != album["id"]:
            continue

        ascii_img = ascii_py.asciiImage()
        img = ascii_img.img2ascii(COVERS_PATH+album["cover"])





def list_all_albums():
    print("\n    LISTADO DE ÁLBUMES\n")
    print(" " * 3, "-" * 20)

    for album in albums:
        print(f"\nID: {album['id']}")
        print(f"\nTítulo: {album['title']}")
        print(f"Artistas: {', '.join([a['name'] for a in album['artists']])}")
        print(f"Canciones: {len(album['songs'])}")
        print(" " * 3, "-" * 20)

def list_all_songs():
    print("\n    LISTADO DE CANCIONES\n")
    print(" " * 3, "-" * 20)

    for song in songs:
        print(f"\nID: {song['id']}")
        print(f"\nTítulo: {song['title']}")
        print(f"Artistas: {', '.join([a['name'] for a in song['artists']])}")
        print(f"Duración: {song['duration']} segundos")
        print(f"Álbum ID: {song['album_id']}")
        print(" " * 3, "-" * 20)

def list_all_artists():
    print("\n    LISTADO DE ARTISTAS\n")
    print(" " * 3, "-" * 20)

    for artist in artists:
        print(f"ID: {artist['id']}")
        print(f"\nNombre: {artist['name']}")
        print(f"Nacionalidad: {artist.get('nationality', 'Desconocida')}")
        print(f"Nacimiento: {artist.get('birth_date', 'No disponible')}")
        print(f"Álbumes: {len(artist.get('albums', []))}")
        print(" " * 3, "-" * 20)

def list_all_genres():
    print("\nLISTADO DE GÉNEROS\n")
    print(" " * 3, "-" * 20)

    for genre in genres:
        print(f"\nID: {genre['id']}")
        print(f"Nombre: {genre['name']}")
        print(f"Origen: {genre.get('origin', 'Desconocido')}")
        print(f"Canciones asociadas: {sum(1 for song in songs if genre['id'] in song['genres'])}")
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
        "cover": album_xml.cover["src"],
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

def load_song_file(file_name):
    file_path = SONGS_PATH+file_name

    song_xml = open_xml(file_path)

    song = {
        "id": song_xml.song["id"],
        "title": song_xml.title.text,
        "artists": [],
        "genres": [],
        "duration": int(song_xml.duration["seconds"]),
        "album_id": song_xml.album["id"]
    }

    for artist in song_xml.artists.find_all("artist"):
        song["artists"].append({
            "id": artist["id"],
            "name": artist.text
            })

    for genre in song_xml.genres.find_all("genre"):
        song["genres"].append(genre["id"])


    return song

def load_artist_file(file_name):
    file_path = ARTISTS_PATH+file_name

    artist_xml = open_xml(file_path)

    artist = {
        "id": artist_xml.artist["id"],
        "name": artist_xml.find('name').text,
        "nationality": artist_xml.nationality["country"],
        "birth_date": artist_xml.birth["date"],
        "albums":[]
    }
    
    albums = artist_xml.find('albums')

    if albums:
        for album in albums.find_all("album"):
            artist["albums"].append(album["id"])

    return artist


def load_genre_file(file_name):
    file_path = GENRES_PATH+file_name
    genre_xml = open_xml(file_path)
    
    genre = {
        "id": genre_xml.genre["id"],
        "name": genre_xml.find('name').text,
        "origin": genre_xml.origin["country"]
    }
    
    return genre



#def load_album_num(album_num):
 #   global ALBUMS_PATH
#
 #   file_name = "album_"+str(album_name)+".xml"

   

def load_albums():
    global ALBUMS_PATH
    global albums

    albums = []

    albums_dir = os.listdir(ALBUMS_PATH)

    for album in albums_dir:
        if not album.endswith(".xml") or not album.startswith("album_"):
            continue
        albums.append(load_album_file(album))

    albums.sort(key=lambda x: int(x['id']))

def load_songs():
    global SONGS_PATH
    global songs

    songs = []

    songs_dir = os.listdir(SONGS_PATH)

    for song in songs_dir:
        if not song.startswith("song_") or not song.endswith(".xml"):
            continue
        songs.append(load_song_file(song))

    songs.sort(key=lambda x: int(x['id']))


def load_artists():
    global ARTISTS_PATH
    global artists

    artists = []

    artists_dir = os.listdir(ARTISTS_PATH)

    for artist in artists_dir:
        if not artist.startswith("artist_") or not artist.endswith(".xml"):
            continue
        artists.append(load_artist_file(artist))

    artists.sort(key=lambda x: int(x['id']))

def load_genres():
    global GENRES_PATH
    global genres

    genres =[]

    genres_dir = os.listdir(GENRES_PATH)

    for genre in genres_dir:
        if not genre.startswith("genre_") or not genre.endswith(".xml"):
            continue
        genres.append(load_genre_file(genre))

    genres.sort(key=lambda x: int(x['id']))

load_albums()
load_songs()
load_artists()
load_genres()

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


