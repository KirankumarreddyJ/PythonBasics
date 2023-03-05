class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = myclass.__iter__()

print(myiter.__next__())
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
