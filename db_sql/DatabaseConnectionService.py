from sqlmodel import SQLModel, create_engine

engine = create_engine("postgresql://user:password@localhost/python-database")
SQLModel.metadata.create_all(engine)