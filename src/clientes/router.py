from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.clientes import schemas, services

router = APIRouter(prefix="/clientes", tags=["clientes"])

# Rutas para Clientes


@router.post("/", response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return services.crear_cliente(db, cliente)


@router.get("/", response_model=list[schemas.Cliente])
def read_cliente(db: Session = Depends(get_db)):
    return services.listar_clientes(db)


@router.get("/{cliente_id}", response_model=schemas.Cliente)
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return services.leer_cliente(db, cliente_id)


@router.put("/{cliente_id}", response_model=schemas.Cliente)
def update_cliente(
    cliente_id: int, cliente: schemas.ClienteUpdate, db: Session = Depends(get_db)
):
    return services.modificar_cliente(db, cliente_id, cliente)


@router.delete("/{cliente_id}", response_model=schemas.Cliente)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return services.eliminar_cliente(db, cliente_id)

