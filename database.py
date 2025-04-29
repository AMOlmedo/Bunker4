
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_CONNECTION = 'mysql+pymsql://root:12345@localhost/test'   
#conexion a la bd

engine = create_engine(URL_CONNECTION)

localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
# actualiza la bd descpues de cada commit desactivada.

Base = declarative_base()





