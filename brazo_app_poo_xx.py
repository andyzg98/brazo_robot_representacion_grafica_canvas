import tkinter as tk
import tkinter.messagebox as messagebox


class Modelo:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

class Vista:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Control del Brazo Robot")
        self.ventana.geometry("500x800")  # Establecer dimensiones de la ventana


        self.label_posicion_inicial = tk.Label(ventana, text="Posición Inicial:")
        self.label_posicion_inicial.grid(row=0, column=0)

        x=self.entry_x = tk.Entry(ventana, width=10)
        self.entry_x.grid(row=0, column=1)

        y=self.entry_y = tk.Entry(ventana, width=10)
        self.entry_y.grid(row=0, column=2)

        z=self.entry_z = tk.Entry(ventana, width=10)
        self.entry_z.grid(row=0, column=3)

        self.boton_mover = tk.Button(ventana, text="Mover", command=self.mover)
        self.boton_mover.grid(row=1, column=0, columnspan=4, pady=10)

        self.boton_arriba = tk.Button(ventana, text="arriba", command=self.mover_arriba)
        self.boton_arriba.grid(row=2, column=0, padx=10, pady=5)

        self.boton_abajo = tk.Button(ventana, text="abajo", command=self.mover_abajo)
        self.boton_abajo.grid(row=3, column=0, padx=10, pady=5)

        self.boton_izquierda = tk.Button(ventana, text="izquierda", command=self.mover_izquierda)
        self.boton_izquierda.grid(row=4, column=0, padx=10, pady=5)

        self.boton_derecha = tk.Button(ventana, text="derecha", command=self.mover_derecha)
        self.boton_derecha.grid(row=5, column=0, padx=10, pady=5)

        self.boton_adelante = tk.Button(ventana, text="adelante", command=self.mover_adelante)
        self.boton_adelante.grid(row=6, column=0, padx=10, pady=5)

        self.boton_atras = tk.Button(ventana, text="atras", command=self.mover_atras)
        self.boton_atras.grid(row=7, column=0, padx=10, pady=5)

        self.label_posicion_actual = tk.Label(ventana, text="Posición Actual:")
        self.label_posicion_actual.grid(row=8, column=0, pady=10)

        self.label_posicion_actual_valor = tk.Label(ventana, text="(0, 0, 0)")
        self.label_posicion_actual_valor.grid(row=8, column=1, columnspan=2)
        
        #se instncia a Canvas en sel canvas con los atributos de estar en la ventana   el ancho largo y de que color 
        self.canvas = tk.Canvas(ventana, width=400, height=400, bg='white')
        self.canvas.grid(row=9, column=0, columnspan=4, padx=10, pady=10) #creo un cuadrado 
