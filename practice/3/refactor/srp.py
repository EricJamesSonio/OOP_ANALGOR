# Applying SRP
# One class Should only do one work!


class Person:  # This is wrong!
    def __init__(self, name, age, job_title, salary):
        self.name = name
        self.age = age
        self.job_title = job_title
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def give_raise(self, amount):
        self.salary += amount

    def promote(self, new_title):
        self.job_title = new_title


# This is correct!


class Person:
    def __init__(self, name, age, job_title, salary):
        self.name = name
        self.age = age
        self.job_title = job_title
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def give_raise(self, amount):
        self.salary += amount

    def promote(self, new_title):
        self.job_title = new_title


class Job:
    def __init__(self, title, salary):
        self.title = title
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def promote(self, new_title):
        self.title = new_title

    def get_salary(self):
        return self.salary
