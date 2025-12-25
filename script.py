# Class representing a business that owns multiple franchises
class Business:
    def __init__(self, name, franchises):  # initialize business
        self.name = name
        self.franchises = franchises

# Class representing a physical franchise location
class Franchise:
    def __init__(self, address, menus):  # initialize franchise
        self.address = address
        self.menus = menus

    def __repr__(self):  # return franchise address
        return self.address

    def available_menus(self, time):  # get menus available at a given time
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus

# Class representing a menu with items and availability times
class Menu:
    def __init__(self, name, items, start_time, end_time):  # initialize menu
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def format_time(self, time):  # format time as am/pm
        hour = time // 100
        suffix = 'am' if hour < 12 or hour == 24 else 'pm'
        hour = hour if hour <= 12 else hour - 12
        return f"{hour}{suffix}"

    def __repr__(self):  # return menu description
        return (
            f"{self.name} menu available from "
            f"{self.format_time(self.start_time)} "
            f"to {self.format_time(self.end_time)}"
        )

    def calculate_bill(self, purchased_items):  # calculate total bill
        item_set = set(purchased_items)
        bill = 0
        for item in item_set:
            if item in self.items:
                bill += self.items[item]
            else:
                print(f"Warning: {purchased_item} not found in menu.")
        return ("£{0:.2f}".format(bill))


early_bird = {
    'cheese board': 8.00,
    'garden salad with rolls (serves 2, no refills)': 14.00,
    'margherita flatbread': 9.00,
    'beef ragu': 17.50,
    'spinach ravioli (vegan)': 13.50,
    'latte': 1.50,
    'cappuccino': 3.00,
}

brunch = {
    'french toast': 7.50, 'crepes': 9.00, 'sandwich': 11.00,
    'roasted potatoes': 4.50, 'latte': 1.50, 'cappuccino': 3.00,
    'herbal tea': 1.00, 'bellini': 10.50, 'grapefruit juice': 3.50
}

dinner = {
    'bruschetta with tomato': 13.00,
    'greek salad': 16.00,
    'margherita flatbread': 11.00,
    'beef ragu': 19.50,
    'spinach ravioli (vegan)': 13.50,
    'latte': 2.00,
    'cappuccino': 3.00,
}

kids = {
    'fish bites': 6.50,
    'penne primavera': 12.00,
    'cranberry juice': 3.00
}

# Create menus
early_bird_menu = Menu('Early Bird', early_bird, 700, 1000)
brunch_menu = Menu('Brunch', brunch, 1100, 1600)
dinner_menu = Menu('Dinner', dinner, 1700, 2100)
kids_menu = Menu('Kids', kids, 1000, 2100)

menus = [early_bird_menu, brunch_menu, dinner_menu, kids_menu]

# Create franchise and business
flagship_store = Franchise('2129 North End Road', menus)
new_installment = Franchise('97 South Cherry Lane', menus)

Dine = Business(
    "Dine all day, every day",
    [flagship_store, new_installment]
)

# Test franchise
print(flagship_store)
print("\n" + str(flagship_store.available_menus(1000)))
print("\n" + str(flagship_store.available_menus(1700)))

# Calculate and print a sample early bird bill
print("\n" + str(
    early_bird_menu.calculate_bill(
        ['cheese board', 'spinach ravioli (vegan)']
    )
))

# Calculate and print a sample brunch bill
print("\n" + str(brunch_menu.calculate_bill(
    ['french toast', 'roasted potatoes', 'latte']
)))

# Create a panini only restaurant similar to Dine all day, every day
panini_items = {
    'caprese panini': 7.00,
    'chicken panini': 8.50,
    'turkey panini': 8.00,
    'avocado panini': 7.50
}

panini_menu = Menu(
    "Panini yesterday, today, and tomorrow",
    panini_items,
    800,
    2000
)
panini_place = Franchise('439 Panini Avenue', [panini_menu])
panini = Business("Panini all day, everyday", [panini_place])

print("\n" + str(panini.franchises[0].menus[0]))