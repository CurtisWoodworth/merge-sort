from random import getrandbits


class SampleMaker:

    def __init__(self):
        self.list_10 = []
        self.list_100 = []
        self.list_1000 = []
        self.list_x = []

    def make_sample_10(self):
        i = 0
        while i < 10:
            self.list_10.append(getrandbits(10))
            i += 1
        print(self.list_10)
        return self.list_10

    def make_sample_100(self):
        i = 0
        while i < 100:
            self.list_100.append(getrandbits(10))
            i += 1
        print(self.list_100)
        print(len(self.list_100))
        return self.list_100

    def make_sample_1000(self):
        i = 0
        while i < 1000:
            self.list_1000.append(getrandbits(10))
            i += 1
        print(self.list_1000)
        print(len(self.list_1000))
        return self.list_1000

    def make_sample_x(self, x):
        i = 0
        while i < x:
            self.list_x.append(getrandbits(10))
            i += 1
        print(self.list_x)
        print(len(self.list_x))
        return self.list_x
