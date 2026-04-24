
class Email():
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
    
    def markAsRead(self):
        self.read = True

class User():
    def __init__(self, name):
        self.name = name
        self.inbox = []
    
    def sendEmail(self, receiver, subject, body):
        email = Email(self, receiver, subject, body)