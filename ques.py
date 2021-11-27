k = int(input('Input k'))
m = int(input('Input m'))

#first list
l1=[]
n = int(input('First list input'))
for i in range(0,n):
    ele = int(input())
    
    l1.append(ele)
    
#second list
l2=[]
x = int(input('Second List input'))
for i in range(0,x):
    ele = int(input())
    
    l2.append(ele)

#third list 
l3=[]
y = int(input('Third List input'))
for i in range(0,y):
    ele = int(input())
    
    l3.append(ele)

# calculation
sum = (pow(max(l1),2)+pow(max(l2),2)+pow(max(l3),2)) % m
 
print(sum)
