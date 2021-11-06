class Cycle:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def current(self):
        return self.data[self.index]

    def next(self):
        if self.index == len(self.data) - 1:
            self.index = 0
        else:
            self.index += 1
        return self.data[self.index]

    def prev(self):
        if self.index == 0:
            self.index = len(self.data) - 1
        else:
            self.index -= 1
        return self.data[self.index]
