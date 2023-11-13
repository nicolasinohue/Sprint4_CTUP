from sqlalchemy.orm import sessionmaker
from models import Bike, Vistoria, Apolice

class Repository:
    def __init__(self, engine):
        self.engine = engine
        self.Session = sessionmaker(bind=engine)
        self.session = None

    def create_session(self):
        self.session = self.Session()

    def close_session(self):
        if self.session:
            self.session.close()

    def close_connection(self):
        if self.engine:
            self.engine.dispose()

    def cadastrar_bike(self, bike):
        try:
            self.session.add(bike)
            self.session.commit()
            print("Bicicleta cadastrada com sucesso!")
            bike_id = bike.id
            self.realizar_vistoria(bike_id)
        except Exception as e:
            self.session.rollback()
            print(f"Erro ao cadastrar bicicleta: {e}")

    def realizar_vistoria(self, bike_id):
        data_vistoria = input("Informe a data da vistoria (YYYY-MM-DD): ")
        etapa = input("Informe a etapa da vistoria: ")

        try:
            nova_vistoria = Vistoria(data_vistoria=data_vistoria, etapa=etapa, bike_id=bike_id)

            bike = self.session.query(Bike).get(bike_id)
            bike.vistorias.append(nova_vistoria)

            self.session.add(nova_vistoria)
            self.session.commit()

            print("Vistoria realizada com sucesso.")
        except Exception as e:
            self.session.rollback()
            print(f"Erro ao realizar vistoria: {e}")

    def listar_bike(self):
        return self.session.query(Bike).all()

    def deletar_bike(self, bike_id):
        bike = self.session.query(Bike).get(bike_id)
        if bike:
            self.session.delete(bike)
            self.session.commit()

    def obter_detalhes_plano(self, plano_id):
        try:
            plano = self.session.query(Apolice).filter_by(id=plano_id).first()

            if plano:
                detalhes_plano = {
                    'id': plano.id,
                    'nome': plano.nome,
                    'valor': plano.valor,
                    'cobertura': plano.cobertura,
                }
                return detalhes_plano
            else:
                print(f"Plano com ID {plano_id} não encontrado.")
                return None
        except Exception as e:
            print(f"Erro ao obter detalhes do plano: {e}")
            return None

