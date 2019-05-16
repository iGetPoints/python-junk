value = 20
def test():
    global value
    print(value)
    value = 1000
    print(value)
    
test()
