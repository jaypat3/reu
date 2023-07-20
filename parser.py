def find_algebra_element(decomp,index):
    if decomp == '[(0, 2)]' or decomp == '[(1, 3)]' or decomp == ' [(0, 2)]' or decomp == ' [(1,3)]' or decomp == ' ':
        return ''
    if index == 1:
        if decomp == '[0->1]' or decomp == ' [0->1]':
            return 'p1*'
        if decomp == '[1->2]' or decomp == ' [1->2]':
            return 'p2*'
        if decomp == '[2->3]' or decomp == ' [2->3]':
            return 'p3*'
        if decomp == '[0->2]' or decomp == ' [0->2]':
            return 'p12*'
        if decomp == '[1->3]' or decomp == ' [1->3]':
            return 'p23*'
        if decomp == '[0->3]' or decomp == ' [0->3]':
            return 'p123*'
    if index == 2:
        if decomp == '[0->1]' or decomp == ' [0->1]':
            return 's1*'
        if decomp == '[1->2]' or decomp == ' [1->2]':
            return 's2*'
        if decomp == '[2->3]' or decomp == ' [2->3]':
            return 's3*'
        if decomp == '[0->2]' or decomp == ' [0->2]':
            return 's12*'
        if decomp == '[1->3]' or decomp == ' [1->3]':
            return 's23*'
        if decomp == '[0->3]' or decomp == ' [0->3]':
            return 's123*'


str1 = """d(g1:((1, 3)),((0, 2))) = [(1, 3)]**[0->1]**g2:((1, 3)),((1, 3))
d(g2:((1, 3)),((1, 3))) = 0
d(g3:((0, 2)),((1, 3))) = [(0, 2)]**[1->2]**g40:((0, 2)),((0, 2))+[2->3]**[(1, 3)]**g35:((1, 3)),((1, 3))+[0->3]**[1->2]**g6:((1, 3)),((0, 2))
d(g4:((0, 2)),((0, 2))) = [2->3]**[(0, 2)]**g28:((1, 3)),((0, 2))+[(0, 2)]**[2->3]**g3:((0, 2)),((1, 3))+[0->3]**[0->3]**g36:((1, 3)),((1, 3))
d(g5:((0, 2)),((0, 2))) = [2->3]**[(0, 2)]**g24:((1, 3)),((0, 2))+[0->3]**[0->1]**g19:((1, 3)),((1, 3))+[0->1]**[2->3]**g34:((1, 3)),((1, 3))
d(g6:((1, 3)),((0, 2))) = [(1, 3)]**[0->1]**g36:((1, 3)),((1, 3))+[(1, 3)]**[2->3]**g34:((1, 3)),((1, 3))+[(1, 3)]**[0->3]**g2:((1, 3)),((1, 3))
d(g7:((0, 2)),((0, 2))) = [0->1]**[2->3]**g19:((1, 3)),((1, 3))+[0->1]**[2->3]**g29:((1, 3)),((1, 3))+[0->3]**[0->3]**g29:((1, 3)),((1, 3))+[2->3]**[0->1]**g29:((1, 3)),((1, 3))+[0->2]**[2->3]**g12:((0, 2)),((1, 3))+[2->3]**[(0, 2)]**g30:((1, 3)),((0, 2))
d(g8:((0, 2)),((0, 2))) = [0->3]**[0->2]**g15:((1, 3)),((0, 2))+[0->1]**[0->3]**g29:((1, 3)),((1, 3))+[0->3]**[0->1]**g25:((1, 3)),((1, 3))
d(g9:((0, 2)),((0, 2))) = [2->3]**[0->1]**g29:((1, 3)),((1, 3))+[0->3]**[0->3]**g29:((1, 3)),((1, 3))+[(0, 2)]**[2->3]**g10:((0, 2)),((1, 3))+[0->3]**[0->3]**g19:((1, 3)),((1, 3))
d(g10:((0, 2)),((1, 3))) = [(0, 2)]**[1->2]**g14:((0, 2)),((0, 2))+[0->2]**[1->2]**g9:((0, 2)),((0, 2))
d(g11:((1, 3)),((1, 3))) = [1->2]**[(1, 3)]**g26:((0, 2)),((1, 3))
d(g12:((0, 2)),((1, 3))) = [(0, 2)]**[1->2]**g21:((0, 2)),((0, 2))+[2->3]**[(1, 3)]**g38:((1, 3)),((1, 3))
d(g13:((1, 3)),((1, 3))) = [(1, 3)]**[1->2]**g24:((1, 3)),((0, 2))+[1->2]**[(1, 3)]**g20:((0, 2)),((1, 3))
d(g14:((0, 2)),((0, 2))) = [0->1]**[0->3]**g2:((1, 3)),((1, 3))+[0->3]**[0->1]**g19:((1, 3)),((1, 3))+[0->2]**[2->3]**g10:((0, 2)),((1, 3))
d(g15:((1, 3)),((0, 2))) = [(1, 3)]**[2->3]**g38:((1, 3)),((1, 3))+[1->3]**[0->3]**g38:((1, 3)),((1, 3))+[1->2]**[(0, 2)]**g18:((0, 2)),((0, 2))+[1->2]**[0->3]**g39:((0, 2)),((1, 3))
d(g16:((0, 2)),((0, 2))) = [(0, 2)]**[2->3]**g20:((0, 2)),((1, 3))+[0->3]**[0->1]**g25:((1, 3)),((1, 3))+[2->3]**[0->1]**g11:((1, 3)),((1, 3))
d(g17:((0, 2)),((1, 3))) = [(0, 2)]**[1->2]**g8:((0, 2)),((0, 2))
d(g18:((0, 2)),((0, 2))) = [(0, 2)]**[2->3]**g17:((0, 2)),((1, 3))+[0->3]**[0->3]**g25:((1, 3)),((1, 3))+[2->3]**[0->3]**g11:((1, 3)),((1, 3))
d(g19:((1, 3)),((1, 3))) = 0
d(g20:((0, 2)),((1, 3))) = [(0, 2)]**[1->2]**g22:((0, 2)),((0, 2))
d(g21:((0, 2)),((0, 2))) = [2->3]**[(0, 2)]**g30:((1, 3)),((0, 2))+[0->1]**[0->3]**g36:((1, 3)),((1, 3))+[0->3]**[0->1]**g32:((1, 3)),((1, 3))
d(g22:((0, 2)),((0, 2))) = [0->1]**[0->1]**g19:((1, 3)),((1, 3))
d(g23:((1, 3)),((0, 2))) = [(1, 3)]**[2->3]**g13:((1, 3)),((1, 3))+[1->2]**[(0, 2)]**g16:((0, 2)),((0, 2))+[1->2]**[0->1]**g39:((0, 2)),((1, 3))
d(g24:((1, 3)),((0, 2))) = [1->2]**[(0, 2)]**g22:((0, 2)),((0, 2))
d(g25:((1, 3)),((1, 3))) = 0
d(g26:((0, 2)),((1, 3))) = [0->1]**[(1, 3)]**g25:((1, 3)),((1, 3))
d(g27:((0, 2)),((0, 2))) = [2->3]**[(0, 2)]**g15:((1, 3)),((0, 2))+[(0, 2)]**[2->3]**g12:((0, 2)),((1, 3))+[0->3]**[0->3]**g32:((1, 3)),((1, 3))
d(g28:((1, 3)),((0, 2))) = [1->2]**[(0, 2)]**g21:((0, 2)),((0, 2))+[1->2]**[(0, 2)]**g7:((0, 2)),((0, 2))+[1->2]**[(0, 2)]**g9:((0, 2)),((0, 2))+[(1, 3)]**[2->3]**g35:((1, 3)),((1, 3))
d(g29:((1, 3)),((1, 3))) = [1->2]**[1->2]**g7:((0, 2)),((0, 2))+[1->3]**[(1, 3)]**g38:((1, 3)),((1, 3))
d(g30:((1, 3)),((0, 2))) = [1->2]**[(0, 2)]**g8:((0, 2)),((0, 2))+[1->2]**[0->2]**g7:((0, 2)),((0, 2))+[1->3]**[0->1]**g38:((1, 3)),((1, 3))
d(g31:((0, 2)),((1, 3))) = [(0, 2)]**[1->2]**g5:((0, 2)),((0, 2))+[2->3]**[(1, 3)]**g13:((1, 3)),((1, 3))+[0->1]**[1->2]**g6:((1, 3)),((0, 2))
d(g32:((1, 3)),((1, 3))) = 0
d(g33:((1, 3)),((0, 2))) = [1->2]**[(0, 2)]**g14:((0, 2)),((0, 2))
d(g34:((1, 3)),((1, 3))) = [(1, 3)]**[1->2]**g1:((1, 3)),((0, 2))
d(g35:((1, 3)),((1, 3))) = [(1, 3)]**[1->2]**g33:((1, 3)),((0, 2))+[1->2]**[(1, 3)]**g10:((0, 2)),((1, 3))
d(g36:((1, 3)),((1, 3))) = 0
d(g37:((0, 2)),((0, 2))) = [2->3]**[(0, 2)]**g23:((1, 3)),((0, 2))+[(0, 2)]**[2->3]**g31:((0, 2)),((1, 3))+[0->3]**[0->3]**g19:((1, 3)),((1, 3))+[0->3]**[0->1]**g32:((1, 3)),((1, 3))
d(g38:((1, 3)),((1, 3))) = [(1, 3)]**[1->2]**g30:((1, 3)),((0, 2))+[1->2]**[(1, 3)]**g17:((0, 2)),((1, 3))
d(g39:((0, 2)),((1, 3))) = [0->1]**[(1, 3)]**g32:((1, 3)),((1, 3))+[2->3]**[(1, 3)]**g11:((1, 3)),((1, 3))+[0->1]**[1->3]**g19:((1, 3)),((1, 3))
d(g40:((0, 2)),((0, 2))) = [2->3]**[(0, 2)]**g33:((1, 3)),((0, 2))+[0->3]**[2->3]**g34:((1, 3)),((1, 3))+[0->3]**[0->3]**g2:((1, 3)),((1, 3))"""

