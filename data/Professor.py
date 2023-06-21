class Professor():
    '''Represents an object of type Professor.'''
    
    # Constructor method
    def __init__(self, name):
        '''Initializes an object of the Professor class.'''
        
        self._name = name

    # Getters methods
    def get_name(self):
        return self._name