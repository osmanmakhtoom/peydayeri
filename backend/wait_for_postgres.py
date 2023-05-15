import logging
import os
from time import time, sleep

import psycopg

check_timeout = os.getenv("POSTGRES_CHECK_TIMEOUT", 30)
check_interval = os.getenv("POSTGRES_CHECK_INTERVAL", 1)
interval_unit = "second" if check_interval == 1 else "seconds"
config = {
    "dbname": os.getenv("DATABASE_NAME", "peydayeri_db"),
    "user": os.getenv("DATABASE_USER", "peydayeri_user"),
    "password": os.getenv("DATABASE_PASSWORD", "123456"),
    "host": os.getenv("DATABASE_URL", "postgres")
}

start_time = time()
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def is_pg_ready(host, user, password, dbname):
    while time() - start_time < check_timeout:
        try:
            conn = psycopg.connect(**vars())
            logger.info("Postgres is ready! ✨ 💅")
            conn.close()
            return True
        except psycopg.OperationalError:
            logger.info(f"Postgres isn't ready. Waiting for {check_interval} {interval_unit}...")
            sleep(check_interval)

    logger.error(f"We could not connect to Postgres within {check_timeout} seconds.")
    return False


is_pg_ready(**config)
