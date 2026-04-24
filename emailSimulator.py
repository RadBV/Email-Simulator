
class Email():
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
        
emailObj = Email("alice@example.com", "bob@example.com", "Hello", "Hi Bob!")

print(emailObj.sender)
print(emailObj.subject)