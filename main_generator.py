from arcslide import *
from digraph import *
from dstructure import *
from ddstructure import *
from braid import *

#manually calculated Arcslides
Z = PMC([(0,2),(1,3), (4,6) ,(5,7)])
W = PMC([(0, 3), (1, 6), (2, 4),  (5, 7)])

#T1
Slide1 = Arcslide(Z, 4, 5)
Slide2 = Arcslide(Z, 4, 5)
Slide3 = Arcslide(Z, 4, 5)
Slide4 = Arcslide(Z, 4, 5)
Slide5 = Arcslide(Z, 4, 5)
Slide6 = Arcslide(Z, 4, 5)

slides_T1 = []
slides_T1.append(Slide1)
slides_T1.append(Slide2)
slides_T1.append(Slide3)
slides_T1.append(Slide4)
slides_T1.append(Slide5)
slides_T1.append(Slide6)

ddstr_list_T1 = []
for slide in slides_T1:
    ddstr_list_T1.append(slide.getDDStructure())
print(len(ddstr_list_T1))

#T1^-1
Slide7 = Arcslide(Z, 7, 6)
Slide8 = Arcslide(Z, 7, 6)
Slide9 = Arcslide(Z, 7, 6)
Slide10 = Arcslide(Z, 7, 6)
Slide11 = Arcslide(Z, 7, 6)
Slide12 = Arcslide(Z, 7, 6)
slides_T1inv = []
slides_T1inv.append(Slide7)
slides_T1inv.append(Slide8)
slides_T1inv.append(Slide9)
slides_T1inv.append(Slide10)
slides_T1inv.append(Slide11)
slides_T1inv.append(Slide12)

ddstr_list_T1inv = []
for slide in slides_T1inv:
    ddstr_list_T1inv.append(slide.getDDStructure())
print(len(ddstr_list_T1inv))

#T1^-1 ONE HALF
Slide1 = Arcslide(Z, 7, 6)
Slide2 = Arcslide(Z, 7, 6)
Slide3 = Arcslide(Z, 7, 6)
slides_T1invhalf = []
slides_T1invhalf.append(Slide1)
slides_T1invhalf.append(Slide2)
slides_T1invhalf.append(Slide3)

ddstr_list_T1invhalf = []
for slide in slides_T1invhalf:
    ddstr_list_T1invhalf.append(slide.getDDStructure())
print(len(ddstr_list_T1invhalf))


#T2
slide1 = Arcslide(W, 1, 2)
slide2 = Arcslide(PMC([(0, 3), (1, 5), (2, 7), (4, 6)]), 7, 6)
slide3 = Arcslide(PMC([(0, 6), (1, 4), (2, 7), (3, 5)]), 6, 5)
slide4 = Arcslide(PMC([(0, 6), (1, 4), (2, 5), (3, 7)]), 3, 4)
slide5 = Arcslide(PMC([(0, 6), (1, 3), (2, 5), (4, 7)]), 4, 5)
slide6 = Arcslide(PMC([(0, 6), (1, 7), (2, 4), (3, 5)]), 1, 2)
slide7 = Arcslide(PMC([(0, 3), (1, 7), (2, 5), (4, 6)]), 3, 4)
slide8 = Arcslide(PMC([(0, 4), (1, 7), (2, 5), (3, 6)]), 4, 5)
slide9 = Arcslide(PMC([(0, 5), (1, 7), (2, 4), (3, 6)]), 5, 6)
slide10 = Arcslide(PMC([(0, 2), (1, 7), (3, 5), (4, 6)]), 2, 3)
slide11 = Arcslide(PMC([(0, 2), (1, 4), (3, 6), (5, 7)]), 4, 5)
slide12 = Arcslide(PMC([(0, 2), (1, 5), (3, 6), (4, 7)]), 5, 6)
slide13 = Arcslide(PMC([(0, 2), (1, 6), (3, 5), (4, 7)]), 6, 7)
slide14 = Arcslide(PMC([(0, 2), (1, 3), (4, 6), (5, 7)]), 3, 4)
slides_T2 = []
slides_T2.append(slide1)
slides_T2.append(slide2)
slides_T2.append(slide3)
slides_T2.append(slide4)
slides_T2.append(slide5)
slides_T2.append(slide6)
slides_T2.append(slide7)
slides_T2.append(slide8)
slides_T2.append(slide9)
slides_T2.append(slide10)
slides_T2.append(slide11)
slides_T2.append(slide12)
slides_T2.append(slide13)
slides_T2.append(slide14)

ddstr_list_T2 = []
for slide in slides_T2:
    ddstr_list_T2.append(slide.getDDStructure())
print(len(ddstr_list_T2))

