from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class OracleDB:
    def create_database():
        db = create_engine('oracle+oracledb://rm98057:250899@oracle.fiap.com.br/?service_name=orcl')
        return db