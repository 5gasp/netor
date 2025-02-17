# @Author: Daniel Gomes
# @Date:   2022-10-19 14:56:50
# @Email:  dagomes@av.it.pt
# @Copyright: Insituto de Telecomunicações - Aveiro, Aveiro, Portugal
# @Last Modified by:   Daniel Gomes
# @Last Modified time: 2022-11-06 10:21:03
import aux.constants as Constants
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import configparser
import time
import logging


# load config
config = configparser.ConfigParser()
config.read('config.ini')

# Logger
logging.basicConfig(
    format="%(module)-15s:%(levelname)-10s| %(message)s",
    level=logging.INFO
)


# Test config
try:
    # Load Variables
    Constants.DB_LOCATION = config['DB']['Location']
    Constants.DB_NAME = config['DB']['Name']
    Constants.DB_USER = config['DB']['User']
    Constants.DB_PASSWORD = config['DB']['Password']
except:
    exit(2)


DB_OK = False
for i in range(10):
    try:
        logging.info(f"Trying to connect to the DB - postgresql://{Constants.DB_USER}:{Constants.DB_PASSWORD}@{Constants.DB_LOCATION}/{Constants.DB_NAME}")
        SQLALCHEMY_DATABASE_URL = f"postgresql://{Constants.DB_USER}:{Constants.DB_PASSWORD}@{Constants.DB_LOCATION}/{Constants.DB_NAME}"
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL
        )
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()
        DB_OK = True
        break
    except:
        logging.error("Waiting for DB. Will sleep 10 more seconds...")
        time.sleep(10)

if not DB_OK:
    logging.critical("Unable to connect to database. Exception:", e)
    exit(2)


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        # if we fail somehow rollback the connection
        db.rollback()
        raise
    finally:
        db.close()
