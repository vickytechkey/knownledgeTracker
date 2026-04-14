from fields.name import Name
from fields.date import dateinput

class CourseDetails:
    _coursename = Name()
    _startdate = dateinput()

    def __init__(self,name,startdate):
        self._coursename = name
        self._startdate = startdate



c = CourseDetails(" vig ", "2023-10-10")
print(c._coursename)
print(c._startdate)
    