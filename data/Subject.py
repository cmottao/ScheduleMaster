from config.db import engine
from .Faculty import Faculty
from .DataBaseAccessible import DataBaseAccessible

from sqlalchemy.sql import text

class Subject(DataBaseAccessible):
    '''Initializes an object of type Subject.'''
    
    # Constructor method
    def __init__(self, id, name, credits, faculty):
        '''Initializes an object of the Subject Class.'''

        self._id = id
        self._name = name
        self._credits = credits
        self._faculty = faculty

    # Getters methods
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
    
    def get_credits(self):
        return self._credits
    
    def get_faculty(self):
        return self._faculty
    
    @classmethod
    def retrieve_from_database(cls, filters={'FACULTY_ID':None, 'CREDITS':None}):
        subjects = []
        query = f'SELECT * FROM subjects WHERE faculty_id = {filters["FACULTY_ID"]}'
        if filters['CREDITS']:
            query += f' AND credits = {filters["CREDITS"]}'

        with engine.connect() as conn:
            faculty = Faculty.retrieve_from_database(filters={'FACULTY_ID': filters['FACULTY_ID']})
            if faculty:
                faculty = faculty[0] 
            else:
                return None # Faculty does not exists, so no courses assosiated with that faculty
            results = conn.execute(text(query + ';'))
            for result in results:
                #faculty = Faculty()
                subjects.append(cls(result[0], result[1], result[2], faculty))
        
        return subjects
    
    @classmethod
    def retrieve_from_database_by_id(cls, id):
        query = f'SELECT * FROM subjects WHERE id = {id};'

        with engine.connect() as conn:
            result = conn.execute(text(query)).first()
            faculty = Faculty.retrieve_from_database(filters={'FACULTY_ID':result[3]})
            return cls(result[0], result[1], result[2], faculty)

    
    def __str__(self):
        return f'id = {self._id}, nombre = {self._name}, creditos = {self._credits}, facultad={self._faculty.get_name()}'
    
    # Methods