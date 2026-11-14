# TimeFlow

TimeFlow is a desktop time-tracking application built with Python and PySide6. It helps users organize activities, track working time, manage categories, and analyze daily productivity.

## Features

- Create, edit, and archive categories.
- Track time with an activity timer.
- Manually create, edit, and delete activities.
- View activities on a daily timeline.
- Analyze daily time usage and category statistics.
- Store data locally using SQLite.

## Requirements

- Python 3.10+
- PySide6
- Linux, Windows, or macOS

## Installation

Clone the repository:

```bash
git clone https://github.com/Svat-dev/time-flow.git
cd time-flow
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate UI Python files:

```bash
make ui-generate
```

Run the application:

```bash
make app-run
```

Alternatively:

```bash
python main.py
```

## Architecture

The project uses a layered architecture that separates the user interface, business logic, data access, and domain models.

```text
time-flow/
├── app/                  # Application initialization and configuration
│   ├── application.py
│   ├── database.py
│   └── styles.py
│
├── models/               # Application data models
│   ├── activity.py
│   ├── analytics.py
│   └── category.py
│
├── repositories/         # SQLite data access layer
│   ├── category_repository.py
│   └── time_entry_repository.py
│
├── services/             # Business logic
│   ├── activity_service.py
│   ├── analytics_service.py
│   ├── category_service.py
│   └── timer_service.py
│
├── ui/                   # PySide6 graphical interface
│   ├── dialogs/           # Activity and category dialogs
│   ├── widgets/           # Custom UI components
│   └── windows/           # Main application window
│
├── resources/            # Icons and QSS stylesheets
├── utils/                # Utility functions
├── data/                 # SQLite database
│
├── config.py             # Application configuration
├── main.py               # Application entry point
├── Makefile              # Development commands
└── requirements.txt      # Python dependencies
```

### Main Components

- **Models** — define application entities using Python dataclasses.
- **Repositories** — handle database queries and persistence.
- **Services** — implement activity management, time tracking, and analytics.
- **UI** — handles user interaction and application presentation.
- **App** — initializes the application, database, and styles.
- **Utils** — provides reusable helper functions.

## Database

TimeFlow uses SQLite for local data storage. The database is automatically initialized when the application starts.
