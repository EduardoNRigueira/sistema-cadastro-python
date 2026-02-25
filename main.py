from funcoes import *

carregar_cadastros()


while True:
    opcao = input(
    "1. Cadastrar pessoa\n"
    "2. Remover cadastro\n"
    "3. Editar cadastro\n"
    "4. Listar cadastros\n"
    "5. Sair\n"
    "Digite o número da sua escolha: "
)


    if opcao == "1":
        cadastrar_pessoa()
    
    elif opcao == "2":
        remover_cadastro()

    elif opcao == "3":
        editar_cadastro()

    elif opcao =="4":
        listar_cadastros()

    elif opcao == "5":
        print("\nPrograma encerrado")
        break
    else:
        print("\n|Opção inválida!|\n")



