#Estrutura da Classe (indica que a árvore começa vazia (sem nós)
class ArvoreBB:
  def __init__(self):
    self.__raiz = None
#Métodos da Classe(getRaiz oferece uma maneira de acessá-lo de fora da classe.)
  def getRaiz(self):
    return self.__raiz
#setRaiz -permite definir ou alterar a raiz(utilizado quando o primeiro nó é inserido, definindo-o como raiz.)
  def setRaiz(self, no):
    self.__raiz = no
#arvoreVazia(Ele é útil para saber se a árvore já tem elementos ou se está vazia antes de inserir novos nós)
  def arvoreVazia(self):
    return self.getRaiz() == None 
#insere -Esse método insere um novo nó (no) na árvore.Se a árvore estiver vazia, ele define o novo nó como a raiz 
# usando setRaiz(no).Caso contrário, ele chama o método insereNo para encontrar a posição correta e inserir o nó
  def insere(self, no):
    if self.arvoreVazia():
      self.setRaiz(no)
    else:
      self.insereNo(None, self.getRaiz(), no)
#insereNo -Esse método recursivo encontra o local correto para inserir o nó (no) na árvore. 
  def insereNo(self, pai, atual, no):
    if atual == None:
      if no.getChave() < pai.getChave():
        pai.setFe(no)
      else:
        pai.setFd(no)
    elif no.getChave() < atual.getChave():
      self.insereNo(atual, atual.getFe(), no)
    else:
      self.insereNo(atual, atual.getFd(), no)  


# Reservado ara a remocao de nos
   
    # Método principal para remover um nó
    def remove(self, chave):
        self.__raiz = self._removeNo(self.__raiz, chave)
    
    # Método auxiliar para a remoção de um nó
    def _removeNo(self, no, chave):
        if no is None:
            return no  # Se o nó é None, não há nada a remover

        # Buscando o nó a ser removido
        if chave < no.getChave():
            no.setFe(self._removeNo(no.getFe(), chave))
        elif chave > no.getChave():
            no.setFd(self._removeNo(no.getFd(), chave))
        else:
            # Caso 1: Nó sem filhos
            if no.getFe() is None and no.getFd() is None:
                return None
            
            # Caso 2: Nó com apenas um filho
            elif no.getFe() is None:
                return no.getFd()
            elif no.getFd() is None:
                return no.getFe()
            
            # Caso 3: Nó com dois filhos
            else:
                sucessor = self._encontrarMinimo(no.getFd())
                no.setChave(sucessor.getChave())
                no.setFd(self._removeNo(no.getFd(), sucessor.getChave()))
        
        return no

    # Função auxiliar para encontrar o menor valor (sucessor)
    def _encontrarMinimo(self, no):
        atual = no
        while atual.getFe() is not None:
            atual = atual.getFe()
        return atual
#Este método percorre a árvore em ordem crescente
  def emOrdem(self, no):
    if no != None:
      self.emOrdem(no.getFe())
      print(no.getValores())
      self.emOrdem(no.getFd())
#No percurso pré-ordem, o nó raiz é visitado antes dos seus filhos.
#A sequência de passos é:
#Visite o nó atual.
#Visite o nó esquerdo.
#Visite o nó direito.
  def preOrdem(self, no):
    if no != None:
      print(no.getValores())
      self.preOrdem(no.getFe())
      self.preOrdem(no.getFd())
#No percurso pós-ordem, os filhos são visitados antes do nó raiz.
#A sequência de passos é:
#Visite o nó esquerdo.
#Visite o nó direito.
#Visite o nó atual.
  def posOrdem(self, no):
    if no != None:
      self.posOrdem(no.getFe())
      self.posOrdem(no.getFd())
      print(no.getValores())

# Insiram os Exercicios Abaixo