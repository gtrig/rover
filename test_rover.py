import unittest
from entities.rover import Rover
from command import comproc

class TestRover(unittest.TestCase):
    def test_turn(self):
        rov = Rover(x=5,y=5,heading='S')
        rov.turn('L')
        self.assertEqual(rov.heading,'E')
        
        rov.turn('R')
        self.assertEqual(rov.heading,'S')

    def test_move(self):
        rov = Rover(x=5,y=5,heading='N')
        rov.move()
        self.assertEqual(rov.y,6)

        rov.turn('L')
        rov.turn('L')
        rov.move()

        self.assertEqual(rov.y,5)

    def test_rov(self):
        command = """5 5
4 5 S
LMLMLMLMM
3 3 E
MMRMMRMRRM
1 1 N
MMLMRMM
"""

        c = comproc()
        c.read(command)
        rovData = c.getRovData()
        rov = Rover(x=int(rovData[0][0]),y=int(rovData[0][1]),heading=rovData[0][2])

        self.assertEqual(rov.x,4)
        self.assertEqual(rov.y,5)
        self.assertEqual(rov.heading,'S')

if __name__=='__main__':
    unittest.main()