from parser import get_input_user, get_input_file
from Graph import Graph
from Visualizer import draw_graph
from os import mkdir, path

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
    print("4. Export to file")
    print("5. Quit")
    op = input("Enter option (1 - 5): ")

    if op == '1':
        draw_graph(nodes, g.edgelst, directed, False)

    elif op == '2':
        v = int(input("\nEnter the source vertex: "))

        if not 0 <= v < nodes:
            print(f"\nVertex can't be lesser than zero or greater than {nodes - 1}\nTry again...")
        else:
            g.set_BFS(v)
            draw_graph(nodes, g.BFS_edge_lst)

    elif op == '3':
        v = int(input("\nEnter the source vertex: "))

        if not 0 <= v < nodes:
            print(f"\nVertex can't be lesser than zero or greater than {nodes - 1}\nTry again...")
        else:
            g.set_DFS(v)
            draw_graph(nodes, g.DFS_edge_lst)

    elif op == '4':
        if not path.exists("Exports"):
            mkdir("Exports")

        fname = input("\nEnter text file name: ").strip()
        fname, _ = path.splitext(fname)

        pname = path.join("Exports", fname + ".txt")
        write = True

        if path.exists(pname):
            print(f"File already exists at {pname}")
            write = False if input("\nRewrite file? (Y/n):").strip().lower() == 'n' else True

        if write:
            with open(pname, "w") as f:
                print(f"File {fname} created at {pname} successfully\n")

                v_bfs = int(input("\nEnter the source vertex for BFS: "))
                v_dfs = int(input("Enter the source vertex for DFS: "))
                if not 0 <= v_bfs < nodes and 0 <= v_dfs < nodes:
                    print(f"\nVertex can't be lesser than zero or greater than {nodes - 1}\nTry again...")
                else:
                    g.set_BFS(v_bfs)
                    g.set_DFS(v_dfs)

                f.write(f"Graph (Directed - {directed}):\n")
                f.write(f"{g.edgelst}\n\n")
                f.write(f"BFS from vertex {v_bfs}:\n")
                f.write(f"{g.BFS_edge_lst}\n\n")
                f.write(f"DFS from vertex {v_dfs}:\n")
                f.write(f"{g.DFS_edge_lst}\n\n")
                print("\nExport Successful :D")

    elif op == '5':
        break

    else:
        print("Invalid Option!!")

print("\nExiting...")

# test.txt