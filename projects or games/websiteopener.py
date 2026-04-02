import webbrowser


print("******************************************")
print(" 1: youtube , 2: github, 3: leetcode")
print("******************************************")

with open("projects or games/recorderwebsiteopener.txt", "a+") as f:
    ch = int(input("Enter choice: "))
    f.write(str(ch))
    match( ch):
        case 1:
            webbrowser.open("https://www.youtube.com/")
        case 2:
            webbrowser.open("https://github.com/")
        case 3:
            webbrowser.open("https://leetcode.com/")
        case _:
            print("wrong choice!!")




