# from typing import List

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         for i in strs:
#             i.sort()
#             print(i)




# # Example usage
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# solution = Solution()
# result = solution.groupAnagrams(strs)
# print(result)

# list2 = [1, 2, 4, 5, 6, 7]
# list3 = ["kabir", 15, "yosha", 10]
# combined = "".join(list1)
# print(combined) #kabirrashmiyosha
# combine2 = " ".join(list1)
# print(combine2) #kabir rashmi yosha
# combine3 = ", ".join(list1)
# print(combine3)


# combine4 = (map(str, list2))
# combine4x = list(combine4)
# print(combine4x)

# list1 = ["tom", "mot", "yosha", "lol"]
# list2 = [1, 2, 4, 5, 6, 7]


# myMap = {}

# new = []
# for word in list1:
#             temp = ''.join(sorted(word))
#             if temp in myMap:
#                 myMap[temp].append(word)
#                 print(myMap)
#                 print("1")
#             else:
#                 myMap[temp] = [word]
#                 print(myMap)
#                 print("2")



# strs = ["flower","flow","flight"]
# output = ""
# for word in strs:
#     #print(word[0])
#     output += word[0]

# print(output)
    
        
    
    
# #     # if len(word[0]) == 1:
# #         output.append(word[0])
        
    
# # print(output)




# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
 
# # Use a for loop and an if statement to print just the capitals in the quote above.
# for char in quote:
#     if char.isupper():
# #         print(char)

# # divseven = range(0, 101, 7)
# # for i in divseven:
# #     print(i)


# # for i in range(0, 10):
# #     listy = []
# #     if i == 5:
# #         continue
# #     elif i == 8:
# #         break
# #     else:
# #         for j in range(0, 10):
# #             listy.append(i*j)
# #         print(listy)



# list1 = ["tom", "mot", "yosha", "lol"]

# # for i in range(len(list1)):
# #     for j in range(len(list1)):
# #         print(i,j)
# # print("------------------------------")
# # for i in list1:
# #     for j in list1:
# #         print([list1.index(i),list1.index(j))

# # while len(list1) >= 1:
# #     print(list1)
# #     list1.pop()

# # for i in range(0, 100, 7):
# #     if i != 0 and i % 11 == 0:
# #         break
# #     print(i)

# import random
# lowest = 0
# highest = 1000
# answer = random.randint(1,highest)
# print(answer)
# count = 0
# guess = 0
# flag = True

# while(flag):
    
#     middle = (highest + lowest) // 2
#     guess = input("my guess is {}, type h, l, or c if my guess is correct: ".format(middle)).casefold()
#     count += 1
#     if guess == "h":
#         lowest = middle + 1
#     elif guess == "l":
#         highest = middle - 1
#     elif guess == "c":
#         print("lets go champ, i got it in {} guesses".format(count))
#         break
#     else:
#         print("enter either h l or c")
    
        


# while(flag):
#     try:
#         guess = int(input("Guess the number between {} and {}, enter 0 if you want to quit: ".format(lowest, highest)))
#         count += 1

#         if guess > highest or guess < lowest:
#             print("mate is said between {} to {}". format(lowest, highest))
#             continue
#         if guess > answer:
#             highest = guess - 1
#             print("you guess is too high, guess again")
            
#         elif guess < answer:
#             lowest = guess + 1
#             print("your guess it too low, guess again")
            
#         elif guess == answer:
#             print("lucky mf u win, you took {} guesses".format(count))
#             flag = False
#         else:
#             print("mateyyyy i said guess between {} and {}".format(lowest, highest))
#     except ValueError:
#         print("mate i said a number, dont use letters")




            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            