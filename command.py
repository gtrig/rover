class comproc():
    
    def __init__(self,*args,**kwargs):
        self.command_list = []
        self.map_x=0
        self.map_y=0

    def read(self,command):
        self.command_list = command.splitlines()
        self.command_list.reverse()
        self.map_x , self.map_y = self.getLine().split(' ') #get first line having the x y of the map

    def getRovData(self):
        rovPos = self.getLine().split(' ')
        rovMove = self.getLine()
        moves = [str(i) for i in rovMove]

        return [rovPos, moves]

    def getLine(self):
        return self.command_list.pop()