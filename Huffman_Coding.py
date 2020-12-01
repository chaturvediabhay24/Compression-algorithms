"""
# **HUFFMAN CODING**



1.   We will be creating node for each probabilities and will be appending these nodes in the list.
2.   Then we will be removing two node with minimum probabilities from the list and will append the new node with probability equals sum of minimum two probabilities in the list.
3.   These two minimum nodes will be the child nodes of the new node.
4.   Will repeat this process untill we are available with only one node in the list.
5.   To extract the codes, we will start traversing tree with the only node present in the list.
6.   Will assign "0" to left child and "1" to the right child and after reaching the leaf node the formed code will be coded value assigned to that leaf node.
"""

import math
global codes

#Creating class "Node" as a node to our tree
class Node:
  def __init__(self, key=None):
    self.left=None
    self.right=None
    self.value=key

#Creating a class which performs huffman coding
class HuffmanCodes:
  def execute(self, probabilities):                         # Main function where all functions needed for execution are called
    self.probabilities=probabilities
    self.codes=self.get_huffman_codes(self.probabilities)
    self.l_bar=self.get_avg_length(self.codes)
    self.entropy=self.get_entropy(self.codes)
    self.efficiency=self.get_efficiency()
    self.print()

  def get_avg_length(self, prob_with_codes):                #function finds average length, given probablities and their codes.
    l_bar=0                                                 #using formula: sigma(p[i]*L[i])   
    for i in prob_with_codes:
      Pi=i[0]
      Li=len(i[1])
      l_bar+=Pi*Li
    return l_bar

  def get_efficiency(self):                                 #Efficiency is calculated using the formula: H(x)/L
    return self.entropy/self.l_bar

  def get_entropy(self, prob_with_codes):                   #Entropy is calculated using the formula: -sigma(Pi*log(Pi))

    entropy=0
    for row in prob_with_codes:
      pi=row[0]
      entropy-=pi*math.log(pi,2 )

    return entropy

  def tree_traverse(self, node,codes, string=""):           #Function for traversing the tree 

    if(node.left==None and node.right==None ):              # If leaf node is present, we save code corresponding to that source
      codes.append([node.value, string])

    if(node.left):
      self.tree_traverse(node.left,codes, string+"0")       # If left node is present we append "0" with the code of that string
      
    if(node.right):
      self.tree_traverse(node.right,codes, string+"1")      # If right node is present we append "1" with the code of that string
  
  def get_huffman_codes(self, probabilities):               # This function performs huffman coding by creating a tree
    
    for i in range(len(probabilities)):
      probabilities[i]=Node(probabilities[i])

    while(len(probabilities)>1):

      probabilities.sort(key= lambda x: x.value)            # Sorting probabilities so that we can get minimum two probabilities at front

      a=probabilities[0]                                    # Extracting the two sources with minimum probabilities
      b=probabilities[1]
      probabilities=probabilities[2:]

      new_node=Node(a.value+b.value)                        # Appending the new node with probability equals sum of two minimum nodes
      new_node.left=a
      new_node.right=b

      probabilities.append(new_node)                        # Appending new node to the list
      
    codes=[]

    self.tree_traverse(probabilities[0], codes)             # Traversing tree to find the corresponding codes
    codes.sort(key=lambda x: x[0], reverse=True)

    return codes
  
  def print(self):                                           # Utility function to print the calculated values
  
    print("Probabilities and their codes:")
    print("\nPROB\tCODE")

    for code in self.codes:
      print("{}\t{}".format(code[0], code[1]))
      
    print("\nAVERAGE LENGTH: {}".format(self.l_bar))
    print("\nENTROPY: {}".format(self.entropy))
    print("\nEFFICIENCY: {}".format(self.efficiency))

# Creating list of input probabilities
# probabilities=[0.22, 0.2, 0.18, 0.15, 0.1, 0.08, 0.05, 0.02]
probabilities=list(map(float, input().strip().split()))

obj=HuffmanCodes()                #Creating object of the class
obj.execute(probabilities)        #calling execute funtions to perform operations and print results
