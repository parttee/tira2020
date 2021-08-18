from collections import namedtuple


def diff(node):
    if not node:
        return 0

    l = nodeSum(node.left)
    r = nodeSum(node.right)

    return max(abs(l - r), diff(node.left), diff(node.right))


def nodeSum(node):
    if not node:
        return 0

    return 1 + nodeSum(node.left) + nodeSum(node.right)


if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,
                Node(
                    Node(None, None),
                    Node(None, None)))
    print(diff(tree))  # 3
    print(diff(Node(None, None)))  # 0
    print(diff(Node(Node(None, None), Node(None, None))))  # 0
    print(diff(Node(Node(Node(Node(Node(None, None), None), None), None),
                    Node(Node(Node(Node(Node(None, None), None), None), None), None))))  # 4
    print(diff(Node(Node(None, Node(None, Node(None, None))),
                    Node(Node(Node(None, Node(None, Node(None, Node(None, None)))), None), None))))  # 5

    # Node(left=Node(left=None, right=Node(left=None, right=Node(left=None, right=None))),
    #      right=Node(left=Node(left=Node(left=None, right=Node(left=None, right=Node(left=None, right=Node(left=None, right=None)))), right=None), right=None))
