class Space:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, availability):
        self.id = id
        self.name = name
        self.availability = availability

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.availability})"

    # These next two methods will be used by the controller to check if
    # books are valid and if not show errors to the user.
    def is_valid(self):
        if self.name == None or self.name == "":
            return False
        if self.availability == None or self.availability == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.name == None or self.name == "":
            errors.append("Title can't be blank")
        if self.availability == None or self.availability == "":
            errors.append("Author name can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
