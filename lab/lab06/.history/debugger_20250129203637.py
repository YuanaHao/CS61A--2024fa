class Email:
    """An email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the client that sent the email
        recipient_name (str): the name of the recipient (another client)
    """
    def __init__(self, msg, sender, recipient_name):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name

class Server:
    """Each Server has one instance attribute called clients that is a
    dictionary from client names to client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Append the email to the inbox of the client it is addressed to.
            email is an instance of the Email class.
        """
        self.clients[email.recipient_name].inbox.append(email)

    def register_client(self, client):
        """Add a client to the clients mapping (which is a 
        dictionary from client names to client instances).
            client is an instance of the Client class.
        """
        self.clients[client] = client

class Client:
    """A client has a server, a name (str), and an inbox (list).

    s = Server()
    a = Client(s, 'Alice')
    b = Client(s, 'Bob')
    a.compose('Hello, World!', 'Bob')
    b.inbox[0].msg
    'Hello, World!'
    a.compose('CS 61A Rocks!', 'Bob')
    len(b.inbox)
    2
    b.inbox[1].msg
    'CS 61A Rocks!'
    b.inbox[1].sender.name
    'Alice'
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        server.register_client(self)

    def compose(self, message, recipient_name):
        """Send an email with the given message to the recipient."""
        email = Email(message, self.name, recipient_name)
        self.server.send(email)

def main():
    s = Server()
    a = Client(s, 'Alice')
    b = Client(s, 'Bob')
    a.compose('Hello, World!', 'Bob')
    b.inbox[0].msg
    a.compose('CS 61A Rocks!', 'Bob')
    len(b.inbox)
    b.inbox[1].msg
    b.inbox[1].sender.name

if __name__ == "__main__":
    main()