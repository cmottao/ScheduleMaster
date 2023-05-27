class TimeSlot():
    '''Represents an object of type TimeSlot.'''

    # Constructor method
    def __init__(self):
        '''Initializes an object of the TimeSlot class.'''

        self._id = None
        self._week_day = None
        self._start_at = None
        self._end_at = None

    # Getters methods
    def get_id(self):
        return self._id
    
    def get_week_day(self):
        return self._week_day
    
    def get_start_at(self):
        return self._start_at
    
    def get_end_at(self):
        return self._end_at
    
    # Methods