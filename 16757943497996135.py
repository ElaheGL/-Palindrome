user_enter = input()
smal_case = user_enter.lower()
user_enter_lis = []
for i in smal_case:
    user_enter_lis.append(i)
x = list(reversed(user_enter_lis))
if ( x == user_enter_lis):
    print('palindrome')
else:
    print('not palindrome')