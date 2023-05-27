class Subject():
    '''Initializes an object of type Subject.'''
    
    # Constructor method
    def __init__(self):
        '''Initializes an object of the Subject Class.'''

        self._id = None
        self._name = None
        self._credits = None
        self._faculty = None

    # Getters methods
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
    
    def get_credits(self):
        return self._credits
    
    def get_faculty(self):
        return self._faculty
    
    # Methods