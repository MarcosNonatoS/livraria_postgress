from model.autor import Autor


class AutorDAO:


    def __init__(self):
        self.__autores: list[Autor] = list()


    def listar(self) -> list[Autor]:
        return self.__autores


    def adicionar(self, autor: Autor) -> None:
        self.__autores.append(autor)


    def remover(self, autor_id: int) -> bool:
        encontrado = False
        for c in self.__autor:
            if (c.id == autor_id):
                index = self.__autores.index(c)
                self.__autores.pop(index)
                encontrado = True
                break
        return encontrado


    def buscar_por_id(self, autor_id) -> Autor:
        cat = None
        for c in self.__autores:
            if (c.id == autor_id):
                cat = c
                break
        return cat
   
    def ultimo_id(self) -> int:
        index = len(self.__autores) -1
        if (index == -1):
            id = 0
        else:
            id = self.__autores[index].id
        return id
   
