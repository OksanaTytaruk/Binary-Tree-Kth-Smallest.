class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):
    """
    Знаходить k-й найменший елемент
    у бінарному дереві пошуку (BST).

    У BST обхід Inorder (ліворуч -> корінь -> праворуч)
    дає значення у відсортованому порядку.
    """

    stack = []
    current = root

    while True:

        # Переходимо якомога далі вліво
        while current is not None:
            stack.append(current)
            current = current.left

        # Беремо наступний найменший елемент
        current = stack.pop()

        k -= 1

        # Якщо це k-й елемент,
        # повертаємо його значення
        if k == 0:
            return current.val

        # Переходимо до правого піддерева
        current = current.right


# ==========================================
# ТЕСТУВАННЯ
# ==========================================

# Приклад 1:
# Input:  root = [3,1,4,null,2], k = 1
# Output: 1

root1 = TreeNode(3)

root1.left = TreeNode(1)
root1.right = TreeNode(4)

root1.left.right = TreeNode(2)

print("Приклад 1:", kthSmallest(root1, 1))


# Приклад 2:
# Input:  root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

root2 = TreeNode(5)

root2.left = TreeNode(3)
root2.right = TreeNode(6)

root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)

root2.left.left.left = TreeNode(1)

print("Приклад 2:", kthSmallest(root2, 3))