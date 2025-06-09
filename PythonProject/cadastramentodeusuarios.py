#Cadastramento de usuarios
usuarios = []

def menu():  # Menu de acesso as opções
    print("\nMENU DE ACESSO")
    print("1. Cadastrar usuário")
    print("2. Listar Usuários")
    print("3. Buscar Usuário por nome")
    print("4. Remover Usuário")
    print("5. Sair")
    opcao = input("Escolha uma Opção: ")
    return opcao

def adicionar_usuario(): # Opção de Adicionar Usuario
    print("\n--- Cadastro de Novo Usuário ---")
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade do usuário: ") 
    email = input("Digite o email do usuário: ") 
    contato = input("Digite o telefone do usuário: ")

    novo_usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "contato": contato
    }

    usuarios.append(novo_usuario)
    print("\nUsuário adicionado com sucesso!")

def listar_usuarios(): # opção para listar usuario
    if not usuarios:
        print("\nNenhum usuário cadastrado.")
        return

    print("\n--- LISTA DE USUÁRIOS ---")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}, Contato: {usuario['contato']}")

def buscar_usuario_por_nome(): # opção para buscar usuario
    if not usuarios:
        print("\nNenhum usuário cadastrado para buscar.")
        return

    nome_busca = input("Digite o nome do usuário que deseja buscar: ")
    encontrados = []
    for usuario in usuarios:
        if nome_busca.lower() in usuario['nome'].lower():
            encontrados.append(usuario)

    if not encontrados:
        print(f"\nNenhum usuário encontrado com o nome '{nome_busca}'.")
    else:
        print(f"\n--- Usuários encontrados com o nome '{nome_busca}' ---")
        for i, usuario in enumerate(encontrados, start=1):
            print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}, Contato: {usuario['contato']}")

def remover_usuario(): # opção para remover usuarios
    if not usuarios:
        print("\nNenhum usuário cadastrado para remover.")
        return

    listar_usuarios() 
    nome_remover = input("Digite o nome exato do usuário que deseja remover: ")

    usuario_encontrado = None
    indice_remover = -1

    for i, usuario in enumerate(usuarios):
        if usuario['nome'] == nome_remover:
            usuario_encontrado = usuario
            indice_remover = i
            break

    if usuario_encontrado:
        confirmacao = input(f"Tem certeza que deseja remover o usuário {usuario_encontrado['nome']}? (s/n): ")
        if confirmacao.lower() == 's':
            del usuarios[indice_remover]
            print(f"\nUsuário '{nome_remover}' removido com sucesso!")
        else:
            print("\nRemoção cancelada.")
    else:
        print(f"\nUsuário com o nome '{nome_remover}' não encontrado.")

def main(): # principal funçãodo sistema/loop do programa
    while True:
        opcao = menu()
        if opcao == '1':
            adicionar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            buscar_usuario_por_nome()
        elif opcao == '4':
            remover_usuario()
        elif opcao == '5':
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__": #Executa a função principal quando o script é rodado
    main()


