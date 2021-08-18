from collections import namedtuple


def f(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def ncr(n, k):
    # n!/(k! * (n-k)!)
    return f(n) // (f(k) * f(n - k))


def count(node):
    t = results(node)
    return t[1]


def results(node):
    if not node.left and not node.right:
        return (1, 1)

    lc = (0, 0)
    if node.left:
        lc = results(node.left)

    rc = (0, 0)
    if node.right:
        rc = results(node.right)

    nodes = rc[0] + lc[0]

    if node.left and node.right:
        return (1 + nodes, ncr(nodes, max(rc[0], lc[0])) * lc[1] * rc[1])

    return (1 + nodes, rc[1] if rc[0] else lc[1])


if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None, Node(Node(None, None), Node(None, None)))
    print(count(tree))  # 2

    tree = Node(Node(Node(Node(Node(None, None),
                               Node(Node(None, None), None)), None), Node(Node(None, None), None)), None)
    print(count(tree))  # 63

    tree = Node(Node(Node(None, None), None), Node(None, Node(
        None, Node(None, Node(None, Node(None, None))))))  # 21

    print(count(tree))

    # Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None),
    #       right=Node(left=Node(left=None, right=None), right=None)), right=None), right=Node(left=Node(left=None, right=None), right=None)), right=None)
    # 63
