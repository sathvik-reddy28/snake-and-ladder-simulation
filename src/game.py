int def board:
    snakes={
        "16 " : "7 ",
        "60 " : "17 ",
        "63 " : " 19",
        "67 " : "30 ",
        " 87" : "24 ",
        " 93" : "69 ",
        " 95" : " 75",
        " 99" : " 77"
    }
    ladder={
        "9 " : "7 ",
        " 18" : "17 ",
        "25 " : " 19",
        "28 " : "30 ",
        "56" : "64",
        " 68" : "24 ",
        " 76" : "69 ",
        " 79" : " 75",
    }
    i=0
    count=0
    while i < 100:
        j=randint(1,6)
        count+=1
        i+=j
        for i in snakes
            i=snakes[i]
        for i in ladder
            i=ladder[i]
    
    if i==100
        return count

    
