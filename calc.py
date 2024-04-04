def main():
    print("Let's implement addition. Type two numbers for x and y.")

    x = int(input("x > "))
    y = int(input("y > "))
    
    print("%d + %d = %d" % (x, y, add(x, y)))    
    
# TODO: add() 함수 정의
def add():
    return x+y
  
def divide():
    if y==0:
        print("Error: cannot divide by zero.")
    else:
        return x/y

  
if __name__ == "__main__":
    main()
