from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection():
    def __init__(self):

        self.conn = {
            'type': 'postgresql',
            'user': 'postgres',
            'host': 'localhost',
            'port': 5432,
            'database': 'gerencia',
            'pass': 'postgres'
        }

        self.db_url = f"{self.conn['type']}://{self.conn['user']}:{self.conn['pass']}@{self.conn['host']}:{self.conn['port']}/{self.conn['database']}"

        self.db_engine = create_engine(self.db_url)
    
    def create_session(self):
        try:
            Session = sessionmaker(bind=self.db_engine)

            return Session()
        
        except Exception as e:
            print(e, 'Erro ao conectar no banco de dados')