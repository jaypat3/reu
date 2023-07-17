from arcslide import *
from digraph import *
from dstructure import *
from ddstructure import *
from braid import *

# In[26]:

ddstr_list = []

#DD structure for T1
Z = PMC([(0,2),(1,3),(4,6),(5,7)])

slide1 = Arcslide(Z, 7, 6)
ddstr1 = slide1.getDDStructure()
ddgraph1 = TypeDDGraph(ddstr1, 1)

pairs1 = []
pairs1.append([7,6])
pairs1.append([7,6])
pairs1.append([7,6])
pairs1.append([7,6])
pairs1.append([7,6])
pairs1.append([7,6])

def computeT1helper(Y, ddgraph2, index, isInverse, ddstr_list):
    #Y: PMC
    #ddgraph1: DD structure on LHS 
    #ddgraph2: DD structure on RHS
    #index: tells us which pair of numbers in the array to use to generate the DD structure on LHS
    #isInverse: true if we're computing T1^-1; false if we're computing T1
    if isInverse == True:
        slide = Arcslide(Y, pairs1[index][0], pairs1[index][1]).inverse()
    else:
        slide = Arcslide(Y, pairs1[index][0], pairs1[index][1])
        
    ddstr1 = slide.getDDStructure()
    ddstr_list.append(ddstr1)
    ddgraph1 = TypeDDGraph(ddstr1, 2)
    
    aa = TypeAAGraph(Y)
    product = aa.tensorDoubleDD(ddgraph1, ddgraph2)
    product.simplify()
    result = TypeDDGraph(product, 1)
    return result.algebra1.pmc, result, product, ddstr_list

def computeT1(Y, ddgraph, isInverse, ddstr_list):
    #Y: PMC
    #ddgraph: rightmost DD structure
    #isInverse: true if we're computing T1^-1; false if we're computing T1
    pmc, graph= Y, ddgraph
    for i in range (1, 6):
        pmc, graph, prod, ddstr_list = computeT1helper(pmc, graph, i, isInverse, ddstr_list)
        print('counter: ', i)
        print(pmc)
    return pmc, graph, prod, ddstr_list

final_pmc1, final_ddgraph1, final_product1, ddstr_list = computeT1(Z, ddgraph1, False, ddstr_list)
print("final pmc: ", final_pmc1)


# In[27]:


#DD structure for T1 inverse

slide1 = Arcslide(Z, 7, 6).inverse()
ddstr1 = slide1.getDDStructure()
ddgraph1 = TypeDDGraph(ddstr1, 1)
print(ddstr1.algebra2.opp())

final_pmc1_inv, final_ddgraph1_inv, final_product1_inv, ddstr_list = computeT1(Z, ddgraph1, True, ddstr_list)


# In[4]:


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


# In[28]:


#DD structure for T2 - playing around with small cases

Z = PMC([(0,2),(1,3),(4,6),(5,7)])
W = PMC([(0, 3), (1, 6), (2, 4), (5, 7)])

#Here we create a list of PMC, to keep track of the PMC when we do the 14 arcslides. This will be useful when computing T2^-1
PMClist = []
PMClist.append(Z)
PMClist.append(W)
slide1 = Arcslide(Z, 4, 3)
ddstr1 = slide1.getDDStructure()
ddgraph1 = TypeDDGraph(ddstr1, 2)
print('ddstr1.algebra1:', ddstr1.algebra1)
print('ddstr1.algebra2.opp()', ddstr1.algebra2.opp())

"""
slide2 = Arcslide(W, 4, 5)
ddstr2 = slide2.getDDStructure()
ddgraph2 = TypeDDGraph(ddstr2, 1)
print('ddgraph2.algebra1', ddgraph2.algebra1)

aa = TypeAAGraph(W)
product1 = aa.tensorDoubleDD(ddgraph1, ddgraph2)
product1.simplify()
product1_graph = TypeDDGraph(product1, 2)
print('product1_graph.algebra2.opp()', product1_graph.algebra2.opp())

Y = product1_graph.algebra2.opp().pmc
slide3 = Arcslide(Y, 3, 4)
ddstr3 = slide3.getDDStructure()
ddgraph3 = TypeDDGraph(ddstr3, 1)
print('ddgraph3.algebra1', ddgraph3.algebra1)

aa1 = TypeAAGraph(Y)
product2 = aa1.tensorDoubleDD(product1_graph, ddgraph3)
product2.simplify()
product2_graph = TypeDDGraph(product2, 2)
print('product2_graph.algebra2.opp(): ', product2_graph.algebra2.opp())

X = product2_graph.algebra2.opp().pmc
slide4 = Arcslide(X, 2, 1)
ddstr4 = slide4.getDDStructure()
ddgraph4 = TypeDDGraph(ddstr4, 1)
print('ddgraph4.algebra1', ddgraph4.algebra1)

aa2 = TypeAAGraph(X)
product3 = aa2.tensorDoubleDD(product2_graph, ddgraph4)
product3.simplify()
product3_graph = TypeDDGraph(product3, 2)
"""

