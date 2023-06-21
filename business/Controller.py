from business.Schedule import Schedule
from data.Course import Course
from data.Subject import Subject


class Controller():
    '''Controller of the ScheduleMaster app.'''

    def __init__(self):
        '''Initializes the controller of the ScheduleMaster app.'''

        self._schedule = Schedule()


    def get_subjects(self, filters):
        '''Retrieves subjects from the database based on the given filters and returns them.'''

        return Subject.retrieve_from_database(filters)
    
    
    def get_courses(self, filters):
        '''Retrieves courses from the database based on the given filters and returns them.'''

        return Course.retrieve_from_database(filters)
    
    
    def get_course(self, id):
        '''Retrieves a course from the database based on the given ID and returns it.'''

        return Course.retrieve_from_database_by_id(id)
    
    
    def course_is_valid(self, course):
        '''Checks if a course is valid by calling the course_is_valid method of the Schedule class.'''

        return self._schedule.course_is_valid(course)
    
    
    def add_course_to_schedule(self, course):
        '''Adds a course to the schedule by calling the add_course method of the Schedule class.'''

        self._schedule.add_course(course)


    def remove_course_from_schedule(self, group_number, subject_id):
        '''Removes a course from the schedule based on the given group number and subject ID by calling the 
            remove_course method of the Schedule class.'''

        self._schedule.remove_course(group_number, subject_id)


    def get_courses_from_schedule(self):
        '''Returns the courses currently in the schedule by calling the get_courses method of the Schedule class.'''

        return self._schedule.get_courses()