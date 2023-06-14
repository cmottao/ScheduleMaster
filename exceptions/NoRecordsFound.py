class NoRecordsFound(Exception):
    '''Exception to be thrown when the data base accesible class methods did not found any records
        so as to stop the CLI GUI process'''
    
    def __init__(self, message):
        super().__init__(message)