class List():

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return self.data.__repr__

    def get_item(self, index):
        return self.data[index]
    