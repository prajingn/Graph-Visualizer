from parser import *
from Graph import Graph
from Visualizer import draw_graph

print(r"""
+----------------------------------------+
|          WELCOME TO THE TOOL           |
|        -- Graph Visualizer --          |
+----------------------------------------+

      🔍 Visualize. Explore. Learn. 🔍
""")

op = input("Do you want to input using a text file? (Y/n): ").strip().lower()
if op == 'n':
    edgeList, nodes, directed = get_input_user()
else:
    edgeList, nodes, directed = get_input_file()

g = Graph(edgeList, nodes, directed)

while True:
    print()
    print("What do you want to do?")
    print("1. Visualize Graph")
    print("2. Visualize BFS tree")
    print("3. Visualize DFS tree")
    print("4. Quit")
    op = input("Enter option (1 - 4): ")

    if op == '1':
        draw_graph(nodes, g.edgelst, directed, False)

    elif op == '2':
        v = int(input("Enter the source vertex: "))

        if v >= nodes:
            print(f"\nVertex can't be greater than {nodes - 1}\nTry again...")
        else:
            g.set_BFS(v)
            draw_graph(nodes, g.BFS_edge_lst)

    elif op == '3':
        v = int(input("Enter the source vertex: "))

        if v >= nodes:
            print(f"\nVertex can't be greater than {nodes - 1}\nTry again...")
        else:
            # g.set_DFS(v)
            # draw_graph(nodes, g.DFS_edge_lst)
            ...

    elif op == '4':
        break

    else:
        print("Invalid Option!!")

print("\nExiting...")