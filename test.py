class  Test:
    def  __init__(self,eno,sal):
        self.eno=eno
        self.sal=sal
    def info(self):
        print(self.eno)
        print(self.sal)
        
        


Test(222,10000).info()