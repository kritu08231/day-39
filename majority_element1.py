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
    return majorityElement
    

givenNums = [1,3,2,1,1,3,3,3,3,]
print(majorityEle(givenNums))
