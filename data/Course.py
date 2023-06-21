from sqlalchemy.sql import text

from config.db import engine

from .DataBaseAccessible import DataBaseAccessible
from .Professor import Professor
from .Subject import Subject
from .TimeSlot import TimeSlot


class Course(DataBaseAccessible):
    '''Represents an object of type Course.'''
    
    # Constructor method
    def __init__(self, group_number, subject, credits, professor, time_slot_one, time_slot_two):
        '''Initializes an object of the Course class.'''

        self._group_number = group_number
        self._subject = subject
        self._credits = credits
        self._professor = professor
        self._time_slot_one = time_slot_one
        self._time_slot_two = time_slot_two

    # Getters methods
    def get_group_number(self):
        return self._group_number
    
    def get_subject(self):
        return self._subject
    
    def get_credits(self):
        return self._credits
    
    def get_professor(self):
        return self._professor
    
    def get_time_slot_one(self):
        return self._time_slot_one
    
    def get_time_slot_two(self):
        return self._time_slot_two
    
    # Methods
    @classmethod
    def retrieve_from_database(cls, filters={'SUBJECT_ID': None}):
        '''Retrieves courses from the database based on the specified filters.'''

        courses = []
        query = 'SELECT * FROM all_course_data'

        if filters['SUBJECT_ID']:
            query += f' WHERE subj_id = {filters["SUBJECT_ID"]}'
        
        with engine.connect() as conn:
            results = conn.execute(text(query + ' ORDER BY group_number;'))
            for result in results:
                subject = Subject.retrieve_from_database_by_id(result[0])
                professor = Professor(result[4])
                time_slot1 = TimeSlot.from_str_repr(result[5])
                time_slot2 = TimeSlot.from_str_repr(result[6])

                courses.append(cls(result[1], subject, int(result[3]), professor, time_slot1, time_slot2))
        
        return courses


    @classmethod
    def retrieve_from_database_by_id(cls, id):
        '''Retrieves a course from the database based on the specified composite ID.

            Args:
                id: A tuple with two elements representing the composite ID of the course.
                    1) Group number
                    2) Subject ID
        '''    

        query = f'SELECT * FROM all_course_data WHERE group_number = {id[0]} AND subj_id = {id[1]};'
        
        with engine.connect() as conn:
            result = conn.execute(text(query)).first()
            subject = Subject.retrieve_from_database_by_id(result[0])
            professor = Professor(result[4])
            time_slot1 = TimeSlot.from_str_repr(result[5])
            time_slot2 = TimeSlot.from_str_repr(result[6])

            return cls(result[1], subject, int(result[3]), professor, time_slot1, time_slot2)