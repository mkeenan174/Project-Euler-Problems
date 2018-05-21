
def find(num):
    for i in range(2,21):
        if num % i != 0:
            return False 
        
    return True

num = 20
while True:
    if find(num):
        break 
    num += 20
    
    
print(num)