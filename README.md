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


## Day 3: Defining Schema with Core

### Features
- Defining database tables using Table and Column in Core style
- Using MetaData to organize schema objects
- Creating tables in SQLite via metadata.create_all()
- Basic column constraints (primary key, nullable, default)

### Progress
- Created a central MetaData object  
- Defined the "tasks" table with id, title, description, completed, created_at  
- Added setup_tables.py script to create tables in the database  
- Used modern column definitions with explicit types and constraints  

### Key Notes
- MetaData acts as a central registry for all tables and schema constructs  
- Table(name, metadata, Column(...), ...) is the Core way to describe tables  
- metadata.create_all(engine) creates missing tables safely (idempotent)  
- Use server_default=func.now() for database-generated timestamps  
- Column parameters like nullable=False and primary_key=True directly translate to SQL constraints  
- In Core style, tables are plain objects – no classes or ORM mapping yet