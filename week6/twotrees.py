from collections import namedtuple


def same(node1, node2):
    if not node1 and node2:
        return False

    if not node2 and node1:
        return False

    if node1 == node2:
        return True

    return same(node1.left if node1 else None, node2.left if node2 else None) and same(node1.right if node1 else None, node2.right if node2 else None)


if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree1 = Node(None, Node(Node(None, None), Node(None, None)))
    tree2 = Node(Node(Node(None, None), Node(None, None)), None)
    tree3 = Node(None, Node(Node(None, None), Node(None, None)))
    print(same(tree1, tree2))  # False
    print(same(tree1, tree3))  # True
    print(same(tree2, tree3))  # False
