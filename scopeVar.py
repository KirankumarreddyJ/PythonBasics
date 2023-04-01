a = 500
def myfunc():
  x = 300
  def myinnerfunc():
    print('x value in nest fun', x)
    print('a value in nest fun', a)

    global y
    y = 100
    print('y value in nest fun', y)
  myinnerfunc()
  print('y value in fun', y)
  print('a value in fun', a)


myfunc()

#print('x value in out fun', x)  # x value can't access outside of fun
print('y value in out fun', y)
print('a value in out fun', a)
