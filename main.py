def convert(s, numRows):
    whichRow = 0
    stringIndex = 0
    direction = 1

    #initialize output
    output = []
    for each in range(numRows):
        output.append('')

    while stringIndex < len(s):
        output[whichRow] += (s[stringIndex])
        stringIndex += 1
        whichRow += direction
        if whichRow == numRows - 1:
            direction = -1
        if whichRow == 0:
            direction = 1

    outputString = ""
    for each in output:
        outputString += str.join('', each)
    return outputString

#Example 1:
#Input: 
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))
#Output: "PAHNAPLSIIGYIR"
#Explanation:
#P   A   H   N
#A P L S I I G
#Y   I   R

#Example 2:
#Input: 
s = "PAYPALISHIRING"
numRows = 4
print(convert(s, numRows))
#Output: "PINALSIGYAHRPI"
#Explanation:
#P     I    N
#A   L S  I G
#Y A   H R
#P     I

#Example 3:
#Input: 
s = "A"
numRows = 1
print(convert(s, numRows))
#Output: "A"
