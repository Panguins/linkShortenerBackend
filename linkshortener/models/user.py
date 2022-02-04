from sqlalchemy.ext.hybrid import hybrid_property

from linkshortener.extensions import db, pwd_context


class User(db.Model):
    """Basic user model"""
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    _password = db.Column("password", db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
    shortenedLinks = db.relationship('ShortenedLink', backref='user', lazy=True)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = pwd_context.hash(value)
    

    def __repr__(self):
        return "<User %s>" % self.username
