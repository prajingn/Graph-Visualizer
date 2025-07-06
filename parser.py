import ast
import sys

def get_input():
    directed = input("Is the graph Directed (Y/n): ").strip().lower()
    directed = False if directed == 'n' else True

    nodes = int(input(("Enter number of nodes: ")))
    edgeList = ast.literal_eval(input("Enter edges as a list of tupples (e.g. [(1,2),(2,3)]): "))

    for i, j in edgeList:
        if i > nodes or j > nodes:
            print("Node out of range!")
            print(f"Value of node must be >= 0 and < {nodes}")
            sys.exit(1)

    return edgeList, nodes, directed