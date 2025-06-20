#Data analysis; counting alpha caracter in list :

list = ['a','c','b','a','l','a','l']
count_alpha_of_a = 0
count_alpha_of_l = 0
n = print(len(list))
for list in list:
    if 'a' in list:
        count_alpha_of_a += 1
    if 'l' in list:
        count_alpha_of_l += 1

print("total alphas of a: ", count_alpha_of_a)
print("total alphas of b: ", count_alpha_of_l)


#list and retriving number greater than 10
number = [1,23,56,3,1,2,3,46]

for num in number:
    if num > 10:
        print(num)