str1 = """d(g1:((1, 3)),((1, 3))) = 0
d(g2:((1, 3)),((0, 2))) = [(1, 3)]**[2->3]**g30:((1, 3)),((1, 3))+[1->2]**[(0, 2)]**g17:((0, 2)),((0, 2))+[1->2]**[0->3]**g26:((0, 2)),((1, 3))+[1->2]**[0->3]**g19:((0, 2)),((1, 3))
d(g3:((1, 3)),((0, 2))) = [1->3]**[(0, 2)]**g20:((1, 3)),((0, 2))+[1->2]**[0->1]**g19:((0, 2)),((1, 3))
d(g4:((0, 2)),((0, 2))) = [(0, 2)]**[2->3]**g13:((0, 2)),((1, 3))+[2->3]**[(0, 2)]**g11:((1, 3)),((0, 2))+[0->3]**[2->3]**g16:((1, 3)),((1, 3))+[0->3]**[0->3]**g9:((1, 3)),((1, 3))
d(g5:((1, 3)),((1, 3))) = [1->2]**[(1, 3)]**g14:((0, 2)),((1, 3))
d(g6:((1, 3)),((1, 3))) = 0
d(g7:((1, 3)),((1, 3))) = [(1, 3)]**[1->3]**g16:((1, 3)),((1, 3))+[1->2]**[(1, 3)]**g23:((0, 2)),((1, 3))
d(g8:((1, 3)),((0, 2))) = [(1, 3)]**[2->3]**g21:((1, 3)),((1, 3))+[(1, 3)]**[0->1]**g9:((1, 3)),((1, 3))+[1->3]**[0->1]**g1:((1, 3)),((1, 3))+[(1, 3)]**[0->3]**g6:((1, 3)),((1, 3))
d(g9:((1, 3)),((1, 3))) = 0
d(g10:((1, 3)),((1, 3))) = 0
d(g11:((1, 3)),((0, 2))) = [(1, 3)]**[2->3]**g7:((1, 3)),((1, 3))+[1->2]**[(0, 2)]**g24:((0, 2)),((0, 2))+[1->2]**[0->3]**g18:((0, 2)),((1, 3))
d(g12:((1, 3)),((1, 3))) = 0
d(g13:((0, 2)),((1, 3))) = [(0, 2)]**[1->2]**g17:((0, 2)),((0, 2))+[2->3]**[(1, 3)]**g7:((1, 3)),((1, 3))+[0->3]**[1->2]**g8:((1, 3)),((0, 2))
d(g14:((0, 2)),((1, 3))) = [0->1]**[(1, 3)]**g6:((1, 3)),((1, 3))
d(g15:((1, 3)),((1, 3))) = [(1, 3)]**[1->2]**g34:((1, 3)),((0, 2))
d(g16:((1, 3)),((1, 3))) = [(1, 3)]**[1->2]**g20:((1, 3)),((0, 2))+[1->2]**[(1, 3)]**g19:((0, 2)),((1, 3))
d(g17:((0, 2)),((0, 2))) = [2->3]**[2->3]**g16:((1, 3)),((1, 3))+[0->3]**[2->3]**g21:((1, 3)),((1, 3))+[2->3]**[0->3]**g5:((1, 3)),((1, 3))+[0->3]**[0->3]**g6:((1, 3)),((1, 3))
d(g18:((0, 2)),((1, 3))) = [0->1]**[(1, 3)]**g9:((1, 3)),((1, 3))+[2->3]**[(1, 3)]**g27:((1, 3)),((1, 3))+[0->1]**[1->3]**g6:((1, 3)),((1, 3))
d(g19:((0, 2)),((1, 3))) = [0->3]**[(1, 3)]**g6:((1, 3)),((1, 3))+[2->3]**[1->3]**g6:((1, 3)),((1, 3))+[0->1]**[1->3]**g22:((1, 3)),((1, 3))+[2->3]**[1->3]**g10:((1, 3)),((1, 3))+[0->3]**[(1, 3)]**g10:((1, 3)),((1, 3))
d(g20:((1, 3)),((0, 2))) = [1->3]**[2->3]**g6:((1, 3)),((1, 3))+[(1, 3)]**[0->3]**g6:((1, 3)),((1, 3))+[1->3]**[2->3]**g10:((1, 3)),((1, 3))+[(1, 3)]**[0->3]**g10:((1, 3)),((1, 3))+[1->3]**[0->1]**g1:((1, 3)),((1, 3))
d(g21:((1, 3)),((1, 3))) = [(1, 3)]**[1->2]**g32:((1, 3)),((0, 2))
d(g22:((1, 3)),((1, 3))) = 0
d(g23:((0, 2)),((1, 3))) = [(0, 2)]**[1->3]**g19:((0, 2)),((1, 3))+[0->2]**[(1, 3)]**g19:((0, 2)),((1, 3))
d(g24:((0, 2)),((0, 2))) = [(0, 2)]**[2->3]**g23:((0, 2)),((1, 3))+[0->1]**[2->3]**g16:((1, 3)),((1, 3))+[0->3]**[0->3]**g1:((1, 3)),((1, 3))+[2->3]**[0->3]**g27:((1, 3)),((1, 3))
d(g25:((0, 2)),((1, 3))) = [0->1]**[(1, 3)]**g1:((1, 3)),((1, 3))
d(g26:((0, 2)),((1, 3))) = [0->1]**[(1, 3)]**g12:((1, 3)),((1, 3))+[2->3]**[(1, 3)]**g5:((1, 3)),((1, 3))+[0->3]**[(1, 3)]**g6:((1, 3)),((1, 3))+[0->1]**[1->3]**g22:((1, 3)),((1, 3))+[0->3]**[(1, 3)]**g10:((1, 3)),((1, 3))
d(g27:((1, 3)),((1, 3))) = [1->2]**[(1, 3)]**g25:((0, 2)),((1, 3))
d(g28:((0, 2)),((0, 2))) = [2->3]**[(0, 2)]**g3:((1, 3)),((0, 2))+[0->3]**[2->3]**g15:((1, 3)),((1, 3))+[0->3]**[0->3]**g22:((1, 3)),((1, 3))
d(g29:((1, 3)),((0, 2))) = [(1, 3)]**[2->3]**g15:((1, 3)),((1, 3))+[(1, 3)]**[0->3]**g22:((1, 3)),((1, 3))+[(1, 3)]**[0->1]**g12:((1, 3)),((1, 3))+[1->3]**[0->1]**g10:((1, 3)),((1, 3))
d(g30:((1, 3)),((1, 3))) = [(1, 3)]**[1->2]**g3:((1, 3)),((0, 2))+[1->3]**[(1, 3)]**g16:((1, 3)),((1, 3))
d(g31:((0, 2)),((0, 2))) = [(0, 2)]**[2->3]**g33:((0, 2)),((1, 3))+[2->3]**[(0, 2)]**g2:((1, 3)),((0, 2))+[0->3]**[0->3]**g12:((1, 3)),((1, 3))
d(g32:((1, 3)),((0, 2))) = [(1, 3)]**[0->1]**g10:((1, 3)),((1, 3))
d(g33:((0, 2)),((1, 3))) = [(0, 2)]**[1->2]**g28:((0, 2)),((0, 2))+[2->3]**[(1, 3)]**g30:((1, 3)),((1, 3))+[0->3]**[1->2]**g29:((1, 3)),((0, 2))
d(g34:((1, 3)),((0, 2))) = [(1, 3)]**[0->1]**g22:((1, 3)),((1, 3))"""

