from entities.rover import Rover
from command import comproc

rov = Rover(x=0,y=1,heading='N')

command = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
1 1 N
MMLMRMM
"""

c = comproc()
c.read(command)
while len(c.command_list) != 0 :
    rovData = c.getRovData()
    rov = Rover(x=int(rovData[0][0]),y=int(rovData[0][1]),heading=rovData[0][2])
    rovMoves = rovData[1]
    for i in rovMoves:
        if(i=='M'):
            rov.move()
        else:
            rov.turn(i)
    
    print(rov.x , rov.y, rov.heading)