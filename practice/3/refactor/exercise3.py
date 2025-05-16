from abc import ABC, abstractmethod

class Notification:
    def __init__(self, method : 'Observer', user, message, logger : 'Logger'):
        self.method = method 
        self.user = user
        self.message = message
        self.logger = logger

    def send(self):
        message = self.method.send(self.user, self.message)
        self.logger.log(message)
        return message

class Logger:
    def __init__(self):
        self.logs = []
        
    def log(self, message):
        self.logs.append(message)


class Observer(ABC):
    @abstractmethod
    def send(self, user,message):
        pass
    
class Email(Observer):
    def send(self, user,message):
        return f"Sending EMAIL to {user}: {message}"
    
class SMS(Observer):
    def send(self, user,message):
        return f"Sending SMS to {user}: {message}"
    
class PUSH(Observer):
    def send(self, user,message):
        return f"Sending PUSH Notification to {user}: {message}"

class Helper:
    @staticmethod
    def base_info():
        method = input("Method : ")
        user = input("User : ")
        message = input("Message : ")
        return method, user, message
        
class NotificationFactory:
    @staticmethod
    def create_notification(method, user, message, logger):
        method, user, message = Helper.base_info()
        if method == "email":
            return Notification(Email(), user, message, logger)
        elif method == "sms":
            return Notification(SMS(), user, message, logger)
        elif method == "push":
            return Notification(PUSH(), user, message, logger)
        else:
            raise ValueError(f"Unknown notification method: {method}")

    

    
