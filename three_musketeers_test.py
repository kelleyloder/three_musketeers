# The Three Musketeers Game Test File
# by Kelley Loder and Ted Fujimoto

import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual((2, 2), string_to_location('C3'))
        self.assertEqual((0, 4), string_to_location('A5'))
        self.assertEqual((4, 0), string_to_location('E1'))

    def test_location_to_string(self):
        self.assertEqual('C3', location_to_string((2, 2)))
        self.assertEqual('B4', location_to_string((1, 3)))
        self.assertEqual('D2', location_to_string((3, 1)))

    def test_at(self):
        self.assertEqual(_, at((0, 0)))
        self.assertEqual('R', at((1, 2)))
        self.assertEqual('M', at((2, 2)))

    def test_all_locations(self):
        self.assertEqual(25, len(all_locations()))
        self.assertEqual(True, (1, 2) in all_locations())
        self.assertEqual(False, (5, 5) in all_locations())
        self.assertEqual(True, (0, 0) in all_locations())

    def test_adjacent_location(self):
        self.assertEqual((1, 1), adjacent_location((1, 2), 'left'))
        self.assertEqual((2, 4), adjacent_location((2, 3), 'right'))
        self.assertEqual((4, 2), adjacent_location((3, 2), 'down'))
        self.assertEqual((3, 5), adjacent_location((4, 5), 'up'))

    def test_is_legal_move_by_musketeer(self):
        self.assertEqual(False, is_legal_move_by_musketeer((0, 3), "left"))
        self.assertEqual(True, is_legal_move_by_musketeer((2, 2), "up"))
        self.assertEqual(True, is_legal_move_by_musketeer((2, 2), "right"))

    def test_is_legal_move_by_enemy(self):
        self.assertEqual(True, is_legal_move_by_enemy((2, 1), "left"))
        self.assertEqual(False, is_legal_move_by_enemy((2, 3), "left"))
        self.assertEqual(False, is_legal_move_by_enemy((3, 1), "up"))

    def test_is_legal_move(self):
        self.assertEqual(True, is_legal_move((2, 2), "up"))
        self.assertEqual(False, is_legal_move((3, 1), "up"))
        self.assertEqual(True, is_legal_move((2, 2), "right"))
        self.assertEqual(False, is_legal_move((0, 3), "down"))

    def test_can_move_piece_at(self):
        self.assertEqual(True, can_move_piece_at((2, 2)))
        self.assertEqual(False, can_move_piece_at((0, 3)))
        self.assertEqual(True, can_move_piece_at((1, 2)))

    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        set_board([ [R, R, R, R, M],
                    [R, R, R, R, R],
                    [R, R, M, R, R],
                    [R, R, R, R, R],
                    [M, R, R, R, R] ] )
        self.assertTrue(has_some_legal_move_somewhere('M'))
        self.assertFalse(has_some_legal_move_somewhere('R'))
        set_board([ [_, _, R, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertTrue(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))

    def test_possible_moves_from(self):
        self.assertEqual([], possible_moves_from((0, 3)))
        self.assertEqual(['left', 'up'], possible_moves_from((1, 2)))
        self.assertEqual([], possible_moves_from((0, 0)))


    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(can_move_piece_at((1, 4)))
        self.assertTrue(can_move_piece_at((2, 2)))
        self.assertFalse(can_move_piece_at((0, 4)))

    def test_is_legal_location(self):
        self.assertTrue(is_legal_location((0, 0)))
        self.assertFalse(is_legal_location((5, 5)))
        self.assertFalse(is_legal_location((0, 5)))
        self.assertTrue(is_legal_location((4, 0)))
        self.assertTrue(is_legal_location((2, 2)))
        self.assertFalse(is_legal_location((-1, 3)))

    def test_is_within_board(self):
        self.assertTrue(is_within_board((0, 0), "right"))
        self.assertFalse(is_within_board((0, 0), "up"))
        self.assertTrue(is_within_board((2, 2), "down"))
        self.assertFalse(is_within_board((4, 0), "left"))

    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )

        self.assertEqual(all_possible_moves_for('R'), [((0, 2), "down"), ((0, 2), "left")])
        self.assertEqual(all_possible_moves_for('M'), [((0, 3), "left"), ((0, 3), "right"), ((1, 4), "up")])

    def test_make_move(self):
        make_move((1, 3), "left")
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, M, _, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ], get_board())

        make_move((4, 3), "up")
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, M, _, _],
                           [_, R, M, R, _],
                           [_, R, _, R, _],
                           [_, _, _, _, _] ], get_board())

        make_move((3, 1), "right")
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, M, _, _],
                           [_, R, M, R, _],
                           [_, _, R, R, _],
                           [_, _, _, _, _] ], get_board())

    def test_choose_computer_move(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual(choose_computer_move('M'), ((0, 3), "left"))
        self.assertEqual(choose_computer_move('R'), ((0, 2), "down"))

    def test_is_enemy_win(self):
        self.assertFalse(is_enemy_win())

        set_board([ [_, _, R, _, R],
                    [_, _, M, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())

        set_board([ [_, _, R, M, R],
                    [_, _, _, M, _],
                    [_, _, _, M, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())

unittest.main()
