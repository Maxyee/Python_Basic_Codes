class JustCounter:
    __secretCount = 0  # double underspace define the
    realCounter = 10

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.__secretCount) #
print(counter.realCounter)