import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

from Biblioteca import *

# COLORES
blanco = "#ffffff"


passwordVisible = "*"
def toggle_password_visibility():
	global passwordVisible
	if passwordVisible == "":
		passwordVisible = "*"
	else:
		passwordVisible = ""
		
login = Tk()
login.title("LOGIN")
login.geometry("600x450+500+75") # tamaño de imagen
login.resizable(width=False, height=False) #evita redimencionar y fallos en imagen
fondoLogin = tk.PhotoImage(file="fondoLogin.png")
fondo1 = tk.Label(login, image=fondoLogin).place(x=0, y=0, relwidth=1,
	 relheight=1)
# TITTLE ADD BOOK
labelTitleAddBook = Label(login, text="LOGIN",bg=None, font=("Arial", 36, "bold"))
labelTitleAddBook.pack()




# ENTRADAS
user = tk.StringVar()
password = tk.StringVar()

def on_entry_click(event, entry, default_text):
	if entry.get() == default_text:
		entry.delete(0, "end")
		entry.configure(fg="white")

def on_entry_leave(event, entry, default_text):
	if entry.get() == "":
		entry.insert(0, default_text)
		entry.configure(fg="gray")

# Definir texto de fondo y entradas
entradas = [
	(tk.Entry(login, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,textvar=user), "USER"),
	(tk.Entry(login, width=22, relief="flat", show=passwordVisible, font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,textvar=password), "PASSWORD"),
]

# Crear y configurar las entradas con texto de fondo
for entry, default_text in entradas:
	entry.place(relx=0.5, y=entradas.index((entry, default_text)) * 45 + 105,anchor=tk.CENTER)
	entry.insert(0, default_text)
	entry.configure(fg="gray")  
	entry.bind("<FocusIn>", lambda event, entry=entry, default_text=default_text: on_entry_click(event, entry, default_text))
	entry.bind("<FocusOut>", lambda event, entry=entry, default_text=default_text: on_entry_leave(event, entry, default_text))
	

#FUNCIONES
def loguearse():
	name = user.get()
	contrasena = password.get()
	if name=='admin' and contrasena == 'admin':
		correcto()
	else:
		incorrecto()

