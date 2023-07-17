from arcslide import *
from digraph import *
from dstructure import *
from ddstructure import *
from braid import *

Z = PMC([(0,2),(1,3),(4,6),(5,7)])
W = PMC([(0, 3), (1, 6), (2, 4), (5, 7)])
ddstr_list = [] #my first attempt to caluclate using computeDD. This list should hold four DD structures: T2, T2, T1^-1, T2^-1
#ddstr_list2 = [] #my second attempt to calculate using computeDD. This list should hold 54 DD structures given by the 54 arcslides

#DD structure for T1

pairs1 = []
pairs1.append([7,6])
pairs1.append([7,6])
pairs1.append([7,6])
pairs1.append([7,6])
pairs1.append([7,6])
pairs1.append([7,6])

def computeT1helper(Y, ddstr2, index, isInverse):
    #Y: PMC
    #ddstr1: DD structure on LHS
    #ddstr2: DD structure on RHS
    #index: tells us which pair of numbers in the array to use to generate the DD structure on LHS
    #isInverse: true if we're computing T1^-1; false if we're computing T1
    if isInverse == True:
        slide = Arcslide(Y, pairs1[index][0], pairs1[index][1]).inverse()
    else:
        slide = Arcslide(Y, pairs1[index][0], pairs1[index][1])
       
    ddstr1 = slide.getDDStructure()
    #ddgraph1 = TypeDDGraph(ddstr1, 2)
   
    #aa = TypeAAGraph(Y)
    product = computeDATensorDD(ddstr1, ddstr2)
    product.simplify()
    product.reindex()
    #result = TypeDDGraph(product, 1)
    return product.algebra1.pmc, product

def computeT1(Y, ddstr2, isInverse):
    #Y: PMC
    #ddgraph: rightmost DD structure
    #isInverse: true if we're computing T1^-1; false if we're computing T1
    pmc, prod = Y, ddstr2
    for i in range (1, 6):
        pmc, prod = computeT1helper(pmc, prod, i, isInverse)
        #ddstr_list2.append(prod)
        print('counter: ', i)
        print(pmc)
    return pmc, prod

slide1 = Arcslide(Z, 7, 6)
ddstr1 = slide1.getDDStructure()
ddstr1.simplify()
#ddgraph1 = TypeDDGraph(ddstr1, 1)

final_pmc1, final_product1= computeT1(Z, ddstr1, False)
print("final pmc: ", final_pmc1)

#DD structure for T1 inverse

slide1 = Arcslide(Z, 7, 6).inverse()
ddstr1 = slide1.getDDStructure()
#ddstr1.simplify()

#ddgraph1 = TypeDDGraph(ddstr1, 1)
#print(ddstr1.algebra2.opp())

#ddstr_list2.append(ddstr1)

final_pmc1_inv, final_product1_inv = computeT1(Z, ddstr1, True)

#print(len(ddstr_list2))

#DD structure for T2
pairs2 = []
pairs2.append([4,3])
pairs2.append([4,5])
pairs2.append([3,4])
pairs2.append([2,1])
pairs2.append([3,2])
pairs2.append([4,3])
pairs2.append([6,5])
pairs2.append([3,2])
pairs2.append([4,3])
pairs2.append([5,4])
pairs2.append([7,6])
pairs2.append([4,3])
pairs2.append([5,4])
pairs2.append([6,5])
print(pairs2)

#DD structure for T2

def computeT2helper(Y, ddstr1, index):
    #Y: PMC
    #ddstr1: DD structure on LHS
    #ddstr2: DD structure on RHS
    #index: tells us which pair of numbers in the array to use to generate the DD structure on LHS
   
    slide = Arcslide(Y, pairs2[index][0], pairs2[index][1])
    ddstr2 = slide.getDDStructure()
       
    #ddgraph2 = TypeDDGraph(ddstr2, 1)
    #print('left dd structure PMC: ', ddgraph2.algebra1)
    #print('right dd structure PMC: ', ddgraph1.algebra2.opp())
   
    #aa = TypeAAGraph(Y)
    product = computeDATensorDD(ddstr1, ddstr2)
    product.simplify()
    product.reindex()
    #result = TypeDDGraph(product, 2)
    return product.algebra2.opp().pmc, product

