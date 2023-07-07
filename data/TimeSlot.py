import datetime


class TimeSlot():
    '''Represents an object of type TimeSlot.'''

    # Constructor method
    def __init__(self, week_day, starts_at, ends_at):
        '''Initializes an object of the TimeSlot class. Attributes like ends_at and starts_at must be in HH:MM:SS format'''
        
        self._week_day = week_day
        self._starts_at = datetime.time(*[int(i) for i in starts_at.split(':')])
        self._ends_at = datetime.time(*[int(i) for i in ends_at.split(':')])
    
    # Getters methods
    def get_id(self):
        return self._id
    
    def get_week_day(self):
        return self._week_day
    
    def get_starts_at(self):
        return self._starts_at
    
    def get_ends_at(self):
        return self._ends_at

    # Methods
    @classmethod
    def from_str_repr(cls, repr):
        '''Recieves a string fromatted as form WEEKDAY HH:MM:SS-HH:MM:SS and creates the TimeSlot object according to that data.'''
        
        info = repr.split()
        week_day = info[0]
        starts_at = info[1].split('-')[0]
        ends_at = info[1].split('-')[1]

        return cls(week_day, starts_at, ends_at)


    def __eq__(self, other):
        '''Dunder method to know if two time slots are the same.'''

        if self._week_day == other.get_week_day() and self._starts_at == other.get_starts_at() and self._ends_at == other.get_ends_at():
            return True
        else:
            return False
        
        
    def __str__(self):
        '''Returns a string representation of the TimeSlot object.'''

        return f'{self._week_day} {self._starts_at}-{self._ends_at}'