class RepositorioFake:
   def __init__(self):
       self.compras = []

   def guardar(self, usuario, cantidad):
       self.compras.append({
           'usuario': usuario,
           'cantidad': cantidad
       })
repo = RepositorioFake()
repo.guardar('Borra', 67)
repo.guardar('Ortega', 69)
print(repo.compras)