from typing import Optional, List
from sqlalchemy import Integer, String, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase
from enum import auto, StrEnum

class Tamanio(StrEnum):
    GRANDE = auto()
    MEDIANA = auto()
    CHICA = auto()


class Producto(ModeloBase):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, index=True)
    precio: Mapped[float] = mapped_column(Float, index=True)
    tamanio: Mapped[Tamanio] = mapped_column(String)
    masa_crocante: Mapped[bool] = mapped_column(Boolean)


