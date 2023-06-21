from abc import abstractmethod


class DataBaseAccessible():
    # Abstract Methods
    @abstractmethod
    def retrieve_from_database(cls, filters=None):
        '''All classes who are data base - accessible, must implement a method which will be responsible of instanciating 
            objects of the class from data retrieved from a data base query according some optional filters.'''
        
        pass

    @abstractmethod
    def retrieve_from_database_by_id(cls, id):
        '''Retrieves a single object by its id.'''

        pass