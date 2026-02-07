from database import engine, metadata
import models_core

print("Registered tables:", list(metadata.tables.keys()))

print("\nCreating tables...")
metadata.create_all(engine, checkfirst=True)
print("Done.")