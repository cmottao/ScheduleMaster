from config.db import engine
from .DataBaseAccessible import DataBaseAccessible

from sqlalchemy.sql import text

class Faculty(DataBaseAccessible):
    '''Represents an object of type Faculty.'''
    
    # Constructor method
    def __init__(self, id, name):
        '''Initializes an object of the Faculty class.'''

        self._id = id
        self._name = name

    # Getters methods
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    @classmethod
    def retrieve_from_database(cls, filters={'FACULTY_ID': None}):
        faculties = []
        query = 'SELECT * FROM faculties'

        if filters['FACULTY_ID']:
            query += f' WHERE id = {filters["FACULTY_ID"]}'
        
        with engine.connect() as conn:
            results = conn.execute(text(query + ';'))
            for result in results:
                faculties.append(cls(result[0], result[1]))
        
        return faculties
    
    def __str__(self):
        return f'{self._id}, {self._name}'

    # Methods