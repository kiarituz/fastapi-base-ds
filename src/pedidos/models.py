from sqlalchemy import Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import auto, StrEnum
from src.models import ModeloBase#, BaseModel
from typing import Optional, List

class Estado(StrEnum):
    ENCARGADO = auto()
    EN_PROCESO = auto()
    LISTO = auto()
    RETIRADO = auto()

pedido_producto = Table(
    "pedido_producto",
    ModeloBase.metadata,
    Column("pedido_id", ForeignKey("pedidos.id"), primary_key=True),
    Column("producto_id", ForeignKey("productos.id"), primary_key=True),
    Column("cant", Integer)
)

class Pedido(ModeloBase):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    estado: Mapped[Estado] = mapped_column(String, index=True)

    cliente_id: Mapped[int] = mapped_column(
        ForeignKey("clientes.id")
    )  # Foreign key a Cliente

    cliente: Mapped["src.clientes.models.Cliente"] = relationship(
        "src.clientes.models.Cliente", back_populates="pedidos"
    )

    @property
    def nombre_cliente(self):
        return self.cliente.nombre
    
    productos: Mapped[Optional[List["src.productos.models.Producto"]]] = relationship(
        "src.productos.models.Producto",
        secondary=pedido_producto
    )