#T2^-1
slide15 = Arcslide(PMC([(0, 2), (1, 6), (3, 5), (4, 7)]), 6, 5)
slide16 = Arcslide(PMC([(0, 2), (1, 5), (3, 6), (4, 7)]), 5, 4)
slide17 = Arcslide(PMC([(0, 2), (1, 4), (3, 6), (5, 7)]), 4, 3)
slide18 = Arcslide(PMC([(0, 2), (1, 7), (3, 5), (4, 6)]), 7, 6)
slide19 = Arcslide(PMC([(0, 5), (1, 7), (2, 4), (3, 6)]), 5, 4)
slide20 = Arcslide(PMC([(0, 4), (1, 7), (2, 5), (3, 6)]), 4, 3)
slide21 = Arcslide(PMC([(0, 3), (1, 7), (2, 5), (4, 6)]), 3, 2)
slide22 = Arcslide(PMC([(0, 6), (1, 7), (2, 4), (3, 5)]), 6, 5)
slide23 = Arcslide(PMC([(0, 6), (1, 3), (2, 5), (4, 7)]), 4, 3)
slide24 = Arcslide(PMC([(0, 6), (1, 4), (2, 5), (3, 7)]), 3, 2)
slide25 = Arcslide(PMC([(0, 6), (1, 4), (2, 7), (3, 5)]), 2, 1)
slide26 = Arcslide(PMC([(0, 3), (1, 5), (2, 7), (4, 6)]), 3, 4)
slide27 = Arcslide(PMC([(0, 3), (1, 6), (2, 4), (5, 7)]), 4, 5)
slide28 = Arcslide(Z, 4, 3)

slides_T2inv = []
slides_T2inv.append(slide15)
slides_T2inv.append(slide16)
slides_T2inv.append(slide17)
slides_T2inv.append(slide18)
slides_T2inv.append(slide19)
slides_T2inv.append(slide20)
slides_T2inv.append(slide21)
slides_T2inv.append(slide22)
slides_T2inv.append(slide23)
slides_T2inv.append(slide24)
slides_T2inv.append(slide25)
slides_T2inv.append(slide26)
slides_T2inv.append(slide27)
slides_T2inv.append(slide28)

ddstr_list_T2inv = []
for slide in slides_T2inv:
    ddstr_list_T2inv.append(slide.getDDStructure())
print(len(ddstr_list_T2inv))

# ddstr_list = ddstr_list_T2 + ddstr_list_T2 + ddstr_list_T1inv + ddstr_list_T2inv
# ddstr_list = ddstr_list_T2 + ddstr_list_T2 + ddstr_list_T2 + ddstr_list_T2 + ddstr_list_T1inv + ddstr_list_T2inv + ddstr_list_T2inv + ddstr_list_T2inv
ddstr_list = ddstr_list_T2 + ddstr_list_T2 + ddstr_list_T1inv + ddstr_list_T2inv
#this is CFDhat(H^2, phi_2)
dstr = zeroTypeD(2)
"""
#running some tests
ddstr_list_test1 = ddstr_list_T2 + ddstr_list_T2inv
ddstr_list_test2 = ddstr_list_T2inv + ddstr_list_T2
ddstr_list_test3 = ddstr_list_T1 + ddstr_list_T1inv
ddstr_list_test4 = ddstr_list_T1inv + ddstr_list_T1

dstr_test1 = composeDD(dstr, ddstr_list_test1, is_dual = False, method = "Tensor")
dstr_test2 = composeDD(dstr, ddstr_list_test2, is_dual = False, method = "Tensor")
dstr_test3 = composeDD(dstr, ddstr_list_test3, is_dual = False, method = "Tensor")
dstr_test4 = composeDD(dstr, ddstr_list_test4, is_dual = False, method = "Tensor")

print('test1:', dstr_test1.compareDStructures(dstr))
print('test2:', dstr_test2.compareDStructures(dstr))
print('test3:', dstr_test3.compareDStructures(dstr))
print('test4:', dstr_test4.compareDStructures(dstr))
"""
#this gives us CFD hat of the drilled manifold
final_dstr = composeDD(dstr, ddstr_list, is_dual = False, method = "Tensor")
final_dstr.simplify()
final_dstr.reindex()
print(final_dstr)

ddstr = DDStrFromDStr(final_dstr, 1)
"""
#I copied down the code for the DStrtoDDStr method
genus1 = 1
pmc_all = final_dstr.algebra.pmc
pmc1, pmc2 = unconnectSumPMC(pmc_all, genus1)
mult_one = final_dstr.algebra.mult_one

ddstr = SimpleDDStructure(F2, pmc1.getAlgebra(mult_one = mult_one), pmc2.getAlgebra(mult_one = mult_one))
gen_map = {}
for x in final_dstr.getGenerators():
    # Split idempotent of x into two parts
    xidem = x.idem
    x1_idem = Idempotent(pmc1,[pairid for pairid in xidem if pairid < 2*genus1])
    x2_idem = Idempotent(pmc2,[pairid-2*genus1 for pairid in xidem if pairid >= 2*genus1])
    if len(x1_idem) != genus1:
        continue
    gen_map[x] = SimpleDDGenerator(ddstr, x1_idem, x2_idem, x.name)
    ddstr.addGenerator(gen_map[x])

cut_point = 4 * genus1
for x in final_dstr.getGenerators():
    for (a, y), coeff in list(x.delta().items()):
        print('cut point', a.multiplicity[cut_point-1], y)
        if a.multiplicity[cut_point-1] == 0:
            # The interval (cut_point-1, cut_point) is unoccupied
            a1, a2 = unconnectSumStrandDiagram(a, genus1)
            print(x)
            print(a, y)
            print(a1, a2)
            print(str(a1), str(a2))
            if str(a1) !='[]' and str(a2) != '[]': #Here I added a check to make sure we don't get keyErrors
                ddstr.addDelta(gen_map[x], gen_map[y], a1, a2, coeff)
            else:
                print('not happen')
print(ddstr)
"""

ddstr.simplify()
ddstr.reindex()
dd_printed = str(ddstr)[19: ]
print(dd_printed)
