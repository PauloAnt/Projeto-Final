from typing import List
class Node:
    '''
    Classe that models a dinamic node of a binary tree.
    '''
    def __init__(self,data:object):
        '''
        Constructor that initializes a node with a data and
        without children.'''
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self)->object:
        return self.__data

    @data.setter
    def data(self, newData:object):
        self.__data = newData

    @property
    def left(self)->'Node':
        return self.__left

    @left.setter
    def left(self, newleft:object):
        self.__left = newleft

    @property
    def right(self)->'Node':
        return self.__right

    @right.setter
    def right(self, newRightChild:'Node'):
        self.__right = newRightChild

    def addLeft(self, data:object):
        if self.__left == None:
            self.__left = Node(data)	

    def hasLeftChild(self)->bool:
        return self.__left != None

    def hasRightChild(self)->bool:
        return self.__right != None

    def addRight(self,data:object):
        if self.__right == None:
            self.__right = Node(data)

    def __str__(self):
        return f'{self.__data}'


        
class BinarySearchTree:
    '''
    Class that models a binary search tree data structure.
    Author: Alex Cunha  
    Date of last modification: 31/10/2023
    Attributes
    ----------
    root (Node): reference to the root node.
    '''
    preorder  = 0
    inorder   = 1
    postorder = 2
    def __init__(self):
        '''
        Initializes the tree with a root node.
        '''
        self.__root = None

    def getRoot(self)->any:
        '''
        Gets the data stored in the root node.
        '''
        return self.__root.data if self.__root is not None else None

    def isEmpty(self)->bool:
        '''
        Checks if the tree is empty.
        '''
        return self.__root == None

    def add(self, data:any):
        '''
        Adds a new node to the tree.
        A new node is inserted in the right place according to BST properties.
        The left subtree of a node contains only nodes with keys lesser than 
        the node’s key. The right subtree of a node contains only nodes 
        with keys greater than the node’s key.

        Parameters
        ----------
        data (any): the data to be stored in the new node.
        '''
        if(self.__root == None):
            self.__root = Node(data)
        else:
            self.__add(data,self.__root)

    def __add(self, data:any, node:'Node'):
        if ( data < node.data):
            if( node.left != None):
                self.__add(data, node.left)
            else:
                node.addLeft(data)
        else:
            if( node.right != None):
                self.__add(data, node.right)
            else:
                node.addRight(data)
    
    def search(self, key:any )->any:
        '''
        Perform a search in the tree for a node with the given key
        Returns
        -------
        data (any): the data stored in the node corresponding the key.
        None: if the key is not found in the tree.
        '''
        if( self.__root != None ):
            node = self.__searchData(key, self.__root)
            return node.data if node is not None else None
        else:
            return None
    
    def __searchData(self, key:any, node:'Node'):
        if ( key == node.data):
            return node
        elif ( key < node.data and node.left != None):
            return self.__searchData( key, node.left)
        elif ( key > node.data and node.right != None):
            return self.__searchData( key, node.right)
        else:
            return None

    # Returns the number of nodes of the tree
    def __len__(self)->int:
        '''
        Counts the number of nodes in the tree.
        '''
        return self.__count(self.__root)

    def __count(self, node:'Node'):
        if ( node == None):
            return 0
        else:
            return 1 + self.__count(node.left) + self.__count(node.right)

    def traversal(self, order:int = None):
        '''
        Print the nodes of the in pre-order, in-order or post-order traversal.
        Arguments
        ---------
        order (int): the order of traversal. The possible values are:
        preorder, inorder, postorder. If no order is given, the traversal
        is performed in pre-order.
        '''
        if order == None:
            self.__preorder(self.__root)
        elif order == self.__class__.preorder:
            self.__preorder(self.__root)
        elif order == self.__class__.inorder:
            self.__inorder(self.__root)
        elif order == self.__class__.postorder:
            self.__postorder(self.__root)
        else:
            raise ValueError('Invalid order value')
        print()


    def __preorder(self, node):
        if( node != None):
            print(f'{node.data} ',end='')
            self.__preorder(node.left)
            self.__preorder(node.right)

    def __inorder(self, node):
        if( node != None):
            self.__inorder(node.left)
            print(f'{node.data} ',end='')
            self.__inorder(node.right)

    def __postorder(self, node):
        if( node != None):
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(f'{node.data} ',end='')

    # delete all nodes of the tree
    def deleteTree(self):
        # garbage collector fará o trabalho de remoção dos nós automaticamente. 
        self.__root = None

    # delete a node with the given key and return its data
    def deleteNode(self, key:any)->'Node':
        node = self.__searchData(key,self.__root)
        if node is not None:
            self.__root = self.__deleteNode(self.__root, key)
            return node.data
        else:
            return None
        
    
    # Dado um nó de uma BST e uma chave busca, este método
    # deleta o nó que contém a chave e devolve o novo nó raiz
    def __deleteNode(self,root:'Node', key:any):
        # Caso primário: não há raiz
        if root is None: 
            return root
  
        # Se a chave a ser deletada é menor do que a chave do nó raiz 
        # (da vez), então a chave se encontra na subárvore esquerda
        if key < root.data:
            root.left = self.__deleteNode(root.left, key) 
        # Se a chave a ser deletada é maior do que a chave do nó raiz (da vez),
        # então a chave se encontra na subárvore esquerda
        elif(key > root.data):
            root.right = self.__deleteNode(root.right, key) 
  
        # Se a chave é igual à chave do nó raiz, então estamos no nó 
        # a ser removido
        else:
            # (1) Nó com apenas 1 filho ou nenhum filho
            if root.left is None : 
                temp = root.right  
                root = None 
                return temp

            elif root.right is None :
                temp = root.left  
                root = None
                return temp 
  
            # (2) Nó com dois filhos: obtem o sucessor inorder
            # (o menor nó da subárvore direita) 
            temp = self.__minValueNode(root.right) 
  
            # copia o conteúdo do sucessor inorder para este nós
            root.data = temp.data 
  
            # Deletao sucessor inorder
            root.right = self.__deleteNode(root.right , temp.data)

        return root

    # Dada uma BST não vazia, retorna o nó
    # com a menor chave encontrada na árvore. Note que a árvore
    # inteira não precisa ser percorrida
    def __minValueNode(self, node:'Node')->'Node':
        current = node 
  
        # loop para baixo a fim de encontrar a folha mais a esquerda
        while(current.left is not None): 
            current = current.left  
  
        return current

    # Dada uma BST não vazia, retorna o nó
    # com o maior valor de chave encontrada na árvore. Note que a árvore
    # inteira não precisa ser percorrida 
    def __maxValueNode(self, node:'Node')->'Node':
        current = node 
  
         # loop para baixo a fim de encontrar a folha mais a direita
        while(current.right is not None): 
            current = current.right
  
        return current

    def __str__(self)->str:
        '''
        Returns a string representation of the tree in preorder traversal.
        '''
        return self.__preorderToStr(self.__root)

    def __preorderToStr(self, root)->str:
        if (root is None):
            return ''
    
        result = f'{root.data} | '
        result += self.__preorderToStr(root.left)
        result += self.__preorderToStr(root.right)
        return result

    def treeview(self):
        '''
        Displays the tree in a visual way, in order to understand where
        nodes were inserted.
        Note: call this method only for small trees.
        '''
        if self.__root is None:
            return
        lines, *_ = self.__visual(self.__root)
        for line in lines:
            print(line)

    def __visual(self, node):
        """
        Returns list of strings, width, height, and horizontal coordinate
        of the root.
        """
        # No child.
        if node.right is None and node.left is None:
            line = f'{node.data}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self.__visual(node.left)
            s = f'{node.data}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self.__visual(node.right)
            s = f'{node.data}'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x  = self.__visual(node.left)
        right, m, q, y = self.__visual(node.right)
        s = f'{node.data}'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2     
    
    def build(self,values:List[any]):
        '''
        Builds a binary search tree in the order the nodes appear in
        the list.        
        Precondition: the tree must be empty

        Arguments
        ---------
        values (List[any]): the list of values to be inserted in 
        the tree.
        '''
        if not values or self.__root != None:
            return None 

        for element in values:
            self.add(element)


    def __storeBSTNodes(self, root:Node, nodes:list):
        if not root:
            return
        self.__storeBSTNodes(root.left, nodes)
        nodes.append(root)
        self.__storeBSTNodes(root.right, nodes)
    
    # Recursive function to construct binary tree 
    def __buildTreeUtil(self, nodes:list, start, end):
        if start > end:
            return None
        # Get the middle element and make it root 
        mid=(start+end)//2
        node = nodes[mid]
        # Using index in Inorder traversal, construct 
        # left and right subtress
        node.left = self.__buildTreeUtil(nodes, start, mid-1)
        node.right = self.__buildTreeUtil(nodes, mid+1, end)
        return node
    
    # This functions converts an unbalanced BST to 
    # a balanced BST
    def buildTree(self):
        # Store nodes of given BST in sorted order 
        nodes=[]
        self.__storeBSTNodes(self.__root, nodes)
    
        # Constructs BST from nodes[] 
        n=len(nodes)
        self.__root = self.__buildTreeUtil(nodes, 0, n-1)

    def __iter__(self):
        '''
        Returns an iterator for the tree.
        '''
        self.__stack = [self.__root]
        return self

    def __next__(self):
        '''
        Returns the next node in the iteration.
        '''
        if not self.__stack:
            raise StopIteration
        node = self.__stack.pop()
        if node.right:
            self.__stack.append(node.right)
        if node.left:
            self.__stack.append(node.left)
        return node.data
    