#grid es el lienzo donde se coloca la cuadricula en la ventanafila 9 columna 0 se extiende a trabes de 4 columnas 
# En resumen, estas líneas de código crean un lienzo gráfico rectangular en blanco y 
# lo colocan en la ventana principal en una ubicación específica dentro de la cuadrícula.
    def mover(self):
        x = int(self.entry_x.get())
        y = int(self.entry_y.get())
        z = int(self.entry_z.get())

        if -100 <= x <= 100 and -100 <= y <= 100 and -100 <= z <= 100:
            controlador.mover_a_posicion(x, y, z)
        else:
        # Realizar alguna acción en caso de valores fuera de rango
            print("Los valores deben estar entre -100 y +100")
            messagebox.showerror("Error", "Los valores deben estar entre -100 y +100")

    def mover_arriba(self):      #------------------------------------------------------arriba
        x_str = self.entry_x.get()
        y_str = self.entry_y.get()
        z_str = self.entry_z.get()

    # Verificar y asignar valores predeterminados si las cadenas están vacías
        x = int(x_str) if x_str else 0
        y = int(y_str) + 1 if y_str else 1
        z = int(z_str) if z_str else 0

        if -100 <= x <= 100 and -100 <= y <= 100 and -100 <= z <= 100:
            controlador.mover_a_posicion(x, y, z)
            self.entry_y.delete(0, tk.END)  # Eliminar valor ingresado en entry_y
            self.entry_y.insert(0, str(y))  # Actualizar entry_y con el nuevo valor
        else:
            print("Los valores deben estar entre -100 y +100")
            messagebox.showerror("Error", "Los valores deben estar entre -100 y +100")


    def mover_abajo(self):        #------------------------------------------------------abajo
        x_str = self.entry_x.get()
        y_str = self.entry_y.get()
        z_str = self.entry_z.get()

    # Verificar y asignar valores predeterminados si las cadenas están vacías
        x = int(x_str) if x_str else 0
        y = int(y_str) - 1 if y_str else 1
        z = int(z_str) if z_str else 0

        if -100 <= x <= 100 and -100 <= y <= 100 and -100 <= z <= 100:
            controlador.mover_a_posicion(x, y, z)
            self.entry_y.delete(0, tk.END)  # Eliminar valor ingresado en entry_y
            self.entry_y.insert(0, str(y))  # Actualizar entry_y con el nuevo valor
        else:
            print("Los valores deben estar entre -100 y +100")
            messagebox.showerror("Error", "Los valores deben estar entre -100 y +100")

    def mover_izquierda(self):        #------------------------------------------------------izquierda
        x_str = self.entry_x.get()
        y_str = self.entry_y.get()
        z_str = self.entry_z.get()

    # Verificar y asignar valores predeterminados si las cadenas están vacías
        x = int(x_str) -1 if x_str else 0
        y = int(y_str) if y_str else 1
        z = int(z_str) if z_str else 0

        if -100 <= x <= 100 and -100 <= y <= 100 and -100 <= z <= 100:
            controlador.mover_a_posicion(x, y, z)
            self.entry_x.delete(0, tk.END)  # Eliminar valor ingresado en entry_y
            self.entry_x.insert(0, str(x))  # Actualizar entry_y con el nuevo valor
        else:
            print("Los valores deben estar entre -100 y +100")
            messagebox.showerror("Error", "Los valores deben estar entre -100 y +100")


    def mover_derecha(self):        #------------------------------------------------------derecha 
        x_str = self.entry_x.get()
        y_str = self.entry_y.get()
        z_str = self.entry_z.get()

    # Verificar y asignar valores predeterminados si las cadenas están vacías
        x = int(x_str) +1 if x_str else 0
        y = int(y_str) if y_str else 1
        z = int(z_str) if z_str else 0

        if -100 <= x <= 100 and -100 <= y <= 100 and -100 <= z <= 100:
            controlador.mover_a_posicion(x, y, z)
            self.entry_x.delete(0, tk.END)  # Eliminar valor ingresado en entry_y
            self.entry_x.insert(0, str(x))  # Actualizar entry_y con el nuevo valor
        else:
            print("Los valores deben estar entre -100 y +100")
            messagebox.showerror("Error", "Los valores deben estar entre -100 y +100")

        

    def mover_adelante(self):        #------------------------------------------------------adelante
        x_str = self.entry_x.get()
        y_str = self.entry_y.get()
        z_str = self.entry_z.get()

    # Verificar y asignar valores predeterminados si las cadenas están vacías
        x = int(x_str) if x_str else 0
        y = int(y_str) if y_str else 1
        z = int(z_str) +1 if z_str else 0

        if -100 <= x <= 100 and -100 <= y <= 100 and -100 <= z <= 100:
            controlador.mover_a_posicion(x, y, z)
            self.entry_z.delete(0, tk.END)  # Eliminar valor ingresado en entry_y
            self.entry_z.insert(0, str(z))  # Actualizar entry_y con el nuevo valor
        else:
            print("Los valores deben estar entre -100 y +100")
            messagebox.showerror("Error", "Los valores deben estar entre -100 y +100")

    def mover_atras(self):        #------------------------------------------------------atras 
        x_str = self.entry_x.get()
        y_str = self.entry_y.get()
        z_str = self.entry_z.get()

    # Verificar y asignar valores predeterminados si las cadenas están vacías
        x = int(x_str) if x_str else 0
        y = int(y_str) if y_str else 1
        z = int(z_str) -1 if z_str else 0

        if -100 <= x <= 100 and -100 <= y <= 100 and -100 <= z <= 100:
            controlador.mover_a_posicion(x, y, z)
            self.entry_z.delete(0, tk.END)  # Eliminar valor ingresado en entry_y
            self.entry_z.insert(0, str(z))  # Actualizar entry_y con el nuevo valor
        else:
            print("Los valores deben estar entre -100 y +100")
            messagebox.showerror("Error", "Los valores deben estar entre -100 y +100")

    def actualizar_posicion_actual(self, posicion_x, posicion_y, posicion_z):
        self.label_posicion_actual_valor.config(text="({}, {}, {})".format(posicion_x, posicion_y, posicion_z))
#canvas
    def actualizar_posicion_actual(self, posicion_x, posicion_y, posicion_z): #actualiza la posicion del cirulo
        self.label_posicion_actual_valor.config(text="({}, {}, {})".format(posicion_x, posicion_y, posicion_z))
        self.canvas.delete("circle")  # Eliminar cualquier círculo previo en el canvas
        self.canvas.create_oval(posicion_x-5, posicion_y-5, posicion_x+5, posicion_y+5, fill="green", tags="circle")  # Dibujar un círculo en la posición actual

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def mover_a_posicion(self, x, y, z):
        # Lógica para mover el brazo robot a una posición específica
        # Verifica que los valores estén dentro del rango permitido
        x = max(min(x, 100), -100)
        y = max(min(y, 100), -100)
        z = max(min(z, 100), -100)
        self.modelo.posicion_x = x
        self.modelo.posicion_y = y
        self.modelo.posicion_z = z
        self.vista.actualizar_posicion_actual(x, y, z)

modelo = Modelo()
ventana = tk.Tk()
vista = Vista(ventana)
controlador = Controlador(modelo, vista)
ventana.mainloop()

