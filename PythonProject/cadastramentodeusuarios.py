# Cadastramento de Usuarios
usuario = []


def menu():  # Menu de acesso as opções
    print("\nMENU DE ACESSO")
    print("1. Cadastar usuarios")
    print("2. Listar Usuarios")
    print("3. Buscar Usuario por nome")
    print("4. Remover Usuario")
    print("5. Sair")
    opcao = input("Escolha uma Opção")
    return opcao


def adicionar_usuario():  # Opção de Adicionar Usuario
    print("n--- Cadastro de Novo Usuario ---")
    nome = input("Digite o nome do usuario")
    idade = input("Digite a idade do usuario")
    email = input("digite o email do usuario")
    contato = input("digite o telefone do usuario")


novo_usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "contato": contato
    }


usuarios.append(novo_usuario)
print("\nUsuario adicionado com sucesso")


def listar_usuarios():  # opção para listar usuario
    if not usuarios:
        print("\nNenhum usuario cadastrado.")
        return

    print("\n--- LISTA DE USUARIOS ---")
    for i, usuario in enumerate(usuarios, start=1):
        print(
            f"{i}. Nome:{usuario['nome']}, Idade: {usuario['idade']}, Email:{usuario['email']}, Contato: {usuario['contato']}")


def buscar_usuario_por_nome():  # opção para buscar usuario
    if not usuarios:
        print("\nNenhum usuario foi encontrado na busca.")
        return

    nome_busca = input("Digite o nome do usuario que deseja buscar: ")
    encontrados = []
    for usuario in usuarios:
        if nome_busca.lower() in usuario['nome'].lower():
            encontrados.append(usuario)

            if not encontrados:
                print(f"\nNenhum usuario encontrado com o nome '{nome_busca}'.")
            else:
                print(f"\n--- Usuaios encontardos cpm o nome '{nome_busca}'.")
                for i, usuario in enumerate(encontrados, start=1):
                    print(
                        f"{i}. Nome: {usuario['nome']}, Idade:{usuario['idade']}, Email: {usuario['email']}, Contato: {usuario['contato']}")


def remover_usuario():  # opção para remover usuarios
    if not usuarios:
        print("\nNenhum usuario cadastrado para remover")
        return

    listar_usuarios()
    nome_remover = input("Digite o nome do usuario que deseja remover")

    usuario_encontrado = None
    indice_remover = -1


for i, usuario in enumerate(usuarios):
    if usuario['nome'] == nome_remover:
        usuario_encontrado = usuario
        indice_remover = i
        break

if usuario_encontrado:
    confirmacao = input(f"Tem certeza que deseja remover o usuario {usuario_encontrado['nome']}?(s/n): ")
    if confirmacao.lower() == 's':
        del usuarios[indice_remover]
        print(f"\nUsuario '{nome_remover}' removido com sucesso!")
    else:
        print("\nRemoção cancelada")
else:
    print(f"\nUsuario com o nome '{nome_remover}' não encontrado.")


def main():  # principal funçãodo sistema/loop do programa
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
            print("\nSaindo do programa. . . ")
            break
        else:
            print("\nOpção Invalida. Tente novamente.")


if __name__ == "__main__": #Executa a função principal quando o script é rodado
    main()