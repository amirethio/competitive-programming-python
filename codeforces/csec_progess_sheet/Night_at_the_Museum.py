

# pointer to xero  and  25 - index

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = input()
result = 0
pointer = 0

for i in range(len(word)):
    index = letter.index(word[i])
    move1 = abs(pointer - index)
    if(pointer > index):
        move2 = index + ((26 - pointer))
    else:
        move2 =  pointer + ((26 - index))
    pointer = index
    result += min(move1 ,move2)
print(result)




# pointer = 25
# move 1  = > 
# for i in word:
#     index = letter.index(i)
#     no = min((pointer + (26-index)) , pointer - index)
#     pointer = index
#     print((pointer + (26-index)) , (pointer - index))
#     result += no
# print(result)