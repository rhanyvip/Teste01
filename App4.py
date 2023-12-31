import pickle


def adicionar_contato(contatos, nome, telefone, email):
    novo_contato = {'nome': nome, 'telefone': telefone, 'email': email}
    contatos.append(novo_contato)
    print('Contato adicionado com sucesso.')


def exibir_contatos(contatos):
    for contato in contatos:
        print('Nome:', contato['nome'])
        print('Telefone:', contato['telefone'])
        print('E-mail:', contato['email'])
        print('---')


def main():
    contatos = []
    try:
        with open('contatos.bin', 'rb') as arquivo:
            contatos = pickle.load(arquivo)
    except FileNotFoundError:
        pass

    while True:
        print('Menu:')
        print('1. Adicionar contato')
        print('2. Exibir contatos')
        print('3. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome = input('Digite o nome do contato: ')
            telefone = input('Digite o telefone do contato: ')
            email = input('Digite o e-mail do contato: ')
            adicionar_contato(contatos, nome, telefone, email)
        elif opcao == '2':
            exibir_contatos(contatos)
        elif opcao == '3':
            with open('contatos.bin', 'wb') as arquivo:
                pickle.dump(contatos, arquivo)
            print('Contatos salvos no arquivo contatos.bin. Encerrando o programa.')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()

 
 