li = str1.splitlines()

multi_list = []
multi_list.append([])

i0p_i0s = []
i0p_i1s = []
i1p_i0s = []
i1p_i1s = []

for first in li:
    newlist = []
    holder = []
    # first = li[0]
    splitter = first.split(':')
    diff = splitter[0].split('(')[1]
    holder.append(diff)
    newlist.append(diff)
    # print(splitter[1])
    # print(splitter[1][1:7], splitter[1][10:16])
    if splitter[1][1:7] == '(0, 2)' and splitter[1][10:16] == '(0, 2)':
        i0p_i0s.append(diff)
    if splitter[1][1:7] == '(0, 2)' and splitter[1][10:16] == '(1, 3)':
        i0p_i1s.append(diff)
    if splitter[1][1:7] == '(1, 3)' and splitter[1][10:16] == '(0, 2)':
        i1p_i0s.append(diff)    
    if splitter[1][1:7] == '(1, 3)' and splitter[1][10:16] == '(1, 3)':
        i1p_i1s.append(diff)
    for i in range(1,len(splitter)):
        element = splitter[i]
        if i == 1:
            split_char = '='
        else:
            split_char = '+'
        split_relation = element.split(split_char)
        if len(split_relation) < 2:
            continue
        else:
            holder.append(element.split(split_char)[1])

    
    # print(holder[1].split('**'))
    print("d(", holder[0], ")", " =", end = " ")
    for i in range(1,len(holder)):
        # print(holder[i].split('**'))
        if i > 1:
            print(' + ', end = " ")
        decomp = holder[i].split('**')
        if(len(decomp)) < 3:
            print("0", end = " ")
            continue
        toprint_1 = find_algebra_element(decomp[0],1)
        toprint_2 = find_algebra_element(decomp[1],2)
        if toprint_1 is None:
            toprint_1 = ''
        if toprint_2 is None:
            toprint_2 = ''
        toprint = toprint_1 + toprint_2 + decomp[2]
        newlist.append(toprint)
        print(toprint, end = " ")
    print("\n")
    multi_list.append(newlist)

print("IDEMPOTENT RHO_0: ")
print(i0p_i0s)
print(i0p_i1s)
print("IDEMPOTENT RHO_1:")
print(i1p_i0s)
print(i1p_i1s)

# print(multi_list)
input_str = ''

def cleanup(summand_separator):
    new_summand_separator = []
    flag = [0] * len(summand_separator)
    for i in range(len(summand_separator)):
        if flag[i] == 1:
            continue
        summand = summand_separator[i]
        new_summands = []
        for gen in summand:
            if gen not in new_summands:
                new_summands.append(gen)
        for j in range(i+1,len(summand_separator)):
            if len(intersection(summand,summand_separator[j])) > 0:
                for gen in summand_separator[j]:
                    if gen not in new_summands:
                        new_summands.append(gen)
                flag[j] = 1
        new_summand_separator.append(new_summands)
    return new_summand_separator


