###################################################################
# Question 1
###################################################################
def is_palindrome(s):

    s = s.lower()

    if len(s) == 0 or len(s) == 1:
        return True

    if (s[0] == s[len(s)-1]):
        return is_palindrome(s[1:len(s)-1])

    else:
        return False

###################################################################
# Question 2
###################################################################
def find_min(a):

    if len(a) == 1:
        return a[0]

    if len(a) == 2:
        return min(a[0],a[len(a)-1])

    minimum = min(a[0], a[len(a)-1])

    if minimum == a[0]:
        return find_min(a[a.index(minimum):len(a)-1])

    elif minimum == a[len(a)-1]:
        return find_min(a[1:a.index(minimum)+1])

###################################################################
# Question 3
###################################################################
def reverso(a):

    if len(a) == 1:
        return a

    index = len(a)-1
    newList = []
    newList.append(a[index])
    b = reverso(a[:-1])

    for i in range(len(b)):
        newList.append(b[i])

    return newList

###################################################################
# Question 4
###################################################################
def tower(x):

    if (x == 1):
        return 2**1

    else:
        return 2 ** tower(x-1)

###################################################################
# Question 5
###################################################################
def helper(n, i):

    if (i == n):
        return True

    if (n % i == 0 and i !=n):
        return False

    else:
        return helper(n, i = i+1)

def is_prime(n):

    return helper(n, 2)
