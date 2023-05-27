class Professor():
    '''Represents an object of type Professor.'''
    
    # Constructor method
    def __init__(self):
        '''Initializes an object of the Professor class.'''

        self._id = None
        self._name = None

    # Getters methods
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    # Methods