# In[30]:


#DD structure for T2

def computeT2helper(Y, ddgraph1, index, ddstr_list):
    #Y: PMC
    #ddgraph1: DD structure on LHS
    #ddgraph2: DD structure on RHS
    #index: tells us which pair of numbers in the array to use to generate the DD structure on LHS
    
    slide = Arcslide(Y, pairs2[index][0], pairs2[index][1])
    ddstr2 = slide.getDDStructure()
    ddstr_list.append(ddstr2)
    ddgraph2 = TypeDDGraph(ddstr2, 1)
    print('left dd structure PMC: ', ddgraph2.algebra1)
    print('right dd structure PMC: ', ddgraph1.algebra2.opp())
    
    aa = TypeAAGraph(Y)
    product = aa.tensorDoubleDD(ddgraph1, ddgraph2)
    product.simplify()
    result = TypeDDGraph(product, 2)
    return result.algebra2.opp().pmc, result, product, ddstr_list

def computeT2(Y, ddgraph, ddstr_list):
    #Y: PMC
    #ddgraph: leftmost DD structure
    pmc, graph= Y, ddgraph
    for i in range (1, 14):
        pmc, graph, prod, ddstr_list = computeT2helper(pmc, graph, i, ddstr_list)
        PMClist.append(pmc)
        print('counter: ', i)
        print(pmc)
    return pmc, graph, prod, ddstr_list


# In[31]:


pmc_final2, ddgraph_final2, product2_final, ddstr_list = computeT2(W, ddgraph1, ddstr_list)
print("final pmc: ", pmc_final2)


# In[33]:


#DD structure for T2^-1
#playing around with small cases

print("length:" , len(PMClist)) #There are 14 arcslides, 15 PMCs. Makes sense.
print(PMClist)
"""
slide1 = Arcslide(PMClist[13], 6, 5).inverse()
ddstr1 = slide1.getDDStructure()
ddgraph1 = TypeDDGraph(ddstr1, 2)
#print('ddstr1.algebra1:', ddstr1.algebra1)
print('ddstr1.algebra2.opp()', ddstr1.algebra2.opp())

slide2 = Arcslide(Z, 5, 4).inverse()
ddstr2 = slide2.getDDStructure()
ddgraph2 = TypeDDGraph(ddstr2, 1)
print('ddstr2.algebra1:', ddstr2.algebra1)

aa = TypeAAGraph(Z)
product = aa.tensorDoubleDD(ddgraph1, ddgraph2)
print(product.algebra2.opp())
print(product.algebra1)
#print('ddstr1.algebra2.opp()', ddstr2.algebra2.opp())

slide3 = Arcslide(Z, 4, 3).inverse()
ddstr3 = slide3.getDDStructure()
ddgraph3 = TypeDDGraph(ddstr3, 1)
print(ddgraph3.algebra1)
print(ddgraph3.algebra2.opp())

slide4 = Arcslide(PMClist[0], 4, 3).inverse()
ddstr_fin = slide4.getDDStructure()
print(ddstr_fin.algebra1)


slide5 = Arcslide(PMClist[1], 4, 5).inverse()
ddstr_fin2 = slide5.getDDStructure()
print(ddstr_fin2.algebra2.opp())
print(PMClist[1])
"""

# In[36]:


#DD structure for T2^-1

