from arcslide import *
from algebra import DGAlgebra, FreeModule, Generator, SimpleChainComplex, \
    Tensor, TensorGenerator, TensorDGAlgebra
from dstructure import zeroTypeD
from ddstructure import identityDD, SimpleDDStructure
from digraph import *

#array of pairs, corresponding to phi_1, ..., phi_n
pairs = []
#T_2
pairs.append([4,3])
pairs.append([4,5])
pairs.append([3,4])
pairs.append([2,1])
pairs.append([3,2])
pairs.append([4,3])
pairs.append([6,5])
pairs.append([3,2])
pairs.append([4,3])
pairs.append([5,4])
pairs.append([7,6])
pairs.append([4,3])
pairs.append([5,4])
pairs.append([6,5])

#T_2
pairs.append([4,3])
pairs.append([4,5])
pairs.append([3,4])
pairs.append([2,1])
pairs.append([3,2])
pairs.append([4,3])
pairs.append([6,5])
pairs.append([3,2])
pairs.append([4,3])
pairs.append([5,4])
pairs.append([7,6])
pairs.append([4,3])
pairs.append([5,4])
pairs.append([6,5])

#T_1^-1
pairs.append([7,6])
pairs.append([7,6])
pairs.append([7,6])
pairs.append([7,6])
pairs.append([7,6])
pairs.append([7,6])

#T_2^-1
pairs.append([6,5])
pairs.append([5,4])
pairs.append([4,3])
pairs.append([7,6])
pairs.append([5,4])
pairs.append([4,3])
pairs.append([3,2])
pairs.append([6,5])
pairs.append([4,3])
pairs.append([3,2])
pairs.append([2,1])
pairs.append([3,4])
pairs.append([4,5])
pairs.append([4,3])
# pairs.reverse()
print(len(pairs))


Z = PMC([(0,2),(1,3),(4,6),(5,7)]) #suppose that the PMC associated to phi_n is the one depicted in the figure

#writing out all the arcslides for the first two DD structures
slide1 = Arcslide(Z, pairs[0][0], pairs[0][1])
slide2 = Arcslide(Z, pairs[1][0], pairs[1][1])
ddstr1 = slide1.getDDStructure()
ddgraph1 = TypeDDGraph(ddstr1,1)
ddstr2 = slide2.getDDStructure()
ddgraph2 = TypeDDGraph(ddstr2,2)
aa = TypeAAGraph(ddgraph1.algebra1.pmc)
product = aa.tensorDoubleDD(ddgraph2,ddgraph1)
product_graph = TypeDDGraph(product,1)

slide3 = Arcslide(product_graph.algebra1.pmc.opp(), pairs[2][0], pairs[2][1])
ddstr3 = slide3.getDDStructure()
ddgraph3 = TypeDDGraph(ddstr3,2)

aa = TypeAAGraph(product_graph.algebra1.pmc)

print(product_graph.algebra2.pmc)
print(product_graph.algebra2.pmc.opp())
print(product_graph.algebra2.pmc.opp().opp())
#print(ddstr3.algebra1)
#print(ddstr3.algebra2)
#print(ddstr3.algebra2.opp())

product = aa.tensorDoubleDD(ddgraph3,product_graph)
product_graph = TypeDDGraph(product,2)
"""   
#from arc slide, compute DD stucture (left)
ddstr1 = slide1.getDDStructure()
ddgraph1 = TypeDDGraph(ddstr1,2)
print('ddgraph1:', ddgraph1.algebra2.opp())
print('tensorside1:', ddgraph1.tensor_side)

#from arc slide, compute DD stucture (right)
ddstr2 = slide2.getDDStructure()
ddgraph2 = TypeDDGraph(ddstr2,1)
print('ddgraph2:', ddgraph2.algebra1)
print('tensorside2:', ddgraph2.tensor_side)

aa = TypeAAGraph(Z)
product = aa.tensorDoubleDD(ddgraph1, ddgraph2)
product_graph = TypeDDGraph(product, 2)

def computeDoubleDDhelper(Y, ddgraph1, index):
    #Y: PMC
    #ddgraph1: DD structure on the left
    #index: tells us which pair of numbers in the array to use to generate the DD structure on the right
   
    if index < 28:
        slide = Arcslide(Y, pairs[index][0], pairs[index][1]).inverse()
    else:
        slide = Arcslide(Y, pairs[index][0], pairs[index][1])    
    ddstr2 = slide.getDDStructure()
    ddgraph2 = TypeDDGraph(ddstr2,1)
   
    aa = TypeAAGraph(Y)
    product = aa.tensorDoubleDD(ddgraph1, ddgraph2)
    product.simplify()
    result = TypeDDGraph(product, 2)
    return result.algebra2.opp().pmc, result

def computeDoubleDD(Y, ddgraph):
    #Y: PMC
    #ddgraph: leftmost DD structure
    counter = 0
    pmc, graph = Y, ddgraph
    for i in range (2,48):
        pmc, graph = computeDoubleDDhelper(pmc, graph, i)
        # i = i+1
        print('counter: ', i)
    return pmc, graph
    
pmc, graph = computeDoubleDD(product_graph.algebra2.opp().pmc, product_graph)
print(pmc)
"""