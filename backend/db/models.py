from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from db.connection import Connection

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True) 
    empresa = Column(BigInteger)
    nome = Column(String)
    email = Column(String)
    cpf = Column(String)
    telefone = Column(String)
    rua = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)
    numero = Column(String)

    def __repr__(self):
        return f"<Pessoa(" \
               f"nome='{self.nome}'," \
               f"email='{self.email}'," \
               f"cpf='{self.cpf}'," \
               f"telefone='{self.telefone}'," \
               f"rua='{self.rua}'," \
               f"bairro='{self.bairro}'," \
               f"cidade='{self.cidade}'," \
               f"estado='{self.estado}'," \
               f"numero='{self.numero}')>"

# if __name__ == "__main__":
#     # Assuming Connection() correctly initializes an engine and session
#     conn = Connection()

#     # Create the table if it doesn't exist
#     Base.metadata.create_all(conn.db_engine)

#     # If you want to insert a new record into the table, do it like this:
#     new_pessoa = Pessoa(
#         empresa=12345,
#         nome='John Doe',
#         email='johndoe@example.com',
#         cpf='12345678900',
#         telefone='555-555-5555',
#         rua='123 Main St',
#         bairro='Downtown',
#         cidade='Big City',
#         estado='CA',
#         numero='98765'
#     )

#     # Add the new_pessoa instance to the session and commit the changes
#     conn.db_session.add(new_pessoa)
#     conn.db_session.commit()
