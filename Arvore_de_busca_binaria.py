#Apresentar os elementos em ordem decrescente

def emOrdem(self,no):
    if no!=None:
        self.emOrdem(no.getfd())
        print(no.getvalores())
        self.emOrdem(no.getfe())

#Encontrar um valor na árvore
def chaveExiste(self,no,x):
    if no==None:
        return False
    else:
        if x==no.getChave():
            return True
        elif x<no.getChave():
            return self.chaveExiste(no.getfe(),x)
        else:
            return self.chaveExiste(no.getfd(),x)
#Retornar a quantidade de elementos na árvore
def contaElementos(self,no):
    if no==None:
        return 0
    else:
        return 1 + self.contaElementos(no.getfe()) + self.contaElementos(no.getfd())