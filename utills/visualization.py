from graphviz import Digraph

def find_nodes_edges(ll):
    nodes,edges = set(),set()
    current = ll.head
    while current != None:
        nodes.add(current)
        edges.add((current,current.next))
        current = current.next
    return nodes,edges
def draw_graph(ll,format='SVG',rankdir='LR'):
    nodes,edges = find_nodes_edges(ll)
    dot = Digraph(name='linked_list',format=format,graph_attr={'rankdir':rankdir})
    for n in nodes:
        dot.node(str(id(n)),label=str(n.data),shape='record')
    for n1,n2 in edges:
        dot.edge(str(id(n1)),str(id(n2)))
    dot.render(directory='../images/').replace('\\', '/')
    return dot