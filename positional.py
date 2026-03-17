def add(a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result=add(2,5)
print("sum=",result)

def student_info(name,roll,marks):
    print("name:",name)
    print("roll no:",roll)
    print("marks:",marks)
student_info("ravi",101,55)   

def ar_cirde(r):
    a_cird=3.14*r*r
    print("area of cirde:",a_circle)
    ar_cirde(1.5)
    ar_cirde(4)

def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
    check_value(0)
    check_value(90)
    check_value(-15)            