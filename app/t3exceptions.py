# Very basic custom exception that throws whatever message it is fed.
class Error(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
