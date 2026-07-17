def display(*args):
    print("received arguments:",args)
    print("Indivisual value:")
    for num in args:
        print(num)
display(10,20,30,40)

def show(**kwargs):
    print(" Employee details:")
    for key,value in kwargs.items():
        print(key,":",value)
show(name="firoz",id=101,salary=10000,course="bca")