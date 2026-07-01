from random import randint, choice
from datetime import timedelta
from decimal import Decimal
from faker import Faker
from database import Base, engine, SESSION_LOCAL
from models import Lead, Activity, LeadPriority, LeadStatus, MeetingType, ActivityStatus

fake = Faker()
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SESSION_LOCAL()
industries = [
    "Software",
    "Finance",
    "Healthcare",
    "Retail",
    "Manufacturing",
    "Education",
]
services = ["AI Consulting", "Cloud", "Automation", "Analytics"]
sources = ["LinkedIn", "Referral", "Website", "Conference", "Cold Email"]
sizes = ["1-10", "11-50", "51-200", "201-1000", "1000+"]
currencies = ["USD", "EUR", "INR"]

for _ in range(50):
    lead = Lead(
        company_name=fake.unique.company(),
        industry=choice(industries),
        website=fake.unique.url(),
        linkedin=f"https://linkedin.com/company/{fake.unique.slug()}",
        country=fake.country(),
        city=fake.city(),
        company_size=choice(sizes),
        lead_source=choice(sources),
        primary_service=choice(services),
        priority=choice(list(LeadPriority)),
        current_status=choice(list(LeadStatus)),
        notes=fake.paragraph(),
    )
    db.add(lead)
    db.flush()
    for _ in range(randint(2, 6)):
        d = fake.date_time_between(start_date="-180d", end_date="now")
        db.add(
            Activity(
                lead_id=lead.id,
                meeting_type=choice(list(MeetingType)),
                contact_person=fake.name(),
                designation=fake.job(),
                email=fake.email(),
                phone=fake.phone_number(),
                contact_date=d,
                follow_up_date=d + timedelta(days=randint(2, 20)),
                status=choice(list(ActivityStatus)),
                quotation_amount=Decimal(randint(1000, 50000)),
                currency=choice(currencies),
                proposal_summary=fake.sentence(),
                meeting_notes=fake.paragraph(),
                follow_up_action="Follow up",
                created_by="Admin",
            )
        )
        
db.commit()
db.close()
print("Done")
