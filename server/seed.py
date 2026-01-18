#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Earthquake

with app.app_context():

    # Delete all rows in the "earthquakes" table
    Earthquake.query.delete()

    # Add several Earthquake instances to the "earthquakes" table
    db.session.add(Earthquake(magnitude=9.5, location="Chile", year=1960))
    db.session.add(Earthquake(magnitude=9.2, location="Alaska", year=1964))

    # Commit the transaction
    db.session.commit()

