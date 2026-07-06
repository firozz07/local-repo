def add (a:int,b:int)->int:
    return a+b
def greet(name:str)->str:
    return f"hello,{name}"
def average(number:list[float])->float:
    return sum(number)/len(number)
result=add(10,20)
message=greet("firoz")
average=average([12.3,33.3,6.7,9])
print("addition=",add)
print(message)
print("average=",average)