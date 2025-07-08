#Principio de responsabilidad única

#Incorrecta

class Usuario:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def guardar_base_de_datos(self):
        pass

    def enviar_correo(self):
        pass


#Manera incorrecta y rompe el principio S

# Correcta

class Usuario:
    def __init__(self,name,email):
        self.name = name
        self.email = email



class GuardarBaseDeDatos:
    def guardar(self,usuario, email):
        pass


class EnviarCorreo:
    def enviar(self,usuario, email):
        pass


#Manejo de Libreria manera Incorrecta

class Libreria:
    def __init__(self,) -> None:
        self.libro = []
        self.cliente = []
        self.prestamo = []
    
    def agregar_Libro(self, Titulo, Autor, Copias):
        self.libro.append({"Titulo" : Titulo, "Autor" : Autor, "Copias" : Copias})
    
    def agregar_cliente(self, Nombre, ID, Correo):
        self.cliente.append({"Nombre" : Nombre, "ID" : ID, "Correo" : Correo})
    
    def prestamo_del_Libro(self, Titulo, IdUsuario):
        for libro in self.libro:
            if libro["Titulo"] == Titulo and libro["copias"] > 0:
                self.prestamo.append({"Titulo" : Titulo, "ID" : IdUsuario})
                libro["copias"] -= 1
                return True
        return False

    def devolver_Libro(self, Titulo, IdUsuario):
        for prestamo in self.prestamo:
            if prestamo["Titulo"] == Titulo and prestamo["ID"] == IdUsuario:
                self.prestamo.remove(prestamo)
                for libro in self.libro:
                    if libro["Titulo"] == Titulo:
                        libro["copias"] += 1
                        return True
        return False



#Libreria con manera correcta del principio solid S

class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias
        self.disponible = True
    
class Usuario:
    def __init__(self, nombre, id, correo):
        self.nombre = nombre
        self.id = id
        self.correo = correo

class Prestamo:
    def __init__(self):
        self.prestamos = []

    def prestar_Libro(self,libro, usuario):
        if libro.copias > 0:
            libro.copias -= 1
            self.prestamos.append({"Titulo" : libro.titulo, "ID" : usuario.id})
            return True
        return False

    def devolver_Libro(self,libro,usuario):
        for prestamo in self.prestamos:
            if prestamo["Titulo"] == libro.titulo and prestamo["ID"] == usuario.id:
                libro.copias += 1
                self.prestamos.remove(prestamo)
                return True
        return False


class Libreria:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos_servicios = Prestamo()
    

    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def prestar_libro(self, titulo_Buscado, IdUsuario):
        #prestar libro a traves de operacion generadora
        usuario = next((usuario for usuario in self.usuarios if usuario.id == IdUsuario), None)
        libro = next((libro for libro in self.libros if libro.titulo == titulo_Buscado), None)
        if usuario and libro:
            return self.prestamos_servicios.prestar_Libro(libro, usuario.id)
        return False
    
    def devolver_libro(self, titulo_Buscado, usuario):
        usuario = next((usuario for usuario in self.usuarios if usuario.id == usuario.id), None)
        libro = next((libro for libro in self.libros if libro.titulo == titulo_Buscado), None)
        if usuario and libro:
            return self.prestamos_servicios.devolver_Libro(libro, usuario.id)
        return False