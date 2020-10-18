#http://zetcode.com/db/sqlalchemy/
#http://zetcode.com/db/sqlalchemy/orm/
#https://docs.sqlalchemy.org/en/13/orm/tutorial.html
from app.models.db import Base, Session, engine, session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String, JSON
from sqlalchemy import Sequence

class NReynas(Base):
    """
        Modelo SolucionNReynas, encargada de resolver, insertar y obtener la solucion de la db

    """
    __tablename__ = "NReynas"

    Id = Column(Integer, Sequence('id'), primary_key=True)
    N = Column(Integer, default=0)
    Soluciones = Column(JSON, default={})

    def __init__(self, n):
        self.N = n