from btree import Btree

def insertion_sort(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            curr = arr[i + 1]
            idx = i + 1
            while idx > 0 and arr[idx - 1] > curr:
                arr[idx] = arr[idx - 1]
                idx -= 1
            arr[idx] = curr

def btrr_to_array(root: Btree):
    """
    This method would require a breadth first traversal/search of the array to put values to the array
    """
    result = []
    height = get_tree_height(root)
    for i in range(1, height + 1):
        bfs(root, result, 1)
    return result

def get_tree_height(node: Btree):
    if node is None:
        return 0
    else:
        lheight = get_tree_height(node.left)
        rheight = get_tree_height(node.right)
        return lheight + 1 if lheight > rheight else rheight + 1

def bfs(node: Btree, result, level):
    if node is None:
        return
    if level == 1:
        print(f"Node Value: {node.val}")
        result.append(node.val)
    elif level > 1:
        bfs(node.left, result, level - 1)
        bfs(node.right, result, level - 1)

def main():
    arr = [3, 4, 5, 1, 2, 9, 8, 6, 7]
    print(f"Before sorting: {arr}")
    insertion_sort(arr)
    print(f"After Sorting: {arr}")
    root = Btree(1)
    root.left = Btree(2)
    root.left.left = Btree(4)
    root.left.right = Btree(5)
    root.right = Btree(3)
    root.right.left = Btree(6)
    root.right.right = Btree(7)

    print(f"The tree to arr: {btrr_to_array(root)}")


if __name__ =="__main__":
    main()
