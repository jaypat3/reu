from arcslide import *
from algebra import DGAlgebra, FreeModule, Generator, SimpleChainComplex, \
    Tensor, TensorGenerator, TensorDGAlgebra
from dstructure import zeroTypeD
from ddstructure import identityDD, SimpleDDStructure
from digraph import *


# test = Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).getDDStructure()

arr = []
arr.append(zeroTypeD(2))
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,5).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),3,4).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),2,1).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),3,2).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),6,5).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),3,2).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),5,4).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),7,6).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),5,4).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),6,5).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,5).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),3,4).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),2,1).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),3,2).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),6,5).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),3,2).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),5,4).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),7,6).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),5,4).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),6,5).getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),7,6).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),7,6).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),7,6).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),7,6).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),7,6).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),7,6).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),6,5).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),5,4).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),7,6).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),5,4).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),3,2).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),6,5).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),3,2).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),2,1).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),3,4).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,5).inverse().getDDStructure())
arr.append(Arcslide(PMC([(0,2),(1,3),(4,6),(5,7)]),4,3).inverse().getDDStructure())

# for i in range(0,len(arr)-2):
# dstr = aa_graph.tensorDDandD(TypeDDGraph(arr[1],2),TypeDGraph(arr[0]))
# aa_graph = getTypeAAGraph(dstr.algebra.pmc)

"""
newstr = aa_graph.tensorDDandD(TypeDDGraph(arr[len(arr)-1],2),TypeDGraph(arr[0]))
print(newstr.algebra)
print(TypeDDGraph(arr[1],2).algebra1)
print(TypeDDGraph(arr[1],2).algebra2)
print(TypeDDGraph(arr[len(arr)-2],2).algebra1)
print(TypeDDGraph(arr[len(arr)-2],2).algebra2)
new_graph = getTypeAAGraph(pmc=newstr.algebra.pmc)
newstr = aa_graph.tensorDDandD(TypeDDGraph(arr[len(arr)-2],2),TypeDGraph(newstr))
"""
# computeDATensorD(TypeDDGraph(arr[1],2),TypeDGraph(arr[0]))

# print(TypeDDGraph(arr[len(arr)-1],2).algebra1)
# print(TypeDDGraph(arr[len(arr)-1],2).algebra2)
# print(TypeDGraph(arr[0]).algebra)
# print(aa_graph.pmc_alg)

final_structure = zeroTypeD(2)
aa_graph = getTypeAAGraph(pmc=PMC([(0,2),(1,3),(4,6),(5,7)]))


