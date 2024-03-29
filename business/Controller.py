import datetime

from tabulate import tabulate

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


    def tabulate_schedule(self):
        '''This method generates a tabular representation of a schedule based on the provided courses and their time slots.'''

        courses = self._schedule.get_courses()
        start_hours = [7, 9, 11, 14, 16, 18] # These are the hours when a course can start, will work as row indexes
        week_days = ['LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES']
        table = [[' ' for _ in range(5)] for _ in range(6)] # Starts with an empty mnatrix
        
        # Filling the matrix
        for course in courses:
            subject_name = course.get_subject().get_name()
            slot_1 = course.get_time_slot_one()
            slot_2 = course.get_time_slot_two()

            # Start time gives us the row index, week day the column one
            table[start_hours.index(slot_1.get_starts_at().hour)][week_days.index(slot_1.get_week_day())] = subject_name
            table[start_hours.index(slot_2.get_starts_at().hour)][week_days.index(slot_2.get_week_day())] = subject_name

        table[0].insert(0, '7:00-9:00')
        table[1].insert(0, '9:00-11:00')
        table[2].insert(0, '11:00-13:00')
        table[3].insert(0, '14:00-16:00')
        table[4].insert(0, '16:00-18:00')
        table[5].insert(0, '18:00-20:00')

        str_schedule = f'HORARIO GENERADO: {datetime.datetime.now()} \n\n' + str(tabulate(table, headers=['', *week_days], tablefmt='presto'))

        return str_schedule