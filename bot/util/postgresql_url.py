from sqlalchemy import URL
from util import (
    DRIVER_NAME, DB_USER, 
    DB_PASSWORD, DB_NAME, DB_PORT, DB_HOST
    )

# TODO переместить создание урла в константы

POSTGRESQL_URL = URL.create(
    drivername=DRIVER_NAME,
    username=DB_USER,
    database=DB_NAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
    )