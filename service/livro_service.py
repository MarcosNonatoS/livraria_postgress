from dao.livro_dao import LivroDAO
from model.livro import Livro
from dao.categoria_dao import CategoriaDAO
from model.categoria import Categoria
from dao.editora_dao import EditoraDAO
from model.editora import Editora
from dao.autor_dao import AutorDAO
from model.autor import Autor


class LivroService:

    def __init__(self, categoria_dao: CategoriaDAO, editora_dao: EditoraDAO, autor_dao: AutorDAO):
        self.__livro_dao: LivroDAO = LivroDAO()
        self.__categoria_dao: CategoriaDAO = categoria_dao
        self.__editora_dao: EditoraDAO = editora_dao
        self.__autor_dao: AutorDAO = autor_dao

    def menu(self):
        print('[Livros] Escolha uma das seguintes opções:\n'
                '1 - Listar todos os livros\n'
                '2 - Adicionar novo livro\n'
                '3 - Excluir livro\n'
                '4 - Ver livro por Id\n'
                '0 - Voltar ao menu anterior\n')
        escolha = input('Digite a opção: ')


        if escolha == '0':
            return
        if escolha == '1':
            self.listar()
        elif escolha == '2':
            self.adicionar()
        elif escolha == '3':
            self.remover()
        elif escolha == '4':
            self.mostrar_por_id()
        else:
            print('Opção inválida! Por favor, tente novamente!')


        self.menu()


    def listar(self):
        print('\nListando livros...')


        try:
            livros = self.__livro_dao.listar()
            if len(livros) == 0:
                print('Nenhum livro encontrado!')


            for livro in livros:
                print(f'{livro.id} | {livro.titulo} | {livro.resumo} | {livro.ano} | {livro.paginas} | {livro.isbn} | {livro.categoria.nome} | {livro.autor.nome} | {livro.editora.nome}')
        except Exception as e:
            print(f'Erro ao exibir os livros! - {e}')
            return


        input('Pressione uma tecla para continuar...')


    def adicionar(self):
        print('\nAdicionando livro...')


        try:
            id = self.__livro_dao.ultimo_id() + 1
            titulo = input('Digite o titulo do livro: ')
            resumo = input('Digite o resumo do livro: ')
            ano = input('Digite o ano do livro: ')
            paginas = int(input('Digite a qtde de páginas: '))
            isbn = input('Digite o isbn do livro: ')

            print('Seleciona a categoria: ')

            categorias = self.__categoria_dao.listar()
            for categoria in categorias:
                print(f'Id: {categoria.id} | Categoria: {categoria.nome}')

            idcategoria = int(input('Insira o id da categoria selecionada: '))
            categoria = self.__categoria_dao.buscar_por_id(idcategoria)

            while categoria==None:
                print('Não foi encontrada a categoria')
                idcategoria = int(input('Insira o id da categoria selecionada: '))
                categoria = self.__categoria_dao.buscar_por_id(idcategoria)

            print('Seleciona o autor: ')
            autores = self.__autor_dao.listar()
            for autores in autores:
                print(f'Id: {autores.id} | Autor: {autores.nome}')

            idautor = int(input('Insira o id do autor selecionado: '))
            autor = self.__autor_dao.buscar_por_id(idautor)

            while autores==None:
                print('Não foi encontrado o autor')
                idautor = int(input('Insira o id do autor selecionado: '))
                autor = self.__autor_dao.buscar_por_id(idautor)

            print('Seleciona a editora: ')
            editoras = self.__editora_dao.listar()
            for editora in editoras:
                print(f'Id: {editora.id} | Editora: {editora.nome}')

            ideditora = int(input('Insira o id da editora selecionada: '))
            editora = self.__editora_dao.buscar_por_id(ideditora)

            while editora==None:
                print('Não foi encontrado o autor')
                ideditora = int(input('Insira o id da editora selecionada: '))
                editora = self.__editora_dao.buscar_por_id(ideditora)
   
            novo_livro = Livro(id, titulo, resumo, ano, paginas, isbn, categoria, editora, autor)
            self.__livro_dao.adicionar(novo_livro)
            print('livro adicionado com sucesso!')

        except Exception as e:
            print(f'Erro ao inserir o livro! - {e}')
            return


        input('Pressione uma tecla para continuar...')


    def remover(self):
        print('\nRemovendo livro...')


        try:
            livro_id = int(input('Digite o ID do livro para excluir: '))
            if (self.__livro_dao.remover(livro_id)):
                print('Livro excluído com sucesso!')
            else:
                print('Livro não encontrado!')
        except Exception as e:
            print(f'Erro ao excluir livro! - {e}')
            return
       
        input('Pressione uma tecla para continuar...')


    def mostrar_por_id(self):
        print('\nLivro por Id...')


        try:
            id = int(input('Digite o Id do livro para buscar: '))
            cat = self.__livro_dao.buscar_por_id(id)


            if (cat == None):
                print('Livro não encontrada!')
            else:
                print(f'Id: {cat.id} | livro: {cat.titulo} | categoria: {cat.categoria}')    
        except Exception as e:
            print(f'Erro ao exibir livro! - {e}')
            return    
       
        input('Pressione uma tecla para continuar...')