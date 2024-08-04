
import java.util.ArrayList;

public class Main {

    public static int getTreeHeight(Btree root) {
        if (root == null) {
            return 0;
        } else {
            int leftHeight = getTreeHeight(root.left);
            int rightHeight = getTreeHeight(root.right);
            return leftHeight > rightHeight ? leftHeight + 1 : rightHeight + 1;
        }
    }

    public static void bfs(Btree node, int level, ArrayList<Integer> result) {
        if (node == null) {
            return;
        } 
        if (level == 1) {
            System.out.println("Looping for " + node.val);
            result.add(node.val);
        } else if (level > 1) {
            bfs(node.left, level--, result);
            bfs(node.right, level--, result);
        }
    }

    public static void main(String[] args) {
        Btree root = new Btree(1);
        root.left = new Btree(2);
        root.right = new Btree(3);
        root.left.left = new Btree(4);
        root.left.right = new Btree(5);
        root.right.left = new Btree(6);
        root.right.right = new Btree(7);
        System.out.println("Root: " + root);

        int tHeight = getTreeHeight(root);

        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 1; i <= tHeight; i++) {
            bfs(root, i, result);
        }
        System.out.println("Hello :" + result);
    }
}
