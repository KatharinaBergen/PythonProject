from sqlmodel import Session, select
from Animal import Animal
from DatabaseConnectionService import engine

# Insert
with Session(engine) as session:
    a = Animal(name="Kira", species="Rabbit", age=3)
    session.add(a)
    session.commit()

    # Update
    a.age = 6
    session.commit()

    # Delete
    # session.delete(a)
    # session.commit()

    # Select
    statement = select(Animal)
    results = session.exec(statement)

    # Print all rows
    for row in results:
        print(row)

    session.close()