class User:
    def __init__(self, full_name, phoneNumber, email, address, password):
        self.full_name = full_name,
        self.phoneNumber = phoneNumber,
        self.email = email,
        self.address = address,
        self.password = password





class Food():
    counter = 10

    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = Food.counter + 1
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock
        Food.counter = Food.counter + 1


def viewListOfFoodItems():
    print("CURRENT FOOD SUPPLY IN RESTAURANT")
    for key in food_dict:
        print(food_dict[key].food_id, "==", food_dict[key].name, "==", food_dict[key].quantity, "==",
              food_dict[key].price, "==", food_dict[key].discount, "==", food_dict[key].stock)


def editFoodItems(foodId):
    food_obj = food_dict[foodId]
    print(type(food_obj))
    print("1. Name --- 2. Quantity --- 3. Price --- 4. Discount --- 5. Stock --- 6. To exit")
    select_option = input("Select the option which you want to edit: ")
    while select_option != "6":
        if select_option == "1":
            name = input("Enter New Food Name")  #dum_Aalu
            food_obj.name = name   #aalu=dum_aalu
        elif select_option == "2":
            quantity = input("Enter the new quantity")
            food_obj.quantity = quantity
        elif select_option == "3":
            price = input("Enter the new price")
            food_obj.price = price
        elif select_option == "4":
            discount = input("Enter the new discount value")
            food_obj.discount = discount
        elif select_option == "5":
            stock = input("Enter the new stock value")
            food_obj.stock = stock
        else:
            print("please enter the valid input")

        print("1. Name --- 2. Quantity --- 3. Price --- 4. Discount --- 5. Stock --- 6. To exit")
        select_option = input("Select the option AGAIN which you want to edit: ")

    print("Updated food item ", ":", food_obj.food_id, ":", food_obj.name, ":", food_obj.quantity, ":", food_obj.price,
          ":", food_obj.discount, ":", food_obj.stock)
    print("***EXIT** YOUR Food Item IS Edited Succesfully ")


def adminLogin():
    print(
        "Select your option \n1.Add the Food item \n2.Edit the food item \n3.Remove the Food item \n4.View List of Food items \n 5. Enter 5 to quit")
    option_selected = input("Enter your choice")
    while option_selected != "5":
        if option_selected == "1":
            print("Add the Food details")
            name = input("Enter food name")
            quantity = input("Enter quantity in gram,ml,pcs")
            price = input("enter the Price")
            discount = input("Enter the discount")
            stock = input("Enter the stock")
            obj = Food(name, quantity, price, discount, stock)
            list_of_food_items.append(obj)
            food_dict.update({obj.food_id:obj})
            print("***Food item Added Successfully***")
        elif option_selected == "2":
            food_id = int(input("Enter food id"))
            editFoodItems(food_id)
        elif option_selected == "3":
            food_id = int(input("Enter food id"))
            del food_dict[food_id]
            print(" Deletion sucessfull")
        elif option_selected == "4":
            viewListOfFoodItems()
        else:
            print("please enter the valid input")

        print(
            "Select your option \n1.Add the Food item \n2.Edit the food item \n3.Remove the Food item \n4.View List of Food items \n 5. Enter 5 to quit")
        option_selected = input("**Enter your option again***")

    print("Exited from ADMIN LOGIN")


def placeNewOrder():
    orderArray = []
    print("Enter your order from the below menu")
    viewListOfFoodItems()
    total_items = int(input("Enter the number of items you want to place"))  #2
    for i in range(total_items):
        item = int(input("enter the food_id to place order"))
        orderArray.append(item)
    #[11,12]
    print("This is your Order", orderArray)
    print("Enter 1.To place order 2.To cancel")
    order_placed = input("Enter::")
    if order_placed == "1":
        print("Order placed sucessfully")
        for x in orderArray:
            orderHistory.append(x)
    print("*************************************")



def orderHistory_meth():
    print(orderHistory)

def updateProfile(object_user):
    print("Enter your option to update 1.Full name 2.phone number 3.address 4.email 5.password 6.exit")
    update_profile = input("Enter::")
    while update_profile != "6":
        if update_profile == "1":
            name = input("Enter full name")
            object_user.full_name=name
        elif update_profile == "2":
            phone_number = input("Enter new phone number")
            object_user.phoneNumber=phone_number
        elif update_profile == "3":
            address = input("Enter new address")
            object_user.address=address
        elif update_profile == "4":
            email = input("Enter new email")
            object_user.email=email
        elif update_profile == "5":
            password = input("Enter new password")
            object_user.password=password
            object_user_cred[object_user.email]=password

        else: print("enter valid option")

        print("Enter your choice Again 1.Full name 2.phone number 3.address 4.email 5.password 6.exit")
        update_profile = input("Enter::")
    print("********************PROFILE***************************")
    print("Name=",object_user.full_name)
    print("Address=",object_user.address)
    print("Phone Number=",object_user.phoneNumber)
    print("Email=",object_user.email)
    print("Password=",object_user.password)
    print("*******************************************************")
    print("Profile updated sucessfully")


def userNowLoggedIn(object_user):
    print("Enter your choice 1.Place new order 2.Order History 3.Update your profile 4.log Out")
    option = input("Enter:")
    while option != "4":
        if option == "1":
            placeNewOrder()
        elif option == "2":
            orderHistory_meth()
        elif option == "3":
            updateProfile(object_user)
        print("Enter your choice 1.Place new order 2.Order History 3.Update your profile 4.log Out")
        option = input("Enter Your Option Again:")




orderHistory = []
object_user_cred={} #user creddentials dictonary
admin_credentials = {"Priyanshu": "Lakhara"}
food_dict = {}           # { obj.food_id : obj}     obj=Food(name, quantity, price, discount, stock)
list_of_food_items = []  # [obj1,obj2,obj3]   obj=Food(name, quantity, price, discount, stock)


def foodOderMain():
    try_again = "1"
    while try_again == "1":
        print("Welcome to Food World" "\nEnter your type")
        user_type = input("\n Admin" "\n User" "\n")
        if user_type == "Admin":
            id = input("Enter your ID:")
            if id in admin_credentials:
                pwd = input("Enter your Password:")
                if admin_credentials[id] == pwd:
                    print("Log in Done")
                    adminLogin()
                else:
                    print("Wrong Password\n Try Again")
            else:
                print("Wrong id\nCheck it again")
        elif user_type == "User":
            print("Enter your User type\n 1.New User\n2.Existing User")
            user = input(":")
            if user == "1":
                print("You are new in this food world")
                full_name = input("Enter  your full name")
                phone_number = input("Enter your phone number")
                address = input("Enter your address")
                email = input("Enter your email")
                password = input("Enter you password")
                object_user = User(full_name, phone_number, email.strip(), address, password)
                object_user_cred.update({email:password})
                print("registration done sucessfully")
                userNowLoggedIn(object_user)

            elif user == "2":
                print("You are already registered with us")
                mail = input("enter mail")
                if mail in object_user_cred:
                    password = input("enter pass")
                    if object_user_cred[mail] == password:
                        print("Log in Done")
                        userNowLoggedIn(object_user)
                else:
                    print("wrong cred")
            else:
                print("Invalid type")

        print("Do you want to try again")
        try_again=input("Enter 1. for YES 2. for No")

    print("***********FINAL EXIT***************")


 #calling
foodOderMain()


