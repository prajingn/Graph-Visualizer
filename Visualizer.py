import pygraphviz as pgv
from PIL import Image
import io

def draw_graph(nodes, edge_lst, directed=True, is_tree=True):
    G = pgv.AGraph(directed=True) if directed else pgv.AGraph()
    G.add_edges_from(edge_lst)
       
    if is_tree:
        image_data = G.draw(format="png", prog="dot")
    else:
        image_data = G.draw(format="png", prog="sfdp")

    image = Image.open(io.BytesIO(image_data))
    image.show()