class Product:
    products={  
              'Clock': [520, 20],
              'Watch': [150, 50],
              'Bottle': [50, 189]
              
              }
    
    def __init__(self, name, price,amount):
        self.name= name
        self.price= price
        self.amount= amount     
        Product.products[name]=[price,amount]
        
        
class Shop():
    # def __init__(self, name, price, amount):
    #     super().__init__(name, price, amount)
    
    def add_product(self, name, price, amount):
        Product.products[name]= [price, amount] 
    
    def buy_product(self,name,amount,payment):
        if name in Product.products:
            if Product.products[name][1] >= amount:
                if payment >= Product.products[name][0]*amount:
                    print("Payment successful. Thanks for buying")
                    print(f'Payed {payment} taka , retuned {payment-Product.products[name][0]*amount} taka')
                    Product.products[name][1]-=amount
                    if Product.products[name][1] ==0:
                        Product.products.pop(name)
                    
                else:
                    print(f"Please add {Product.products[name][0]-amount} Taka more")
                    payment= int(input())
            else:
                print("Sorry, not available")
                
ask= input("Buyer or seller ?\n")
if ask=='Seller' or ask=='seller':
    print("Please wait for the next update\n")
    
elif ask=='Buyer' or ask=='buyer':
    name= input('Enter products name\n')
    quantity = int(input('How many do you want ?\n'))
    payment= int(input('Please proceed payment\n'))
   
    price=Product.products[name][0]
    amount = Product.products[name][1]
    
    # buyer= Shop(name, price, amount)
    buyer= Shop()
    buyer.buy_product(name,quantity,payment)
    
    
    
                    
