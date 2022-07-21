# roombuilder, builds rooms from text file

class Room:
    # define an initializer that takes fielanem
    def __init__(self,filename):
        # reads in the filename The idea is to use
        # *.txt and then just read the description
        # and navigate around different file names
        self.filename = filename
        self.getRoomInfo() # automatically reads when room is made

    def getRoomInfo(self):
        roominfo = []
        with open(self.filename,'r') as file:
            for e in file:
                if e[0:7] in e: # start of every text file <START>
                    roominfo.append(e) # append string
        print(str(roominfo[0])[8::]+"\n//")

    def getRoomDesc(self,filename): # seperate file
        roomdesc = []
        with open(filename,'r') as file:
            for e in file:
                print(e.strip())
    
    
            
                
                
                
                
            
        
        
        
