import unittest

from gof import get_neighbors_of,over3_neighbors_die



class GameOfLifeTest(unittest.TestCase):
    def test_get_neighbors_of_cell_1_2_should_return_neighbors(self):
        cell = (1, 2)
        result = get_neighbors_of(cell)
        expected = {(0,1),(0,2),(0,3),
                    (1,1),(1,3),
                    (2,1),(2,2),(2,3)}
        self.assertEqual(result, expected)

    def test_rule3_is_neighbors_over3_should_i_die(self):
        board = {
             (2,3), (3,1), (3,3), (2,2), (3, 2),(2, 1)
            }
        cell = (2,2)
        result = over3_neighbors_die(board, cell)

        expected = {
             (2,3), (3,1), (3,3), (3, 2),(2, 1)
            }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
