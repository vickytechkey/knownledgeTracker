class positiveInteger:
    def __set_name__(self, owner, value):
        self.positive_integer = '_' + value

    def __get__(self, instance, owner):
        return getattr(instance, self.positive_integer)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Value must be a positive integer")
        setattr(instance, self.positive_integer, value)