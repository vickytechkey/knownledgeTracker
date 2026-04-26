class PositiveInteger:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Value must be a positive integer")
        setattr(instance, self.private_name, value)
        
