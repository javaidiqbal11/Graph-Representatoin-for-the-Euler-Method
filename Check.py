# simple recursion case

def factorial(n):

    if n == 1:
        return 1

    else:
        return n * factorial(n-1)

print(factorial(5))

seen = [1,2,3,4]

print(seen[3])

seen= [False] * 5
print(seen)

seen[1] = True
print(seen)

for i in range(1,3):
    print(i)

n = [1, 2, 3]
def cool():
    for i in range(3):
        if(n[i] > 0):
            continue
        else:
            print("hi")
    print(1)

cool()

seen = []
edges = 7
for j in range(edges):
    seen.append(j)

print(seen)
