# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.database import SessionLocal
# from app.models import Tenant

# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/tenants/")
# async def list_tenants(db: Session = Depends(get_db)):
#     tenants = db.query(Tenant).all()
#     return tenants

# @router.get("/tenants/{tenant_id}")
# async def get_tenant(tenant_id: int, db: Session = Depends(get_db)):
#     tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
#     if not tenant:
#         return {"error": "Tenant not found"}
#     return tenant
