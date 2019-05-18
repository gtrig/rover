class Rover:

    def __init__(self, *args, **kwargs):
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        self.heading = kwargs.get('heading', 'N')

    def turn(self, orientation):
        if(orientation=='L'):
            switcher = {
                'N':'W',
                'E':'N',
                'S':'E',
                'W':'S'
            }
        elif(orientation=="R"):
            switcher = {
                'N':'E',
                'E':'S',
                'S':'W',
                'W':'N'
            }

        self.heading = switcher.get(self.heading)
    
    def move(self):
        if(self.heading == 'N'):
            self.y+=1
        if(self.heading == 'S'):
            self.y-=1
        if(self.heading == 'E'):
            self.x+=1
        if(self.heading == 'W'):
            self.x-=1

