from src.productos.constants import ErrorCode
from src.exceptions import NotFound, BadRequest
from typing import List

class ProductoNoEncontrado(NotFound):
    DETAIL = ErrorCode.PRODUCTO_NO_ENCONTRADO

class NombreDuplicado(BadRequest):
    DETAIL = ErrorCode.NOMBRE_DUPLICADO

class TamanioInvalido(ValueError):
    def __init__(self, posibles_tipos: List[str]):
        posibles_tipos = ", ".join(posibles_tipos)
        message = f"{ErrorCode.TAMANIO_INVALIDO} {posibles_tipos}."
        super().__init__(message)

