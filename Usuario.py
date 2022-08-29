class Usuario(BVirtual):
    
    def __init__(self, nombre, apellido, dni, VBirtual,usuario, password):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.VBirtual = VBirtual
        self.usuario = usuario
        self.password = password
