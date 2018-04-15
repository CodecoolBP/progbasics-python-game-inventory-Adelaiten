# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

inventory = {}

def bubble_sort(inventory):
    iterations = 1
    N = len(inventory)
    list_inventory = list(inventory.items())
    while iterations < N:
        j = 0
        while j <= N - 2:
            if list_inventory[j][1] > list_inventory[j + 1][1]:
                temp = list_inventory[j + 1]
                list_inventory[j + 1] = list_inventory[j]
                list_inventory[j] = temp

            j = j + 1

        iterations = iterations + 1
    return list_inventory

def printing_inventory(order, max_left, lists, longest_item, max_right):
    if order == "count,asc" or order == "count,desc":
        print(" " * (max_left - len(str(lists[1]))) + str(lists[1]) + " " * (
                len(longest_item) + (max_right - len(lists[0]))) + lists[0])



def printing_pauses(max_left, max_right, longest_item):
    print("-" * (max_left + max_right + len(longest_item)))


# Displays the inventory.
def display_inventory(inventory):
    print("Inventory: ")
    for key, value in inventory.items():
        print("{0} {1}".format(key, value))

    print("Total number of items: " + str(sum(inventory.values())))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        elif item not in inventory:
            inventory[item] = 1
    display_inventory(inventory)


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    longest_item = ""
    inventory_sorted = sorted(inventory)
    lenght = len("Inventory:\n count" + " " * (len(longest_item)) + "item name")

    for i in range(0, len(inventory)):
        for inventory_sorted[i] in inventory_sorted:
            if len(inventory_sorted[i]) > len(longest_item):
                longest_item = inventory_sorted[i]
            else:
                continue
                
    max_left = len("count") + 1
    max_right = len("item name")

    print("Inventory:\n count" + " " * (len(longest_item)) + "item name")

    printing_pauses(max_left, max_right, longest_item)

    if order is None:
        for item, value in inventory.items():
            print(" " * (max_left - len(str(value))) + str(value) + " " * (
                 len(longest_item) + (max_right - len(item))) + item)

    elif order == "count,asc":
        list_inventory = bubble_sort(inventory)
        for lists in list_inventory:
            printing_inventory(order, max_left, lists, longest_item, max_right)

    elif order == "count,desc":
        list_inventory = bubble_sort(inventory)
        for lists in reversed(list_inventory):
            printing_inventory(order, max_left, lists, longest_item, max_right)

    printing_pauses(max_left, max_right, longest_item)
    print("Total number of items: " + str(sum(inventory.values())))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename, "r") as imported_inventory:
        for line in imported_inventory:
            listed_line = line.split(',')
        add_to_inventory(inventory, listed_line)



# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    list_to_export = []
    for key, value in inventory.items():
        if value > 1:
            for i in range(1, value +1):
                    list_to_export.append(key)
        else:
            list_to_export.append(key)
    string_to_export = ",".join(list_to_export)

    with open(filename, "w") as export_inventory:
        export_inventory.write(string_to_export)