def update_summands(new_potential):
    flag = 0
    if len(summand_separator) == 0:
            new_summand = [new_potential[0],new_potential[len(new_potential)-1]]
            summand_separator.append(new_summand)
            # new_relation = [new_potential]
            summand_relations.append([new_potential])
            # print(new_potential)
            return
    for i in range(len(summand_separator)):
        summand = summand_separator[i]
        if new_potential[0] in summand or new_potential[len(new_potential)-1] in summand:
            if new_potential[0] in summand and new_potential[len(new_potential)-1] not in summand:
                summand.append(new_potential[len(new_potential)-1])
            elif new_potential[0] not in summand and new_potential[len(new_potential)-1] in summand:
                summand.append(new_potential[0])
            summand_relations[i].append(new_potential)
            flag = 1
    if flag == 0:
        new_summand = [new_potential[0],new_potential[len(new_potential)-1]]
        summand_separator.append(new_summand)
        summand_relations.append([new_potential])

def nomrelations(multi_list):
    global input_str
    # print(multi_list)
    for first in multi_list:
        # first = multi_list[1]
        for i in range(1,len(first)):
            dummy = first[i]
            if (not any('p' in dummy for dummy in dummy)):
                if any('s' in dummy for dummy in dummy):
                    toprint = first[i].split('*')
                    new_potential = [first[0],toprint[0],toprint[1]]
                    # print(first[0], " -> ", toprint[1], " : ", toprint[0])
                    if first[0] in i0p_i0s or first[0] in i0p_i1s:
                        idem = 0
                    if first[0] in i1p_i0s or first[0] in i1p_i1s:
                        idem = 1
                    update_summands(new_potential)
                    print(new_potential, ": ", idem)
                    input_str = input_str + str(new_potential) + " :  " + str(idem) + "\n"


def helperfunc(multi_list,index,potential,input,input_index,repeating):
    global input_str
    next = multi_list[index]
    new_res = [j for j in next if input[input_index] in j]
    # print("res:",new_res)
    repeat_status = repeating[input_index]
    if len(new_res) > 0:
        for new_item in new_res:
            new_potential = potential.copy()
            # new_potential.append(next[0])
            new_split = new_item.split('*')
            # print(new_split)
            if len(new_split) == 2:
                new_potential.append(new_split[0])
                new_potential.append(new_split[1])
                new_index = int(new_split[1].split('g')[1])
            elif len(new_split) == 3:
                new_potential.append(new_split[0])
                new_potential.append(new_split[1])
                new_potential.append(new_split[2])
                new_index = int(new_split[2].split('g')[1])
        # print("SENDING:",test_case,new_index,potential)
            # print(new_potential, " ", new_index)
            if input_index == len(input)-1:
                idem = 0
                if new_potential[0] in i0p_i0s or new_potential[0] in i0p_i1s:
                    idem = 0
                if new_potential[0] in i1p_i0s or new_potential[0] in i1p_i1s:
                    idem = 1
                update_summands(new_potential)
                print(new_potential, ": ", idem)
                input_str = input_str + str(new_potential) + " :  " + str(idem) + "\n"
            else:
                if repeat_status == 1:
                    helperfunc(multi_list,new_index,new_potential,input,input_index,repeating)
                else:
                    helperfunc(multi_list,new_index,new_potential,input,(input_index+1),repeating)
                       
            # print(potential)
    if repeat_status == 1:
        helperfunc(multi_list,index,potential,input,(input_index+1),repeating)

# input_array = ['p3*','p23*','p2*','p1*']
# repeating = [0,1,0,0]
input_array = ['p1*']
repeating = [0]

def callerfunc(multi_list,input_array,repeating):
    for i in range(1,len(multi_list)):
        first = multi_list[i]
        potential = []
        potential.append(first[0])
        helperfunc(multi_list,i,potential,input_array,0,repeating)

