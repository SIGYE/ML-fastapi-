from pydantic import BaseModel
from datetime import date
from typing import Optional

class TenantBase(BaseModel):
    name: str
    phone_number: str
    email: str


class TenantCreate(TenantBase):
    pass


class Tenant(TenantBase):
    id: int

    class Config:
        orm_mode = True


from pydantic import BaseModel
from datetime import date  

class HousingApplicationBase(BaseModel):
    tenant_id: int
    status: Optional[str]
    application_date: date  


class HousingApplicationCreate(HousingApplicationBase):
    pass


class HousingApplication(HousingApplicationBase):
    id: int

    class Config:
        orm_mode = True


class RentalPaymentBase(BaseModel):
    tenant_id: int
    amount: float
    payment_date: date


class RentalPaymentCreate(RentalPaymentBase):
    pass


class RentalPayment(RentalPaymentBase):
    id: int

    class Config:
        orm_mode = True
