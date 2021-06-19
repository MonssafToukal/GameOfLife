import numpy as np

class Board:
    def __init__(self, size=10):
        self.size = size
        self.state = np.zeros((self.size, self.size), dtype=int)
    
    def init(self, initial_pos: list) -> None:
        [self.state[coord] := 1 for coord in initial_pos]

    def next_state(self) -> None:
        [[self.apply_rules(row, col) for col in range(self.size)] for row in range(self.size)]
        
    def apply_rules(self, row: int, col: int) -> None:
        self._apply_rule1(row, col)
        self._apply_rule2(row, col)
        self._apply_rule3(row, col)
        self._apply_rule4(row, col)
    
    def _apply_rule1(self, row: int, col: int) -> None:
        if not self._is_cell_alive(row, col):
            return
        if self._count_live_neighbors(row, col) < 2:
            self.state[row, col] = 0
    
    # This rule is a bit redundant, not really necessary 
    def _apply_rule2(self, row: int, col: int) -> bool:
        if not self._is_cell_alive(row, col):
            return
        if self._count_live_neighbors(row, col) in [2,3]:
            self.state[row, col] = 1

    def _apply_rule3(self, row: int, col: int) -> bool:
        if not self._is_cell_alive(row, col):
            return
        if self._count_live_neighbors(row, col) > 3:
            self.state[row, col] = 0

    def _apply_rule4(self, row: int, col: int) -> bool:
        if self._is_cell_alive(row, col):
            return
        if self._count_live_neighbors(row, col) == 3: 
            self.state[row, col] = 1
    
    def _is_cell_alive(self, row: int, col: int) -> bool:
        return bool(self.state[row,col]) 

    def _count_live_neighbors(self, row: int, col: int) -> int:
        offsets = [-1, 0,1]
        count = 0
        for i in offsets:
            for j in offsets:
                if i == 0 and j == 0:
                    continue
                try:
                    count += self.state[row + i, col + j]
                except Exception as e:
                    continue
        
        return count
                

