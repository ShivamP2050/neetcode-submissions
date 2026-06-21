class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squ = collections.defaultdict(set)

        

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                quad = (int(r/3), int(c/3))
                if val.isdigit():
                    if cols[c]:
                        if val not in cols[c]:
                            cols[c].add(val)
                        else:
                            
                            return False
                    else:
                        cols[c].add(val)

                    if rows[r]:
                        if val not in rows[r]:
                            rows[r].add(val)
                        else:
                            print(cols[c])
                            return False
                    else:
                        rows[r].add(val)

                    if squ[quad]:
                        if val not in squ[quad]:
                            squ[quad].add(val)
                        else:
                            return False
                    else:
                        squ[quad].add(val)

        return True
                
                
                
        