from arcslide import *
from digraph import *
from dstructure import *
from ddstructure import *

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
# print("opposite: ", Z.opp())

#writing out all the arcslides for the first two DD structures
slide1 = Arcslide(Z, pairs[0][0], pairs[0][1])

#from arc slide, compute DD stucture (left)
ddstr1 = slide1.getDDStructure()
ddgraph1 = TypeDDGraph(ddstr1,2)
print('ddgraph1:', ddgraph1.algebra2.opp())
print('tensorside1:', ddgraph1.tensor_side)

aa = TypeAAGraph(Z)

#compute CFDhat(H^2, phi_2)
dstr_start = zeroTypeD(2)
dgraph_start = TypeDGraph(dstr_start)
# print(dgraph_start.algebra)

product = aa.tensorDDandD(ddgraph1, dgraph_start)
product_graph = TypeDGraph(product)

Y = product_graph.algebra.pmc

# slide2 = Arcslide(Y, pairs[0][0], pairs[0][1]).inverse()
# ddstr2 = slide2.getDDStructure()
# ddgraph2 = TypeDDGraph(ddstr2,2)
# print('ddgraph2:', ddgraph2.algebra2.opp())
# print('tensorside2:', ddgraph2.tensor_side)

# aa = TypeAAGraph(Y)
# product2 = aa.tensorDDandD(ddgraph2, product_graph)
# product_graph2 = TypeDGraph(product2)
# print(product_graph2.algebra)

def computeDDandDhelper(Y, dgraph, index):
    #Y: PMC
    #dgraph: D structure on the right
    #index: tells us which pair of numbers in the array to use to generate the DD structure on the left
    # print(Arcslide(Y, pairs[index][0], pairs[index][1]))
    # print(Arcslide(Y, pairs[index][0], pairs[index][1]).inverse())
    if index < 28:
        slide = Arcslide(Y, pairs[index][0], pairs[index][1]).inverse()
    else:
        slide = Arcslide(Y, pairs[index][0], pairs[index][1])
    ddstr = slide.getDDStructure()
    ddgraph = TypeDDGraph(ddstr,2)
   
    aa = TypeAAGraph(Y)
    product = aa.tensorDDandD(ddgraph, dgraph)
    product.simplify()
    result = TypeDGraph(product)
    print(result.algebra.pmc)
    # print(ddgraph.algebra1)
    # print(ddgraph.algebra2)
    return result.algebra.pmc, result, product

def computeDoubleDD(Y, dgraph):
    #Y: PMC
    #ddgraph: rightmost D structure
    pmc, graph = Y, dgraph
    for i in range (0,48):
        pmc, graph, product = computeDDandDhelper(pmc, graph, i)
        print('counter: ', i)
    return pmc, graph, product
    
pmc_final, dgraph_final, final_product = computeDoubleDD(Z, dgraph_start)
print(pmc_final)

final = DDStrFromDStr(final_product,2)

print(final)