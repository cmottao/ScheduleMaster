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
    def add_course(self, course):
        '''Adds a course to the schedule.'''

        self._courses.append(course)


    def remove_course(self, group_number, subject_id):
        '''Removes a course from the schedule based on the given group number and subject ID.'''

        for i in range(len(self._courses)):
            course = self._courses[i]
            if course.get_group_number() == group_number and course.get_subject().get_id() == subject_id:
                self._courses.pop(i)
                return


    def course_is_valid(self, course_to_add):
        ''' Checks if a course is valid to be added to the schedule.'''

        for course in self._courses:
            if course_to_add.get_time_slot_one() == course.get_time_slot_one() or course_to_add.get_time_slot_one() == course.get_time_slot_two():
                return 'croice'
            elif course_to_add.get_time_slot_two() == course.get_time_slot_one() or course_to_add.get_time_slot_two() == course.get_time_slot_two():
                return 'croice'
            elif course_to_add.get_subject() == course.get_subject():
                return 'same subject'
        return 'valid'