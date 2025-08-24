from typing import List
from sqlalchemy import delete, select, update, insert
from sqlalchemy.orm import Session
from src.pedidos.models import Pedido, pedido_producto
from src.pedidos import schemas, exceptions


# operaciones CRUD para Pedido

def crear_pedido(db: Session, pedido: schemas.PedidoCreate) -> schemas.Pedido:
    _pedido = Pedido(**pedido.model_dump())
    db.add(_pedido)
    db.commit()
    db.refresh(_pedido)
    return _pedido


def listar_pedidos(db: Session) -> List[schemas.Pedido]:
    return db.scalars(select(Pedido)).all()


def leer_pedido(db: Session, pedido_id: int) -> schemas.Pedido:
    db_pedido = db.scalar(select(Pedido).where(Pedido.id == pedido_id))
    if db_pedido is None:
        raise exceptions.PedidoNoEncontrado()
    return db_pedido


def modificar_pedido(
    db: Session, pedido_id: int, pedido: schemas.PedidoUpdate
) -> Pedido:
    db_pedido = leer_pedido(db, pedido_id)
    db.execute(update(Pedido).where(Pedido.id == pedido_id).values(**pedido.model_dump()))
    db.commit()
    db.refresh(db_pedido)
    return db_pedido


def eliminar_pedido(db: Session, pedido_id: int) -> schemas.PedidoDelete:
    db_pedido = leer_pedido(db, pedido_id)
    db.execute(
        delete(Pedido).where(Pedido.id == pedido_id)
    )
    db.commit()
    return db_pedido

def agregar_producto_a_pedido(
    db: Session, pedido_id: int, data: schemas.PedidoAgregarProducto ) -> dict:

    db_pedido = leer_pedido(db, pedido_id)
    db.execute(
        insert(pedido_producto).values(
            pedido_id=pedido_id,
            producto_id=data.producto_id,
            cant=data.cantidad
        )
    )
    db.commit()
    return {"pedido_id": pedido_id, "producto_id": data.producto_id, "cantidad": data.cantidad}