def intersection(lst1,lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


import re
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


#Unknot
def create_graph_from_string_0(input_string):
    graph = nx.DiGraph()

    # Split the input string into sections
    sections = re.split(r'\n(?=[a-z])', input_string.strip())
    print(len(sections))
   
    # Section 1: Nodes ax and az with arrow labeled as sy
    section_1 = sections[0].split('\n')
    for line in section_1:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, y, z = elements[0][1:][1:-1], elements[1][1:-1], elements[2][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        graph.add_edge(f'a{x}', f'a{z}', label=f'{y}')
                        print('Edge added:', f'a{x}, a{z}, label={y}')

    # Section 2: p3, p23 rep, p2: a -> U^{i+1}*a
    section_2 = sections[1].split('\n')
    for line in section_2:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, z = elements[0][1:][1:-1], elements[-1][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        i = elements.count('\'p23\'')
                        s_elements = [el for el in elements if el[1:-1].startswith('s')]
                        if len(s_elements) == 0:
                            label = f'U^{i+1}'
                        else:
                            s_concatenated = ''.join([el[1:-1] for el in s_elements])
                            label = f'U^{i+1}*{s_concatenated}'
                    graph.add_edge(f'a{x}', f'a{z}', label=label)
                    print('Edge added:', f'a{x}, a{z}, label={label}')
    return graph

#(2,1) cable

def create_graph_from_string_21(input_string):
    graph = nx.DiGraph()

    # Split the input string into sections
    sections = re.split(r'\n(?=[a-z])', input_string.strip())
    print(len(sections))
    
    # Section 1: Nodes ax and az with arrow labeled as sy
    section_1 = sections[0].split('\n')
    for line in section_1:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, y, z = elements[0][1:][1:-1], elements[1][1:-1], elements[2][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        graph.add_edge(f'a{x}', f'a{z}', label=f'{y}')
                        print('Edge added:', f'a{x}, a{z}, label={y}')
                    else:
                        graph.add_edge(f'b{x}', f'b{z}', label=f'{y}')
                        graph.add_edge(f'c{x}', f'c{z}', label=f'{y}')
                        graph.add_edge(f'b{x}', f'c{z}', label=f'U^1*{y}')
                        print('Edge added:', f'b{x}, b{z}, label={y}')
                        print('Edge added:', f'c{x}, c{z}, label={y}')
                        print('Edge added:', f'b{x}, c{z}, label=U^1*{y}')

    # Section 2: Nodes ax and az with arrow labeled as "U^{2i+2}*y"
    section_2 = sections[1].split('\n')
    for line in section_2:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, z = elements[0][1:][1:-1], elements[-1][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        i = elements.count('\'p23\'')
                        s_elements = [el for el in elements if el[1:-1].startswith('s')]
                        if len(s_elements) == 0:
                            label = f'U^{2*i+2}'
                        else:
                            s_concatenated = ''.join([el[1:-1] for el in s_elements])
                            label = f'U^{2*i+2}*{s_concatenated}'
                    graph.add_edge(f'a{x}', f'a{z}', label=label)
                    print('Edge added:', f'a{x}, a{z}, label={label}')

    # Section 3: Nodes ax and bz with arrow labeled as "U^{2i+1}*y"
    section_3 = sections[2].split('\n')
    for line in section_3:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, z = elements[0][1:][1:-1], elements[-1][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        i = elements.count('\'p23\'')
                        s_elements = [el for el in elements if el[1:-1].startswith('s')]
                        if len(s_elements) == 0:
                            label = f'U^{2*i+1}'
                        else:
                            s_concatenated = ''.join([el[1:-1] for el in s_elements])
                            label = f'U^{2*i+1}*{s_concatenated}'
                    graph.add_edge(f'a{x}', f'b{z}', label=label)
                    print('Edge added:', f'a{x}, b{z}, label={label}')

    # Section 4: Nodes ax and cz with arrow labeled as y
    section_4 = sections[3].split('\n')
    for line in section_4:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, z = elements[0][1:][1:-1], elements[-1][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        s_elements = [el for el in elements if el[1:-1].startswith('s')]
                        label = ''.join([el[1:-1] for el in s_elements])
                    graph.add_edge(f'a{x}', f'c{z}', label=label)
                    print('Edge added:', f'a{x}, c{z}, label={label}')
                    
    # Section 5: Idempotents
    section_5 = sections[4].split('\n')
    line1 = section_5[-2]
    line2 = section_5[-1]
    line_elements1 = line1[1:-1].split(', ')
    line_elements2 = line2[1:-1].split(', ')
    label = f'U'
    for el in line_elements1:
        if el[1:-1].startswith('g'):
            x = el[2:-1]
            graph.add_edge(f'b{x}', f'c{x}', label=label)
            print('Edge added:', f'b{x}, c{x}, label={label}')
    for el in line_elements2:
        if el[1:-1].startswith('g'):
            x = el[2:-1]
            graph.add_edge(f'b{x}', f'c{x}', label=label)
            print('Edge added:', f'b{x}, c{x}, label={label}')
    return graph


#(2,-1) cable

def create_graph_from_string_2neg1(input_string):
    graph = nx.DiGraph()

    # Split the input string into sections
    sections = re.split(r'\n(?=[a-z])', input_string.strip())
    print(len(sections))
    
    # Section 1: NOT M RELATIONS
    section_1 = sections[0].split('\n')
    for line in section_1:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, y, z = elements[0][1:][1:-1], elements[1][1:-1], elements[2][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        graph.add_edge(f'a{x}', f'a{z}', label=f'{y}')
                        print('Edge added:', f'a{x}, a{z}, label={y}')
                    else:
                        graph.add_edge(f'b{x}', f'b{z}', label=f'{y}')
                        graph.add_edge(f'c{x}', f'c{z}', label=f'{y}')
                        graph.add_edge(f'd{x}', f'd{z}', label=f'{y}')
                        graph.add_edge(f'e{x}', f'e{z}', label=f'{y}')
                        graph.add_edge(f'b{x}', f'c{z}', label=f'U^1*{y}')
                        graph.add_edge(f'd{x}', f'e{z}', label=f'U^1*{y}')
                        print('Edge added:', f'b{x}, b{z}, label={y}')
                        print('Edge added:', f'c{x}, c{z}, label={y}')
                        print('Edge added:', f'd{x}, d{z}, label={y}')
                        print('Edge added:', f'e{x}, e{z}, label={y}')
                        print('Edge added:', f'b{x}, c{z}, label=U^1*{y}')
                        print('Edge added:', f'd{x}, e{z}, label=U^1*{y}')

    # Section 2: p3, p23 rep, p2: a -> U^{2i+2}*a
    section_2 = sections[1].split('\n')
    for line in section_2:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, z = elements[0][1:][1:-1], elements[-1][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        i = elements.count('\'p23\'')
                        s_elements = [el for el in elements if el[1:-1].startswith('s')]
                        if len(s_elements) == 0:
                            label = f'U^{2*i+2}'
                        else:
                            s_concatenated = ''.join([el[1:-1] for el in s_elements])
                            label = f'U^{2*i+2}*{s_concatenated}'
                        graph.add_edge(f'a{x}', f'a{z}', label=label)
                    print('Edge added:', f'a{x}, a{z}, label={label}')

    # Section 3: p3, p23 rep, p2, p1: a -> U^{2i+1}*b
    section_3 = sections[2].split('\n')
    for line in section_3:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, z = elements[0][1:][1:-1], elements[-1][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        i = elements.count('\'p23\'')
                        s_elements = [el for el in elements if el[1:-1].startswith('s')]
                        if len(s_elements) == 0:
                            label = f'U^{2*i+1}'
                        else:
                            s_concatenated = ''.join([el[1:-1] for el in s_elements])
                            label = f'U^{2*i+1}*{s_concatenated}'
                        graph.add_edge(f'a{x}', f'b{z}', label=label)
                    print('Edge added:', f'a{x}, b{z}, label={label}')

    # Section 4: p3, p23 rep, p2, p12: a -> U^{2i+1}*d
    section_4 = sections[3].split('\n')
    for line in section_4:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, z = elements[0][1:][1:-1], elements[-1][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        i = elements.count('\'p23\'')
                        s_elements = [el[1:-1] for el in elements if el[1:-1].startswith('s')]
                        if len(s_elements) == 0:
                            label = f'U^{2*i+1}'
                        else:
                            s_concatenated = ''.join([el[1:-1] for el in s_elements])
                            label = f'U^{2*i+1}*{s_concatenated}'
                        graph.add_edge(f'a{x}', f'd{z}', label=label)
                    print('Edge added:', f'a{x}, d{z}, label={label}')
                    
    # Section 5: p1: a -> c
    section_5 = sections[4].split('\n')
    for line in section_5:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, z = elements[0][1:][1:-1], elements[-1][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        s_elements = [el for el in elements if el[1:-1].startswith('s')]
                        label = ''.join([el[1:-1] for el in s_elements])
                        graph.add_edge(f'a{x}', f'c{z}', label=label)
                    print('Edge added:', f'a{x}, c{z}, label={label}')
                    
    # Section 6: p12: a -> e
    section_6 = sections[5].split('\n')
    for line in section_6:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, z = elements[0][1:][1:-1], elements[-1][1:][1:-1]
                    w = int(w)
                    if w == 0:
                        s_elements = [el for el in elements if el[1:-1].startswith('s')]
                        label = ''.join([el[1:-1] for el in s_elements])
                        graph.add_edge(f'a{x}', f'e{z}', label=label)
                    print('Edge added:', f'a{x}, e{z}, label={label}')
              
    # Section 7: p2: b,c -> d,e
    section_7 = sections[6].split('\n')
    for line in section_7:
        if line and ':' in line:
            line_elements = line.split(' : ')
            if len(line_elements) == 2:
                if line_elements[1] == ' 0' or line_elements[1] == ' 1':
                    elements, w = line_elements
                    elements = elements[1:-1].split(', ')
                    x, z = elements[0][1:][1:-1], elements[-1][1:][1:-1]
                    w = int(w)
                    if w == 1:
                        s_elements = [el for el in elements if el[1:-1].startswith('s')]
                        label = ''.join([el[1:-1] for el in s_elements])
                        graph.add_edge(f'b{x}', f'c{z}', label=label)
                        graph.add_edge(f'd{x}', f'e{z}', label=label)

                    print('Edge added:', f'b{x}, c{z}, label={label}')
                    print('Edge added:', f'd{x}, e{z}, label={label}')
                    
    # Section 8: Idempotents
    section_8 = sections[7].split('\n')
    line1 = section_8[-2]
    line2 = section_8[-1]
    line_elements1 = line1[1:-1].split(', ')
    line_elements2 = line2[1:-1].split(', ')
    label = f'U'
    for el in line_elements1:
        if el[1:-1].startswith('g'):
            x = el[2:-1]
            graph.add_edge(f'b{x}', f'c{x}', label=label)
            graph.add_edge(f'd{x}', f'e{x}', label=label)
            print('Edge added:', f'b{x}, c{x}, label={label}')
            print('Edge added:', f'd{x}, e{x}, label={label}')
    for el in line_elements2:
        if el[1:-1].startswith('g'):
            x = el[2:-1]
            graph.add_edge(f'b{x}', f'c{x}', label=label)
            graph.add_edge(f'd{x}', f'e{x}', label=label)
            print('Edge added:', f'b{x}, c{x}, label={label}')
            print('Edge added:', f'd{x}, e{x}, label={label}')             
    return graph

def draw_graph(graph):
    np.random.seed(42)  # Set the seed for random position generation
    pos = nx.circular_layout(graph)
    edge_labels = {(u, v): d['label'] for u, v, d in graph.edges(data=True)}
    node_labels = {node: node for node in graph.nodes()}

    plt.figure(figsize=(12, 6))
    nx.draw_networkx(graph, pos, with_labels=False, node_color='lightblue', node_size=200)
    nx.draw_networkx_labels(graph, pos, labels=node_labels, font_color='black', font_size=8)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red', font_size=8)
    plt.axis('off')
    plt.show()

    # Print the list of edges
    print("List of Edges:")
    counter = 0
    for u, v in graph.edges():
        edge = graph.edges[u, v]['label']
        print(f"{edge}: {u}->{v}")
        counter = counter + 1
    print ('counter:', counter)

# draw_graph(graph)

"""
#UNKNOT:
summand_separator = []
summand_relations = []
i0p_i0s.append('a')
print("UNKNOT:")
print("NOT M RELATIONS")
input_str = "UNKNOT:\nNOT M RELATIONS\n"
nomrelations(multi_list)
print("p3, p23 rep, p2: a -> U^{i+1}*a")
input_str = input_str + "p3, p23 rep, p2: a -> U^{i+1}*a\n"
callerfunc(multi_list,['p3*','p23*','p2*'],[0,1,0])
print(input_str)
print("IDEMPOTENT RHO_0: ")
print(i0p_i0s)
print(i0p_i1s)
print("IDEMPOTENT RHO_1:")
print(i1p_i0s)
print(i1p_i1s)
# summand_separator = cleanup(summand_separator)
# print("\nComponents: ",summand_separator)
"""

#(2,1) CABLE:
summand_separator = []
summand_relations = []
i0p_i0s.append('a')
i1p_i0s.append('b')
i1p_i0s.append('c')
print("\n\n(2,1) CABLE:")
input_str = "(2,1) CABLE:\nNOT M RELATIONS\n"
print("NOT M RELATIONS")
nomrelations(multi_list)
print("p3, p23 rep, p2: a -> U^{2i+2}*a")
input_str = input_str + "p3, p23 rep, p2: a -> U^{2i+2}*a\n"
callerfunc(multi_list,['p3*','p23*','p2*'],[0,1,0]) #U^(2i+2)*a
print("p3, p23 rep, p2, p1: a -> U^{2i+1}*b")
input_str = input_str + "p3, p23 rep, p2, p1: a -> U^{2i+1}*b\n"
callerfunc(multi_list,['p3*','p23*','p2*','p1*'],[0,1,0,0]) #U^(2i+1)*b
print("p1: a -> c")
input_str = input_str + "p1: a -> c\n"
callerfunc(multi_list,['p1*'],[0]) #c
print("note that m(b) = U*c for nomrelations")
input_str = input_str + "note that m(b) = U*c for nomrelations\n"
print("IDEMPOTENT RHO_0: ")
input_str = input_str + "IDEMPOTENT RHO_0: \n"
print(i0p_i0s)
input_str = input_str + str(i0p_i0s) + "\n"
print(i0p_i1s)
input_str = input_str + str(i0p_i1s) + "\n"
print("IDEMPOTENT RHO_1:")
input_str = input_str + "IDEMPOTENT RHO_1: \n"
print(i1p_i0s)
input_str = input_str + str(i1p_i0s) + "\n"
print(i1p_i1s)
input_str = input_str + str(i1p_i1s)
# summand_separator = cleanup(summand_separator)
# print("\nComponents: ",summand_separator)

"""
#(2,-1) CABLE:
summand_separator = []
summand_relations = []
i0p_i0s.append('a')
i1p_i0s.append('b')
i1p_i0s.append('c')
i1p_i0s.append('d')
i1p_i0s.append('e')
print("\n\n(2,-1) CABLE:")
input_str = "(2,-1) CABLE:\nNOT M RELATIONS\n"
print("NOT M RELATIONS")
nomrelations(multi_list)
print("p3, p23 rep, p2: a -> U^{2i+2}*a")
input_str = input_str + "p3, p23 rep, p2: a -> U^{2i+2}*a\n"
callerfunc(multi_list,['p3*','p23*','p2*'],[0,1,0]) #U^(2i+2)*a
print("p3, p23 rep, p2, p1: a -> U^{2i+1}*b")
input_str = input_str + "p3, p23 rep, p2, p1: a -> U^{2i+1}*b\n"
callerfunc(multi_list,['p3*','p23*','p2*','p1*'],[0,1,0,0]) #U^(2i+1)*b
print("p3, p23 rep, p2, p12: a -> U^{2i+1}*d")
input_str = input_str + "p3, p23 rep, p2, p12: a -> U^{2i+1}*d\n"
callerfunc(multi_list,['p3*','p23*','p2*','p12*'],[0,1,0,0]) #U^(2i+1)*d
print("p1: a -> c")
input_str = input_str + "p1: a -> c\n"
callerfunc(multi_list,['p1*'],[0]) #c,e
print("p12: a -> e")
input_str = input_str + "p12: a -> e\n"
callerfunc(multi_list,['p12*'],[0]) #e
print("p2: b,c -> d,e")
input_str = input_str + "p2: b,c -> d,e\n"
callerfunc(multi_list,['p2*'],[0]) #d,e
print("note that m(b) = U*c, m(d) = U*e for nomrelations\n")
print("IDEMPOTENT RHO_0: ")
input_str = input_str + "IDEMPOTENT RHO_0: \n"
print(i0p_i0s)
input_str = input_str + str(i0p_i0s) + "\n"
print(i0p_i1s)
input_str = input_str + str(i0p_i1s) + "\n"
print("IDEMPOTENT RHO_1:")
input_str = input_str + "IDEMPOTENT RHO_1: \n"
print(i1p_i0s)
input_str = input_str + str(i1p_i0s) + "\n"
print(i1p_i1s)
input_str = input_str + str(i1p_i1s)
# summand_separator = cleanup(summand_separator)
# print("\nComponents: ",summand_separator)
"""

# input_string = input_str

print(input_str)

# graph = create_graph_from_string_2neg1(input_str)
graph = create_graph_from_string_21(input_str)
# graph = create_graph_from_string_0(input_str)

# print("input_str:\n",input_str)


for u, v in graph.edges():
        interesting_part = graph.edges[u, v]['label'].split('*')
        new_edge = ''
        flag = ''
        putin = 0
        if 'U' in interesting_part[0]:
            new_edge = new_edge + interesting_part[0]
            flag = '*'
            putin = 1
        partition = interesting_part[-1].split('s')
        for i in range(1,len(partition)):
            if putin == 1:
                new_edge = new_edge + flag
                putin = 0
            if partition[i] == '1':
                new_edge = new_edge + 'p3'
            if partition[i] == '2':
                new_edge = new_edge + 'p2'
            if partition[i] == '3':
                new_edge = new_edge + 'p1'
            if partition[i] == '12':
                new_edge = new_edge + 'p3p2'
            if partition[i] == '23':
                new_edge = new_edge + 'p2p1'
            if partition[i] == '123':
                new_edge = new_edge + 'p3p2p1'
        graph.edges[u, v]['label'] = new_edge
        # edge = graph.edges[u, v]['label']
        print(f"{new_edge}: {u}->{v}")

def make_sequences(originalu,u,upower,newstring,newgraph):
    # print(u)
    for v in newgraph.__getitem__(u):
        if u == v:
            print(u,v)
            continue
        # print(newgraph.edges[u,v]['label'].split('*'))
        relations = newgraph.edges[u,v]['label'].split('+')
        for relation in relations:
            differential = relation.split('*')
            if len(differential) == 1 and 'U' in differential[0]:
                return
            else:
                index = 0
                if 'U' in differential[0]:
                    # print(differential[0])
                    upower = upower + int(differential[0].split('^')[1])
                    index = 1
                nextstring = newstring + differential[index]
                if upower == 0:
                    toadd = ''
                else:
                    toadd = f'U^{upower}*'
                final_str = toadd + nextstring
                # print("adding edge ", u, " to ", v, " through ", final_str)
                if graph.has_edge(originalu,v) and final_str not in graph.edges[originalu,v]['label']:
                    final_str = graph.edges[originalu,v]['label'] + ' + ' + final_str
                graph.add_edge(originalu,v,label = final_str)
                make_sequences(originalu,v,upower,nextstring,newgraph)


print("\n\nNEW SECTION")

for u in graph.nodes:
    # print(graph.neighbors(u))
    upower = 0
    make_sequences(u,u,upower,'',graph.copy())

for u, v in graph.edges():
    edge = graph.edges[u, v]['label']
    print(f"{edge}: {u}->{v}")

# n0 -> u1 -> ... -> us <- x0 through D3, D23,...,D23,D1

#SET THIS FLAG TO 1 WHEN DOING IT


arr = ['p2','p1p2p3','p2p3','p2p3','p2']
direction = ['f','f','f','f','f']

arr = ['p2','p1p2']
direction = ['f','f']

arr = ['p1p2', 'p1p2', 'p1p2', 'p1p2', 'p1p2', 'p1p2', 'p1p2', 'p1p2']
direction = ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f']

arr = ['p3','p2p3','p2p3','p1','p2']
direction = ['f','f','f','b','b']
p2p1flag = 1

def last_iter(potential_summand,arr,direction,index):
    search_list = []
    for item in potential_summand:
        split_item = item.split(' ')
        # print(split_item, int(split_item[-1]), split_item[-2], split_item[-3])
        if int(split_item[-1]) == (index-1):
            # print("HERE")
            determinecoeff = split_item[0].split('*')
            if len(determinecoeff) == 1 and 'U' in determinecoeff[0]:
                search_list.append(split_item[-2])
                search_list.append(split_item[-3])
                continue
            if direction[index-1] == 'f':
                search_list.append(split_item[-2])
            elif direction[index-1] == 'b':
                search_list.append(split_item[-3])

    for item in search_list:
        for neighbor in graph.edges(item):
            neighbor = neighbor[1]
            edge = graph.edges[item,neighbor]['label']
            allrelations = edge.split('+')
            # print(allrelations, item, neighbor)
            for relation in allrelations:
                edge_split = relation.split('*')
                toappend = relation + ' ' + str(item) + ' ' + str(neighbor) + ' ' + str(index)
                if len(edge_split) == 1 and 'U' in edge_split[0] and toappend not in potential_summand:
                    potential_summand.append(toappend)
        
        for neighbor in graph.in_edges(item):
            neighbor = neighbor[0]
            edge = graph.edges[neighbor,item]['label']
            allrelations = edge.split('+')
            for relation in allrelations:
                edge_split = relation.split('*')
                toappend = relation + ' ' + str(neighbor) + ' ' + str(item) + ' ' + str(index)
                if len(edge_split) == 1 and 'U' in edge_split[0] and toappend not in potential_summand:
                    potential_summand.append(toappend)
    return potential_summand


def summand_helper(potential_summand,arr,direction,index):
    # print(index)
    search_list = []
    for item in potential_summand:
        split_item = item.split(' ')
        # print(split_item, int(split_item[-1]), split_item[-2], split_item[-3])
        if int(split_item[-1]) == (index-1):
            # print("HERE")
            determinecoeff = split_item[0].split('*')
            if len(determinecoeff) == 1 and 'U' in determinecoeff[0]:
                search_list.append(split_item[-2])
                search_list.append(split_item[-3])
                continue
            if direction[index-1] == 'f':
                search_list.append(split_item[-2])
            elif direction[index-1] == 'b':
                search_list.append(split_item[-3])
    
    final_list = []
    # print("search list:", search_list)
    for u in search_list:
        if direction[index] == 'f':
            edge_list = graph.edges(u)
        elif direction[index] == 'b':
            edge_list = graph.in_edges(u)
        # print("edge list:", edge_list)
        for v in edge_list:
            if direction[index] == 'f':
                v = v[1]
                edge = graph.edges[u, v]['label']
            elif direction[index] == 'b':
                v = v[0]
                edge = graph.edges[v, u]['label']
            # print(edge)
            allrelations = edge.split('+')
            for relation in allrelations:
                edge_split = relation.split('*')
                if direction[index] == 'f':
                    relation = relation + ' ' + str(u) + ' ' + str(v)
                elif direction[index] == 'b':
                    relation = relation + ' ' + str(v) + ' ' + str(u)
                toappend = relation + ' ' + str(index)
                if edge_split[-1] == arr[index] and toappend not in potential_summand:
                    potential_summand.append(toappend)
                    final_list.append(v)
    
    for item in final_list:
        for neighbor in graph.edges(item):
            neighbor = neighbor[1]
            edge = graph.edges[item,neighbor]['label']
            allrelations = edge.split('+')
            for relation in allrelations:
                edge_split = relation.split('*')
                toappend = relation + ' ' + str(item) + ' ' + str(neighbor) + ' ' + str(index)
                if len(edge_split) == 1 and 'U' in edge_split[0] and toappend not in potential_summand:
                    potential_summand.append(toappend)
        
        for neighbor in graph.in_edges(item):
            neighbor = neighbor[0]
            edge = graph.edges[neighbor,item]['label']
            allrelations = edge.split('+')
            for relation in allrelations:
                edge_split = relation.split('*')
                toappend = relation + ' ' + str(neighbor) + ' ' + str(item) + ' ' + str(index)
                if len(edge_split) == 1 and 'U' in edge_split[0] and toappend not in potential_summand:
                    potential_summand.append(toappend)
    return potential_summand

def p2p1check(potential_summand,arr):
    
    start_index = arr.index('p2')
    end_index = arr.index('p1')

    left_index = []
    for item in potential_summand:
        slice = item.split(' ')
        index = slice[-1]
        relations = slice[0].split('+')
        for relation in relations:
            if int(index) == start_index and 'p1' not in relation:
                left_index.append(slice[-3])
                left_index.append(slice[-2])

    right_index = []
    for item in potential_summand:
        slice = item.split(' ')
        index = slice[-1]
        if int(index) == end_index:
            right_index.append(slice[-3])
            right_index.append(slice[-2])

    left_index = list(set(left_index))
    right_index = list(set(right_index))
    import itertools
    for u,v in itertools.product(left_index,right_index):
        if graph.has_edge(u,v):
            breakdown = graph.edges[u,v]['label'].split('+')
            for relation in breakdown:
                tensor_break = relation.split('*')
                if (len(tensor_break) == 1 and 'p2p1' == tensor_break[0]) or (len(tensor_break) == 2 and 'p2p1' == tensor_break[1]):
                    potential_summand.append(relation + ' ' + u + ' ' + v + ' ' + str(len(arr)))
    return potential_summand


print("SUMMAND MAKING")
for u in graph.nodes:
    final_list = []
    index = 0
    if direction[index] == 'f':
        edge_list = graph.edges(u)
    elif direction[index] == 'b':
        edge_list = graph.in_edges(u)
    for v in edge_list:
        if direction[index] == 'f':
            v = v[1]
            edge = graph.edges[u, v]['label']
        elif direction[index] == 'b':
            v = v[0]
            edge = graph.edges[v, u]['label']
        allrelations = edge.split('+')
        for relation in allrelations:
            edge_split = relation.split('*')
            if direction[index] == 'f':
                relation = relation + ' ' + str(u) + ' ' + str(v)
            elif direction[index] == 'b':
                relation = relation + ' ' + str(v) + ' ' + str(u)

            if edge_split[-1] == arr[index]:
                potential_summand = []
                potential_summand.append(relation + ' ' + str(index))
                for neighbor in graph.edges(u):
                    # print(neighbor)
                    neighbor = neighbor[1]
                    edge = graph.edges[u,neighbor]['label']
                    allrelations = edge.split('+')
                    for relation in allrelations:
                        edge_split = relation.split('*')
                        if len(edge_split) == 1 and 'U' in edge_split[0]:
                            potential_summand.append(relation + ' ' + str(u) + ' ' + str(neighbor) + ' ' + str(index))
                
                for neighbor in graph.in_edges(u):
                    neighbor = neighbor[0]
                    edge = graph.edges[neighbor,u]['label']
                    allrelations = edge.split('+')
                    for relation in allrelations:
                        edge_split = relation.split('*')
                        if len(edge_split) == 1 and 'U' in edge_split[0]:
                            potential_summand.append(relation + ' ' + str(neighbor) + ' ' + str(u) + ' ' + str(index))
                for neighbor in graph.edges(v):
                    # print(neighbor)
                    neighbor = neighbor[1]
                    edge = graph.edges[v,neighbor]['label']
                    allrelations = edge.split('+')
                    for relation in allrelations:
                        edge_split = relation.split('*')
                        if len(edge_split) == 1 and 'U' in edge_split[0]:
                            potential_summand.append(relation + ' ' + str(v) + ' ' + str(neighbor) + ' ' + str(index))
                
                for neighbor in graph.in_edges(v):
                    neighbor = neighbor[0]
                    edge = graph.edges[neighbor,v]['label']
                    allrelations = edge.split('+')
                    for relation in allrelations:
                        edge_split = relation.split('*')
                        if len(edge_split) == 1 and 'U' in edge_split[0]:
                            potential_summand.append(relation + ' ' + str(neighbor) + ' ' + str(v) + ' ' + str(index))
                for i in range(1,len(arr)):
                    # print("potential_summand:", potential_summand)
                    potential_summand = summand_helper(potential_summand,arr,direction,i)
                potential_summand = last_iter(potential_summand,arr,direction,len(arr)-1)
                if p2p1flag == 1:
                    potential_summand = p2p1check(potential_summand,arr)
                print("final potential:", potential_summand)


print("GRADING MAKING")
#recall that idems are:
alex_grading_summand = []
i0p_i0s.pop()
useful_indices = []
for gen in i0p_i0s:
    useful_indices.append(gen[1:])


nodes_to_test = []
for node in graph.nodes():
    if node[1:] in useful_indices:
        nodes_to_test.append(node)

print(i0p_i0s)
print(nodes_to_test)

for node in nodes_to_test:
    for v in graph.__getitem__(node):
        label = graph.edges[node,v]['label']
        toappend = label + ' ' + node + ' ' + v
        edge_split = label.split('+')
        for relation in edge_split:
            further_split = relation.split('*')
            if v in nodes_to_test and toappend not in alex_grading_summand and ('p1p2' in graph.edges[node,v]['label'] or (len(further_split) == 1 and 'U' in further_split[0])):
                alex_grading_summand.append(toappend)

print(alex_grading_summand)


# def alex_summand_helper(potential_summand,v,arr):
