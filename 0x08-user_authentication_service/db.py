#!/usr/bin/env python3
""" DB class """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """ DB class """
    def __init__(self):
        """ constructor """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ session getter """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ adds and returns a new user Object """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)  # add the new user
        self._session.commit()  # update the DataBase

        return user

    def find_user_by(self, **kwargs) -> User:
        """ function that finds a created user
        using a argument """
        if kwargs is None:
            raise InvalidRequestError

        for i in kwargs.keys():
            if i not in User.__table__.columns.keys():
                raise InvalidRequestError

        user_query = self._session.query(User).filter_by(**kwargs).first()

        if user_query is None:
            raise NoResultFound

        return user_query

    def update_user(self, user_id: int, **kwargs) -> None:
        """ update properties of an user """
        user = self.find_user_by(id=user_id)
        for i in kwargs.keys():
            if i not in User.__table__.columns.keys():
                raise ValueError

        for k, v in kwargs.items():
            setattr(user, k, v)

        self._session.commit()
