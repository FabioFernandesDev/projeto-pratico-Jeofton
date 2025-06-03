#Cadastramento de Usuarios
usuario= []

def menu(): #Menu de acesso as opções 
 print("MENU DE ACESSO")
 print("Cadastar usuarios")
 print("Listar Usuarios")
 print("Buscar Usuario por nome")
 print("Remover Usuario")
 print("Sair")
 opcao= input("Escolha uma Opção")
 return opcao

def adicionar usuario(): #Opção de Adicionar Usuario
 nome = input("Digite o nome do usuario")
 idade = input("Digite a idade do usuario")
 email = input("digite o email do usuario")
 contato = input("digite o telefone do usuario")

usuario = {
 "nome": nome,
 "idade": idade,
 "email": email,
 "contato": contato
}

usuario.append(usuario)
print("Usuario adicionado com sucesso")