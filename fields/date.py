from datetime import datetime
class dateinput:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name)
 
    def __set__(self, instance, value):
        today = datetime.now().date()
        print(today)
        if not isinstance(value, str):
            raise ValueError("Date must be a string in the format 'YYYY-MM-DD'")
        # Additional validation for date format can be added here
        setattr(instance, self.private_name, value)