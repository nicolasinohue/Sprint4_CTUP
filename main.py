from database import OracleDB
from repository import Repository
from controller import Controller

def main():
    db = OracleDB.create_database()
    repository = Repository(db)
    repository.create_session()
    controller = Controller(repository)

    while True:
        print("\nMenu:")
        print("1 - Cadastrar Bicicleta")
        print("2 - Listar Bicicletas")
        print("3 - Excluir Bicicleta")
        print("4 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if opcao == 1:
            controller.cadastrar_bikes()
        elif opcao == 2:
            repository.listar_bike()
        elif opcao == 3:
            controller.excluir_bike()
        elif opcao == 4:
            repository.close_session()
            repository.close_connection()
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()