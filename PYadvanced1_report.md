  
전체 코드
------
```python
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
```

Problem
-------
  
```python
if a[number_counter] == answer:
    a_count+=1
if b[number_counter] == answer:
    b_count+=1
if c[number_counter] == answer:
    c_count+=1
```
  
이부분에서 문제를 맞힌 개수를 카운트하지 못하는 경우가 있었음.

Problem Solving
---------------

원래 코드
  
```python
if a[number_counter] == answer:
    a_count+=1
elif b[number_counter] == answer:
    b_count+=1
elif c[number_counter] == answer:
    c_count+=1
```

if와 elif의 차이 :
[Stack overflow](https://stackoverflow.com/questions/66504958/what-is-different-if-and-elif)

```python
x=1

if (x==1):
  print("Hi")
elif (x==1):
  print("Hi2")
```

```
result : Hi
```

```python
x=1

if (x==1):
  print("Hi")
if (x==1):
  print("Hi2")
```

```
result : Hi
         Hi2
```

한마디로 elif는 전의 if의 조건이 만족한다면 그 뒤에 위치해있는 elif는 씹힌다.
하지만 if 뒤에 if가 있는경우에는 전의 if의 조건이 만족하더라도 그 뒤에 if도 계산을 한다.
그래서 내가 아까 c_count 가 카운트되지 않았던것이다.
