def greet(name,msg="good morning"):
    print ("hello",name+",",msg)
greet ("asha")
greet ("ravi","good evening")   

def power(num,exp=2):
    return num**exp
print(power(3))
print(power(3,3))
print(power(2,4))

def student_info(name,age=18,course="BCA"):
    print("name:",name)
    print("age:",age)
    print("course:",course)
student_info("ravi")
student_info("seema",20)
student_info("amit",19,"bscIT")