def computeT2helper_inv(ddgraph1, index, ddstr_list):
    #ddgraph1: DD structure on LHS
    #ddgraph2: DD structure on RHS
    #index: tells us which pair of numbers in the array to use to generate the DD structure on RHS
    
    #We use the stored PMCs in PMCList to generate the Arcslides, before inverting them
    slide = Arcslide(PMClist[13-index], pairs2[13-index][0], pairs2[13-index][1]).inverse()
    ddstr2 = slide.getDDStructure()
    ddstr_list.append(ddstr2)
    ddgraph2 = TypeDDGraph(ddstr2, 1)
    print('left dd structure PMC: ', ddgraph2.algebra1)
    print('right dd structure PMC: ', ddgraph1.algebra2.opp())
    
    
    aa = TypeAAGraph(PMClist[14-index])
    product = aa.tensorDoubleDD(ddgraph1, ddgraph2)
    product.simplify()
    result = TypeDDGraph(product, 2)
    return result.algebra2.opp().pmc, result, product, ddstr_list

def computeT2_inv(ddgraph, ddstr_list):
    #Y: PMC
    #ddgraph: leftmost DD structure
    graph= ddgraph
    for i in range (1, 14):
        pmc, graph, prod, ddstr_list = computeT2helper_inv(graph, i, ddstr_list)
        print('counter: ', i)
        print(pmc)
    return pmc, graph, prod, ddstr_list


# In[37]:


slide1 = Arcslide(PMClist[13], 6, 5).inverse()
ddstr1 = slide1.getDDStructure()
ddgraph1 = TypeDDGraph(ddstr1, 2)

pmc_final2_inv, ddgraph_final2_inv, product2_final_inv, ddstr_list = computeT2_inv(ddgraph1, ddstr_list)
print("final pmc: ", pmc_final2_inv)


# In[38]:


#T1
final_pmc1, final_ddgraph1, final_product1

#T1^-1
final_pmc1_inv, final_ddgraph1_inv, final_product1_inv

#T2
pmc_final2, ddgraph_final2, product2_final

#T2^-1
pmc_final2_inv, ddgraph_final2_inv, product2_final_inv

#T2*T2
aa = TypeAAGraph(Z)
graphT2_1 = TypeDDGraph(final_product1, 2)
graphT2_2 = TypeDDGraph(final_product1, 1)
productT2 = aa.tensorDoubleDD(graphT2_1, graphT2_2)
productT2.simplify()
productT2_graph = TypeDDGraph(productT2, 1)
print(productT2_graph.algebra1)
print(productT2_graph.algebra2.opp())

#test_minus_graph = TypeDDGraph(productT2,2)

# In[39]:


#T1^-1*T2*T2
graphT1_inv = TypeDDGraph(final_product1_inv, 2)
productT1T2 = aa.tensorDoubleDD(graphT1_inv, productT2_graph)
productT1T2.simplify()
productT1T2_graph = TypeDDGraph(productT1T2, 1)
print(productT1T2_graph.algebra1)
print(productT1T2_graph.algebra2.opp())

#graphT1_inv_test = TypeDDGraph(final_product1_inv,1)
#test = aa.tensorDoubleDD(test_minus_graph,graphT1_inv_test)
#test_graph = TypeDDGraph(test,2)


# In[40]:


#T2^-1*T1^-1*T2*T2
graphT2_inv = TypeDDGraph(product2_final_inv, 2)
productT2T1T2 = aa.tensorDoubleDD(graphT2_inv, productT1T2_graph)
productT2T1T2.simplify()
productT2T1T2_graph = TypeDDGraph(productT2T1T2, 2)
print(productT2T1T2_graph.algebra1)
print(productT2T1T2_graph.algebra2.opp())

#graphT2_inv_test = TypeDDGraph(product2_final_inv,1)
#test2 = aa.tensorDoubleDD(test_graph,graphT2_inv_test)
#test2_graph = TypeDDGraph(test2,2)


# In[41]:


#compute CFDhat(H^2, phi_2)
dstr = zeroTypeD(2)
dgraph = TypeDGraph(dstr)
print(dgraph.algebra)

#compute CFDhat(X_dr(L))
dstr_final = aa.tensorDDandD(productT2T1T2_graph, dgraph)
print(dstr_final.algebra)
# print(dstr_final.delta_map)
# print(dstr_final.generators)
dstr_final.simplify()
dstr_final.reindex()
print(dstr_final.delta_map)
print(dstr_final.generators)

