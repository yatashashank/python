python=[]
web=[]
n=input("enter number of elements in list python")
m=input("enter number of elements in web")
print "Enter students list in python"
for i in range(n) :
    python.append(raw_input())
print "Enter students list in web"
for i in range(m) :
    web.append(raw_input())
a=set(python)
b=set(web)
print "List of students in common"
print a&b
print "List of students not common"
print a^b





