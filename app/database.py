from sqlalchemy import create_engine, text
from sqlalchemy.orm import  sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

#SERVER_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_HOST')}
SERVER_URL = "mysql+pymysql://rooadmin@localhost"

engine_server = create_engine(SERVER_URL)

with engine_server.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS series_api"))
    conn.commit()

#Conexão com o banco já criado
DATABASE_URL = "mysql+pymysql://root:admin@localhost/series_api"

# Criar um "motor" que fara o gerenciamento da conxão
engine = create_engine(DATABASE_URL)

#Criando uma sessão para executar os comandos sql
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria um objeto da base de dados manipulavel pelo Python
Base = declarative_base()

# Injeção de dependencia: injeta a sessao de bando de dados em casa rota que for criada 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()