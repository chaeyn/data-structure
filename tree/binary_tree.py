# 이진트리를 위한 노드 클래스
class TNode:
    def __init__(self, elem, left, right):
        self.data = elem
        self.left = left
        self.right = right


# 이진트리의 전위순회
def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)


# 이진트리의 중위순회
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)


# 이진트리의 후위순회
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


# 이진트리의 레벨순회
from circular_queue import CircularQueue

def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)


# 이진트리의 노드 수 계산
def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)


# 이진트리의 단말노드 수 계산
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)


# 이진트리의 트리의 높이 계산
def calc_height(n):
    if n is None: return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1


# 이진 트리 연산 테스트 프로그램
if __name__ == "__main__":
    # print("\n======= 이진트리 테스트 ===================================")
    # d = TNode('D', None, None)
    # e = TNode('E', None, None)
    # b = TNode('B', d, e)
    # f = TNode('F', None, None)
    # c = TNode('C', f, None)
    # root = TNode('A', b, c)

    print("\n======= 수식 표기 테스트 ===================================")

    n = TNode('2', None, None)
    m = TNode('3', None, None)
    k = TNode('8', None, None)
    l = TNode('2', None, None)
    i = TNode('/', k, l)
    j = TNode('3', None, None)
    g = TNode('-', i, j)
    h = TNode('*', m, n)
    root = TNode('+', g, h)

    print('\n   In-Order : ', end='')
    inorder(root)
    print('\n  Pre-Order : ', end='')
    preorder(root)
    print('\n Post-Order : ', end='')
    postorder(root)
    print('\nLevel-Order : ', end='')
    levelorder(root)
    print()

    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 단말의 개수 = %d개" % count_leaf(root))
    print(" 트리의 높이 = %d" % calc_height(root))

