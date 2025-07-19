import ast
import sys

def get_input_user():
    nodes = int(input(("Enter number of nodes: ")))
    directed = input("Is the graph Directed (Y/n): ").strip().lower()
    directed = False if directed == 'n' else True
    edgeList = ast.literal_eval(input("Enter edges as a list of tupples (e.g. [(1,2),(2,3)]): "))

    for i, j in edgeList:
        if i > nodes or j > nodes:
            print("Node out of range!")
            print(f"Value of node must be >= 0 and < {nodes}")
            print("Exiting...")
            sys.exit(1)

    return edgeList, nodes, directed

def get_input_file():
    print("\nINSTRUCTIONS!!")
    print("First line must contain number of nodes.")
    print('Second line must contain "True" or "False" to indicate whether the graph is directed or not.')
    print("Third line must contain a list of tupples (e.g. [(1,2),(2,3)]) reprasenting edges of the graph.\n")
    fl_name = input("Enter file path: ")
    try:
        with open(fl_name, "r") as f:
            nodes = int(f.readline())
            directed = bool(f.readline())
            edgeList = ast.literal_eval(f.readline())

    except FileNotFoundError:
        print("File not Found!")
        print("Exiting...")
        sys.exit(1)
    
    return edgeList, nodes, directed