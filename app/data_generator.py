import random
from faker import Faker
from sqlalchemy.orm import Session
from datetime import datetime, date, timedelta
from app.database import engine
from app.models import Tenant, HousingApplication, RentalPayment

# Faker setup
fake = Faker()

# Number of records to generate
NUM_TENANTS = 100
NUM_APPLICATIONS = 200
NUM_PAYMENTS = 300

def create_fake_data():
    """Generate fake data and populate the database."""
    with Session(engine) as session:
        # Generate tenants
        tenant_ids = []
        for _ in range(NUM_TENANTS):
            tenant = Tenant(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number()
            )
            session.add(tenant)
            session.flush()  # Save to get the tenant ID
            tenant_ids.append(tenant.id)

        # Generate housing applications
        for _ in range(NUM_APPLICATIONS):
            application = HousingApplication(
                tenant_id=random.choice(tenant_ids),
                application_date=fake.date_between(start_date='-2y', end_date='today'),
                status=random.choice(['Pending', 'Approved', 'Rejected'])
            )
            session.add(application)

        # Generate rental payments
        for _ in range(NUM_PAYMENTS):
            payment = RentalPayment(
                tenant_id=random.choice(tenant_ids),
                amount=round(random.uniform(500.00, 2000.00), 2),
                payment_date=fake.date_between(start_date='-1y', end_date='today')
            )
            session.add(payment)

        # Commit all changes to the database
        session.commit()

if __name__ == "__main__":
    print("Starting data generation...")
    create_fake_data()
    print("Data generation complete!")
