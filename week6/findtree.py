from collections import namedtuple


def count(node1, node2):

    cnt = 0

    if node2 is not None:
        if isSame(node1, node2):
            cnt = 1
        else:
            cnt += count(node1, node2.left)
            cnt += count(node1, node2.right)

    return cnt


def isSame(node1, node2):
    if node1 == node2:
        return True
    if node1 is not None and node2 is not None:
        return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
    return False


if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree1 = Node(Node(None, None), Node(None, None))
    tree2 = Node(None, Node(Node(None, None), Node(None, None)))
    print(count(tree1, tree2))  # 1
    tree1 = Node(Node(None, None), Node(None, None))
    tree2 = Node(None, Node(Node(None, None), Node(Node(Node(None, None), Node(
        None, None)), Node(Node(None, None), Node(None, None)))))
    tree1 = Node(Node(None, None), Node(None, None))
    tree2 = Node(tree1, Node(Node(tree1, tree1), Node(None, None)))
    print(count(tree1, tree2))  # 1
