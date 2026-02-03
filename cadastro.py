cadastros = []

def cadastrar_pessoa():
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")

    pessoa = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    cadastros.append(pessoa)
    print("\n|Cadastro realizado com sucesso!|\n")


while True:
    opcao = input("1. Cadastrar pessoa.\n2. Sair.\nDigite o número da sua escolha: ")

    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "2":
        print("Programa encerrado")
        break

print(f'Lista de pessoas cadastradas:\n {cadastros}')


