
# Executable
name = "module1"
print(f"Hi I am {name} executed")

def add(n1,n2):
    print(f'sum of {n1} and {n2} : '+ str((n1+n2)))


print(f"value of __name__ of module1:", __name__)

if __name__ == "__main__":
    add(5,2)