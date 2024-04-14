class Tree:
    def __init__(self,value):
         self.data = value 
         self.left  = None
         self.right = None


root = Tree('200')
Node50 = Tree('50')
Node100 = Tree('100')
Node30 = Tree('30')
Node40 = Tree('40')
Node60 = Tree('60')
Node80 = Tree('80')


root.left = Node50
root.right = Node100

Node50.left = Node30
Node50.right =  Node40

Node100.left = Node60
Node100.right = Node80


print(root.right.left.data) 








        
