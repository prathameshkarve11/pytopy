# # file with variable 
# f = open("room1.txt" , "x+") 

# f.close()

# with open("room1.txt", "a+") as ff:
#     ff.write(" this is next line after your first line \n")
#     ff.seek(0)
#     print(ff.read())



# f2 = open("room2.txt" , "x")

fr1 = open("room1.txt" , "r")
fr1.seek(0)
fr2 = open("room2.txt", "a")
fr2.write(fr1.read())
fr1.close()
fr2.close()

