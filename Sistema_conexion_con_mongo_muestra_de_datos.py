from tkinter import *
from tkinter import ttk
from pymongo import MongoClient

class Database:
    def __init__(self):
        # URI de conexión a MongoDB Atlas
        uri = ""#aqui va el link de mongo del overview entre las comillas
        self.client = MongoClient(uri)  # Conexión a MongoDB Atlas
        self.db = self.client['']  # entre las comillas simples va el cluster
        self.collection = self.db['estudiantes']  # la coleccion debe llamarse estudiantes en la base de datos para que puedan ser insertados los datos

    def insert_student(self, data):
        self.collection.insert_one(data)  # Insertar un estudiante en la base de datos




class StudentInterface:
    def __init__(self, ventana, db):
        self.db = db

        self.ventana = ventana
        self.ventana.title("Sistema de administración de estudiantes")
        self.ventana.geometry("1370x700+0+0")
        self.ventana.resizable(False, False)

        self.matricula_var = StringVar()
        self.nombre_var = StringVar()
        self.apellido_var = StringVar()
        self.fecha_var = StringVar()
        self.correo_var = StringVar()
        self.genero_var = StringVar()
        self.telefono_var = StringVar()
        self.direccion_var = StringVar()

        #titulo del programa
        title = Label(self.ventana, text="Sistema de administración de estudiantes", bd=10, relief=RAISED, font=("Arial", 40, "bold"), bg="blue", fg="white")
        title.pack(side=TOP)
        
        #parte de la interfaz donde iran los campos a llenar
        manage_frame = Frame(self.ventana, bd=4, relief=RIDGE, bg="blue")
        manage_frame.place(x=20, y=125, width=520, height=550)

        #el subtitulo de los campos
        m_title = Label(manage_frame, text="Control de estudiantes", bg="white", fg="black", font=("Arial", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=0)

        #el primer campo matricula
        lb_id = Label(manage_frame, text="Matricula: ", bg="white", fg="black", font=("Arial", 15, "bold"))
        lb_id.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        #el primer campo vacio para llenar
        txt_field=Entry(manage_frame, font=("Arial", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.matricula_var)
        txt_field.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        #el segundo campo nombre
        lb_name = Label(manage_frame, text="Nombre: ", bg="white", fg="black", font=("Arial", 15, "bold"))
        lb_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        #el segundo campo vacio para llenar
        txt_field2=Entry(manage_frame, font=("Arial", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.nombre_var)
        txt_field2.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        #el tercer campo apellido
        lb_name = Label(manage_frame, text="Apellido: ", bg="white", fg="black", font=("Arial", 15, "bold"))
        lb_name.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        #el tercer campo vacio para llenar
        txt_field3=Entry(manage_frame, font=("Arial", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.apellido_var)
        txt_field3.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        #el cuarto campo la fecha de nacimiento
        lb_name = Label(manage_frame, text="Fecha: ", bg="white", fg="black", font=("Arial", 15, "bold"))
        lb_name.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        #el cuarto campo vacio para llenar
        txt_field4=Entry(manage_frame, font=("Arial", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.fecha_var)
        txt_field4.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        #el quinto campo correo
        lb_mail = Label(manage_frame, text="Correo: ", bg="white", fg="black", font=("Arial", 15, "bold"))
        lb_mail.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        #el quinto campo vacio para llenar
        txt_field5=Entry(manage_frame, font=("Arial", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.correo_var)
        txt_field5.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        #el sexto campo el genero
        lb_gen = Label(manage_frame, text="Genero: ", bg="white", fg="black", font=("Arial", 15, "bold"))
        lb_gen.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        #aqui esta la configuracion de la caja del sexto campo
        box_gender=ttk.Combobox(manage_frame, width=9, font=("Arial", 15, "bold"), state= 'readonly', textvariable=self.genero_var)# se utilizo la utilidad readonly para evitar que escriban
        box_gender['values'] = ("Masculino", "Femenino", "Otro")
        box_gender.grid(row=6, column=1, padx=20, pady=10)

        #el septimo campo telefono
        lb_tel = Label(manage_frame, text="Telefono: ", bg="white", fg="black", font=("Arial", 15, "bold"))
        lb_tel.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        #el seotimo vacio para llenar
        txt_field6=Entry(manage_frame, font=("Arial", 15, "bold"), bd=5, relief=GROOVE, textvariable=self.telefono_var)
        txt_field6.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        #el octavo campo direccion
        lb_direccion = Label(manage_frame, text="Direccion: ", bg="white", fg="black", font=("Arial", 15, "bold"))
        lb_direccion.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        #el octavo campo vacio para llenar
        self.txt_direccion=Text(manage_frame, width=25, height=3, font=("Arial", 10, "bold"))
        self.txt_direccion.grid(row=8, column=1, pady=10, padx=20)

        direccion_value = self.txt_direccion.get("1.0", "end-1c")

        self.txt_direccion.insert("1.0", direccion_value)



        #parte del codigo que sirve para colocar los botones de agregar, actualizar, eliminar y limpiar pantalla
        bt_frame=Frame(manage_frame, bd=4, relief=RIDGE, bg="white")
        bt_frame.place(x=25, y=490, width=400)

        #boton de agregar
        add_bt=Button(bt_frame, text="Agregar", width=7, command=self.add_student)
        add_bt.grid(row=0, column=2, padx=10, pady=10)

        #en este campo ira la base de datos de mysql
        detail_frame = Frame(self.ventana, bd=4, relief=RIDGE, bg="blue")
        detail_frame.place(x=550, y=125, width=790, height=550)

        lb_search=Label(detail_frame, text="Buscar por", bg="white", fg="black", font=("Arial", 20, "bold"))
        lb_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search=ttk.Combobox(detail_frame, width=10, font=("Arial", 15, "bold"), state='readonly')
        combo_search['values']=("Matricula", "Nombre")
        combo_search.grid(row=0, column=2, pady=20, padx=10)

        #campo de llenado del la parte derecha
        txt_search=Entry(detail_frame, width=20, font=("Arial", 11, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")

        #boton de buscar
        search_bt=Button(detail_frame, text="Buscar", width=7)
        search_bt.grid(row=0, column=4, pady=10, padx=10)

        #boton de buscar
        show_bt=Button(detail_frame, text="mostrar todo", width=12)
        show_bt.grid(row=0, column=5, pady=10, padx=10)

        table_frame=Frame(detail_frame, bd=4, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=70, width=770, height=470)

        scroll_x=Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, columns=("Matricula", "Nombre", "Apellido", "Fecha", "Email", "Genero", "Telefono", "Domicilio"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Matricula", text="Matricula")
        self.student_table.heading("Nombre", text="Nombre")
        self.student_table.heading("Apellido", text="Apellido")
        self.student_table.heading("Fecha", text="Fecha")
        self.student_table.heading("Email", text="correo")
        self.student_table.heading("Genero", text="genero(s)")
        self.student_table.heading("Telefono", text="Telefono")
        self.student_table.heading("Domicilio", text="Domicilio")

        self.student_table['show']='headings'
        self.student_table.column("Matricula", width=100)
        self.student_table.column("Nombre", width=100)
        self.student_table.column("Apellido", width=100)
        self.student_table.column("Fecha", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Genero", width=100)
        self.student_table.column("Telefono", width=100)
        self.student_table.column("Domicilio", width=100)

        self.student_table.pack(fill=BOTH, expand=1)

        

    def load_students(self):
        # Limpiar la tabla antes de cargar los datos
        for record in self.student_table.get_children():
            self.student_table.delete(record)

        # Obtener los estudiantes de la base de datos
        students = self.db.collection.find()

        # Agregar cada estudiante a la tabla
        for student in students:
            self.student_table.insert('', 'end', values=(
                student['Matricula'],
                student['Nombre'],
                student['Apellido'],
                student['Fecha'],
                student['Correo'],
                student['Genero'],
                student['Telefono'],
                student['Direccion']
            ))


    def add_student(self):
        # Obtener los datos ingresados por el usuario desde la interfaz gráfica
        matricula = self.matricula_var.get()
        nombre = self.nombre_var.get()
        apellido = self.apellido_var.get()
        fecha = self.fecha_var.get()
        correo = self.correo_var.get()
        genero = self.genero_var.get()
        telefono = self.telefono_var.get()
        direccion = self.txt_direccion.get("1.0", END)

        # Crear un diccionario con los datos del estudiante
        student_data = {
            "Matricula": matricula,
            "Nombre": nombre,
            "Apellido": apellido,
            "Fecha": fecha,
            "Correo": correo,
            "Genero": genero,
            "Telefono": telefono,
            "Direccion": direccion
        }


        # Insertar el estudiante en la base de datos
        self.db.insert_student(student_data)
        # Llamar al método para cargar los datos en la tabla después de agregar un estudiante
        self.load_students()

        # Limpiar los campos de entrada después de agregar el estudiante
        self.matricula_var.set("")
        self.nombre_var.set("")
        self.apellido_var.set("")
        self.fecha_var.set("")
        self.correo_var.set("")
        self.genero_var.set("")
        self.telefono_var.set("")
        self.txt_direccion.delete("1.0", END)

        # Llamar al método load_students una vez que se crea la tabla
        self.load_students()

# Crear una instancia de la base de datos
db = Database()

# Crear la ventana de la interfaz gráfica
ventana = Tk()
ob = StudentInterface(ventana, db)
ventana.mainloop()
