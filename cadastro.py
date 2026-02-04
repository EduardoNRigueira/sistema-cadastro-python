cadastros = []

def cadastrar_pessoa():

    while True:
        nome = input("Nome: ").title()

        if nome.replace(" ", "").isalpha():
            break
        else:
            print("|O nome deve possuir apenas letras|")

    while True:
        try:
            idade = int(input("Idade: "))
            if 0 < idade <= 120:
                break
            else:
                print("|Digite uma idade válida!|")
        except ValueError:
            print("|Digite apenas números!|")

    while True:
        email = input("Email: ")
        if "@" not in email or "." not in email:
            print("|Email inválido!|")
        else:
            break

    pessoa = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    cadastros.append(pessoa)
    print("\n|Cadastro realizado com sucesso!|\n")

def remover_cadastro():
    if not cadastros:
        print("|A lista está vazia!|\n")
        return

    listar_cadastros()

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

def editar_cadastro():
    if not cadastros:
        print("\n|Não há cadastros para editar!|\n")
        return

    listar_cadastros()

    try:
        escolha = int(input("Escolha o número do cadastro a ser editado: "))

        if not (1 <= escolha <= len(cadastros)):
            print("\n|Número inválido!|\n")
            return

        pessoa = cadastros[escolha - 1]

        print("\n|Pressione ENTER para manter o valor atual|")

        while True:
            novo_nome = input(f"Nome({pessoa['nome']}): ").title()
            if not novo_nome:
                break        

            elif novo_nome.replace(" ", "").isalpha():
                break
            else:
                print("|O nome deve possuir apenas letras|")


        while True:
            nova_idade = input(f"Idade ({pessoa['idade']}): ")
            if not nova_idade:
                break
            try:
                nova_idade = int(nova_idade)
                if 1 <= nova_idade <= 120:
                    pessoa["idade"] = nova_idade
                    break
                else:
                    print("|Digite uma idade válida!|")
            except ValueError:
                print("|Digite apenas números!|")

        novo_email = input(f"Email ({pessoa['email']}): ")
        if novo_email:
            pessoa["email"] = novo_email

        print("\n|Cadastro atualizado com sucesso!|\n")

    except ValueError:
        print("\n|Digite um número válido!|\n")

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



