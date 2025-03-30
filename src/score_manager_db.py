import sqlite3
from datetime import datetime

class ScoreManagerDB:
    """
    A database manager class for handling game scores storage and retrieval.

    Provides methods to store player scores and retrieve high scores from a SQLite database. It handles connection
    management and SQL operations while maintaining data integrity through proper transaction management.
    Methods: create_table, add_score, get_high_scores
    """
    DB_NAME = '../data/score.db'
    def __init__(self) -> None:
        self.conn = sqlite3.connect(self.DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    date DATETIME NOT NULL
                )'''
                            )
        self.conn.commit()

    def add_score(self, username: str, score: int) -> None:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute('''
                INSERT INTO scores (username, score, date) VALUES (?, ?, ?)
                ''', (username, score, current_time)
                            )
        self.conn.commit()
        self.conn.close()

    def get_high_scores(self, limit=10) -> list:
        self.cursor.execute("SELECT username, score, date FROM scores ORDER BY score DESC LIMIT ?", (limit,))
        high_scores = self.cursor.fetchall()
        self.conn.close()
        return high_scores if high_scores else []