def computeT2(Y, ddstr1):
    #Y: PMC
    #ddstr1: leftmost DD structure
    pmc, prod= Y, ddstr1
    for i in range (1, 14):
        pmc, prod = computeT2helper(pmc, prod, i)
        #ddstr_list2.append(prod)
        PMClist.append(pmc)
        print('counter: ', i)
        print(pmc)
    return pmc, prod

PMClist = []
PMClist.append(Z)
PMClist.append(W)
slide1 = Arcslide(Z, 4, 3)
ddstr1 = slide1.getDDStructure()
#ddstr1.simplify()


pmc_final2, product2_final = computeT2(W, ddstr1)
print("final pmc: ", pmc_final2)

#ddstr_list2.reverse()
#print(len(ddstr_list2))

print(len(PMClist)) #There are 14 arcslides, 15 PMCs. Makes sense.
print(PMClist)

#DD structure for T2^-1
#helper_list = []

def computeT2helper_inv(ddstr1, index):
    #ddstr1: DD structure on LHS
    #ddstr2: DD structure on RHS
    #index: tells us which pair of numbers in the array to use to generate the DD structure on RHS
   
    #We use the stored PMCs in PMCList to generate the Arcslides, before inverting them
    slide = Arcslide(PMClist[13-index], pairs2[13-index][0], pairs2[13-index][1]).inverse()
    ddstr2 = slide.getDDStructure()
    #ddstr2.simplify()
    #ddstr_list.append(ddstr2)
    #ddgraph2 = TypeDDGraph(ddstr2, 1)
    #print('left dd structure PMC: ', ddgraph2.algebra1)
    #print('right dd structure PMC: ', ddgraph1.algebra2.opp())
   
   
    #aa = TypeAAGraph(PMClist[14-index])
    product = computeDATensorDD(ddstr1, ddstr2)
    product.simplify()
    product.reindex()
    #result = TypeDDGraph(product, 2)
    return product.algebra2.opp().pmc, product

def computeT2_inv(ddstr1):
    #Y: PMC
    #ddstr1: leftmost DD structure
    prod = ddstr1
    for i in range (1, 14):
        pmc, prod = computeT2helper_inv(prod, i)
        #helper_list.append(prod)
        print('counter: ', i)
        print(pmc)
    return pmc, prod


slide1 = Arcslide(PMClist[13], 6, 5).inverse()
ddstr1 = slide1.getDDStructure()
#ddstr1.simplify()
#helper_list.append(ddstr1)
#ddgraph1 = TypeDDGraph(ddstr1, 2)

pmc_final2_inv, product2_final_inv = computeT2_inv(ddstr1)
print("final pmc: ", pmc_final2_inv)

#T1
final_pmc1, final_product1
#final_product1.simplify()

#T1^-1
final_pmc1_inv, final_product1_inv
#final_product1_inv.simplify()

#T2
pmc_final2, product2_final
#product2_final.simplify()

#T2^-1
pmc_final2_inv, product2_final_inv
#product2_final_inv.simplify()

# ddstr_list.append(product2_final)
# ddstr_list.append(product2_final_inv)
ddstr_list.append(product2_final_inv)
ddstr_list.append(product2_final_inv)
ddstr_list.append(product2_final_inv)
ddstr_list.append(product2_final_inv)
ddstr_list.append(final_product1)
ddstr_list.append(product2_final)
# ddstr_list.append(product2_final)
# ddstr_list.append(product2_final)
# ddstr_list.reverse()

# newlist = []
# for i in range(0,len(ddstr_list)):
    # newlist.append(ddstr_list[len(ddstr_list)-1-i])

"""
#T2*T2
aa = TypeAAGraph(Z)
graphT2_1 = TypeDDGraph(final_product1, 2)
graphT2_2 = TypeDDGraph(final_product1, 1)
productT2 = aa.tensorDoubleDD(graphT2_1, graphT2_2)
productT2.simplify()
productT2_graph = TypeDDGraph(productT2, 1)
print(productT2_graph.algebra1)
print(productT2_graph.algebra2.opp())
"""
dstr = zeroTypeD(2)
dgraph = TypeDGraph(dstr)

print("LEN DDSTR_LIST: ", len(ddstr_list))

final_dstr = composeDD(dstr, ddstr_list, is_dual = False, method = "Tensor")


# final_dstr.simplify()
# final_dstr.reindex()


print(final_dstr)

"""
print(final_dstr.delta_map)
print(final_dstr.generators)
"""

dd = DDStrFromDStr(final_dstr, 1)
dd.simplify()
dd.reindex()

print(dd)

