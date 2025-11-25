#Зад. 2 Напишете програма, която да симулира работа с ресторант.


#----------------------#
#   Class Restaurant   #
#----------------------#
class Restaurant:
    def __init__(self, name, address, menu):
        self.name = name
        self.address = address
        self.menu = menu
    
    def get_order_data(self):
        table_number = int(input("Table: "))
        ordered_dishes = input("Поръчани ястия: ").split(",")
        cleaned_dishes = []
        for dish in ordered_dishes:
            cleaned_dishes.append(dish.strip())
        return table_number, cleaned_dishes
    
    def calculate_order_value(self, order):
        table_number, ordered_dishes = order
        order_value = 0.0

        for dish_name in ordered_dishes:
            for dish in self.menu:
                if dish["name"] == dish_name:
                    order_value += dish["price"]
        return order_value

    def generate_receipt(self, order):
        table_number, ordered_dishes = order
        total = self.calculate_order_value(order)

        print("\n        **Receipt**")
        print(f"Restaurant: {self.name}")
        print(f"Address: {self.address}")
        print(f"Order № {table_number}")

        for dish_name in ordered_dishes:
            for dish in self.menu:
                if dish["name"] == dish_name:
                    print(f"* {dish['name']} : {dish['price']} lv.")
        print(f"Total: {total} lv.")


#----------------#
#    Main Body   #
#----------------#
name = input("Restaurant name: ")
address = input("Address: ")

menu = []
while True:
    dish_name = input("Dish name: ")
    dish_price = float(input("Price: "))

    menu.append({"name": dish_name, "price": dish_price})

    more = input("Do you wish to add more dishes? (Y/N): ")
    if more.upper() != "Y":
        break
restaurant = Restaurant(name, address, menu)
order = restaurant.get_order_data()
restaurant.generate_receipt(order)