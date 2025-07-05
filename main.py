import ast
from Graph import Graph

print("WELCOME TO THE GRAPH VISUALIZER\n\n")
directed = input("Is the graph Directed (Y/n): ").strip().lower()
directed = False if directed == 'n' else True
nodes = int(input(("Enter nummber of nodes: ")))

edgeList = ast.literal_eval(input("Enter edges as a list of tupples (e.g. [(1,2),(2,3)]): "))

print(f"\nEdge List: {edgeList}")
print(f"Directed: {directed}")
print(f"Number of Nodes: {nodes}")

g = Graph(edgeList, nodes, directed)
print()
g.getAdjLst()