from pydantic import BaseModel, field_validator
from src.productos.models import Tamanio
from src.productos import exceptions

# Los siguientes schemas contienen atributos sin muchas restricciones de tipo.
# Podemos crear atributos con ciertas reglas mediante el uso de un "Field" adecuado.
# https://docs.pydantic.dev/latest/concepts/fields/


class ProductoBase(BaseModel):
    nombre: str
    precio: float
    tamanio: Tamanio
    masa_crocante: bool

    @field_validator("tamanio", mode="before")
    @classmethod
    def is_valid_tipo_mascota(cls, v: str) -> str:
        if v.lower() not in Tamanio:
            raise exceptions.TamanioInvalido(list(Tamanio))
        return v.lower()


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(ProductoBase):
    pass


class Producto(ProductoBase):
    id: int
    precio: float
    tamanio: Tamanio
    masa_crocante: bool

    # from_atributes=True permite que Pydantic trabaje con modelos SQLAlchemy
    # más info.: https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.from_attributes
    model_config = {"from_attributes": True}
