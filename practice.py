def max_num(a,b,c):
    i=0
    if a>i:
        i=a
    if b>i:
        i=b
    if c>i:
        i=c
    return print(i) 

max_num(4,44,4)

def mult_list(num,i=0):
    if i == len(num)-1:
        return num[i]
    else:
        return num[i]*mult_list(num,i+1)

print(mult_list([5,3,5,2]))

def rev_string(str, i=0):
    if i == len(str)-1:
        return str[0]
    else:
        return str[-1-i] + rev_string(str,i+1)

print(rev_string("kaisensei"))

def num_within(num,a,b):
    for i in range(a,b,1):
        if num == i:
            return True
    return False
print(num_within(10,2,4))

def pascal(n):
    for row in range(1, n+1):
        container = [1]
        [container.append(container[element-1] * (row - element) // element) for element in range(1, row)]
        print(' '.join(str(number) for number in container))

pascal(15)


'''
output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1 
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1

'''    
                                                