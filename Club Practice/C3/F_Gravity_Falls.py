# only based on the remaining falling rows

class Row:
    def __init__(self,index,length,values):
        self.index = index
        self.length = length
        self.values = values
    


t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(t):
        k, *a = map(int, input().split())
        row = self.Row(i,len(a),a)
        print(row)