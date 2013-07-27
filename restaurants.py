import json

class restaurants:
    def __init__(self):
        self.restaurants = {}
    def dumpDataFile(self, filename):
        # heh, he said dump
        # will always overwrite
        fh = open('./%s' % filename, 'w')
        fh.write(json.dumps(self.restaurants))
        fh.close()
    def loadDataFile(self, filename):
        # heh, he said load
        fh = open('./%s' % filename, 'r')
        output = fh.readlines()[0]
        fh.close()
        self.restaurants = json.loads(output)
    def add(self, name, location, flags=None, nick=None):
        # name = string
        # location = string
        # flags = list
        self.restaurants[name] = {} 
        self.restaurants[name]['location'] = location
        self.restaurants[name]['flags'] = flags
        self.restaurants[name]['nick'] = nick
    def mod(self, name, location=None, flags=None, nick=None):
        # Note: flags is a tuple here (['potential', 'new', 'flags'], 'a')
        #                             (['potential', 'new', 'flags'], 'w')
        if name in self.restaurants:
            if location:
                self.restaurants[name]['location'] = location
            if nick:
                self.restaurants[name]['nick'] = nick
            if flags:
                if flags[1] == 'a':
                    # append
                    self.restaurants[name]['flags'] = self.restaurants[name]['flags'] + flags[0]
                elif flags[1] == 'w':
                    self.restaurants[name]['flags'] = flags[0]
                else:
                    raise TypeError("flags is not in correct format")
        else: 
            raise IndexError("%s does not exist" % name)
