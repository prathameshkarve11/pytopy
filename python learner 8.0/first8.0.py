
try:
    mytuple = ("aplle" , "banana", "chiko")
    itr = iter(mytuple)
    print(next(itr))
    print(next(itr))
    print(next(itr))
    print(next(itr))
  
except Exception as e:
    print("Exeption occured")
    print(e)
else:
    print("nothing weent wrong")
finally:
    print("The try expet is finished")