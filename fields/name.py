class Name:
    def __set_name__(self, owner, name):
        self.private_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if len(value.strip()) == 0:
            raise ValueError("name should not be empty")
        setattr(instance, self.private_name, value)