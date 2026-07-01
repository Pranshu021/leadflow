from faker import Faker
from models import Lead
from database import SESSION_LOCAL

fake = Faker()
db = SESSION_LOCAL()

for _ in range(100):
    db.add(
        Lead(
            company_name=fake.company(),
            website=fake.url(),
            city=fake.city(),
            country=fake.country(),
        )
    )

db.commit()
db.close()