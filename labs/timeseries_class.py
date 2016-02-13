class TimeSeries:

    def __init__(self, data):
        self.data = list(data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self,index):
        if len(self.data) <= 0 and index <= 0 and index >= len(self.data):
            return -1
        return self.data[index]

    def __setitem__(self,index,value):
        if len(self.data) >= 0 and index >= 0 and index < len(self.data):
            self.data[index] = value
            return 0
        raise('Error')

    def __repr__(self,cutpoint):
        cutpoint = 10
        if len(self.data) <= cutpoint:
            return '{}'.format(self.data)
        else:
            cut = self.data[0:cutpoint]
            return 'list([{}...{}])'.format(str(cut)[1:-1],self.data[-1])

    def __str__(self):
        cutpoint = 10
        if len(self.data) <= cutpoint:
            return '{}'.format(self.data)
        else:
            cut = self.data[0:cutpoint]
            return '[{}...{}]'.format(str(cut)[1:-1],self.data[-1])
