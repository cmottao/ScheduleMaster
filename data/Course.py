from config.db import engine
from .Subject import Subject
from .Professor import Professor
from .DataBaseAccessible import DataBaseAccessible

from sqlalchemy.sql import text

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
    
    @classmethod
    def retrieve_from_database(cls, filters={'SUBJECT_ID':None}):
        courses = []
        query = 'SELECT * FROM all_course_data'
        if filters['SUBJECT_ID']:
            query += f' WHERE subj_id = {filters["SUBJECT_ID"]}'
        
        with engine.connect() as conn:
            results = conn.execute(text(query + ' ORDER BY group_number;'))
            for result in results:
                subject = Subject.retrieve_from_database_by_id(result[0])
                professor = Professor(result[4])
                courses.append(cls(result[1], subject, int(result[3]), professor, result[5], result[6]))
        
        return courses

    @classmethod
    def retrieve_from_database_by_id(cls, id):
        '''Courses have a composite pkey, so id must be a touple with 2 elements
            1) group number
            2) subj id
        '''    
        query = f'SELECT * FROM all_course_data WHERE group_number = {id[0]} AND subj_id = {id[1]};'
        
        with engine.connect() as conn:
            result = conn.execute(text(query)).first()
            subject = Subject.retrieve_from_database_by_id(result[0])
            professor = Professor(result[4])
            return cls(result[1], subject, int(result[3]), professor, result[5], result[6])
        
    def __str__(self):
        return f'Grupo = {self._group_number}, Materia = {self._subject.get_name()}'
    # Methods