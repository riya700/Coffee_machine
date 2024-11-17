# from resources_data import MENU

MENU={
    "espresso":{
        "ingredients":{
            "milk":0,
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "milk":150,
            "water":200,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuciano":{
        "ingredients":{
            "milk":100,
            "water":250,
            "coffee":30,
        },
        "cost":3.5,
    }
}
resources={
"milk":300,
"water":300,
"coffee":300
}
def is_resource_sufficient(order_ingredients):
    for item in resources:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
        else:
            resources[item]-=order_ingredients[item]
    return True

is_on=True

while is_on:
    choice=input("What would you like? espresso/latte/cappuciano: ")
    if choice=="off":
        is_on=False 
    else:
        drink=MENU[choice]
        print(resources)
        if is_resource_sufficient(drink["ingredients"]):
            amount=float(input("Enter the amount: "))
            if amount>=drink["cost"]:
                print("Here's your coffee. Enjoy!")
            else:
                print("Insufficient amount.")
    


