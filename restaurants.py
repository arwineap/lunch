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
    def add(self, name, location, flags):
        # name = string
        # location = string
        # flags = list
        self.restaurants[name] = {} 
        self.restaurants[name]['location'] = location
        self.restaurants[name]['flags'] = flags