#test_final = aa.tensorDDandD(test2_graph,dgraph)
#test_final.reindex()
#test_final.simplify()
#print(test_final.delta_map)
#print(test_final.generators)

#T2_inv:T1_inv:T2:T2
graphT2_inv = TypeDDGraph(product2_final_inv, 2)
graphT1_inv = TypeDDGraph(final_product1_inv, 1)
productT2_invT1_inv = aa.tensorDoubleDD(graphT2_inv,graphT1_inv)
productT2_invT1_inv.simplify()
productT2_invT1_inv_graph = TypeDDGraph(productT2_invT1_inv,2)
graphT2_1 = TypeDDGraph(product2_final,1)
productT2_invT1_invT2 = aa.tensorDoubleDD(productT2_invT1_inv_graph,graphT2_1)
productT2_invT1_invT2.simplify()
productT2_invT1_invT2_graph = TypeDDGraph(productT2_invT1_invT2,2)
graphT2_2 = TypeDDGraph(product2_final,1)
final = aa.tensorDoubleDD(productT2_invT1_invT2_graph,graphT2_2)
final.simplify()
final_graph = TypeDDGraph(final,2)
testfinal = aa.tensorDDandD(final_graph,dgraph)
print(testfinal.algebra)
testfinal.simplify()
testfinal.reindex()
print(testfinal.delta_map)
print(testfinal.generators)


##try composeDD with braid.py

ddstr_list = []


PMClist = []
PMClist.append(Z)
PMClist.append(W)
slide1 = Arcslide(Z, 4, 3)
ddstr1 = slide1.getDDStructure()
ddstr_list.append(ddstr1)
ddgraph1 = TypeDDGraph(ddstr1, 2)
print('ddstr1.algebra1:', ddstr1.algebra1)
print('ddstr1.algebra2.opp()', ddstr1.algebra2.opp())
pmc_final2, ddgraph_final2, product2_final, ddstr_list = computeT2(W, ddgraph1, ddstr_list)

"""
PMClist = []
PMClist.append(Z)
PMClist.append(W)
slide1 = Arcslide(Z, 4, 3)
ddstr1 = slide1.getDDStructure()
ddstr_list.append(ddstr1)
ddgraph1 = TypeDDGraph(ddstr1, 2)
print('ddstr1.algebra1:', ddstr1.algebra1)
print('ddstr1.algebra2.opp()', ddstr1.algebra2.opp())
pmc_final2, ddgraph_final2, product2_final, ddstr_list = computeT2(W, ddgraph1, ddstr_list)
"""

slide1 = Arcslide(Z, 7, 6).inverse()
ddstr1 = slide1.getDDStructure()
ddstr_list.append(ddstr1)
ddgraph1 = TypeDDGraph(ddstr1, 1)
# print(ddstr1.algebra2.opp())

final_pmc1_inv, final_ddgraph1_inv, final_product1_inv, ddstr_list = computeT1(Z, ddgraph1, True, ddstr_list)

slide1 = Arcslide(PMClist[13], 6, 5).inverse()
ddstr1 = slide1.getDDStructure()
ddstr_list.append(ddstr1)
ddgraph1 = TypeDDGraph(ddstr1, 2)

pmc_final2_inv, ddgraph_final2_inv, product2_final_inv, ddstr_list = computeT2_inv(ddgraph1, ddstr_list)
print("final pmc: ", pmc_final2_inv)

print("final length: ", len(ddstr_list))

newlist = []
for i in range(0,len(ddstr_list)):
    newlist.append(ddstr_list[len(ddstr_list)-1-i])


final_dstr = composeDD(dstr,newlist, is_dual = False, method = "Tensor")

final_dstr.simplify()
final_dstr.reindex()
print(final_dstr.delta_map)
print(final_dstr.generators)
print(final_dstr)

print("NEW SECTION")

enddstr = DDStrFromDStr(final_dstr,1)

print(enddstr.delta_map)
print(enddstr.generators)

#enddstr = DDStrFromDStr(dstr_final,1)

#print(enddstr.delta_map)
#print(len(enddstr.generators))

#enddstr = DDStrFromDStr(testfinal,1)

#print(enddstr.delta_map)
#print(enddstr.generators)
#print(len(enddstr.generators))
# %%
