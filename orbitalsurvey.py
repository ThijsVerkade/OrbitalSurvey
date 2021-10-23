def decimalToBinary(decimal):
    return "{0:b}".format(decimal)

def binaryToList(binary):
    return list(map(int, str(binary)))

def getHighestPointRows(rows):
    counter=0
    for x in rows:
        if x == 0:
            return counter
        counter += 1
    return counter

def parseRows(binaryList ,start, end):
    return binaryList[start:end]

def parseColumns(rows, row):
    column=[]
    for x in rows:
        column.insert(0,x[row])
    return column

def generateTable(binaryList, rows, columns):
    allRows=[]
    for x in range(rows):
        start=x*columns
        end=(x+1)*columns
        allRows.append(parseRows(binaryList,start,end))
    return allRows

def getHighestPoint(rows, columns, decimal):
    binary=decimalToBinary(decimal)
    amountCols=rows*columns

    if(amountCols > len(binary)):
        binary=(amountCols-len(binary))*"0"+str(binary)
    else:
        binary[0:amountCols]

    binaryList=binaryToList(binary)
    highestPoint=0

    allRows=generateTable(binaryList, rows, columns)

    for x in range(len(allRows)):
        newPoint=getHighestPointRows(parseColumns(allRows, x))
        if(newPoint > highestPoint):
            highestPoint = newPoint

    return highestPoint

if __name__ == '__main__':   
    rows = int(input())
    columns = int(input())
    decimal = int(input())
    
    print(getHighestPoint(rows, columns, decimal))

