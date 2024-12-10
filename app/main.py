from fastapi import FastAPI, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.database import SessionLocal, engine

# Initialize the app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Router for tenants, housing applications, and rental payments
router = APIRouter()

# Tenants Routes
@router.post("/tenants/", response_model=schemas.Tenant)
async def create_tenant(tenant: schemas.TenantCreate, db: Session = Depends(get_db)):
    return crud.create_tenant(db=db, tenant=tenant)

@router.get("/tenants/", response_model=List[schemas.Tenant])
async def list_tenants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tenants(db=db, skip=skip, limit=limit)

@router.get("/tenants/{tenant_id}", response_model=schemas.Tenant)
async def get_tenant(tenant_id: int, db: Session = Depends(get_db)):
    tenant = crud.get_tenant(db=db, tenant_id=tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant

@router.put("/tenants/{tenant_id}", response_model=schemas.Tenant)
async def update_tenant(tenant_id: int, tenant: schemas.TenantCreate, db: Session = Depends(get_db)):
    db_tenant = crud.update_tenant(db=db, tenant_id=tenant_id, tenant_update=tenant)
    if not db_tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return db_tenant

@router.delete("/tenants/{tenant_id}", response_model=schemas.Tenant)
async def delete_tenant(tenant_id: int, db: Session = Depends(get_db)):
    db_tenant = crud.delete_tenant(db=db, tenant_id=tenant_id)
    if not db_tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return db_tenant


# Housing Applications Routes
@router.post("/applications/", response_model=schemas.HousingApplication)
async def create_application(application: schemas.HousingApplicationCreate, db: Session = Depends(get_db)):
    return crud.create_housing_application(db=db, application=application)

@router.get("/applications/", response_model=List[schemas.HousingApplication])
async def list_applications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_housing_applications(db=db, skip=skip, limit=limit)

@router.get("/applications/{application_id}", response_model=schemas.HousingApplication)
async def get_application(application_id: int, db: Session = Depends(get_db)):
    application = crud.get_housing_application(db=db, application_id=application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Housing application not found")
    return application

@router.put("/applications/{application_id}", response_model=schemas.HousingApplication)
async def update_application(application_id: int, application: schemas.HousingApplicationCreate, db: Session = Depends(get_db)):
    db_application = crud.update_housing_application(db=db, application_id=application_id, application_update=application)
    if not db_application:
        raise HTTPException(status_code=404, detail="Housing application not found")
    return db_application

@router.delete("/applications/{application_id}", response_model=schemas.HousingApplication)
async def delete_application(application_id: int, db: Session = Depends(get_db)):
    db_application = crud.delete_housing_application(db=db, application_id=application_id)
    if not db_application:
        raise HTTPException(status_code=404, detail="Housing application not found")
    return db_application


# Rental Payments Routes
@router.post("/payments/", response_model=schemas.RentalPayment)
async def create_payment(payment: schemas.RentalPaymentCreate, db: Session = Depends(get_db)):
    return crud.create_rental_payment(db=db, payment=payment)

@router.get("/payments/", response_model=List[schemas.RentalPayment])
async def list_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_rental_payments(db=db, skip=skip, limit=limit)

@router.get("/payments/{payment_id}", response_model=schemas.RentalPayment)
async def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = crud.get_rental_payment(db=db, payment_id=payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Rental payment not found")
    return payment

@router.put("/payments/{payment_id}", response_model=schemas.RentalPayment)
async def update_payment(payment_id: int, payment: schemas.RentalPaymentCreate, db: Session = Depends(get_db)):
    db_payment = crud.update_rental_payment(db=db, payment_id=payment_id, payment_update=payment)
    if not db_payment:
        raise HTTPException(status_code=404, detail="Rental payment not found")
    return db_payment

@router.delete("/payments/{payment_id}", response_model=schemas.RentalPayment)
async def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = crud.delete_rental_payment(db=db, payment_id=payment_id)
    if not db_payment:
        raise HTTPException(status_code=404, detail="Rental payment not found")
    return db_payment

# Add the router to the FastAPI app
app.include_router(router)

# Optionally, create all tables in the database (if not done already)
from app.database import Base
Base.metadata.create_all(bind=engine)
