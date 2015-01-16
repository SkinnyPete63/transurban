class Classification:
    def __init__(self, csid = '', classif = '', desc = '', level = 0, map = []):
        self.csid = csid
        self.classif = classif
        self.desc = desc
        self.level = level
        self.map = map
        

myclass = Classification()
myclass.desc = 'New description'
print myclass.desc
