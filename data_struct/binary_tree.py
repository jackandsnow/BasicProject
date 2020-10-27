class TreeNode(object):
    """
    Tree Node definition
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder_traverse_recu(root):
    """
    前序遍历（递归）
    """
    if root is None:
        return
    print(root.val)
    # 遍历左子树
    preorder_traverse_recu(root.left)
    # 遍历右子树
    preorder_traverse_recu(root.right)


def preorder_traverse_nonrecu(root):
    """
    前序遍历（非递归）
    """
    if root is None:
        return
    stack = [root]
    while stack:
        print(root.val)
        # 注意要先入栈右孩子，再入栈左孩子（先进后出）
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        root = stack.pop(-1)


def inorder_traverse_recu(root):
    """
    中序遍历（递归）
    """
    if root is None:
        return
    # 遍历左子树
    inorder_traverse_recu(root.left)
    print(root.val)
    # 遍历右子树
    inorder_traverse_recu(root.right)


def inorder_traverse_nonrecu(root):
    """
    中序遍历（递归）
    """
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            # 如果有左孩子，会一直入栈，直到叶子节点
            root = root.left
        # 出栈，然后处理右孩子
        root = stack.pop(-1)
        print(root.val)
        root = root.right


def backorder_traverse_recu(root):
    """
    后序遍历（递归）
    """
    if root is None:
        return
    # 遍历左子树
    backorder_traverse_recu(root.left)
    # 遍历右子树
    backorder_traverse_recu(root.right)
    print(root.val)


def backorder_traverse_nonrecu(root):
    """
    后序遍历（非递归）
    """
    if root is None:
        return
    stack1, stack2 = [root], []
    # 利用stack1找出后序遍历的逆序，并存入stack2
    while stack1:
        root = stack1.pop(-1)
        stack2.append(root)
        # 左孩子先入栈
        if root.left:
            stack1.append(root.left)
        # 右孩子后入栈
        if root.right:
            stack1.append(root.right)
    # 将stack2中的元素出栈，即为后序遍历顺序
    while stack2:
        node = stack2.pop(-1)
        print(node.val)


def layer_traverse(root):
    """
    层次遍历
    """
    if root is None:
        return
    queue = [root]
    while queue:
        # 取第一个（先进先出）
        node = queue.pop(0)
        print(node.val)
        # 左孩子入队
        if node.left:
            queue.append(node.left)
        # 右孩子入队
        if node.right:
            queue.append(node.right)


root = TreeNode(1)
a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(2)
d = TreeNode(5)
e = TreeNode(6)
root.left = a
root.right = b
a.left = c
a.right = d
b.right = e
# preorder_traverse_recu(root)
# inorder_traverse_nonrecu(root)
# backorder_traverse_nonrecu(root)
layer_traverse(root)
