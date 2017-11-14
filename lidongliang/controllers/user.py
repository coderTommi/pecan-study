from pecan import expose, redirect
from webob.exc import status_map
from lidongliang.model import Session
from lidongliang.model import User

class UserController():
    @expose( template='addUser.html')
    def addPre(self):
        return dict()

    @expose(template='addUserResult.html', method='POST')
    def add(self, userName, age):
        user = User(userName=userName, age=age)
        session = Session()
        session.add(user)
        dd = dict((name, getattr(user, name)) for name in dir(user) if not name.startswith('__'))
        return dd

    @expose(template='userList.html')
    def index(self):
        session = Session()
        users = session.query(User).all()
        return dict(users=users)

    @expose(template='modifyPre.html')
    def modifyPre(self, id):
        session = Session()
        user = session.query(User).filter(User.id==id).one()
        return dict((name, getattr(user, name)) for name in dir(user) if not name.startswith('__'))

    @expose(template='modifyResult.html', method='POST')
    def modify(self, id, userName, age):
        session = Session()
        user = session.query(User).filter(User.id==id).one()
        user.age=age
        user.userName = userName
        return dict((name, getattr(user, name)) for name in dir(user) if not name.startswith('__'))

    @expose(template='userList.html', method='POST')
    def delUser(self, id):
        session = Session()
        user = session.query(User).filter(User.id==id).one()
        session.delete(user)
        session.commit()
        users = session.query(User).all()
        return dict(users=users)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)