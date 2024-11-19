stack =[]
def push():
    element=input("enter the element:")
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("no element in stack")
    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)
while True:
    print("select option 1 to push and 2 to pop  & 3 to quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("select the right option dumb fuck ")                      