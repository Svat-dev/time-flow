from os import path, makedirs

import sqlite3

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

DB_DIR = path.join(BASE_DIR, "database")
DB_PATH = path.join(DB_DIR, "timeflow.db")


def get_connection() -> sqlite3.Connection:
    makedirs(DB_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")

    return conn


def initialize_database() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id          INTEGER                PRIMARY KEY AUTOINCREMENT,
                name        VARCHAR(100) NOT NULL,
                color       VARCHAR(7)   NOT NULL  DEFAULT '#ffffff',
                icon        VARCHAR(50),
                created_at  DATETIME     NOT NULL  DEFAULT CURRENT_TIMESTAMP,
                is_archived BOOLEAN      NOT NULL  DEFAULT 0
            );
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS time_entries (
                id          INTEGER                PRIMARY KEY AUTOINCREMENT,
                category_id INTEGER      NOT NULL,
                title       VARCHAR(100) NOT NULL,
                description VARCHAR(255),
                started_at  DATETIME     NOT NULL,
                ended_at    DATETIME               DEFAULT NULL,
                source      TEXT         NOT NULL  DEFAULT 'timer',
                created_at  DATETIME     NOT NULL  DEFAULT CURRENT_TIMESTAMP,
                updated_at  DATETIME     NOT NULL  DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT,

                CHECK (source IN ('timer', 'manual')),

                CHECK (ended_at IS NULL OR ended_at >= started_at)
            );
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key   VARCHAR(100) PRIMARY KEY,
                value TEXT
            );
        """)

        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_time_entries_category ON time_entries(category_id);
        """)

        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_time_entries_started_at ON time_entries(started_at);
        """)

        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_time_entries_ended_at ON time_entries(ended_at);
        """)
