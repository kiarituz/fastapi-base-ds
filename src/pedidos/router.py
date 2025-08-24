from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.pedidos import schemas, services

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

# Rutas para pedidos


@router.post("/", response_model=schemas.Pedido)
def create_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    return services.crear_pedido(db, pedido)


@router.get("/", response_model=list[schemas.Pedido])
def read_pedidos(db: Session = Depends(get_db)):
    return services.listar_pedidos(db)


@router.get("/{pedido_id}", response_model=schemas.Pedido)
def read_pedido(pedido_id: int, db: Session = Depends(get_db)):
    return services.leer_pedido(db, pedido_id)


@router.put("/{pedido_id}", response_model=schemas.Pedido)
def update_pedido(
    pedido_id: int, pedido: schemas.PedidoUpdate, db: Session = Depends(get_db)
):
    return services.modificar_pedido(db, pedido_id, pedido)


@router.delete("/{pedido_id}", response_model=schemas.PedidoDelete)
def delete_pedido(pedido_id: int, db: Session = Depends(get_db)):
    return services.eliminar_pedido(db, pedido_id)


@router.post("/{pedido_id}/productos", response_model=schemas.PedidoProducto)
def agregar_producto(pedido_id: int, item: schemas.PedidoAgregarProducto, db: Session = Depends(get_db)):
    return services.agregar_producto_a_pedido(db, pedido_id, item)