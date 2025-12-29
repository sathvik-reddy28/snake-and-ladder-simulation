import random
def board():
    snakes={
         16 : 7,
         60 : 17,
         63 : 19,
         67 : 30,
         87 : 24,
         93 : 69,
         95 : 75,
         99 : 77

    }
    ladder={
        9  : 7,
        18 : 17,
        25 : 19,
        28 : 30,
        56 : 64,
        68 : 24,
        76 : 69,
        79 : 75
    }
    i=0
    count=0
    while i<100:
        j=random.randrange(1,7)
        count+=1
        if i+j >100 :
            i+=0
        else:
            i+=j
        
        for k in snakes:
            if i==k :
                i=snakes[k]
        for k in ladder:
            if i==k :
                i=ladder[k]
     

    return count

print(board() ) 
