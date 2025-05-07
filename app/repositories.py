# Simulating a data source
class UserRepository:
    def __init__(self):
        self.users = [
            {"id": 1, "name": "Alice", "age": 30},
            {"id": 2, "name": "Bob", "age": 25},
            {"id": 3, "name": "Charlie", "age": 35},
        ]

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, user_id: int):
        return next((user for user in self.users if user["id"] == user_id), None)
