#Cadastramento de Usuarios
usuario= []

def menu(): #Menu de acesso as opções 
 print("\nMENU DE ACESSO")
 print("1. Cadastar usuarios")
 print("2. Listar Usuarios")
 print("3. Buscar Usuario por nome")
 print("4. Remover Usuario")
 print("5. Sair")
 opcao= input("Escolha uma Opção")
 return opcao

def adicionar_usuario(): #Opção de Adicionar Usuario
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

def listar_usuarios(): #opção para listar usuario
 if not usuarios:
    print("\nNenhum usuario cadastrado.")
    return
 
 print("\n--- LISTA DE USUARIOS ---")
 for i, usuario in enumerate(usuarios, start=1):
  print(f"{i}. Nome:{usuario['nome']}, Idade: {usuario['idade']}, Email:{usuario['email']}, Contato: {usuario['contato']}")

  