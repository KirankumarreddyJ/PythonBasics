import module1 as m1
from module3 import m3_dic
name = "module2"
print(f"Hi I am {name} executed")

def sub(n1,n2):
    print(f'subtraction of {n1} and {n2} : '+ str((n1-n2)))

print(f"value of __name__ of module2:", __name__)

if __name__ == "__main__":
    sub(5,2)

m1.add(10, 20)
print(f"imported module name is {m1.name}")

print(f"Module1 vars & funs: {dir(m1)}")

print(f"Access only m3_dic from module3 : {m3_dic}")
