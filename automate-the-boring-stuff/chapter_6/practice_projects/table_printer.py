def printTable(tableData):
    colWidths = [0] * len(tableData)
    columns = len(tableData)
    rows = len(tableData[0])

    # Finding the max width for each column
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])

    # Print table
    for i in range(rows):
        for j in range(columns):
            result = tableData[j][i].rjust(colWidths[j] + 1, ' ')
            print(result, end="")
        print()


tableData = [
                ['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']
            ]

printTable(tableData)
