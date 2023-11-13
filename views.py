
class View:
    def __init__(self, db):
        self.db = db
    
    def exibir_bike(self, bikes, num_serie):
        bike = bikes.get(num_serie)

        if bike:
            print(f"Informações da Bicicleta:")
            print(f"Número de Série: {bike.num_serie}")
            print(f"Marca: {bike.marca}")
            print(f"Modelo: {bike.modelo}")
            print(f"Valor: {bike.valor}")
            print(f"Modalidade: {bike.modalidade}")
            print(f"Ano de fabricacao: {bike.a_fabric}")
            print(f"Aessorios: {bike.acess}")
            print(f"Tipo de quadro: {bike.tipo_quadro}")
            print(f"Tamanho do quadro: {bike.tamanho_quadro}")
            print(f"Tipo de pneu: {bike.tipo_pneu}")
            print(f"Tamanho de pneu{bike.tamanho_pneu}")
            print(f"Quantidade de marchas: {bike.quant_marcha}")
            print(f"Suspensão: {bike.tipo_suspensao}")
            print(f"Tipo de freio: {bike.tipo_freio}")
            print(f"{bike.plano}")
        else:
            print("Bicicleta não encontrada.")