def correcto():
	# MAIN PRINCIPAL
	login.withdraw()
	main = tk.Toplevel()
	main.title("Biblioteca")
	main.geometry("600x750+500+1") # tamaño de imagen
	main.resizable(width=False, height=False) #evita redimencionar y fallos en imagen

	# BIBLIOTECA
	biblioteca = Biblioteca()

	# COLORES
	backgroundClickButton = "#1C2833"    #"#5F6A6A" 
	backgroundButtonMain = "#2E4053"  #"#717D7E"
	backgroundMain = "#2E4053"
	backgroundEntrada = "#17202A"
	fondo_salir="#ed1c24"
	backgroundPizarra = "#1B2631"
	backgroundTitle = "#117A65"
	negro="#000000"
	backgroundSecond="#273746"
	

	# Cambiar el color de fondo
	main.config(bg=negro)

	# FUNCIONES BOTONES
	def addBook():
		main.withdraw()
		windowAdd = tk.Toplevel()
		windowAdd.title("Add Book")
		windowAdd.geometry("600x750+500+1")
		windowAdd.resizable(width=False, height=False)
		windowAdd.config(background=backgroundSecond)
		

		# FUNCIONES
		# Label add or not
		labelAddBook = Label(windowAdd, text="", bg=backgroundSecond, font=("Arial", 22), fg=blanco)
		labelAddBook.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
		def add():
			title = titulo.get()
			nombreAutor = autor.get()
			gener = genero.get()
			anio = anio_publicacion.get()
			if title != "Título" and nombreAutor != "Autor" and gener != "Género" and anio != "Año de Publicación":
				libro = Libro(title,nombreAutor,gener,anio, True)
				clearentries()
				Mensaje = biblioteca.agregar_libro(libro)
			else:
				Mensaje = "Campos vacios"

			# Label add or not
			labelAddBook.config(text=Mensaje)
			
			
		
		def regreso():
			windowAdd.withdraw()
			main.deiconify()
		# TITTLE ADD BOOK
		labelTitleAddBook = Label(windowAdd, text="Add Book", bg=backgroundTitle, font=("Arial", 27), fg=blanco)
		labelTitleAddBook.place(relx=0.5, rely=0.10, anchor=tk.CENTER, relwidth=1, relheight=0.2)
		
		# ENTRADAS
		titulo = tk.StringVar()
		autor = tk.StringVar()
		genero = tk.StringVar()
		anio_publicacion =tk.StringVar()

		def on_entry_click(event, entry, default_text):
			if entry.get() == default_text:
				entry.delete(0, "end")
				entry.configure(fg="white")

		def on_entry_leave(event, entry, default_text):
			if entry.get() == "":
				entry.insert(0, default_text)
				entry.configure(fg="gray")

		# Definir texto de fondo y entradas
		entradas = [
			(tk.Entry(windowAdd, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,textvar=titulo), "Título"),
			(tk.Entry(windowAdd, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,textvar=autor), "Autor"),
			(tk.Entry(windowAdd, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada, textvar=genero), "Género"),
			(tk.Entry(windowAdd, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada, textvar=anio_publicacion), "Año de Publicación"),
		]

		# Crear y configurar las entradas con texto de fondo
		for entry, default_text in entradas:
			entry.place(relx=0.5, y=entradas.index((entry, default_text)) * 45 + 195,anchor=tk.CENTER, relwidth=1)
			entry.insert(0, default_text)
			entry.configure(fg="gray")  
			entry.bind("<FocusIn>", lambda event, entry=entry, default_text=default_text: on_entry_click(event, entry, default_text))
			entry.bind("<FocusOut>", lambda event, entry=entry, default_text=default_text: on_entry_leave(event, entry, default_text))

		def clearentries():
			for entry, default_text in entradas:
				entry.delete(0, 'end')
				entry.insert(0, default_text)
				entry.configure(fg="gray")

		# BOTONES
		buttonAdd = Button(windowAdd, text="Agregar Libro", cursor="hand2", relief="flat", 
			bg=backgroundButtonMain, font=("Arial", 18), fg=blanco,
			activebackground=backgroundClickButton, command=add, 
			borderwidth=3, highlightbackground="black")
		buttonAdd.place(relx=0.5, rely=0.85, anchor=tk.CENTER, relwidth=1, relheight=0.095)
		
		buttonReturn = tk.Button(windowAdd, text="Regresar", command=regreso, 
			cursor="hand2", relief="flat", 
		bg=fondo_salir, font=("Comic Sans MS", 18), fg=blanco,
		activebackground=backgroundClickButton)
		buttonReturn.place(relx=0.5, rely=0.95, anchor=tk.CENTER, relwidth=1, relheight=0.095)
		windowAdd.mainloop()

	def viewBooks():
		main.withdraw()
		windowView = tk.Toplevel()
		windowView.title("View Books")
		windowView.geometry("600x750+500+1")
		windowView.resizable(width=False, height=False)
		windowView.config(background=backgroundSecond)

		def regreso():
			windowView.withdraw()
			main.deiconify()
		
		# TITTLE ADD BOOK
		labelTitleViewBook = Label(windowView, text="VER LIBROS", bg=backgroundTitle, font=("Arial", 27),fg=blanco)
		labelTitleViewBook.place(relx=0.5, rely=0.10, anchor=tk.CENTER, relwidth=1, relheight=0.2)

		libros_text = scrolledtext.ScrolledText(windowView, wrap=tk.WORD, width=80, height=15, font=("Arial", 18), bg= backgroundPizarra, fg=blanco)
		libros_text.place(relx=0.5, rely=0.55, anchor=tk.CENTER, relwidth=1, relheight=0.75)
		libros_text.config(state=tk.DISABLED)  # Para que no sea editable

		libros = biblioteca.libros
		biblioteca.mostrarLibros(libros,libros_text)



		buttonReturn = tk.Button(windowView, text="Regresar", command=regreso, 
			cursor="hand2", relief="flat", 
		bg=fondo_salir, font=("Comic Sans MS", 18), fg=blanco,
		activebackground=backgroundClickButton)
		buttonReturn.place(relx=0.5, rely=0.95, anchor=tk.CENTER, relwidth=1, relheight=0.095)
		windowView.mainloop()

	def searchBook():
		main.withdraw()
		windowSearch = tk.Toplevel()
		windowSearch.title("Search Books")
		windowSearch.geometry("1200x750+200+1")
		windowSearch.resizable(width=False, height=False)
		windowSearch.config(background=backgroundSecond)

		# Variables de cadena para entradas
		autor = tk.StringVar()
		titulo = tk.StringVar()
		anio = tk.StringVar()
		genero = tk.StringVar()

		# Definir texto de fondo y entradas
		entradas = [
			(tk.Entry(windowSearch, width=44, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,
					  textvar=autor), "Autor"),
			(tk.Entry(windowSearch, width=44, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,
					  textvar=titulo), "Título"),
			(tk.Entry(windowSearch, width=44, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,
					  textvar=anio), "Año de Publicación"),
			(tk.Entry(windowSearch, width=44, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,
					  textvar=genero), "Género")
		]

		# Crear y configurar las entradas con texto de fondo
		for entry, default_text in entradas:
			entry.place(relx=0.5, rely=entradas.index((entry, default_text)) * 0.05 + 0.22, anchor=tk.CENTER, relwidth=1)
			entry.insert(0, default_text)
			entry.configure(fg="gray")
			entry.bind("<FocusIn>",
					   lambda event, entry=entry, default_text=default_text: on_entry_click(event, entry, default_text))
			entry.bind("<FocusOut>",
					   lambda event, entry=entry, default_text=default_text: on_entry_leave(event, entry, default_text))

		libros_text = scrolledtext.ScrolledText(windowSearch, wrap=tk.WORD, width=80, height=15, font=("Arial", 18),
												bg=backgroundPizarra, fg=blanco)
		libros_text.place(relx=0.5, rely=0.55, anchor=tk.CENTER, relwidth=1, relheight=0.3)
		libros_text.config(state=tk.DISABLED)  # Para que no sea editable

		def on_entry_click(event, entry, default_text):
			if entry.get() == default_text:
				entry.delete(0, "end")
				entry.configure(fg="white")

		def on_entry_leave(event, entry, default_text):
			if entry.get() == "":
				entry.insert(0, default_text)
				entry.configure(fg="gray")

		def regreso():
			windowSearch.withdraw()
			main.deiconify()

		def search():
			Autor = autor.get()
			Titulo = titulo.get()
			Anio = anio.get()
			Genero = genero.get()

			if Autor == "Autor" and Titulo == "Título" and Anio == "Año de Publicación" and Genero == "Género":
				libros_text.config(state=tk.NORMAL)  # Habilitar edición temporalmente
				libros_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
				libros_text.insert(tk.END, 'Por favor, ingrese al menos un criterio de búsqueda.\n')
				libros_text.config(state=tk.DISABLED)
				return

			libros_encontrados = []

			for libro in biblioteca.libros:
				if ((not Autor and Autor != "Autor" or Autor.lower() in libro.autor.lower()) or
						(not Titulo and Titulo != "Título" or Titulo.lower() in libro.titulo.lower()) or
						(not Anio and Anio != "Año de Publicación" or Anio == str(libro.anio_publicacion)) or
						(not Genero and Genero != "Género" or Genero.lower() in libro.genero.lower())):
					libros_encontrados.append(libro)

				libros_text.config(state=tk.NORMAL)  # Habilitar edición temporalmente
				libros_text.delete(1.0, tk.END)  # Limpiar el contenido anterior

			if not libros_encontrados:
				libros_text.insert(tk.END, 'No se encontraron libros con los criterios de búsqueda.\n')
				libros_text.config(state=tk.DISABLED)
			else:
				for libro in libros_encontrados:
					libros_text.insert(tk.END, f'Título: {libro.titulo}\n')
					libros_text.insert(tk.END, f'Autor: {libro.autor}\n')
					libros_text.insert(tk.END, f'Género: {libro.genero}\n')
					libros_text.insert(tk.END, f'Año de Publicación: {libro.anio_publicacion}\n')
					libros_text.insert(tk.END, "Disponible\n" if libro.disponible else "Reservado\n")
					libros_text.insert(tk.END, '----------------------------------------\n')
				libros_text.config(state=tk.DISABLED)

		labelTitleSearchBook = Label(windowSearch, text="BUSCAR LIBRO", bg=backgroundTitle, font=("Arial", 27),
									 fg=blanco)
		labelTitleSearchBook.place(relx=0.5, rely=0.10, anchor=tk.CENTER, relwidth=1, relheight=0.2)

		buttonSearch = Button(windowSearch, text="Buscar Libro", cursor="hand2", relief="flat",
							  bg=backgroundButtonMain, font=("Arial", 18), fg=blanco,
							  activebackground=backgroundClickButton, command=search,
							  borderwidth=3, highlightbackground="black")
		buttonSearch.place(relx=0.5, rely=0.85, anchor=tk.CENTER, relwidth=1, relheight=0.095)

		buttonReturn = tk.Button(windowSearch, text="Regresar", command=regreso,
								 cursor="hand2", relief="flat",
								 bg=fondo_salir, font=("Comic Sans MS", 18), fg=blanco,
								 activebackground=backgroundClickButton)
		buttonReturn.place(relx=0.5, rely=0.95, anchor=tk.CENTER, relwidth=1, relheight=0.095)

		windowSearch.mainloop()

	def reservarBook():
		main.withdraw()
		windowReservar = tk.Toplevel()
		windowReservar.title("Reserve Books")
		windowReservar.geometry("600x750+500+1")
		windowReservar.resizable(width=False, height=False)
		windowReservar.config(background=backgroundSecond)


		def regreso():
			windowReservar.withdraw()
			main.deiconify()

		# Label reservado o no
		labelReservarBook = Label(windowReservar, text="", bg=backgroundSecond, font=("Arial", 22), fg=blanco)
		labelReservarBook.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
		def reservar():
			title = titulo.get()
			if title!="Titulo":
				Mensaje = biblioteca.reservar(title)
				clearentries()
			else:
				Mensaje = "Campo vacios, Escriba el autor a buscar"

			# Label reservado o no
			labelReservarBook.config(text=Mensaje)
			
		# TITTLE reserve BOOK
		labelTitleReserveBook = Label(windowReservar, text="RESERVAR LIBRO", bg=backgroundTitle, font=("Arial", 27), fg=blanco)
		labelTitleReserveBook.place(relx=0.5, rely=0.10, anchor=tk.CENTER, relwidth=1, relheight=0.2)

		# ENTRADAS
		titulo = tk.StringVar()

		def on_entry_click(event, entry, default_text):
			if entry.get() == default_text:
				entry.delete(0, "end")
				entry.configure(fg="white")

		def on_entry_leave(event, entry, default_text):
			if entry.get() == "":
				entry.insert(0, default_text)
				entry.configure(fg="gray")

		# Definir texto de fondo y entradas
		entradas = [
			(tk.Entry(windowReservar, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,textvar=titulo), "Titulo"),
		]

		# Crear y configurar las entradas con texto de fondo
		for entry, default_text in entradas:
			entry.place(relx=0.5, y=entradas.index((entry, default_text)) * 45 + 195, anchor=tk.CENTER, relwidth=1)
			entry.insert(0, default_text)
			entry.configure(fg="gray")  
			entry.bind("<FocusIn>", lambda event, entry=entry, default_text=default_text: on_entry_click(event, entry, default_text))
			entry.bind("<FocusOut>", lambda event, entry=entry, default_text=default_text: on_entry_leave(event, entry, default_text))

		def clearentries():
			for entry, default_text in entradas:
				entry.delete(0, 'end')
				entry.insert(0, default_text)
				entry.configure(fg="gray")

		# BOTONES
		buttonReservar = Button(windowReservar, text="Reservar Libro", cursor="hand2", relief="flat", 
			bg=backgroundButtonMain, font=("Arial", 18), fg=blanco,
			activebackground=backgroundClickButton, command=reservar, 
			borderwidth=3, highlightbackground="black")
		buttonReservar.place(relx=0.5, rely=0.85, anchor=tk.CENTER, relwidth=1, relheight=0.095)
		
		buttonReturn = tk.Button(windowReservar, text="Regresar", command=regreso, 
			cursor="hand2", relief="flat", 
		bg=fondo_salir, font=("Comic Sans MS", 18), fg=blanco,
		activebackground=backgroundClickButton)
		buttonReturn.place(relx=0.5, rely=0.95, anchor=tk.CENTER, relwidth=1, relheight=0.095)

		windowReservar.mainloop()
		
	def cancelReservaBook():
		main.withdraw()
		windowCancelReservar = tk.Toplevel()
		windowCancelReservar.title("Cancel Reserve Book")
		windowCancelReservar.geometry("600x750+500+1")
		windowCancelReservar.resizable(width=False, height=False)
		windowCancelReservar.config(background=backgroundSecond)

		def regreso():
			windowCancelReservar.withdraw()
			main.deiconify()

		# Label cancel reservado o no
		labelCancelReservarBook = Label(windowCancelReservar, text="", bg=backgroundSecond, font=("Arial", 22),fg=blanco)
		labelCancelReservarBook.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
		def cancelReservar():
			title = titulo.get()
			Mensaje = biblioteca.cancelarReserva(title)
			clearentries()

			# Label cancel reservado o no
			labelCancelReservarBook.config(text=Mensaje)
			



		# TITTLE cancel reserve BOOK
		labelTitleCancelReserveBook = Label(windowCancelReservar, text="CANCELAR RESERVA \n DE LIBRO", bg=backgroundTitle, font=("Arial", 27), fg=blanco)
		labelTitleCancelReserveBook.place(relx=0.5, rely=0.10, anchor=tk.CENTER, relwidth=1, relheight=0.2)

		# ENTRADAS
		titulo = tk.StringVar()

		def on_entry_click(event, entry, default_text):
			if entry.get() == default_text:
				entry.delete(0, "end")
				entry.configure(fg="white")

		def on_entry_leave(event, entry, default_text):
			if entry.get() == "":
				entry.insert(0, default_text)
				entry.configure(fg="gray")

		# Definir texto de fondo y entradas
		entradas = [
			(tk.Entry(windowCancelReservar, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,textvar=titulo), "Titulo"),
		]

		# Crear y configurar las entradas con texto de fondo
		for entry, default_text in entradas:
			entry.place(relx=0.5, y=entradas.index((entry, default_text)) * 45 + 195,anchor=tk.CENTER, relwidth=1)
			entry.insert(0, default_text)
			entry.configure(fg="gray")  
			entry.bind("<FocusIn>", lambda event, entry=entry, default_text=default_text: on_entry_click(event, entry, default_text))
			entry.bind("<FocusOut>", lambda event, entry=entry, default_text=default_text: on_entry_leave(event, entry, default_text))

		def clearentries():
			for entry, default_text in entradas:
				entry.delete(0, 'end')
				entry.insert(0, default_text)
				entry.configure(fg="gray")

		# BOTONES
		buttonReservar = Button(windowCancelReservar, text=" Cancelar Reserva Libro", cursor="hand2", relief="flat", 
			bg=backgroundButtonMain, font=("Arial", 18), fg=blanco,
			activebackground=backgroundClickButton, command=cancelReservar, 
			borderwidth=3, highlightbackground="black")
		buttonReservar.place(relx=0.5, rely=0.85, anchor=tk.CENTER, relwidth=1, relheight=0.095)
		
		buttonReturn = tk.Button(windowCancelReservar, text="Regresar", command=regreso, 
			cursor="hand2", relief="flat", 
		bg=fondo_salir, font=("Comic Sans MS", 18), fg=blanco,
		activebackground=backgroundClickButton)
		buttonReturn.place(relx=0.5, rely=0.95, anchor=tk.CENTER, relwidth=1, relheight=0.095)

		windowCancelReservar.mainloop()

	def editBook():
		main.withdraw()
		windowEdit = tk.Toplevel()
		windowEdit.title("Edit Book")
		windowEdit.geometry("600x750+500+1")
		windowEdit.resizable(width=False, height=False)
		windowEdit.config(background=backgroundSecond)

		labelEditBook = Label(windowEdit, text="", bg=backgroundSecond, font=("Arial", 22), fg=blanco)
		labelEditBook.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

		# Get books in library and create the dropdown labels
		libros = biblioteca.libros
		nombresLibros = []
		for libro in libros:
			nombresLibros.append(libro.titulo + ", " + libro.genero + "," + libro.autor + ", " + libro.anio_publicacion)

		# Set default values for selected book
		selected_book = Libro("", "", "", "", "")
		selected_index = -1

		# Create and place the Combobox
		book_combobox = ttk.Combobox(windowEdit, values=nombresLibros, state="readonly", width=60, font=("Arial", 18, "bold"))
		book_combobox.set("Seleccione un libro")
		book_combobox.place(relx=0.5, rely=0.25, anchor=tk.CENTER, relwidth=1, relheight=0.07)

		# Sets the currently selected book every time the value changes, and sets the inputs accordingly
		def update_selected_book(*args):
			nonlocal selected_index
			selected_index = book_combobox.current()
			selected_book = libros[selected_index]
			set_entries_as_book(selected_book)

		book_combobox.bind("<<ComboboxSelected>>", update_selected_book)

		def regreso():
			windowEdit.withdraw()
			main.deiconify()

		# TITLE ADD BOOK
		labelTitleEditBook = Label(windowEdit, text="EDITAR LIBRO", bg=backgroundTitle, font=("Arial", 27), fg=blanco)
		labelTitleEditBook.place(relx=0.5, rely=0.10, anchor=tk.CENTER, relwidth=1, relheight=0.2)
		
		# ENTRADAS
		titulo = tk.StringVar()
		autor = tk.StringVar()
		genero = tk.StringVar()
		anio_publicacion =tk.StringVar()

		def on_entry_click(event, entry, default_text):
			if entry.get() == default_text:
				entry.delete(0, "end")
				entry.configure(fg="white")

		def on_entry_leave(event, entry, default_text):
			if entry.get() == "":
				entry.insert(0, default_text)
				entry.configure(fg="gray")

		# Definir texto de fondo y entradas
		entradas = [
			(tk.Entry(windowEdit, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,textvar=titulo), "Título"),
			(tk.Entry(windowEdit, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada,textvar=autor), "Autor"),
			(tk.Entry(windowEdit, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada, textvar=genero), "Género"),
			(tk.Entry(windowEdit, width=22, relief="flat", font=("Comic Sans MS", 18, "bold"), bg=backgroundEntrada, textvar=anio_publicacion), "Año de Publicación"),
		]

		# Crear y configurar las entradas con texto de fondo
		for entry, default_text in entradas:
			entry.place(relx=0.5, y=entradas.index((entry, default_text)) * 45 + 255, anchor=tk.CENTER, relwidth=1)
			entry.insert(0, default_text)
			entry.configure(fg="gray")  
			entry.bind("<FocusIn>", lambda event, entry=entry, default_text=default_text: on_entry_click(event, entry, default_text))
			entry.bind("<FocusOut>", lambda event, entry=entry, default_text=default_text: on_entry_leave(event, entry, default_text))

		# FUNCIONES
		def edit():
			if selected_index != -1:
				title = titulo.get()
				author = autor.get()
				genre = genero.get()
				year = anio_publicacion.get()
				Mensaje = biblioteca.editar(selected_index, title, author, genre, year)
			else:
				Mensaje = "Seleccione un libro"
			labelEditBook.config(text=Mensaje)

		def set_entry_format():
			for entry, default_text in entradas:
				if entry.get() == "":
					entry.insert(0, default_text)
					entry.configure(fg="gray")
				else:
					entry.configure(fg="white")

		def set_entries_as_book(book):
			titulo.set(book.titulo)
			autor.set(book.autor)
			genero.set(book.genero)
			anio_publicacion.set(book.anio_publicacion)
			set_entry_format()

		# BOTONES
		buttonAdd = Button(windowEdit, text="Editar Libro", cursor="hand2", relief="flat",
			bg=backgroundButtonMain, font=("Arial", 18), fg=blanco,
			activebackground=backgroundClickButton, command=edit, 
			borderwidth=3, highlightbackground="black")
		buttonAdd.place(relx=0.5, rely=0.85, anchor=tk.CENTER, relwidth=1, relheight=0.095)
		
		buttonReturn = tk.Button(windowEdit, text="Regresar", command=regreso, 
			cursor="hand2", relief="flat", 
		bg=fondo_salir, font=("Comic Sans MS", 18), fg=blanco,
		activebackground=backgroundClickButton)
		buttonReturn.place(relx=0.5, rely=0.95, anchor=tk.CENTER, relwidth=1, relheight=0.095)
		windowEdit.mainloop()

	def deleteBook():
		main.withdraw()
		windowDeleteBook = tk.Toplevel()
		windowDeleteBook.title("Search Books")
		windowDeleteBook.geometry("600x750+500+1")
		windowDeleteBook.resizable(width=False, height=False)
		windowDeleteBook.config(background=backgroundSecond)


		def regreso():
			windowDeleteBook.withdraw()
			main.deiconify()

		# Label reservado o no
		labelDeleteBook = Label(windowDeleteBook, text="", bg=backgroundSecond, font=("Arial", 22) ,fg=blanco)
		labelDeleteBook.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=1 )
		def delete():
			title = titulo.get()
			Mensaje = biblioteca.eliminar(title)
			clearentries()

			# Label reservado o no
			labelDeleteBook.config(text=Mensaje)
			



		# TITTLE delete BOOK
		labelTitleDeleteBook = Label(windowDeleteBook, text="ELIMINAR LIBRO", bg=backgroundTitle, font=("Arial", 27), fg=blanco)
		labelTitleDeleteBook.place(relx=0.5, rely=0.10, anchor=tk.CENTER, relwidth=1, relheight=0.2)

		# ENTRADAS
		titulo = tk.StringVar()

		def on_entry_click(event, entry, default_text):
			if entry.get() == default_text:
				entry.delete(0, "end")
				entry.configure(fg="white")

		def on_entry_leave(event, entry, default_text):
			if entry.get() == "":
				entry.insert(0, default_text)
				entry.configure(fg="gray")

		# Definir texto de fondo y entradas
		entradas = [
			(tk.Entry(windowDeleteBook, width=22, relief="flat", font=("Comic Sans MS", 15, "bold"), bg=backgroundEntrada,textvar=titulo), "Titulo"),
		]

		# Crear y configurar las entradas con texto de fondo
		for entry, default_text in entradas:
			entry.place(relx=0.5, y=entradas.index((entry, default_text)) * 45 + 195, anchor=tk.CENTER, relwidth=1, relheight=0.07)
			entry.insert(0, default_text)
			entry.configure(fg="gray")  
			entry.bind("<FocusIn>", lambda event, entry=entry, default_text=default_text: on_entry_click(event, entry, default_text))
			entry.bind("<FocusOut>", lambda event, entry=entry, default_text=default_text: on_entry_leave(event, entry, default_text))

		def clearentries():
			for entry, default_text in entradas:
				entry.delete(0, 'end')
				entry.insert(0, default_text)
				entry.configure(fg="gray")

		# BOTONES
		buttonReservar = Button(windowDeleteBook, text="Eliminar Libro", cursor="hand2", relief="flat", 
			bg=backgroundButtonMain, font=("Arial", 18), fg=blanco,
			activebackground=backgroundClickButton, command=delete, 
			borderwidth=3, highlightbackground="black")
		buttonReservar.place(relx=0.5, rely=0.85, anchor=tk.CENTER, relwidth=1, relheight=0.095)
		
		buttonReturn = tk.Button(windowDeleteBook, text="Regresar", command=regreso, 
			cursor="hand2", relief="flat", 
		bg=fondo_salir, font=("Comic Sans MS", 18), fg=blanco,
		activebackground=backgroundClickButton)
		buttonReturn.place(relx=0.5, rely=0.95, anchor=tk.CENTER, relwidth=1, relheight=0.095)

		windowDeleteBook.mainloop()
		
	def salir():
		biblioteca.__del__()
		main.destroy()
		login.deiconify()


	# BIBLIOTECA
	titulo_label = Label(main, text="BIBLIOTECA", bg=backgroundTitle, font=("Arial", 27), fg=blanco )
	titulo_label.place(relx=0.5, rely=0.10, anchor=tk.CENTER, relwidth=1, relheight=0.2)

	# BOTONES
	buttonAddBook = Button(main, text="Agregar Libro", cursor="hand2", relief="flat", 
		bg=backgroundButtonMain, font=("Arial", 18),
		activebackground=backgroundClickButton, command=addBook, 
		borderwidth=3, highlightbackground="black", fg=blanco)
	buttonAddBook.place(relx=0.5, rely=0.25, anchor=tk.CENTER, relwidth=1, relheight=0.095)

	buttonViewBooks = Button(main, text="Ver Libros", cursor="hand2", relief="flat", 
		bg=backgroundButtonMain, font=("Arial", 18),
		activebackground=backgroundClickButton, command=viewBooks, 
		borderwidth=3, highlightcolor="black", fg=blanco)
	buttonViewBooks.place(relx=0.5, rely=0.35, anchor=tk.CENTER, relwidth=1, relheight=0.095)

	buttonSearchBook = Button(main, text="Buscar Libro", cursor="hand2", relief="flat", 
		bg=backgroundButtonMain, font=("Arial", 18),
		activebackground=backgroundClickButton, command=searchBook, 
		borderwidth=3, highlightcolor="black", fg=blanco)
	buttonSearchBook.place(relx=0.5, rely=0.45, anchor=tk.CENTER, relwidth=1, relheight=0.095)

	buttonReservarBook = Button(main, text="Reservar Libro", cursor="hand2", relief="flat", 
		bg=backgroundButtonMain, font=("Arial", 18),
		activebackground=backgroundClickButton, command=reservarBook, 
		borderwidth=3, highlightcolor="black", fg=blanco)
	buttonReservarBook.place(relx=0.5, rely=0.55, anchor=tk.CENTER, relwidth=1, relheight=0.095)

	buttonCancelReservaBook = Button(main, text="Cancelar Reserva De Libro", cursor="hand2", relief="flat", 
		bg=backgroundButtonMain, font=("Arial", 18),
		activebackground=backgroundClickButton, command=cancelReservaBook, 
		borderwidth=3, highlightcolor="black", fg=blanco)
	buttonCancelReservaBook.place(relx=0.5, rely=0.65, anchor=tk.CENTER, relwidth=1, relheight=0.095)

	buttonEditBook = Button(main, text="Editar Información Del Libro", cursor="hand2", relief="flat", 
		bg=backgroundButtonMain, font=("Arial", 18),
		activebackground=backgroundClickButton, command=editBook, 
		borderwidth=3, highlightcolor="black", fg=blanco)
	buttonEditBook.place(relx=0.5, rely=0.75, anchor=tk.CENTER, relwidth=1, relheight=0.095)

	buttonDeleteBook = Button(main, text="Eliminar Libro", cursor="hand2", relief="flat", 
		bg=backgroundButtonMain, font=("Arial", 18),
		activebackground=backgroundClickButton, command=deleteBook, 
		borderwidth=3, highlightcolor="black", fg=blanco)
	buttonDeleteBook.place(relx=0.5, rely=0.85, anchor=tk.CENTER, relwidth=1, relheight=0.095)

	buttonExit = tk.Button(main, text="Cerrar sesión", cursor="hand2", relief="flat",
		bg=fondo_salir, font=("Comic Sans MS", 18),
		activebackground=backgroundClickButton, width=22, command=salir, fg=blanco)
	buttonExit.place(relx=0.5, rely=0.95, anchor=tk.CENTER, relwidth=1, relheight=0.095)

	main.mainloop()

