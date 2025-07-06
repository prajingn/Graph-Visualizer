import pygraphviz as pgv
from PIL import Image
import tempfile

def draw_graph(nodes, edge_lst, directed=True, is_tree=True):
    G = pgv.AGraph(directed=directed)
    G.add_edges_from(edge_lst)
    
    if is_tree:
        layout_prog = "dot"
    elif nodes <= 50:
        layout_prog = "neato"
    elif nodes <= 250:
        layout_prog = "fdp"
    else:
        layout_prog = "sfdp"

    if layout_prog in ("neato", "fdp", "sfdp"):
        G.graph_attr.update(
            overlap='scale',
            sep='+10',
            splines='true'
        )

    with tempfile.NamedTemporaryFile(suffix=".png") as tmp:
        G.draw(tmp.name, format="png", prog=layout_prog)
        image = Image.open(tmp.name)
        image.show()
