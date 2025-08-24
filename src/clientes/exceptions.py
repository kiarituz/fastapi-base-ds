from src.clientes.constants import ErrorCode
from src.exceptions import NotFound, BadRequest
from typing import List

class ProductoNoEncontrado(NotFound):
    DETAIL = ErrorCode.CLIENTE_NO_ENCONTRADO

class NombreDuplicado(BadRequest):
    DETAIL = ErrorCode.NOMBRE_DUPLICADO

class EmailDuplicado(BadRequest):
    DETAIL = ErrorCode.EMAIL_DUPLICADO

