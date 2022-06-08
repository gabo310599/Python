#Clase que maneja las excepciones asociadas a un archivo
class FileException(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message
    
    def __str__(self):
        return self.message