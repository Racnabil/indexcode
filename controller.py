from model import Database

class FoodController:
    def __init__(self):
        self.db = Database()

    def get_food_items(self):
        return self.db.fetch_food()

    def get_stationery_items(self):
        return self.db.fetch_stationery()

    def close(self):
        self.db.close_connection()