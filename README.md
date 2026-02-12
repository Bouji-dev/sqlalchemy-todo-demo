# SQLAlchemy Todo Demo

A clean, console-based **Todo List** application built with **Python** and **SQLAlchemy 2.0+** (both Core & ORM layers).  

This project was created as a structured, step-by-step learning journey to deeply understand SQLAlchemy — from basic setup to advanced ORM features, relationships, querying, transactions, migrations, and production best practices.

Perfect for:
- Developers learning SQLAlchemy in a practical way
- Portfolio showcase for ORM & database handling skills
- Reference for modern SQLAlchemy 2.0+ patterns


## Learning Journey Summary

| Day | Topic                              | Key Concepts & Files                          |
|-----|------------------------------------|-----------------------------------------------|
| 1   | Setup & Meaningful Names           | database.py, engine, sessionmaker             |
| 2   | Core Basics                        | Engine, Connection, text() queries            |
| 3   | Schema Definition (Core)           | Table, Column, MetaData, create_all           |
| 4   | Core DML                           | insert, select, update, delete                |
| 5   | Datatypes                          | String, Enum, DateTime, server_default        |
| 6   | ORM Quick Start                    | DeclarativeBase, mapped_column, Session       |
| 7   | Relationships                      | One-to-Many, back_populates, foreign key      |
| 8   | Advanced Querying                  | select(), join, group_by, having, subquery    |
| 9   | Session & Transactions             | flush, commit, rollback, context manager      |
| 10  | Extensions & Best Practices        | hybrid_property, case(), eager loading        |
| 11  | Migrations with Alembic            | alembic init, revision --autogenerate         |

## Features Implemented

- **Core Layer** (Days 1–5)
  - Engine & Connection management
  - Table / Column / MetaData definition
  - Full CRUD with expression language
  - Basic & advanced datatypes (Enum, DateTime, server_default, etc.)

- **ORM Layer** (Days 6–11)
  - Declarative models with `mapped_column()` & typing
  - One-to-Many relationship (User ↔ Task)
  - Advanced querying (filter, join, group_by, having, subquery)
  - Session management, transactions, flush/commit/rollback
  - Hybrid properties
  - Migrations with **Alembic** (autogenerate + manual review)

## Installation


### 1. Clone the repository
git clone https://github.com/Bouji-dev/sqlalchemy-todo-demo.git
cd sqlalchemy-todo-demo

### 2. Create and activate virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
### or
.venv\Scripts\activate         # Windows

### 3. Install dependencies
pip install sqlalchemy alembic


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


## Day 4: SQL Statements with Core

### Features
- Insert data into tables using Core
- Select and fetch records
- Update existing records
- Delete records
- Basic transaction management with begin()

### Progress
- Created crud_core.py with functions for insert, select, update, delete  
- Demonstrated usage in main.py  
- Used insert().values(), select(), update().where(), delete().where()  
- Handled transactions with connection.begin()

### Key Notes
- All DML statements (insert/update/delete) are executed via connection.execute()  
- where() is mandatory for update/delete to avoid affecting entire table  
- result.lastrowid or returning() can retrieve auto-generated IDs  
- Use with connection.begin() for automatic commit/rollback  
- Core expression language is database-agnostic and prevents SQL injection


## Day 5: Datatypes

### Features
- Basic datatypes (Integer, String, Boolean, DateTime)
- Advanced datatypes (Enum, JSON)
- Dialect-specific behavior

### Progress
- Updated models_core.py with Enum for priority  
- Tested insert/select with new datatype

### Key Notes
- Specify length for String to ensure portability  
- Use Enum for restricted values  
- DateTime with timezone for global apps


## Day 6: ORM Quick Start

### Features
- Defining models with DeclarativeBase
- Using mapped_column() for type-safe columns
- Creating tables with Base.metadata
- Basic CRUD with Session

### Progress
- Created models_orm.py with Task model  
- Added setup_orm_tables.py for table creation  
- Introduced Session and basic add/query operations  

