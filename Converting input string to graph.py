#!/usr/bin/env python
# coding: utf-8

# In[8]:


import re
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# I fixed the methods for (2,1) cable and (2,-1) cable. The unknot method seems to be correct.

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

# Example usage
input_string = """
(2,1) CABLE:
NOT M RELATIONS
['g1', 's2', 'g7'] :  0
['g2', 's2', 'g20'] :  1
['g6', 's3', 'g32'] :  0
['g11', 's3', 'g31'] :  1
['g12', 's3', 'g1'] :  0
['g14', 's3', 'g26'] :  0
['g15', 's3', 'g28'] :  1
['g17', 's2', 'g21'] :  1
['g18', 's1', 'g25'] :  1
['g18', 's3', 'g17'] :  1
['g18', 's123', 'g27'] :  1
['g20', 's1', 'g3'] :  1
['g21', 's1', 'g27'] :  1
['g24', 's2', 'g34'] :  1
['g26', 's2', 'g23'] :  0
['g28', 's2', 'g33'] :  1
['g30', 's1', 'g4'] :  1
['g30', 's3', 'g2'] :  1
['g30', 's123', 'g3'] :  1
['g31', 's23', 'g24'] :  1
['g32', 's23', 'g10'] :  0
['g34', 's123', 'g13'] :  1
p3, p23 rep, p2: a -> U^{2i+2}*a
['g1', 'p3', 'g28', 'p23', 'g24', 'p2', 'g10'] :  0
['g6', 'p3', 's123', 'g29', 'p2', 'g5'] :  0
['g7', 'p3', 'g33', 'p2', 's1', 'g10'] :  0
['g12', 'p3', 'g15', 'p2', 'g23'] :  0
['g12', 'p3', 'g15', 'p2', 's123', 'g16'] :  0
['g12', 'p3', 'g15', 'p2', 's123', 'g10'] :  0
['g14', 'p3', 'g11', 'p2', 'g6'] :  0
['g14', 'p3', 'g11', 'p2', 's123', 'g19'] :  0
['g16', 'p3', 'g8', 'p2', 'g22'] :  0
['g19', 'p3', 'g29', 'p2', 'g5'] :  0
['g23', 'p3', 's3', 'g24', 'p2', 'g10'] :  0
['g23', 'p3', 's123', 'g8', 'p2', 'g22'] :  0
['g26', 'p3', 'g31', 'p2', 'g32'] :  0
p3, p23 rep, p2, p1: a -> U^{2i+1}*b
['g1', 'p3', 'g28', 'p23', 'g24', 'p2', 'g10', 'p1', 's23', 'g27'] :  0
['g6', 'p3', 's123', 'g29', 'p2', 'g5', 'p1', 'g9'] :  0
['g7', 'p3', 'g33', 'p2', 's1', 'g10', 'p1', 's23', 'g27'] :  0
['g12', 'p3', 'g15', 'p2', 's123', 'g16', 'p1', 'g25'] :  0
['g12', 'p3', 'g15', 'p2', 's123', 'g16', 'p1', 's23', 'g27'] :  0
['g12', 'p3', 'g15', 'p2', 's123', 'g10', 'p1', 's23', 'g27'] :  0
['g14', 'p3', 'g11', 'p2', 'g6', 'p1', 's3', 'g24'] :  0
['g14', 'p3', 'g11', 'p2', 's123', 'g19', 'p1', 'g4'] :  0
['g14', 'p3', 'g11', 'p2', 's123', 'g19', 'p1', 's23', 'g3'] :  0
['g16', 'p3', 'g8', 'p2', 'g22', 'p1', 'g13'] :  0
['g16', 'p3', 'g8', 'p2', 'g22', 'p1', 'g3'] :  0
['g19', 'p3', 'g29', 'p2', 'g5', 'p1', 'g9'] :  0
['g23', 'p3', 's3', 'g24', 'p2', 'g10', 'p1', 's23', 'g27'] :  0
['g23', 'p3', 's123', 'g8', 'p2', 'g22', 'p1', 'g13'] :  0
['g23', 'p3', 's123', 'g8', 'p2', 'g22', 'p1', 'g3'] :  0
p1: a -> c
['g5', 'p1', 'g9'] :  0
['g6', 'p1', 's3', 'g24'] :  0
['g10', 'p1', 's23', 'g27'] :  0
['g16', 'p1', 'g25'] :  0
['g16', 'p1', 's23', 'g27'] :  0
['g19', 'p1', 'g4'] :  0
['g19', 'p1', 's23', 'g3'] :  0
['g22', 'p1', 'g13'] :  0
['g22', 'p1', 'g3'] :  0
note that m(b) = U*c for nomrelations
IDEMPOTENT RHO_0: 
['g6', 'g7', 'g12', 'g14', 'g23', 'a']
['g1', 'g5', 'g10', 'g16', 'g19', 'g22', 'g26', 'g32']
IDEMPOTENT RHO_1:
['g11', 'g15', 'g18', 'g20', 'g21', 'g30', 'g33', 'g34', 'b', 'c']
['g2', 'g4', 'g3', 'g8', 'g9', 'g13', 'g17', 'g24', 'g25', 'g27', 'g28', 'g29', 'g31']
"""

graph = create_graph_from_string_21(input_string)
draw_graph(graph)


# In[9]:


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

