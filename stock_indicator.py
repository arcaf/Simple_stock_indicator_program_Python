
class Simple_Moving:
    
    def __init__(self, values, days):
        self._values = values[::1]
        self._days = days

        
    def execute(self):
        result = 0

        for i in range(len(self._values)):
            result+=float(self._values[i])
        new = result/self._days
        return new
            
class Directional_Moving:
    def __init__(self, values, days):
        self._values = values[::1]
        self._days = days
    def execute(self):
        result = []
        new_result = []
        sum_it1 = 0
        for i in range(len(self._values)):
            if i == 0:
                result.append(0)
            elif (float(self._values[i]) - float(self._values[i-1])) < 0:
                result.append(-1)
            else:
                result.append(1)

        for i in range(len(self._values)):
            if i < (self._days):
                sum_it1 += result[i]
                new_result.append(sum_it1)
                
            else:
                sum_it2 = 0
                for j in range(self._days):
                    sum_it2 += result[(i+1)-(self._days-j)]
                new_result.append(sum_it2)
        return new_result
        
