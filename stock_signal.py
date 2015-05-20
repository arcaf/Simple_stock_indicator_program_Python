class Signal_Simple_moving:
    def __init__(self, days, values, indicator, buy, sell):
        self._days = days
        self._values = values
        self._indicator = indicator
        self._buy = buy
        self._sell = sell

    def execute(self):
        result = []
        del self._indicator[-1]
        for i in range(self._days-1):
            self._indicator.insert(i, 0)
        for i in range(len(self._values)):
            if i <= (self._days):
                result.append(' ')
            else:
                if float(self._values[i]) > self._indicator[i] and float(self._values[i-1]) < self._indicator[i-1]:
                    result.append('BUY')
                    
                elif float(self._values[i]) < self._indicator[i] and float(self._values[i-1]) > self._indicator[i-1]:
                    result.append('SELL')
                else:
                    result.append(' ')

        return result
class Signal_Directional:
    def __init__(self, days, values, indicator, buy, sell):
        self._days = days
        self._values = values
        self._indicator = indicator
        self._buy = buy
        self._sell = sell
    def execute(self):
        new_result = []
        for n in range(len(self._values)):
            if n == 0:
                new_result.append('   ')
            elif int(self._buy) < int(self._values[n]) and int(self._buy) >= int(self._values[n-1]):
                new_result.append('BUY')
            elif int(self._sell) > int(self._values[n]) and int(self._sell) <= int(self._values[n-1]):
                new_result.append('SELL')
            else:
                new_result.append('   ')
        return new_result