# Example usage
input_string = """
(2,-1) CABLE:
NOT M RELATIONS
['g1', 's2', 'g7'] :  0
['g2', 's2', 'g20'] :  1
['g6', 's3', 'g32'] :  0
['g11', 's3', 'g31'] :  1
['g12', 's3', 'g1'] :  0
['g14', 's3', 'g26'] :  0
['g15', 's3', 'g28'] :  1
['g17', 's2', 'g21'] :  1
['g18', 's1', 'g25'] :  1
['g18', 's3', 'g17'] :  1
['g18', 's123', 'g27'] :  1
['g20', 's1', 'g3'] :  1
['g21', 's1', 'g27'] :  1
['g24', 's2', 'g34'] :  1
['g26', 's2', 'g23'] :  0
['g28', 's2', 'g33'] :  1
['g30', 's1', 'g4'] :  1
['g30', 's3', 'g2'] :  1
['g30', 's123', 'g3'] :  1
['g31', 's23', 'g24'] :  1
['g32', 's23', 'g10'] :  0
['g34', 's123', 'g13'] :  1
p3, p23 rep, p2: a -> U^{2i+2}*a
['g1', 'p3', 'g28', 'p23', 'g24', 'p2', 'g10'] :  0
['g6', 'p3', 's123', 'g29', 'p2', 'g5'] :  0
['g7', 'p3', 'g33', 'p2', 's1', 'g10'] :  0
['g12', 'p3', 'g15', 'p2', 'g23'] :  0
['g12', 'p3', 'g15', 'p2', 's123', 'g16'] :  0
['g12', 'p3', 'g15', 'p2', 's123', 'g10'] :  0
['g14', 'p3', 'g11', 'p2', 'g6'] :  0
['g14', 'p3', 'g11', 'p2', 's123', 'g19'] :  0
['g16', 'p3', 'g8', 'p2', 'g22'] :  0
['g19', 'p3', 'g29', 'p2', 'g5'] :  0
['g23', 'p3', 's3', 'g24', 'p2', 'g10'] :  0
['g23', 'p3', 's123', 'g8', 'p2', 'g22'] :  0
['g26', 'p3', 'g31', 'p2', 'g32'] :  0
p3, p23 rep, p2, p1: a -> U^{2i+1}*b
['g1', 'p3', 'g28', 'p23', 'g24', 'p2', 'g10', 'p1', 's23', 'g27'] :  0
['g6', 'p3', 's123', 'g29', 'p2', 'g5', 'p1', 'g9'] :  0
['g7', 'p3', 'g33', 'p2', 's1', 'g10', 'p1', 's23', 'g27'] :  0
['g12', 'p3', 'g15', 'p2', 's123', 'g16', 'p1', 'g25'] :  0
['g12', 'p3', 'g15', 'p2', 's123', 'g16', 'p1', 's23', 'g27'] :  0
['g12', 'p3', 'g15', 'p2', 's123', 'g10', 'p1', 's23', 'g27'] :  0
['g14', 'p3', 'g11', 'p2', 'g6', 'p1', 's3', 'g24'] :  0
['g14', 'p3', 'g11', 'p2', 's123', 'g19', 'p1', 'g4'] :  0
['g14', 'p3', 'g11', 'p2', 's123', 'g19', 'p1', 's23', 'g3'] :  0
['g16', 'p3', 'g8', 'p2', 'g22', 'p1', 'g13'] :  0
['g16', 'p3', 'g8', 'p2', 'g22', 'p1', 'g3'] :  0
['g19', 'p3', 'g29', 'p2', 'g5', 'p1', 'g9'] :  0
['g23', 'p3', 's3', 'g24', 'p2', 'g10', 'p1', 's23', 'g27'] :  0
['g23', 'p3', 's123', 'g8', 'p2', 'g22', 'p1', 'g13'] :  0
['g23', 'p3', 's123', 'g8', 'p2', 'g22', 'p1', 'g3'] :  0
p3, p23 rep, p2, p12: a -> U^{2i+1}*d
['g26', 'p3', 'g31', 'p2', 'g32', 'p12', 'g10'] :  0
p1: a -> c
['g5', 'p1', 'g9'] :  0
['g6', 'p1', 's3', 'g24'] :  0
['g10', 'p1', 's23', 'g27'] :  0
['g16', 'p1', 'g25'] :  0
['g16', 'p1', 's23', 'g27'] :  0
['g19', 'p1', 'g4'] :  0
['g19', 'p1', 's23', 'g3'] :  0
['g22', 'p1', 'g13'] :  0
['g22', 'p1', 'g3'] :  0
p12: a -> e
['g32', 'p12', 'g10'] :  0
p2: b,c -> d,e
['g8', 'p2', 'g22'] :  1
['g11', 'p2', 'g6'] :  1
['g11', 'p2', 's123', 'g19'] :  1
['g15', 'p2', 'g23'] :  1
['g15', 'p2', 's123', 'g16'] :  1
['g15', 'p2', 's123', 'g10'] :  1
['g24', 'p2', 'g10'] :  1
['g29', 'p2', 'g5'] :  1
['g31', 'p2', 'g32'] :  1
['g33', 'p2', 's1', 'g10'] :  1
note that m(b) = U*c, m(d) = U*e for nomrelations
IDEMPOTENT RHO_0: 
['g6', 'g7', 'g12', 'g14', 'g23', 'a']
['g1', 'g5', 'g10', 'g16', 'g19', 'g22', 'g26', 'g32']
IDEMPOTENT RHO_1:
['g11', 'g15', 'g18', 'g20', 'g21', 'g30', 'g33', 'g34', 'b', 'c', 'd', 'e']
['g2', 'g4', 'g3', 'g8', 'g9', 'g13', 'g17', 'g24', 'g25', 'g27', 'g28', 'g29', 'g31']
"""

graph = create_graph_from_string_2neg1(input_string)
draw_graph(graph)


# In[ ]:




