def minmax(x):
    new = []
    max = 0
    min = 0

    for i in x:
        new.append(i)
    
    max = new[0]
    min = new[0]
 
    y = 0
 

    for i in new:
      
        if (new[y] / max) > 1:
            max = new[y]
        if (min / new[y]) > 1:
            min = new[y] 
        y += 1


        
    

    return min, max


print(minmax([123, 44, 66, 500]))