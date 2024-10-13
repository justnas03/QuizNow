import sqlite3
class QuizNowDB:
    def __init__(self):
        self.db_url =  "E:\\QuizNowDB\\QuizNow.db"
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_url)
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def close(self):
        if self.connection:
            self.connection.close()

