class Hash:

     def __init__(self,tam):
          self.tab = {}
          self.tam_max = tam

     def funcaohash(self, chave):
          v = int(chave)
          return v%self.tam_max

     def cheia(self):
          return len(self.tab) == self.tam_max

     def imprimir(self):
          for i in self.tab:
               print("Hash[%d] = " %i, end="")
               print (self.tab[i])

     def apagar(self, chave):
          pos = self.buscar(chave)
          if pos != -1:
               del self.tab[pos]
               print("-> Dado da posicao %d apagado" %pos) 
          else:
               print("Item nao encontrado")

     def buscar(self, chave):
          pos = self.funcaohash(chave)
          if self.tab.get(pos) == None: 
               return- -1 
          if self.tab[pos] == chave: 
               return pos
          return -1

     def inserir(self, item):
          pos = self.funcaohash(item)
          if self.tab.get(pos) == None: 
               self.tab[pos] = item
               print("-> Inserido HASH[%d]" %pos)
          else:
               print("-> Ocorreu uma colisao na posicao %d, item não registrado" %pos)            
#####################################

            
tamanho = 6
tab = Hash(tamanho)
print("Tabela HASH %d itens" %tamanho)
for i in range (0,tamanho,1):
     print("\nInserindo elemento %d:" %(i + 1));
     item = input("Forneca valor numerico inteiro:")
     tab.inserir(item)
  
item = input("\n - Forneca valor numerico inteiro para buscar: ")
pos = tab.buscar(item)
if pos == -1:
     print("Item nao encontrado")
else:
     print("Item encontrado na posicao: ", pos)
item = input("\n - Forneca valor numerico inteiro para apagar: ")
tab.apagar(item)
print("\nImprimindo conteudo")
tab.imprimir()
print("\n")