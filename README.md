## Day 1: SQLAlchemy Setup

### Features
- Project initialization with SQLAlchemy 2.0+
- Database engine creation using SQLite
- Session factory configuration
- Base class definition for declarative models
- Persistent storage in SQLite database

### Progress
- Installed SQLAlchemy and created project structure  
- Created engine with connection string 'sqlite:///todo.db'  
- Configured SessionLocal factory with autocommit=False and autoflush=False  
- Defined Base class inheriting from DeclarativeBase  
- Created initial files: database.py, main.py, README.md

### Key Notes
- SQLAlchemy 2.0+ uses DeclarativeBase instead of the older declarative_base()  
- Recommended to set autocommit=False and autoflush=False on sessionmaker  
- echo=True on engine is useful during learning and debugging  
- SQLite is a good choice for learning because it requires no separate server  
- The engine and session factory should be created once and reused


## Day 2: Core Basics

### Features
- Introduction to SQLAlchemy Core layer
- Engine and Connection management
- Executing raw SQL statements
- Basic table creation and insertion
- Testing connection to SQLite database

### Progress
- Updated main.py
- Added core_test.py to demonstrate Core usage (create table, insert, select)  
- Ensured echo=True for query logging in development  
- Tested first connection and query execution  

### Key Notes
- Core is the low-level layer for direct SQL-like operations in Python  
- Always use with engine.connect() for safe connection handling  
- In SQLAlchemy 2.0+, execute() is called on Connection, not Engine  
- Use text() for raw SQL to prevent injection risks  
- Engine manages dialect and connection pooling automatically
