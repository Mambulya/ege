f = open("24 варианты 1-5.txt") 
 s = f.read() 
 m = z = 0 
 start = 0 
 for i in range(len(s)): 
     if s[ i] == 'Z': 
         z += 1 
         if z == 1: 
             fz = i 
         elif z == 2: 
             sz = i 
         else: 
             if i - start > m: 
                 m = i - start 
                 beg_f = start 
                 end_f = i 
             start = fz + 1 
             fz = sz 
             sz = i 
             z = 2 
 print(m) 
 print(s[beg_f:end_f])
