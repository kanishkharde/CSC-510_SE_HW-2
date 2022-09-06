import math
class Sym:
    def __init__(self, c, s):
        self.n = 0                  
        self.at = c if c else 0     
        self.name = s or ""         
        self._has = {}              
    
    def add(self, v):
        if v != "?":
            self.n += 1
            if v in self._has:
                self._has[v] +=1
            else:
                self._has[v] = 1

    def mid(self):
        most = -1
        for k, v in self._has.items():
            print((k,v))
            if v > most:
                mode = k
                most = v
        return mode

    def div(self):
        def fun(p):
            return p * math.log(p, 2)
        e = 0
        for _, _n in self._has.items():
            if _n > 0:
                e = e - fun(_n/self.n)
        return e
