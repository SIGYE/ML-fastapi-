from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from .database import Base

class Tenant(Base):
    __tablename__ = "housing_tenant"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(30), nullable=False)

    def __repr__(self):
        return f"<Tenant(name={self.name}, email={self.email})>"

    applications = relationship("HousingApplication", back_populates="tenant")
    payments = relationship("RentalPayment", back_populates="tenant")


class HousingApplication(Base):
    __tablename__ = "housing_housingapplication"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("housing_tenant.id"), nullable=False)
    application_date = Column(Date, nullable=False)
    status = Column(String(20), nullable=False)

    tenant = relationship("Tenant", back_populates="applications")

    def __repr__(self):
        return f"<HousingApplication(tenant_id={self.tenant_id}, status={self.status})>"




class RentalPayment(Base):
    __tablename__ = "housing_rentalpayment"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("housing_tenant.id"), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    payment_date = Column(Date, nullable=False)

    tenant = relationship("Tenant", back_populates="payments")

    def __repr__(self):
        return f"<RentalPayment(housing_tenant_id={self.tenant_id}, amount={self.amount})>"
