import sqlite3


class Database(object):
    """sqlite3 database class that holds testers jobs"""
    DB_LOCATION = "pizzaria.db"

    def __init__(self):
        """Initialize db class variables"""
        sqlite3.enable_callback_tracebacks(True)
        self.connection = sqlite3.connect(Database.DB_LOCATION)
        self.cur = self.connection.cursor()
        self.connection.set_trace_callback(self.callback)

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()

    def execute(self, *new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(*new_data)

    def commit(self):
        """commit changes to database"""
        self.connection.commit()
    
    def callback(self, stin):
        if stin == "COMMIT":
            print(f"New commit in {self.__class__.__name__}")
        
    def __del__(self):
        """close sqlite3 connection"""
        self.cur.close()
        self.connection.close()

