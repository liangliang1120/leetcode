class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in cols[c] or \
                    board[r][c] in rows[r] or \
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        # print(cols, rows, squares)
        return True


# java
class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> squares = new HashMap<>();

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char curr = board[r][c];
                if (curr == '.') {
                    continue;
                }
                if (cols.getOrDefault(c, new HashSet<>()).contains(curr) ||
                    rows.getOrDefault(r, new HashSet<>()).contains(curr) ||
                    squares.getOrDefault((r / 3) * 3 + c / 3, new HashSet<>()).contains(curr)) {
                    return false;
                }
                cols.computeIfAbsent(c, key -> new HashSet<>()).add(curr);
                rows.computeIfAbsent(r, key -> new HashSet<>()).add(curr);
                squares.computeIfAbsent((r / 3) * 3 + c / 3, key -> new HashSet<>()).add(curr);
            }
        }

        return true;
    }
}
