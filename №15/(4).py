Q = range(29,47+1) 
P = {48,52,56} 
  
def f(x,A): 
    return ((x%3!=0 and x not in P)<=((abs(x-50)<=7)<=(x in Q))) or (x & A == 0) 
    
for A in range(1,100): 
    if all(f(x,A) for x in range(100)): 
        print(A) 
        break
