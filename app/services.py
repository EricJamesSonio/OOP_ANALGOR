from repositories import UserRepository


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_users_above_age(self, age_threshold: int):
        all_users = self.repo.get_all_users()
        return [user for user in all_users if user["age"] > age_threshold]

    def get_user(self, user_id: int):
        return self.repo.get_user_by_id(user_id)
