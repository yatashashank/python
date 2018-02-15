a = raw_input("Enter the string:\n")
words=a.split()
b=len(words)
if b%2 == 0 :
    mid=b/2
    print "Middle words are :", words[mid-1] ,words[mid]
else :
    mid=b/2
    print "Middle words are :", words[mid]
lword=''
long=0
for i in range(b):
    if len(words[i]) > long :
        lword = words[i]
        long=len(words[i])
print "Longest word in the sentence:", lword
print "Reverse all the words in sentence"
for i in range(b):
    print words[i][::-1],

