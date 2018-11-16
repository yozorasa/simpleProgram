import numpy as np
while 1:
    pNum = int(input("How many people? "))
    tNum = int(input("How many groups will people Divide into? "))
    mode = int(input("Choose mode 1 or 2? "))
    while mode != 1 and mode != 2:
        mode = int(input("Choose mode 1 or 2? "))
    
    if mode == 1:
        member = np.arange(pNum)
        np.random.shuffle(member)
        print(member)

        group = []
        for i in range(tNum):
            group.append([])
        
        for i in range(pNum):
            group[i%tNum].append(member[i])
        
    elif mode == 2:
        member = np.zeros((pNum))
        m = 0
        for i in range(tNum):
            if i < pNum%tNum:
                mNum = int(pNum/tNum) + 1
            else:
                mNum = int(pNum/tNum)
            for j in range(mNum):
                member[m] = i
                m += 1

        np.random.shuffle(member)
        print(member+1)
            
        group = []
        for i in range(tNum):
            group.append([])

        for i in range(pNum):
            group[int(member[i])].append(i)
    
    i = 0
    for team in group:
        print()
        i += 1
        print("Group", str(i), ">", end = "")
        for person in team:
            print("%4d"%person, end = "")
    print()
    print("==================================")