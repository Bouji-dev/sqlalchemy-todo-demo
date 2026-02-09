from database import engine
from models_orm import Base


print('Creating ORM tables...')
Base.metadata.create_all(engine)
print('ORM tables created!')