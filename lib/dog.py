from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit

def get_all(session):
    dogs = session.query(Dog)
    return ([dog for dog in dogs])

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name.like(f'%{name}%'))
    for instance in query:
        return instance

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id)
    for instance in query:
        return instance

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name.like(f'%{name}%'),
        Dog.breed.like(f'%{breed}%'))
    for instance in query:
        return instance

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()
