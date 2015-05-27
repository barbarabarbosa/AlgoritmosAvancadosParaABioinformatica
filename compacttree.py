# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:02:54 2015

@author: Tiago
"""

class CreateTree:
    
    def __init__(self):
        self.nodes={0:(-1,{})}#root node
        self.num=0 #numero de no

##imprimir a arvore
        
    def print_tree(self):
        for k in self.nodes.keys():
            if self.nodes[k][0]<0:
                print str(k)+"->"+str(self.nodes[k][1])
            else:
                print str(k)+":"+str(self.nodes[k][0])


###########################################################
###Construcao da arvore de compactacao###
###########################################################
    
   
    def addNode(self,origin,symbol,leafnum=-1):
        self.num+=1
        self.nodes[origin][1][symbol]=self.num
        self.nodes[self.num]=(leafnum,{})
        
    def addSufix(self,p,sufnum):
        pos=0
        node=0
        while pos<len(p):
            if not self.nodes[node][1].has_key(p[pos]):
                if pos==len(p)-1:
                    self.addNode(node,p[pos],sufnum)
                else:
                    self.addNode(node,p[pos])
            node=self.nodes[node][1][p[pos]]
            pos+=1


    def suffixTrieFromSeq(self,text):
        t=text+"$"
        for i in range (len(t)):
            self.addSufix(t[i:],i)
            

    def nobiforca(self,node=0):#procura por caminhos nao bifurcados dado um nodo.
        res=[]
        if len(self.nodes[node][1].keys())==0:#if len(self.nodes[node][1].keys())==0:#atingimos uma folha
            res.append(self.nodes[node][0])#numero da folha colocado na lista
            return res[0]#cada no retornara apenas uma folha no caso de ser um caminho nao biforcado
        #for k in self.nodes[0][1].keys():
        elif len(self.nodes[node][1].keys())==1:#tem um no destino
            new_node=self.nodes[node][1].values()[0]#vai buscar o elemento a lista dos valores (neste caso é apenas um, por isso retira-se o primeiro)
            self.nobiforca(new_node)
        else:
            return None#encontra uma bifurcação
        #return res
        
        
    def InitialSearch(self):
        res=[]
        for k in self.nodes[0][1].keys():#raiz possui muitos nodos ligados
            search=self.nobiforca(self.nodes[0][1][k])
            if search !=None:
                res.append(search)
        return res
                
#ok, até aqui temos as folhas onde existem caminhos diretos da raiz ate elas... e agora? 
                
            
                
                
            
            
        
            
#criar um metodo para encurtar as folhas ate a raiz dooss nao biforcados
#depois e so chamar aqui na funcao de cima            
            
            
            
            


########################################################
###Algoritmo de pesquisa###
########################################################





    def findPattern(self,pattern):
        pos=0
        node=0
        for pos in range(len(pattern)):
            if self.nodes[node][1].has_key(pattern[pos]):
                node=self.nodes[node][1][pattern[pos]]
                pos+=1
            else:
                return None
        return self.getLeafesBelow(node)
        
        
        
        
    def getLeafesBelow(self,node):
        res=[]
        if self.nodes[node][0]>=0:
            res.append(self.nodes[node][0])
        else:
            for k in self.nodes[node][1].keys():
                newnode=self.nodes[node][1][k]
                leafes=self.getLeafesBelow(newnode)
                res.extend(leafes)         
        return res
        
        
        
        

if __name__=='__main__':
    
    def test():
        seq="TACTA"
        st=CreateTree()
        st.suffixTrieFromSeq(seq)
        st.print_tree()
    
  #  test()
    
    def test2():
        seq="TACT"
        st=CreateTree()
        st.suffixTrieFromSeq(seq)
    #    print st.findPattern("TA")
        print st.InitialSearch()
        #st.print_tree()       
        
        
    test2()