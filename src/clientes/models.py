from typing import Optional, List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import ModeloBase


class Cliente(ModeloBase):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    #pedidos: Mapped[Optional[List["src.pedidos.models.Pedido"]]] = relationship(
    #    "src.pedidos.models.Pedido", back_populates="tutor"
    #)


