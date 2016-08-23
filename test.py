import unittest
from grid import process,is_alive,demo,main
def test_process():
    assert num_neighbour([[1,0,1],[0,1,1],[1,1,0]])== [[0, 0, 1], [0, 0, 1], [1, 1, 1]]
    assert is_alive([[1,1],[0,1]],0,1)== True
    assert demo(2)==[[0,0],[0,0]]
   # assert main([[1,0],[1,1]])==[[1, 1], [1, 1]]
#[[1, 1], [1, 1]]
#"OVER"
   # assert printer([[1,0],[1,1]])

    


    