### Key Notes
- DeclarativeBase is the modern way in SQLAlchemy 2.0+  
- mapped_column() provides better typing and validation  
- Session manages transactions and object state  
- Use session.commit() and session.refresh() for new objects  
- Avoid mixing Core and ORM tables in the same metadata unless necessary


## Day 7: Relationship Configuration

### Features
- One-to-Many relationship
- back_populates and foreign key
- Cascade options
- Accessing related objects

### Progress
- Added User and Task models with relationship  
- Implemented two-way relationship using back_populates  
- Tested adding tasks to a user and loading them  

### Key Notes
- Foreign key is always placed on the Many side  
- back_populates defines a bidirectional relationship in a clear and controlled way  
- cascade="all, delete-orphan" automatically deletes dependent objects when parent is removed  
- Lazy loading is the default; for better performance, use joined or selectin loading  
- For Many-to-Many relationships, use an association table or secondary parameter


## Day 8: ORM Querying Guide (Advanced)

### Features
- Filtering with where() and complex conditions
- Joining tables
- Aggregation (count, sum, etc.) + group_by / having
- Ordering, limit, offset
- Subqueries

### Progress
- Learned modern select() syntax in SQLAlchemy 2.0+  
- Implemented joins, aggregations, and subqueries  
- Added advanced query examples in crud_orm.py  

### Key Notes
- Use select() instead of session.query() in 2.0+  
- Combine conditions with and_(), or_(), or & | ~ operators  
- Use joinedload() or selectinload() to avoid N+1 query problem  
- func.count(), func.sum() for aggregations  
- Subqueries are powerful for nested filtering  
- Always use scalars() or execute() with select() for results


## Day 9: Using the ORM Session (Transactions & Advanced Management)

### Features
- Session as unit of work
- Manual flush, commit, rollback
- Transaction nesting with begin()
- Error handling and rollback
- flush() for intermediate persistence

### Progress
- Learned Session lifecycle and transaction control  
- Added transaction-safe user/task creation  
- Demonstrated flush() for ID generation  
- Implemented try/except + rollback pattern  

### Key Notes
- Always use with SessionLocal() as session: for auto cleanup  
- flush() sends changes to DB without committing (useful for IDs)  
- commit() finalizes the transaction, rollback() cancels it  
- autoflush=True (default) ensures consistency before queries  
- Use session.begin() for explicit nested transactions  
- Handle exceptions and always rollback on failure


## Day 10: Configuration Extensions & Best Practices

### Features
- Hybrid properties
- Association proxy (basic)
- Automap for legacy databases
- Advanced debugging and error handling

### Progress
- Added hybrid_property to Task model for readable status  
- Implemented query using hybrid expression  
- Reviewed best practices for production use  

### Key Notes
- hybrid_property allows computed attributes usable in queries  
- Use @expression decorator for SQL-level computation  
- Always set autocommit=False and autoflush=False on sessionmaker  
- Use selectinload() / joinedload() to prevent N+1 queries  
- Prefer Alembic for migrations instead of create_all() in production  
- Handle common exceptions: NoResultFound, IntegrityError, DetachedInstanceError


## Day 11: Migrations with Alembic + Final Best Practices + Project Wrap-up

### Features
- Database migrations using Alembic
- Autogenerate revisions
- Upgrade / downgrade schema changes
- Production-ready best practices

### Progress
- Installed and initialized Alembic  
- Created initial migration for existing models  
- Added a new column (due_date) and generated migration  
- Reviewed full project best practices  

### Key Notes
- Never use create_all() in production – always use Alembic for schema changes  
- Run `alembic revision --autogenerate` after model changes  
- Always review and edit autogenerated migration files  
- Use `alembic upgrade head` to apply migrations  
- For data seeding, use separate Alembic revisions or scripts  
- Production tips: echo=False, separate test DB, CI/CD migration step  
- Project complete: Core + ORM + Relationships + Advanced Querying + Migrations