import io
import pathlib
import ast

import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

# COLORES
backgroundClickButton = "#5F6A6A"
backgroundButtonMain = "#717D7E"
backgroundMain = "#2E4053"
backgroundEntrada = "#17202A"
fondo_salir="#ed1c24"

# VARIABLES GLOBALES
centroEntrada = 160

class Libro:
    def __init__(self, titulo, autor, genero, anio_publicacion, disponible):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible


class Biblioteca:
    def __init__(self):
        self.libros =[]
        path_to_file = 'libreria.csv'
        path = pathlib.Path(path_to_file)

        if not path.is_file():
            file = io.open(r"libreria.csv","w")
            file.close()
        file = io.open(r"libreria.csv","r")
        content = file.readlines()
        for line in content:
            data = line.strip().split(",")
            libro = Libro(data[0], data[1], data[2], data[3],ast.literal_eval(data[4]))
            self.libros.append(libro)
        file.close()

    def __del__(self):
        file = io.open(r"libreria.csv","w")
        for libro in self.libros:
            output = libro.titulo+","+libro.autor+","+libro.genero+","+libro.anio_publicacion+","+str(libro.disponible)+"\n"
            file.write(output)
        file.close()


    def agregar_libro(self,libro):
        self.libros.append(libro)
        return 'Libro registrado con exito.'
            
    def mostrarLibros(self,libros,libros_text):
        libros_text.config(state=tk.NORMAL)  # Habilitar edición temporalmente
        libros_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
        if not libros:
            libros_text.insert(tk.END, 'No hay libros registrados\n')
        else:
            for libro in libros:
                libros_text.insert(tk.END, f'Titulo: \t{libro.titulo}\n')
                libros_text.insert(tk.END, f'Autor: \t{libro.autor}\n')
                libros_text.insert(tk.END, f'Genero: \t{libro.genero}\n')
                libros_text.insert(tk.END, f'Año de publicación: \t{libro.anio_publicacion}\n')
                libros_text.insert(tk.END, "Disponible\n" if libro.disponible else "Reservado\n")
                libros_text.insert(tk.END, '-------------------------------------------------------\n')
        libros_text.config(state=tk.DISABLED)

    def mostrarLibro(self,libros_text):
        self.mostrarLibros(self.libros,libros_text)

    def buscar(self, autor, libros_text):
        libros_encontrados = []
        for libro in self.libros:
            if libro.autor.lower() == autor.lower():
                libros_encontrados.append(libro)
        self.mostrarLibros(libros_encontrados,libros_text)

    def reservar(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower() and libro.disponible:
                libro.disponible = False
                return "Libro reservado con exito"
        return "No hay libros disponibles \n con ese Titulo"

    def cancelarReserva(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower() and not libro.disponible:
                libro.disponible = True
                return "Reservacion Cancelada con \nexito"
        return "No hay libros Reservados \n con ese Titulo"
    
    def editar(self, index, titulo, autor, genero, anio):
        self.libros[index].titulo = titulo;
        self.libros[index].autor = autor;
        self.libros[index].genero = genero;
        self.libros[index].anio_publicacion = anio;
        return "El libro se actualizó \ncorrectamente"
    


    def eliminar(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                self.libros.remove(libro)
                return (f'El Libro con el titulo:\n {titulo} fue eliminado')
        return ("No hay libros con ese Titulo")