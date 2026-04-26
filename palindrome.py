
s= input("Enter the string:- ")

# if s==s[::-1]:
#     print('it number is palindrome')
# else:
#     print('it is not palindrome number')



flag=True

for i in range (0, len(s)//2):
    s[i]!= s[len(s)-i-1]
    flag = False
    print("not palindrome")
    break

if flag:
    print("number is palindrome")




# flag= True

# for i in range(0,len(s)//2):
#     if s[i] != s[len(s)- i-1]:
#         flag=False
#         print("not palindrome")
#         break

# if flag:
#     print("Palindrome number")