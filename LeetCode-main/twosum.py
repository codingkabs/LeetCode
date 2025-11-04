# numbers = [2, 5, 7, 11, 29, 30]
# target = int(input("Enter a Target number: "))
# # length = len(numbers)

# # for i in numbers:
# #     for j in numbers:
# #         if i + j == target:
# #             length = len(numbers)
# #             print("number are: " + str(i) + " and "+ str(j))
# #             print("number index are: " + str() + " and " + str(len(numbers[j - 1])))
# #     break

# for i in range(len(numbers)):
#     for j in range(i+1, (len(numbers))):
#         sums = numbers[i] + numbers[j]
#         if sums == target:
#             print("numbers are " + str(numbers[i]) + " " + str(numbers[j]))
#             print("numbers are {0} {1}".format(numbers[i],numbers[j]))
#             print([i,j])
#     break
        
        
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         sum = nums[i] + nums[j]
#         if sum == target:
#             print("The numbers are: {0}, {1}".format(nums[i], nums[j])
        
# print (len(numbers))
# print(range(len(numbers)))








numbers = [2, 5, 7, 11, 29, 30]
target = int(input("Enter a Target number: "))


#2 sum problem so given a list, work out the the 2 numbers that equal into the target

for i in range(len(numbers)):
    for j in range(len(numbers)):
        total = numbers[i] + numbers [j]
        if total == target:
            print("the 2 numbers are {0} & {1}".format(numbers[i], numbers[j]))
            break
    else:
        continue
    break
else:
    print("LOL")
            
    






























