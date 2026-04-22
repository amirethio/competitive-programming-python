strs = ["flower","flower","flower","flower"]
word = strs[0]
string = ""
end = 1
stop = False
temp = ""
for j in range(0,len(word)):
    for i in range(1 , len(strs)):
        if(word[0:end] != strs[i][0:end]):
           stop = True
           break
    if(stop):
        break
    end +=1
string = word[0:end-1]
print(string)




#     if(word[start:end] in strs[1] and word[start:end] in strs[2]):
#         temp = word[start:end]
#         end +=1
#     else:
#         start += 1
#         end= start + 1
#         break
#     if(len(temp) > len(string)):
#             string = temp    
# print(string)


