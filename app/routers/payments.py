# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.database import SessionLocal
# from app.models import RentalPayment, Tenant
# from datetime import date
# from typing import List

# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/payments/", response_model=List[dict])
# async def list_payments(db: Session = Depends(get_db)):
#     payments = db.query(RentalPayment).all()
#     return [
#         {
#             "id": payment.id,
#             "tenant_name": payment.tenant.name,
#             "amount": payment.amount,
#             "payment_date": payment.payment_date
#         }
#         for payment in payments
#     ]

# @router.get("/payments/{payment_id}")
# async def get_payment(payment_id: int, db: Session = Depends(get_db)):
#     payment = db.query(RentalPayment).filter(RentalPayment.id == payment_id).first()
#     if not payment:
#         raise HTTPException(status_code=404, detail="Payment not found")
#     return {
#         "id": payment.id,
#         "tenant_name": payment.tenant.name,
#         "amount": payment.amount,
#         "payment_date": payment.payment_date
#     }

# @router.post("/payments/")
# async def create_payment(tenant_id: int, amount: float, payment_date: date, db: Session = Depends(get_db)):
#     tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
#     if not tenant:
#         raise HTTPException(status_code=404, detail="Tenant not found")
#     new_payment = RentalPayment(
#         tenant_id=tenant_id,
#         amount=amount,
#         payment_date=payment_date
#     )
#     db.add(new_payment)
#     db.commit()
#     db.refresh(new_payment)
#     return {
#         "id": new_payment.id,
#         "tenant_name": tenant.name,
#         "amount": new_payment.amount,
#         "payment_date": new_payment.payment_date
#     }

# @router.put("/payments/{payment_id}")
# async def update_payment(payment_id: int, amount: float, payment_date: date, db: Session = Depends(get_db)):
#     payment = db.query(RentalPayment).filter(RentalPayment.id == payment_id).first()
#     if not payment:
#         raise HTTPException(status_code=404, detail="Payment not found")
#     payment.amount = amount
#     payment.payment_date = payment_date
#     db.commit()
#     return {"message": "Payment updated successfully"}

# @router.delete("/payments/{payment_id}")
# async def delete_payment(payment_id: int, db: Session = Depends(get_db)):
#     payment = db.query(RentalPayment).filter(RentalPayment.id == payment_id).first()
#     if not payment:
#         raise HTTPException(status_code=404, detail="Payment not found")
#     db.delete(payment)
#     db.commit()
#     return {"message": "Payment deleted successfully"}
