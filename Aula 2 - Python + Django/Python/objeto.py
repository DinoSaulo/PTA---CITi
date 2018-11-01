# -*- coding: utf-8 -*-

class funcionario:
    def __init__(self, nome, idade, empresa, apelido):
        self.__nome = nome
        self.__idade = idade
        self.__empresa = empresa
        self.publicName = apelido

    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getEmpresa(self):
        return self.__empresa
    
    def envevhecer(self):
        self.__idade = self.__idade + 1

    def mudarNome (self, nome):
        self.__nome = nome

citiano = funcionario('João',20, 'CITi','Joãozin')   
    
print(citiano.getIdade())
citiano.envevhecer()
print(citiano.getIdade())

