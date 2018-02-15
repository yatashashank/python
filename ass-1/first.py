import re
p=raw_input("enter a password : ")
if len(p)>16 or len(p)<6 :
    print "not a valid password. Make sure length of password should be in range 6-16 characters"
elif p.isalnum()==True :
    print"not a valid password. should contain atleat one digit"
elif not re.search("[[$@!*]",p):
    print " not a valid password. Make sure it contain atleast one of this $@!* special charceter"
elif not re.search("[a-z]",p) :
    print " not a valid password. Make sure it contain atleast one lower case letter"
elif not re.search("[A-Z]",p):
    print " not a valid password. Make sure it contain atleast one upper case letter"
elif re.search("\s",p):
    print "not a valid password. Make sure there is no spaces "
else :
    print "valid password"

