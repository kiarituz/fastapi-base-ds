from typing import List
from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session
from src.clientes.models import Cliente
from src.clientes import schemas, exceptions

# operaciones CRUD para clientes

def crear_cliente(db: Session, cliente: schemas.ClienteCreate) -> schemas.Cliente:
    _cliente = Cliente(**cliente.model_dump())
    db.add(_cliente)
    db.commit()
    db.refresh(_cliente)
    return _cliente


def listar_clientes(db: Session) -> List[schemas.Cliente]:
    return db.scalars(select(Cliente)).all()


def leer_cliente(db: Session, cliente_id: int) -> schemas.Cliente:
    db_cliente = db.scalar(select(Cliente).where(Cliente.id == cliente_id))
    if db_cliente is None:
        raise exceptions.ClienteNoEncontrado()
    return db_cliente


def modificar_cliente(
    db: Session, cliente_id: int, cliente: schemas.ClienteUpdate
) -> Cliente:
    db_cliente = leer_cliente(db, cliente_id)
    db.execute(
        update(Cliente).where(Cliente.id == cliente_id).values(**cliente.model_dump())
    )
    db.commit()
    db.refresh(db_cliente)
    return db_cliente


def eliminar_cliente(db: Session, cliente_id: int) -> schemas.Cliente:
    db_cliente = leer_cliente(db, cliente_id)
    db.execute(delete(Cliente).where(Cliente.id == cliente_id))
    db.commit()
    return db_cliente
