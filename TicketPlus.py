from InventarioStub import InventarioStub
from RepositorioFake import RepositorioFake
from UsuarioDummy import UsuarioDummy
from EmailDummy import EmailDummy
from unittest.mock import Mock
from InventarioSpy import InventarioSpy

class TicketService:
   def __init__(self, inventario, repositorio, email_service):
      self.inventario = inventario
      self.repositorio = repositorio
      self.email_service = email_service
 
   def comprar(self, usuario, cantidad):
      disponibles = self.inventario.consultar_disponibilidad()
      if disponibles < cantidad:
          return False
      self.repositorio.guardar(usuario, cantidad)
      self.email_service.enviar_confirmacion(usuario)
      return True

#service = TicketService(InventarioStub(),RepositorioFake(),EmailDummy())
#resultado = service.comprar("Borra", 2)
#resultado= service.comprar(UsuarioDummy(), 2)
#print(resultado)  
email_mock = Mock()
inventario = InventarioSpy()

service = TicketService(inventario, RepositorioFake(), email_mock)

resultado = service.comprar(UsuarioDummy(), 2)
service.comprar(UsuarioDummy(), 1)

email_mock.enviar_confirmacion.assert_called()

print(resultado)
print(inventario.veces_consultado)
