#!/usr/bin/env python3

# Script goes here!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

# Set up the database
DATABASE_URL = "sqlite:///freebies.db"
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)

# Create sample data
company1 = Company(name="TechCorp", founding_year=1999)
dev1 = Dev(name="Alice")

session.add(company1)
session.add(dev1)
session.commit()

# Add a freebie
company1.give_freebie(dev1, "T-Shirt", 10)

# Test methods
print(dev1.received_one("T-Shirt"))  # Should print True
print(Freebie.query.first().print_details())  # Should print 'Alice owns a T-Shirt from TechCorp'
print(Company.oldest_company())  # Should print the oldest company
