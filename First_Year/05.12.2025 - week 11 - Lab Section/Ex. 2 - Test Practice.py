#Зад. 2.
'''
o	Да се създадат 3 артикула (обекти-инстанции на класа ClothesShop) и нов списък clothes_list, където да бъдат 
    добавени и да се съхраняват всички артикули (обекти).
Да се дефинират и следните функции:
•	search_by_id (clothes_list, id) потребителят въвежда от клавиатурата номер на артикула и функцията принтира цялата информация за 
съответния артикул.
•	search_by_brand(clothes_list, brand) потребителят въвежда от клавиатурата марка на артикул и функцията принтира списък с всички 
артикули на тази марка.
•	sell_clothe_by_id(clothes_list, id, num) потребителят въвежда от клавиатурата номер (id) и желан брой/количество (num) от даден 
артикул. 
    o	Функцията проверява има ли наличен артикул с такъв номер. 
        	Ако има проверява колко бройки има налични (quantity).
        	Ако количеството (quantity) от търсения продукт е равно или по-голямо от количеството (num), което е въвел 
        потребителя, то тогава да се принтира в конзолата съобщение „Успешна продажба“ и от общото количество (quantity) на 
        съответния артикул да се извади стойността (num), която е въвел потребителя. 
        	В случай, че няма продукт с такъв номер да се принтирав конзолата съобщение „Не е открит такъв продукт“, а ако 
        количеството(quantity) от търсения продукт е по-малко от количеството (num), което е въвел потребителя- да се принтира 
        в конзолата съобщение „Недостатъчна наличност“.
'''

class ClothesShop:
    def __init__(self, product_id, type_cloth, brand, quantity):
        self.product_id = product_id
        self.type_cloth = type_cloth
        self.brand = brand
        self.quantity = quantity

# The list to store all objects
clothes_list = []

# --- FUNCTIONS ---
def search_by_id(clothes_list, search_id):
    found = False
    for item in clothes_list:
        if item.product_id == search_id:
            print(f"RESULT --> ID: {item.product_id}, Type: {item.type_cloth}, Brand: {item.brand}, Qty: {item.quantity}")
            found = True
            break
    if not found:
        print("Product with this ID was not found.")

def search_by_brand(clothes_list, search_brand):
    print(f"--- Results for '{search_brand}' ---")
    found_any = False
    for item in clothes_list:
        if item.brand == search_brand:
            print(f"ID: {item.product_id}, Type: {item.type_cloth}, Qty: {item.quantity}")
            found_any = True
    if not found_any:
        print("No items found for this brand.")

def sell_clothe_by_id(clothes_list, search_id, num):
    product_found = None
    
    # 1. Find the product
    for item in clothes_list:
        if item.product_id == search_id:
            product_found = item
            break
            
    # 2. Logic Check
    if product_found is None:
        print("Product not found!")
    elif product_found.quantity < num:
        print(f"Insufficient quantity. Available: {product_found.quantity}")
    else:
        product_found.quantity -= num
        print("Successful sale!")
        print(f"Remaining quantity: {product_found.quantity}")


while True:
    print("\n" + "============================")
    print("      CLOTHES SHOP MENU      ")
    print("============================")
    print("1. Add new item")
    print("2. Search by ID")
    print("3. Search by Brand")
    print("4. Sell Item")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        # ADD ITEM
        print("\n--- Adding New Item ---")
        try:
            # We must use int() for ID and Qty because the class expects numbers
            uid = int(input("Enter ID: "))
            utype = input("Enter Type (e.g. Shirt): ")
            ubrand = input("Enter Brand: ")
            uqty = int(input("Enter Quantity: "))

            if uqty < 0:
                print("Error: Quantity cannot be negative!")
            else:
                # Only create the object if validation passes
                new_item = ClothesShop(uid, utype, ubrand, uqty)
                clothes_list.append(new_item)
                print("Item added successfully!")
        except ValueError:
            print("ERROR: ID and Quantity must be numbers!")

    elif choice == '2':
        # SEARCH ID
        try:
            uid = int(input("Enter ID to search: "))
            search_by_id(clothes_list, uid)
        except ValueError:
            print("ERROR: ID must be a number.")

    elif choice == '3':
        # SEARCH BRAND
        ubrand = input("Enter Brand name: ")
        search_by_brand(clothes_list, ubrand)

    elif choice == '4':
        # SELL ITEM
        try:
            uid = int(input("Enter Item ID to sell: "))
            uqty = int(input("How many to sell?: "))

            if uqty <= 0:
                print("Error: You must sell at least 1 item.")
            else:
                sell_clothe_by_id(clothes_list, uid, uqty)
                
        except ValueError:
            print("ERROR: Numbers only please.")
            
    elif choice == '5':
        print("Exiting program...")
        break # This stops the loop
        
    else:
        print("Invalid choice, please try again.")