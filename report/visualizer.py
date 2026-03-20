from graphiz import Digraph

def create_graph(nodes, filename="attack_surface"):
  dot = Digraph()
  for parent, child in nodes:
    dot.edge(parent,child)
  dot.render(filename, format='png')