def incorrecto():

	login.withdraw()
	root = tk.Toplevel()
	root.title("Error")
	root.geometry("600x450+500+75") # tamaño de imagen
	root.resizable(width=False, height=False) #evita redimencionar y fallos en imagen
	root.config(bg='red')

	# FUNCIONES
	def regresar():
		root.destroy()
		login.deiconify()

	def on_closing():
		regresar()

	# LABEL
	labelTiltleError = Label(root, text="USUARIO Y CONTRASEÑA INCORRECTO", bg='red',fg='white', font=("Arial", 16, "bold"))
	labelTiltleError.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

	# BOTONES
	buttonRegresar = Button(root, text="Regresar", cursor="hand2", relief="flat", 
		bg='white', font=("Arial", 18, "bold"),
		activebackground=backgroundClickButton, command=regresar, 
		borderwidth=3, highlightbackground="black")
	buttonRegresar.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
	
	# Manejar el cierre de la ventana
	root.protocol("WM_DELETE_WINDOW", on_closing)
    # Esperar hasta que la ventana se cierre
	root.wait_window()

	root.mainloop()

# BOTONES
buttonLogin = Button(login, text="Logearse", cursor="hand2", relief="flat", 
	bg=blanco, font=("Arial", 18, "bold"),
	activebackground=backgroundClickButton, command=loguearse, 
	borderwidth=3, highlightbackground="black")
buttonLogin.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# toggle_button = tk.Button(login, text="Mostrar/ocultar contraseña", command=toggle_password_visibility)
# toggle_button.pack()

buttonClose = Button(login, text="Exit", cursor="hand2", relief="flat", 
	bg=blanco, font=("Arial", 18, "bold"),
	activebackground=backgroundClickButton, command=exit, 
	borderwidth=3, highlightbackground="black")
buttonClose.place(relx=0.5, rely=0.85, anchor=tk.CENTER)


login.mainloop()