public class Btree {

    int val;
    Btree left;
    Btree right;

    public Btree(int val) {
        this.val = val;
    }

    @Override
    public String toString() {
        if (null != this.left && null != left.right) 
            return "Val: " + this.val + "\nLeft: " + this.left.toString() + "\nRight: " + this.right.toString();
        else
            return "Val: " + this.val;
    }
}
