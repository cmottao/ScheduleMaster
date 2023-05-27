class Schedule():
    '''Represents an object of type Schedule.'''

    # Constructor method
    def __init__(self):
        '''Initializes an object of the Schedule class.'''

        self._courses = []

    # Getters methods 
    def get_courses(self):
        return self._courses
    
    # Methods
    def add_course(self):
        '''Adds a course to the schedule.'''

        pass

    def validate(self):
        '''Validates if there are no crossings of courses in the schedule.'''

        pass