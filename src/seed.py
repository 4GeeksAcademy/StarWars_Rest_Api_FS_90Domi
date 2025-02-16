from models import db, Planets,People

from app import app

# Create several planets 
with app.app_context():
    p1 = Planets(nombre="Tierra")
    p2 = Planets(nombre="Marte")

    p3 = People(nombre="Luc")
    
   
    

    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)

    db.session.commit()