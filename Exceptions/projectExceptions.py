class FailedInsertException(Exception):
    def __init__(self, message="Insert procedure was failed"):
        self.message = message

class FailedUpdatingException(Exception):
    def __init__(self, message="Update procedure was failed"):
        self.message = message

class FailedDeleteexception(Exception):
    def __init__(self, message="Delete procedure was failed"):
        self.message = message