#Зад. 2.
'''
Да се състави програма на Python, чрез която се дефинира клас Market(хранителен магазин) с полета: barcod (баркод на артикула), nате (име на продукта),
 manufacturer (производител), price(цена), quantity (количество). 
•	Да се създаде конструктор, който инициализира полетата на класа.  
В класа са дефинирани и методи: 
•	sale(self, quantity) за продажба на определен брой от тези продукти , 
•	discount(self), който прилага отстъпка към цената на продукта, по следния начин: 
o	ако цената на продукта е между 50 и 30лв. (включително)отстъпката е 5% от цената, 
o	ако цената е между 30 и 10лв. (включително) отстъпката е 7%, 
o	ако цената е под 10лв. или над 50лв. няма отстъпка 

•	Да се създаде списък product_list, който съдържа п инстанции на класа Market (n се въвежда от потребителя) 
Да се дефинират и следните функции:
•	search_by_ barcod, която получава като аргумент списък с обекти от класа Market и число(баркод на продукта). Функцията принтира цялата 
информация за съответния продукт, ако не е намерен продукт с търсения баркод се принтира следното съобщение: " Wrong barcode !!! " и информация 
за наличните баркодове от списъка 
•	search_by manufacturer, която получава като аргумент списък с обекти от класа Market и производителя на продукта и връща като резултат списък 
с всички продукти от търсения производител, с цена по-ниска или равна на средната цена на продуктите от съответния производител в списъка 
•	sort_by_quantity, която получава като аргумент списък с обекти от класа Market Функцията сортира продуктите в списъка по атрибут количество във 
възходящ ред и извежда получения резултат на екрана. 
•	delete_by_name, която получава като аргумент списък с обекти от класа Market и име на продукта. Функцията изтрива от списъка всички продукти, 
който са с посоченото име и чието количество е по-малко от или равно на 3. 
'''

class Market:
    def __init__(self, barcod, name, manufacturer, price, quantity):
        self.barcod = barcod
        self.name = name
        self.manufacturer = manufacturer
        self.price = float(price)
        self.quantity = int(quantity)

    # Метод за продажба
    def sale(self, qty):
        if self.quantity >= qty:
            self.quantity -= qty
            print(f"Успешна продажба на {qty} бр. от {self.name}.")
        else:
            print(f"Няма достатъчно количество от {self.name}. Налични: {self.quantity}")

    # Метод за отстъпка
    def discount(self):
        # Ако цената е между 50 и 30 (включително) -> 5%
        if 30 <= self.price <= 50:
            self.price = self.price * 0.95
        # Ако цената е между 30 и 10 (включително) -> 7%
        # Забележка: Тъй като 30 е включено и в горното, използваме elif, 
        # за да не се приложи двойна логика, ако приемем приоритет на реда.
        elif 10 <= self.price < 30: 
            self.price = self.price * 0.93
        # Иначе (под 10 или над 50) -> няма отстъпка (не правим нищо)

    #Обикновен метод за показване на информацията
    def show_info(self):
        print(f"Баркод: {self.barcod} | Име: {self.name} | Производител: {self.manufacturer} | Цена: {self.price:.2f} лв. | Кол: {self.quantity}")

# --- ФУНКЦИИ ---

def search_by_barcod(product_list, code):
    found = False
    for product in product_list:
        if product.barcod == code:
            print("\nНамерен продукт:")
            product.show_info()
            found = True
            break
    
    if not found:
        print("Wrong barcode !!!")
        # Извличаме всички налични баркодове
        available_codes = [p.barcod for p in product_list]
        print(f"Налични баркодове в списъка: {available_codes}")

def search_by_manufacturer(product_list, manufacturer_name):
    # 1. Намираме всички продукти на този производител
    manuf_products = []
    for p in product_list:
        if p.manufacturer == manufacturer_name:
            manuf_products.append(p)
    
    # Ако няма такива, връщаме празен списък
    if len(manuf_products) == 0:
        return []

    # 2. Смятаме средната цена
    total_price = 0
    for p in manuf_products:
        total_price = total_price + p.price
        
    avg_price = total_price / len(manuf_products)
    
    # 3. Събираме продуктите с ниска цена
    result_list = []
    for p in manuf_products:
        if p.price <= avg_price:
            result_list.append(p)
            
    return result_list # ВАЖНО: Връщаме списъка, за да спазим условието

# --- ПОМОЩНА ФУНКЦИЯ ЗА СОРТИРАНЕ ---
def get_quantity_key(product):
    return product.quantity

def sort_by_quantity(product_list):
    # Сортиране на списъка по количество във възходящ ред
    product_list.sort(key=get_quantity_key)
    
    print("\nСписък сортиран по количество (възходящ ред):")
    for product in product_list:
        product.show_info()

def delete_by_name(product_list, product_name):
    # Изтрива продукти с даденото име И количество <= 3
    # Използваме slice assignment [:] за да модифицираме оригиналния списък
    initial_count = len(product_list)
    product_list[:] = [p for p in product_list if not (p.name == product_name and p.quantity <= 3)]
    
    deleted_count = initial_count - len(product_list)
    if deleted_count > 0:
        print(f"\nИзтрити са {deleted_count} продукта с име '{product_name}' и малко количество.")
    else:
        print(f"\nНяма намерени продукти за изтриване (с име '{product_name}' и количество <= 3).")

# --- ОСНОВНА ПРОГРАМА (MAIN) ---

# 1. Създаване на списък с n инстанции
product_list = []
try:
    n = int(input("Въведете брой продукти (n): "))
except ValueError:
    n = 0
    print("Невалидно число!")

for i in range(n):
    print(f"\n--- Въвеждане на продукт {i+1} ---")
    b_code = input("Баркод: ") # Може да е число или стринг, оставяме го стринг за гъвкавост
    p_name = input("Име на продукт: ")
    p_manuf = input("Производител: ")
    p_price = float(input("Цена: "))
    p_qty = int(input("Количество: "))
    
    # Създаване на обект и добавяне в списъка
    new_product = Market(b_code, p_name, p_manuf, p_price, p_qty)
    
    # Прилагане на отстъпка веднага при създаване (или по желание може да се извика по-късно)
    # Според условието методът съществува, ще го приложим, за да са актуални цените
    new_product.discount()
    
    product_list.append(new_product)

# --- ТЕСТВАНЕ НА ФУНКЦИИТЕ ---

# 2. Търсене по баркод
search_code = input("\nВъведете баркод за търсене: ")
search_by_barcod(product_list, search_code)

# 3. Търсене по производител
manuf_search = input("\nВъведете производител за справка: ")
found_products = search_by_manufacturer(product_list, manuf_search)
print(f"--- Продукти на '{manuf_search}' с ниска цена ---")
if len(found_products) > 0:
    for p in found_products:
        p.show_info()
else:
    print("Няма намерени продукти.")

# 4. Изтриване по име (ако количество <= 3)
del_name = input("\nВъведете име на продукт за изчистване (ако к-во <= 3): ")
delete_by_name(product_list, del_name)

# 5. Сортиране по количество (и принтиране)
sort_by_quantity(product_list)