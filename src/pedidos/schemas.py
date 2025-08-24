from pydantic import BaseModel, field_validator
from src.pedidos import exceptions
from src.pedidos.models import Estado

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class PedidoBase(BaseModel):
    estado: Estado

    @field_validator("estado", mode="before")
    @classmethod
    def is_valid_estado(cls, v: str) -> str:
        if v.lower() not in Estado:
            raise exceptions.EstadoInvalido(list(Estado))
        return v.lower()


class PedidoCreate(PedidoBase):
    cliente_id: int


class PedidoUpdate(PedidoBase):
    pass


class Pedido(PedidoBase):
    id: int
    estado: Estado
    cliente_id: int
    nombre_cliente: str

    model_config = {"from_attributes": True}


class PedidoDelete(PedidoBase):
    id: int
    cliente_id: int

class PedidoProductoBase(BaseModel):
    producto_id: int
    cantidad: int

class PedidoAgregarProducto(PedidoProductoBase):
    pass

class PedidoProducto(PedidoProductoBase):
    pedido_id: int