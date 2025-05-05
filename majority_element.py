def majorityEle(givenNums):
    givenNums.sort()

    majorityElement = givenNums[0]
    maxCount = 0
    count = 1

    for i in range(len(givenNums)-1):
        if givenNums[i] != givenNums[i+1]:
            if maxCount < count:
                majorityElement = givenNums[i]
                maxCount = count
            count = 1
        else:
            count += 1
    if maxCount < count:
        majorityElement = givenNums[-1]

    return majorityElement

givenNums = [1,3,2,1,1]
print(majorityEle(givenNums))
