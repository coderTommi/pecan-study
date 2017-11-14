from lidongliang.model.user import User
from pecan import conf  # noqa
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

Session = scoped_session(sessionmaker())
metadata = MetaData()


def init_model():
    """
    This is a stub method which is called at application startup time.

    If you need to bind to a parsed database configuration, set up tables or
    ORM classes, or perform any database initialization, this is the
    recommended place to do it.

    For more information working with databases, and some common recipes,
    see https://pecan.readthedocs.io/en/latest/databases.html
    """
    #pass
    conf.sqlalchemy_w.engine = _engine_from_config(conf.sqlalchemy_w)
    conf.sqlalchemy_ro.engine = _engine_from_config(conf.sqlalchemy_ro)

def _engine_from_config(configuration):
    configuration = dict(configuration)
    url = configuration.pop('url')
    return create_engine(url, **configuration)


def start():
    Session.bind = conf.sqlalchemy_w.engine
    metadata.bind = conf.sqlalchemy_w.engine


def start_read_only():
    Session.bind = conf.sqlalchemy_ro.engine
    metadata.bind = conf.sqlalchemy_ro.engine


def commit():
    Session.commit()


def rollback():
    Session.rollback()


def clear():
    Session.close()


def flush():
    Session.flush()

