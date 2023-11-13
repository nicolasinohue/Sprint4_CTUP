from models import Bike
from repository import Repository

class Controller:
    def __init__(self, repository):
        self.repository = repository

    def cadastrar_bikes(self):
        try:
            n_serie = int(input("Número de Série: "))
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            valor = float(input("Valor: "))
            modalidade = input("Modalidade: ")
            ano_fab = int(input("Ano de Fabricação: "))
            acessorio = input("Acessórios: ")
            tipo_quadro = input("Tipo de Quadro: ")
            tipopneu = input("Tipo de Pneu: ")
            tamanho_pneu = int(input("Tamanho do Pneu: "))
            quantmarcha = int(input("Quantidade de Marchas: "))
            tiposuspensao = input("Suspensão: ")
            tipofreio = input("Tipo de Freio: ")

            plano = self.select_plano()

        except ValueError:
            print("Por favor, insira um valor válido.")
            return

        nova_bike = Bike(
            n_serie=n_serie, marca=marca, modelo=modelo, valor=valor,
            modalidade=modalidade, ano_fab=ano_fab, acessorio=acessorio,
            tipo_quadro=tipo_quadro,tipopneu=tipopneu, tamanho_pneu=tamanho_pneu,
            quantmarcha=quantmarcha, tiposuspensao=tiposuspensao,
            tipofreio=tipofreio, plano=plano
        )

        self.cadastrar_bike(nova_bike)

    def excluir_bike(self):
        try:
            bike_id = int(input("Informe o ID da bicicleta a ser excluída: "))
            self.repository.deletar_bike(bike_id)
        except ValueError:
            print("Por favor, insira um ID de bicicleta válido.")

    def select_plano(self):
        print("1 - Plano Pedal Essencial")
        print("2 - Plano Pedal Leve")
        print("3 - Plano Pedal Elite")
        op_plano = int(input("Qual plano você deseja?: "))

        plano = None

        if op_plano in [1, 2, 3]:
            plano_id = op_plano
            plano = self.repository.obter_detalhes_plano(plano_id)

            if plano:
                print(f"Você contratou o '{plano['nome']}' - {plano['cobertura']}")
            else:
                print("Erro ao obter detalhes do plano.")
        else:
            print("Opção inválida.")

        return plano

    def salvar_e_sair(self):
        self.repository.close_session()
