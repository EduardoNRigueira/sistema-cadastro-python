cadastros = []

def cadastrar_pessoa():
    nome = input("Nome: ")
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("|Digite uma idade válida|")
    email = input("Email: ")

    pessoa = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    cadastros.append(pessoa)
    print("\n|Cadastro realizado com sucesso!|\n")

def remover_cadastro():
    if not cadastros:
        print('|Não há cadastro para ser removido!|')
    else:
        for i , pessoa in enumerate(cadastros, start = 1):
            print(f"{i}. Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Email: {pessoa['email']}")
        print()

        try:
            escolha = int(input('Escolha o número do cadastro a ser removido: '))

            if 1 <= escolha <= len(cadastros):
                removido = cadastros.pop(escolha - 1)
                print(f"\n|Cadastro de {removido['nome']} removido com sucesso!|\n")
            else:
                print('\n|Número inválido!|\n')

        except ValueError:
            print('\n|Digite um número válido!|')


def listar_cadastros():
    if not cadastros:
        print('|A lista está vazia!|')
    else:
        print("\n|Lista de pessoas cadastradas|")
        print('=' * 50)
        for i , pessoa in enumerate(cadastros, start = 1):
            print(f"{i}. Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Email: {pessoa['email']}")
        print('=' * 50)
        print()

while True:
    opcao = input("1. Cadastrar pessoa\n2. Remover cadastro\n3. Lista de cadastros\n4. Sair\nDigite o número da sua escolha: ")

    if opcao == "1":
        cadastrar_pessoa()
    
    elif opcao == "2":
        remover_cadastro()

    elif opcao == "3":
        listar_cadastros()

    elif opcao == "4":
        print("\nPrograma encerrado")
        break




