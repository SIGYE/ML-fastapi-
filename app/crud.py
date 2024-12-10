from sqlalchemy.orm import Session
from app import models, schemas


def create_tenant(db: Session, tenant: schemas.TenantCreate):
    db_tenant = models.Tenant(name=tenant.name,
                              phone_number=tenant.phone_number,
                              email=tenant.email)
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant

def get_tenant(db: Session, tenant_id: int):
    return db.query(models.Tenant).filter(models.Tenant.id == tenant_id).first()

def get_tenants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tenant).offset(skip).limit(limit).all()

def update_tenant(db: Session, tenant_id: int, tenant_update: schemas.TenantCreate):
    db_tenant = db.query(models.Tenant).filter(models.Tenant.id == tenant_id).first()
    if db_tenant:
        db_tenant.name = tenant_update.name
        db_tenant.phone_number = tenant_update.phone_number
        db_tenant.email = tenant_update.email
        db.commit()
        db.refresh(db_tenant)
    return db_tenant

def delete_tenant(db: Session, tenant_id: int):
    db_tenant = db.query(models.Tenant).filter(models.Tenant.id == tenant_id).first()
    if db_tenant:
        db.delete(db_tenant)
        db.commit()
    return db_tenant



def create_housing_application(db: Session, application: schemas.HousingApplicationCreate):
    db_application = models.HousingApplication(
        application_date = application.application_date,
        tenant_id=application.tenant_id,
        status=application.status
    )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

# READ - HousingApplication
def get_housing_application(db: Session, application_id: int):
    return db.query(models.HousingApplication).filter(models.HousingApplication.id == application_id).first()

def get_housing_applications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.HousingApplication).offset(skip).limit(limit).all()

# UPDATE - HousingApplication
def update_housing_application(db: Session, application_id: int, application_update: schemas.HousingApplicationCreate):
    db_application = db.query(models.HousingApplication).filter(models.HousingApplication.id == application_id).first()
    if db_application:
        db_application.status = application_update.status
        db.commit()
        db.refresh(db_application)
    return db_application

# DELETE - HousingApplication
def delete_housing_application(db: Session, application_id: int):
    db_application = db.query(models.HousingApplication).filter(models.HousingApplication.id == application_id).first()
    if db_application:
        db.delete(db_application)
        db.commit()
    return db_application


# CREATE - RentalPayment
def create_rental_payment(db: Session, payment: schemas.RentalPaymentCreate):
    db_payment = models.RentalPayment(
        tenant_id=payment.tenant_id,
        amount=payment.amount,
        payment_date=payment.payment_date
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

# READ - RentalPayment
def get_rental_payment(db: Session, payment_id: int):
    return db.query(models.RentalPayment).filter(models.RentalPayment.id == payment_id).first()

def get_rental_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RentalPayment).offset(skip).limit(limit).all()

# UPDATE - RentalPayment
def update_rental_payment(db: Session, payment_id: int, payment_update: schemas.RentalPaymentCreate):
    db_payment = db.query(models.RentalPayment).filter(models.RentalPayment.id == payment_id).first()
    if db_payment:
        db_payment.amount = payment_update.amount
        db_payment.payment_date = payment_update.payment_date
        db.commit()
        db.refresh(db_payment)
    return db_payment

# DELETE - RentalPayment
def delete_rental_payment(db: Session, payment_id: int):
    db_payment = db.query(models.RentalPayment).filter(models.RentalPayment.id == payment_id).first()
    if db_payment:
        db.delete(db_payment)
        db.commit()
    return db_payment
