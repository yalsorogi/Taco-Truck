# Taco-Truck

Taco Truck Ordering System

This Python program is an interactive ordering system for a taco truck, guiding users through the process of placing customized orders. The system begins by asking for a user’s name and whether they prefer a vegetarian or non-vegetarian option. It employs a selection algorithm using conditional logic to adjust the available protein options based on the customer’s dietary preference. Users then select items like tortillas, toppings, guacamole, and salsa from predefined lists.

The program utilizes while loops to handle multiple orders, continuously prompting the user until they indicate they are done. It also features an indexed menu system where items are presented with user-friendly numbered options, allowing for input validation via list indexing.

A dictionary is used to track the number of times each item is ordered. This dictionary is dynamically updated by iterating through the items_ordered list and incrementing the count for each item in the counted_items dictionary. The algorithm for counting uses dictionary key lookups and a filtering mechanism that creates a final summary of only the items that were actually ordered, excluding those with zero counts.

At the end of the transaction, the program generates a random survey code and offers the customer the option to leave a tip, adding an interactive experience to the order completion process. The final output displays a breakdown of the ordered items and their quantities.
