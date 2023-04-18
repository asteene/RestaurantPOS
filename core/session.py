from core.utils import calculate_total_cost
from datetime import datetime
from database.db import Database


class UserSession:
    """
    UserSession is a class that represents a user's shopping session.

    args:
        - username: The username of the user.
        - db: The database to use.

    attributes:
        - username: The username of the user.
        - cart: A dictionary of dictionaries representing the items in the user's cart.
        - total_cost: The total cost of the user's cart.
        - date: The date of the user's session.
        - db: The database to use.
        - table_number: the location of the sale
    """

    def __init__(self, username: str, db: Database, manager: bool):
        self.table_number = 0
        self.username = username
        self.manager = manager
        self.total_cost = 0
        self.date = None
        self.db = db
        self.carts = {}

    def add_cart(self, table_number: int):
        '''
        Checks if there is an open check at a location, if not, opens a check at that location.

        args:
            - table_number: the location of the sale
        '''
        if f'{table_number}' not in self.carts.keys():
            self.carts[f'{table_number}'] = self.empty_cart()

    def set_table_num(self, table_number):
        '''
        sets the table number of the session

        args:
            - table_number: the location
        '''
        self.table_number = table_number

    def empty_cart(self) -> dict:
        """
        Fills the cart dictionary with item ids and 0 quantities.

        args:
            - None

        returns:
            - A dictionary of dictionaries representing the items in the user's cart.
        """
        inventory = self.db.get_full_inventory()
        new_cart = {}
        for item in inventory:
            new_cart[item["id"]] = {"name": item["item_name"], "price": item["price"], "quantity": 0,
                                    "discount": 0, "tax_rate": 0}
        return new_cart

    def is_item_in_cart(self, id: str, table_number: int) -> bool:
        """
        Checks if an item is in the user's cart.

        args:
            - id: The id of the item.
            - table_number: The location of the sale.

        returns:
            - True if the item is in the user's cart, False otherwise.
        """
        return id in self.carts[f'{table_number}']

    def add_new_item(self, id: str, name: str, price: int, quantity: int,  table_number: int, discount: float = 0.0, tax_rate: float = 0.05) -> None:
        """
        Creates a new item to add to the user's cart.

        args:
            - id: The id of the item.
            - name: The name of the item.
            - price: The price of the item.
            - quantity: The quantity of the item.
            - discount: The discount of the item.
            - tax_rate: The tax rate of the item.
            - table_number: The location of the sale.

        returns:
            - None
        """
        self.carts[f'{table_number}'][id] = {"name": name, "price": price, "quantity": quantity,
                         "discount": discount, "tax_rate": tax_rate}

    def update_item_quantity(self, id: str, change_to_quantity: int, table_number: int) -> None:
        """
        Updates the quantity of an item in the user's cart.

        args:
            - id: The id of the item.
            - quantity: The quantity of the item.
            - table_number: The location of the sale.
        """
        if self.carts[f'{table_number}'][id]["quantity"] + change_to_quantity <= 0:
            self.remove_item(id)
        else:
            self.carts[f'{table_number}'][id]["quantity"] += change_to_quantity

    def remove_item(self, id: str, table_number: int) -> None:
        """
        Removes an item from the user's cart.

        args:
            - id: The id of the item.
            - table_number: The location of the sale.
        """
        del self.carts[f'{table_number}'][id]

    def update_total_cost(self, table_number: int) -> None:
        """
        Updates the total cost of the user's cart.

        args:
            - table_number: The location of the sale.
        """
        self.total_cost = calculate_total_cost(self.cart, table_number)

    def submit_cart(self, table_number: int) -> None:
        """
        Called when the order is submitted. Finalizes user session details.

        args:
            - table_number: The location of the sale.

        returns:
            - None
        """
        self.update_total_cost(table_number)
        self.date = datetime.now()


class Sessions:
    """
    Sessions is a class that represents the collection of active sessions.

    args:
        - None

    attributes:
        - sessions: A dictionary of user sessions.
    """

    def __init__(self):
        self.sessions = {}

    def add_new_session(self, username: str, db: Database, manager: bool) -> None:
        """
        Adds a new user session to the collection of sessions.

        args:
            - username: The username of the user.
            - db: The database to use.

        returns:
            - None
        """
        self.sessions[username] = UserSession(username, db, manager)

    def get_session(self, username: str) -> UserSession:
        """
        Gets a user session from the collection of sessions.

        args:
            - username: The username of the user.

        returns:
            - The user session.
        """
        return self.sessions[username]

    def remove_session(self, username: str) -> None:
        """
        Removes a user session from the collection of sessions.

        args:
            - username: The username of the user.

        returns:
            - None
        """
        del self.sessions[username]

    def get_all_sessions(self) -> dict:
        """
        Gets all user sessions from the collection of sessions.

        args:
            - None

        returns:
            - A dictionary of user sessions.
        """
        return self.sessions
