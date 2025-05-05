def majorityEle(givenNums):
    majorityElement= -1
    votes = 0
    for i in givenNums:
        if votes ==0 :
            majorityElement=i
            votes  =1
        else:
            if majorityElement==i:
                votes  +=1
            else:
                votes -=1
    votes = 0
    for i in givenNums:
        if majorityElement==i:
            votes +=1
    if votes > len(givenNums)//2:
        return majorityElement
    return -1

givenNums = [1,1,1,1,2,2,2,2,2]
print(majorityEle(givenNums))
