# 15. Reverse a string

def rev_str(str):
    return str[::-1]

s=input("Enter a string:")
print(rev_str(s))

# output:
# Enter a string:Manju
# ujnaM

# # 16. Check for Palindrome String

def palindrome(str):
    p1=0
    p2=(len(str)-1)
    f=0
    while p1<p2:
        if str[p1]==str[p2]:
            p1+=1
            p2-=1
        else:
            f=1
            return False
    if f==0:
        return True

s=input("Enter a string:")
print(palindrome(s))

# output:
# Enter a string:madam
# True

# 17. Sum of Digits

def sum_0f_digits(num):
    res=0
    while num>0:
        digit=num%10
        res+=digit
        num//=10
    return res

n=int(input("Enter a number:"))
print(sum_0f_digits(n))

# output:
# Enter a number:123
# 6

# 18. Product of Digits

def product_of_digits(num):
    res=1
    while num>0:
        digit=num%10
        res*=digit
        num//=10
    return res

n=int(input("Enter a number:"))
print(product_of_digits(n))

# output:
# Enter a number:234
# 24

# 19. Armstrong number check

def armstrong_num_check(num):
    temp=num
    power=len(str(num))
    res=0
    while num>0:
        digit=num%10
        res+=digit**power
        num//=10

    if temp==res:
        return "Armstrong number"
    else:
        return "Not an Armstrong number"
    
n=int(input("Enter a number:"))
print(armstrong_num_check(n))

# output:
# Enter a number:153
# Armstrong number

# 20. Reverse a number

def rev_num(num):
    res=0
    while num>0:
        digit=num%10
        res=(res*10)+digit
        num//=10
    return res

n=int(input("Enter a number:"))
print(rev_num(n))

# output:
# Enter a number:1234
# 4321

# 21. Palindrome number check

def palin_num(num):
    temp=num
    res=0
    while num>0:
        digit=num%10
        res=(res*10)+digit
        num//=10
    if temp==res:
        return "Palindrome"
    else:
        return "Not a Palindrome"
    
n=int(input("Enter a number:"))
print(palin_num(n))

# output:
# Enter a number:1221
# Palindrome

# 22. neon number

def neon_num(num):
    temp=num**2
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit
        temp//=10
    if num==sum:
        return "Neon number"
    else:
        return "Not a neon number"

num=int(input("Enter a number:"))
print(neon_num(num))

# output:
# Enter a number:9
# Neon number

# # 23. strong number 

def strong_num(num):
    fact_sum=0
    temp=num

    while temp>0:
        digit=temp%10
        fact=1

        for i in range(1,digit+1):
            fact*=i
        fact_sum+=fact
        temp//=10

    if fact_sum==num:
        return "Strong number"
    else:
        return "Not a strong number"

num=int(input("Enter a number:"))
print(strong_num(num))

# output:
# Enter a number:145
# Strong number

# # 24. perfect number

def perfect(num):
    temp=num
    sum=0
    for i in range(1,temp):
        if temp%i==0:
            sum+=i
    if num==sum:
        return "Perfect number"
    else:
        return "Not a perfect number"
    
n=int(input("Enter a number:"))
print(perfect(n))

# output:
# Enter a number:28
# Perfect number

# 25. harshad number

def harshed(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit
        temp//=10
    if sum!=0 and num%sum==0:
        return "Harsed number"
    else:
        return "Not a harshed number"

num=int(input("Enter a number:"))
print(harshed(num))

# output:
# Enter a number:18
# Harsed number