
    
def fibCalc(to = 10):
    a = 1
    b = 2
    while a < to: 
        yield (a) 
        a, b = b, a + b 
    
        
     

print (sum([i for i in fibCalc(4000000) if i % 2 == 0]))

    