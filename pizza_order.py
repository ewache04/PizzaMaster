import random

'''
Author name: Jeremiah E. Ochepo
Code description: Class and function and Inheritance)
Last Updated Date: 8/26/19
'''


# Define a horizontal line with a given length
def horizontal_line(line_length):
    for i in range(line_length):
        print('___', end='')


# Create a class for pizza orders
class PizzaOrder(object):
    def __init__(self, user_input, numb_count, available_items,
                 out_of_stock, my_cart, sales_tax):
        self.user_input = user_input
        self.numb_count = numb_count
        self.available_items = available_items
        self.out_of_stock = out_of_stock
        self.my_cart = my_cart
        self.sales_tax = sales_tax

    # Method to place an order
    def place_order(self):
        return self.user_input

    # Method to check if the ordered item is available or out of stock
    def check_order(self):
        # Convert both the user input and the pizza names to lowercase for case-insensitive comparison
        user_input_lower = self.user_input.lower()
        available_items_lower = {key.lower(): value for key, value in self.available_items.items()}

        if user_input_lower in self.out_of_stock and available_items_lower:
            return f"{self.user_input} is out of stock."
        else:
            return f"{self.user_input} is available."

    # Method to generate an invoice and estimated wait time
    def generate_invoice(self):
        item_price = float(self.available_items.get(self.user_input, 0))  # Convert to float
        total_price = item_price + (item_price * self.sales_tax)
        estimated_wait_time = random.randint(15, 45)  # Random wait time between 15 to 45 minutes

        return f"\n--- Invoice ---\nItem: {self.user_input}\nPrice: ${item_price:.2f}\nTax: ${item_price * self.sales_tax:.2f}\nTotal: ${total_price:.2f}\nEstimated Wait Time: {estimated_wait_time} minutes\nThank you for your order!"


# Define real pizza options and randomly pick one to be out of stock
pizza_options = {'Margherita': '12', 'Pepperoni': '15', 'Vegetarian': '18', 'Hawaiian': '20'}
out_of_stock = random.sample(pizza_options.keys(), 1)

# Start the order process with a while loop
while True:
    print("\n----- Menu -----")
    for item, price in pizza_options.items():
        print(f"{item}: ${price}")

    # Get user input for the order
    user_input = input('\nEnter item to order (or type "exit" to quit): ')
    user_input = user_input.capitalize()  # Capitalize the user input for consistency

    if user_input.lower() == 'exit':
        print("Thank you for using our service. Goodbye!")
        break  # Exit the loop if the user wants to quit

    # Create an instance of the PizzaOrder class
    pizza_info = PizzaOrder(user_input, 0, pizza_options, out_of_stock, {}, 0.25)

    # Check if the ordered item is available or out of stock
    availability_status = pizza_info.check_order()
    print(availability_status)

    if "out of stock" in availability_status.lower():
        order_something_else = input("Would you like to order something else? (Yes/No): ").lower()
        if order_something_else != 'yes':
            print("Thank you for using our service. Goodbye!")
            break  # Exit the loop if the user doesn't want to order anything else
    else:
        # Generate and display the invoice
        invoice = pizza_info.generate_invoice()
        print(invoice)
        print("Thank you for your order!")

# End of the program
