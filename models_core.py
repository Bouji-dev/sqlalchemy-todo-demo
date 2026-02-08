from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, func, Enum
from database import metadata


tasks = Table(
    'tasks',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(200), nullable=False),
    Column('description', String(1000)),
    Column('completed', Boolean, default=False),
    Column('created_at', DateTime, server_default=func.now(), nullable=False),
    Column('priority', Enum('low', 'medium', 'high', name='priority_enum'), default='medium'),
)