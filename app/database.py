import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.environ.get("TIMEFLOW_DB_PATH", os.path.join(DB_DIR, "timeflow.db"))

RUNTIME_ERROR = "Database is not connected"


class Database:
    def __init__(self, db_path: str | None = None) -> None:
        self.db_path = db_path or DB_PATH
        self.conn: sqlite3.Connection | None = None
        self.cursor: sqlite3.Cursor | None = None

    def connect(self) -> None:
        if self.conn is not None:
            return

        os.makedirs(os.path.dirname(os.path.abspath(self.db_path)), exist_ok=True)

        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

        self.conn.execute("PRAGMA foreign_keys = ON")
        self.conn.execute("PRAGMA journal_mode = WAL")

        self.cursor = self.conn.cursor()

    def disconnect(self) -> None:
        if self.cursor is not None:
            self.cursor.close()
            self.cursor = None

        if self.conn is not None:
            self.conn.close()
            self.conn = None

    def initialize_database(self) -> None:
        self.execute("""CREATE TABLE IF NOT EXISTS categories (
            id          INTEGER      PRIMARY KEY AUTOINCREMENT,
            name        VARCHAR(100) NOT NULL    COLLATE NOCASE UNIQUE,
            color       VARCHAR(7)   NOT NULL    DEFAULT '#8b5cf6',
            icon        VARCHAR(50),
            created_at  DATETIME     NOT NULL    DEFAULT CURRENT_TIMESTAMP,
            is_archived BOOLEAN      NOT NULL    DEFAULT 0,

            CHECK(length(color) = 7 AND substr(color, 1, 1) = '#')
        )""")

        self.execute("""CREATE TABLE IF NOT EXISTS time_entries (
            id          INTEGER      PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER      NOT NULL,
            title       VARCHAR(100) NOT NULL,
            description VARCHAR(255),
            started_at  TEXT         NOT NULL,
            ended_at    TEXT                     DEFAULT NULL,
            source      TEXT         NOT NULL    DEFAULT 'timer',
            created_at  DATETIME     NOT NULL    DEFAULT CURRENT_TIMESTAMP,
            updated_at  DATETIME     NOT NULL    DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT,

            CHECK(source IN ('timer', 'manual')),

            CHECK(ended_at IS NULL OR ended_at >= started_at)
        )""")

        self.execute(
            "CREATE TABLE IF NOT EXISTS settings (key VARCHAR(100) PRIMARY KEY, value TEXT)"
        )

        self.execute(
            "CREATE INDEX IF NOT EXISTS idx_time_entries_category ON time_entries(category_id)"
        )

        self.execute(
            "CREATE INDEX IF NOT EXISTS idx_time_entries_started_at ON time_entries(started_at)"
        )

        self.execute(
            "CREATE INDEX IF NOT EXISTS idx_time_entries_ended_at ON time_entries(ended_at)"
        )

        self.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS idx_time_entries_active ON time_entries(ended_at) WHERE ended_at IS NULL"
        )

        self.execute(
            """CREATE TRIGGER IF NOT EXISTS trg_time_entries_updated_at
            AFTER UPDATE ON time_entries FOR EACH ROW
            WHEN NEW.updated_at = OLD.updated_at
            BEGIN UPDATE time_entries SET updated_at=CURRENT_TIMESTAMP WHERE id = NEW.id; END"""
        )

        self.commit()

    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        if self.conn is None:
            raise RuntimeError(RUNTIME_ERROR)
        return self.conn.execute(query, params)

    def fetch_one(self, query: str, params: tuple = ()):
        return self.execute(query, params).fetchone()

    def fetch_all(self, query: str, params: tuple = ()):
        return self.execute(query, params).fetchall()

    def commit(self) -> None:
        if self.conn is None:
            raise RuntimeError(RUNTIME_ERROR)
        self.conn.commit()

    def rollback(self) -> None:
        if self.conn is not None:
            self.conn.rollback()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.rollback() if exc_type else self.commit()
        self.disconnect()

        return False
