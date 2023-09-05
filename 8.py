#using polymorphism
class A:
    def __init__(self,s):
        self.s=s
        def palindrome(self):
            rev=self.s[::-1]
            if rev==self.s:
                print("the string is palindrome")
            else:
                print("not a palindrome")
class B(A):
    def __init__(self,s):
        self.s=s
    def palindrome(self):
        temp=self.s
        rev=0
        count=0
        while(self.s!=0):
              clig=self.s%10
              rev=rev*10+dig
              self.s=self.s//10
        if temp==rev:
             print("the no is palindrome")
        else:
              print("not a palindrome")
a=A(input("enter a string"))
b=B(int(input("enter an integer")))
a.palindrome()
b.palindrome()
