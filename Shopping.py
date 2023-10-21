from abc import ABC, abstractclassmethod

class Product:
    products=[]
    def __init__(self,name, price, quantity, seller_name) -> None:
        self.name= name
        self.price= price
        self.quantity= quantity
        self.seller_name= seller_name
        
        Product.products.append(self)
        
    def __repr__(self) :
        return f"{self.name} is only {self.quantity} left Price: {self.price}\nUploaded by : {self.seller_name}"

    def changeInfo(self, price):
        self.price= price
        
    def changeInfo(self,price, quantity):
        self.price= price
        self.quantity= quantity
    
class User(ABC):
    userList={}
    def __init__(self, name, email, pas, usertype):
        self.name= name
        self.email= email
        self.pas= pas 
        if usertype== "seller":
            User.userList["seller"]= self
            
        elif usertype =="buyer":
            User.userList["buyer"] = self
            
    @abstractclassmethod       
    def show_profile(self):
        raise NotImplemented
    
class Seller(User):
    def __init__(self, name, email, pas):
        
        super().__init__(name, email, pas,"seller")
    
    def add_product(self):
        name= input("Product Name: ")
        price= input("Price: ")
        quantity= input("Quantity: ")
        product=Product(name, price,quantity, self.name)
        Product.products.append(product)
        
    def show_profile(self):
        print("Name: {self.name}  Email: {self.email}")
        print("Account Type: Seller")
        
        
class Buyer(User):
    def __init__(self, name, email, pas):
        super().__init__(name, email, pas,"buyer")
        
    def place_order(self, product_name, quantity):
        flag= 0
        for product in Product.products:
            if product.name== product_name:
                flag=1
                if product.quantity >= quantity:
                    
                    payment=int(input(("Please proceed payment ")))
                    if payment >= (quantity*product.price):
                        print("\nPayment successful.")
                        print(f"{quantity} {product.name}, is bought by {self.name}")
                        print(f"payed {payment} taka, returned {payment-(quantity*product.price)} taka")
                        break
                    else:
                        correct_pay= int(input(f"Please pay the correct price for the last time "))
                        if correct_pay >= (quantity*product.price):
                            print("\nPayment successful.")
                            print(f"{quantity} {product.name}, is bought by {self.name}")
                            print(f"payed {correct_pay} taka, returned {correct_pay-(quantity*product.price)} taka")
                            break
                else:
                    print("Not available")
                    break
        if flag==0:
            print("Not available")
            
    def show_profile(self):
        print("Name: {self.name}  Email: {self.email}")
        print("Account Type: Buyer")
            
            
listy= Product("Bottle", 30, 20, "CocaCola")

currentUser= None
while True:
    if currentUser==None:
        LR= input("Login or Register ?(L/R) ")
        if LR=="R":
            name= input("Enter name: ")
            email= input("Enter email")
            pas= input("Password: ")
            BS= input("Buyer or Seller ?(B/S) ")
            if BS== "S":
                currentUser= Seller(name,email,pas)
                
            else: 
                currentUser = Buyer(name,email,pas)
                
        elif LR== "L":
            name= input("Enter name: ")
            email= input("Enter email")
            pas= input("Password: ")
            BS= input("Buyer or Seller ?(B/S) ")
            flag= 0
            for user in User.userList:
                if user.name== name:
                    if user.email== email:
                        if user.pas== pas:
                            print("Login Successful")
                            currentUser= user
                            flag=1
                            
            if flag==0:
                print("Wrong Information")
                
    else: 
        if currentUser.userType
        
            
                            
                            
                            