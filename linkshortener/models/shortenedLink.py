from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.hybrid import hybrid_property
from linkshortener import config
from datetime import datetime
from linkshortener.extensions import db
from hashids import Hashids
import uuid

class ShortenedLink(db.Model):
    __tablename__ = "shortened_link"
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(500))
    _linkHash = db.Column("linkHash", db.String(500), unique=True)
    timeCreated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref='shortened_link')

    @hybrid_property
    def linkHash(self):
        return self._linkHash

    @linkHash.setter
    def linkHash(self, link):
        self.link = link
        someUUID = str(uuid.uuid4())
        hasher = Hashids(someUUID, min_length=2)
        hashedLink = hasher.encode(1)
        self._linkHash = hashedLink

    def __repr__(self):
        return f"User('{self.id}', '{self.author}',{self.timeCreated},{self._linkHash}')"