def main():
    max =1000
    for c in range(max):
        for b in range(max):
            for a in range(max):
                if a + b + c == max:
                    if isPytrip(a, b, c):
                        print(a,b,c)
    
def isPytrip(a,b,c):
       if a^2 + b^2 == c^2:
           return(True)
       else:
           return(False)
       
main()       
       