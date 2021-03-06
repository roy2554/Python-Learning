a=[1,2,3,4,5,1,2,3,4,5]
b=[2,1,2,3,2,4,2,5,2,1]
c=[3,3,1,1,2,2,4,4,5,5]

a_count = 0
b_count = 0
c_count = 0

answer_whatnumber=int(input("Enter Answer count : "))

number_counter = 0

for i in range(answer_whatnumber):
    answer=int(input("Enter Answer : "))
    
    if a[number_counter] == answer:
        a_count+=1
    if b[number_counter] == answer:
        b_count+=1
    if c[number_counter] == answer:
        c_count+=1

    number_counter+=1

print(a_count)
print(b_count)
print(c_count)

maxesanswer=max(a_count,b_count,c_count)

print("\n")

check=0

if a_count == maxesanswer and b_count == maxesanswer:
    print("a,b")
    check+=1
if a_count == maxesanswer and c_count == maxesanswer:
    print("a,c")
    check+=1
if b_count == maxesanswer and c_count == maxesanswer:
    print("b,c")
    check+=1
if a_count == maxesanswer and b_count == maxesanswer and c_count == maxesanswer:
    print("a,b,c")
    check+=1
if check==0:
    if a_count == maxesanswer:
        print("a")
    elif b_count == maxesanswer:
        print("b")
    elif c_count == maxesanswer:
        print("c")