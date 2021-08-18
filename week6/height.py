from collections import namedtuple


def korkeus(solmu):
    if not solmu:
        return -1

    return 1 + max(korkeus(solmu.left), korkeus(solmu.right))


if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree1 = Node(None,
                 Node(Node(None, None), Node(None, Node(None, None))))
    tree2 = Node(Node(Node(None, None), Node(None, None)), None)
    tree3 = Node(None, Node(Node(None, None), Node(
        None, Node(Node(None, None), None))))
    print(korkeus(tree1))
    print(korkeus(tree2))
    print(korkeus(tree3))
    print(korkeus(Node(None, None)))
