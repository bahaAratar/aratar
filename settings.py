from peewee import PostgresqlDatabase as PDB

db = PDB(
    'orm_py25',
    user = 'aratar',
    password = '1111',
    host = 'localhost',
    port = 5432
    )