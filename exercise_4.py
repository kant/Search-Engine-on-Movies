"""Using the dinamic programming we construct amatrix where all cell represent the length of the maximal subsequence 
of the substring of the original string identified by the row and column index, using the previus cells and filling the matrix by diagonal
we solve the problem in polinomial time."""

def LongestSubsequence(sequence):
    
    lenOfString = len(sequence) #take the length of the sequence
    table=[] #create empty list for going to create a table
    
    #create table with 0 (lenOfString x lenOfString)
    for x in range(lenOfString):
        table.append([])
        for y in range(lenOfString):
            table[x].append(0)

    #all single letter of lenght 1 recorded on the diagonal of the table
    for i in range(lenOfString):
        table[i][i] = 1
    
    #take the palindromes if length of these palindromes goes from 2 to 'lenOfString' and pick the longest one
    for diagonal in range(2, lenOfString+1):
        for i in range(lenOfString-diagonal+1):
            j = i + diagonal-1
            if sequence[i] == sequence[j]:
                if diagonal == 2:
                    table[i][j] = 2
                else:
                    table[i][j] = table[i][j-1]+2 #if the last and first character of this string are same , add 2 to the length
            else:
                table[i][j] = max(table[i][j-1], table[i+1][j]); #check and take one at a time and than take maximum
    
    #print the table
    for row in table:
          print(row)
    
    #return length of the longset subsequence
    return table[0][lenOfString-1]


LongestSubsequence('DATAMININGSAPIENZA')

