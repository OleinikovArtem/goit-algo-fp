# Task 4,5
import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, step, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(f"{title} - Step {step}")
    plt.show()


def build_heap(elements):
    nodes = [Node(e) for e in elements]
    for i in range(len(nodes) // 2):
        nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]


def get_color_gradient(num_colors):
    colors = list(mcolors.TABLEAU_COLORS.values())
    step = max(len(colors) // num_colors, 1)
    return colors[::step][:num_colors]


def dfs(root, order=[]):
    if root:
        order.append(root)
        dfs(root.left, order)
        dfs(root.right, order)
    return order


def bfs(root):
    queue = [root]
    order = []
    while queue:
        node = queue.pop(0)
        if node:
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return order


def visualize_traversal(order, title):
    colors = get_color_gradient(len(order))
    for i, node in enumerate(order):
        node.color = colors[i]
        draw_tree(root, i + 1, title)


if __name__ == '__main__':
    # Створення бінарної купи з елементів
    elements = [10, 15, 20, 17, 25]
    root = build_heap(elements)

    # Візуалізація DFS
    dfs_order = dfs(root)
    visualize_traversal(dfs_order, "DFS Traversal")

    # Візуалізація BFS
    bfs_order = bfs(root)
    # visualize_traversal(bfs_order, "BFS Traversal")
