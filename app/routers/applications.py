# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.database import SessionLocal
# from app.models import HousingApplication, Tenant
# from datetime import date
# from typing import List

# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/applications/", response_model=List[dict])
# async def list_applications(db: Session = Depends(get_db)):
#     applications = db.query(HousingApplication).all()
#     return [
#         {
#             "id": app.id,
#             "tenant_name": app.tenant.name,
#             "application_date": app.application_date,
#             "status": app.status
#         }
#         for app in applications
#     ]

# @router.get("/applications/{application_id}")
# async def get_application(application_id: int, db: Session = Depends(get_db)):
#     application = db.query(HousingApplication).filter(HousingApplication.id == application_id).first()
#     if not application:
#         raise HTTPException(status_code=404, detail="Application not found")
#     return {
#         "id": application.id,
#         "tenant_name": application.tenant.name,
#         "application_date": application.application_date,
#         "status": application.status
#     }

# @router.post("/applications/")
# async def create_application(tenant_id: int, application_date: date, status: str, db: Session = Depends(get_db)):
#     tenant = db.query(Tenant).filter(Tenant.id == tenant_id).first()
#     if not tenant:
#         raise HTTPException(status_code=404, detail="Tenant not found")
#     new_application = HousingApplication(
#         tenant_id=tenant_id,
#         application_date=application_date,
#         status=status
#     )
#     db.add(new_application)
#     db.commit()
#     db.refresh(new_application)
#     return {
#         "id": new_application.id,
#         "tenant_name": tenant.name,
#         "application_date": new_application.application_date,
#         "status": new_application.status
#     }

# @router.put("/applications/{application_id}")
# async def update_application(application_id: int, status: str, db: Session = Depends(get_db)):
#     application = db.query(HousingApplication).filter(HousingApplication.id == application_id).first()
#     if not application:
#         raise HTTPException(status_code=404, detail="Application not found")
#     application.status = status
#     db.commit()
#     return {"message": "Application updated successfully"}

# @router.delete("/applications/{application_id}")
# async def delete_application(application_id: int, db: Session = Depends(get_db)):
#     application = db.query(HousingApplication).filter(HousingApplication.id == application_id).first()
#     if not application:
#         raise HTTPException(status_code=404, detail="Application not found")
#     db.delete(application)
#     db.commit()
#     return {"message": "Application deleted successfully"}
