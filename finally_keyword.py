try:
    num=int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted")
finally:
    print("This block always executed")
    
# finally clause

def func1 ():
    try:
        l=[1,5,6,7]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("This block is always executed")

x=func1()
print(x)