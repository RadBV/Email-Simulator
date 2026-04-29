
class Email():
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read = False
    
    def markAsRead(self):
        self.read = True

    def displayFullEmail(self):
        self.markAsRead()
        print("\n--- Email ---")
        print(f"From: {self.sender.name}")
        print(f"To: {self.receiver.name}")
        print(f"Subject: {self.subject}")
        print(f"Body: {self.body}")
        print('------------\n')

    def __str__(self):
        status = "Read" if self.read else "Unread"
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject}"

class User():
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()
    
    def sendEmail(self, receiver, subject, body):
        email = Email(self, receiver, subject, body)
        receiver.inbox.receiveEmail(email)
        
class Inbox():
    def __init__(self):
        self.emails = []
        
    def receiveEmail(self, email):
        self.emails.append(email)

    def listEmails(self):
        if not self.emails:
            print("Your inbox is empty.\n")
            return
        print("\nYour Emails:")
        for i, email in enumerate(self.emails, 1):
            print(f"{i}. {str(email)}")