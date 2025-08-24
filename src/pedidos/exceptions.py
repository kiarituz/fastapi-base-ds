from typing import List
from src.pedidos.constants import ErrorCode
from src.exceptions import NotFound

class PedidoNoEncontrado(NotFound):
    DETAIL = ErrorCode.PEDIDO_NO_ENCONTRADO

class EstadoInvalido(ValueError):
    def __init__(self, posibles_tipos: List[str]):
        posibles_tipos = ", ".join(posibles_tipos)
        message = f"{ErrorCode.ESTADO_INVALIDO} {posibles_tipos}."
        super().__init__(message)