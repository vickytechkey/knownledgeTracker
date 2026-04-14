class CourseStatus:
    def __init__(self,status):
        self._status = status
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self._status)
        
    def __set__(self, instance, value):
        if value not in ["active","inactive","Inprogress","Completed","NotStarted","NotRequired"]:
            raise ValueError("status should be either active or inactive")
        setattr(instance, self._status, value)