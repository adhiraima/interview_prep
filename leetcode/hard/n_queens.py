class Solution(object):
    def solveNQueens(self, n):
        rows = [] # containing the columns for the 
        solution = []
        self.solve(rows, solution, n)

        return solution

    def solve(self, rows, solution, n):
        print("Rows: ", str(len(rows)), " Board size: ", n)
        if len(rows) == n:
            # print("Matched Row, ", rows)
            solution.append(rows[:])
            return
        for i in range(0, n):
            if self.check_valid_pos(rows, i, n):
                rows.append(i)
                print("Position found: ", rows)
                self.solve(rows, solution, n)
            
    
    def check_valid_pos(self, rows, col, n):
        print("Validation: ", rows, " Iterating for column # ", col)
        if len(rows) == 0:
            return True
        else:
            for i in range(0, n):
                print(f"Checking column {i} for row # {len(rows)}")
                if i in rows:
                    return False
                print(f"Comparing {i} with {rows[-1] + 1} and {rows[-1] - 1}")
                if i != (rows[-1] + 1) and i != (rows[-1] - 1):
                    return True
                else:
                    return False
        print("outside of validations")
        return True 
        

def main():
    Solution().solveNQueens(4)

if __name__ == "__main__":
    main()