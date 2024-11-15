from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Criando a classe base
Base = declarative_base()

# Conexão com o banco
def database():
    try:
        engine = create_engine('mysql+mysqlconnector://root:senha123@localhost/sms', echo=True)
        print("Connection to MySQL DB successful using SQLAlchemy")
        return engine
    except Exception as e:
        print(f"Failed to connect to DB: {str(e)}")
        engine = None
        return engine

def create_session(engine):
    # Criando uma sessão
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def create_db(engine):
    Base.metadata.create_all(bind=engine)