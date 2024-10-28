class arvoreBB:
    def __init(self):
        self.__raiz=None
    def getraiz(self):
        return self.__raiz
    def setraiz (self,no):
        self.__raiz = no
    def arvoreVazia (self):
        return self.__getRaiz() == None
    def insere (self,no):
        if self.arvoreVazia(self,no):
            self.setRaiz(no)
        else:
            self.insereNo(None, self.getRaiz(), no)
            