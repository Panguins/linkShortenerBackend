from linkshortener.models import User
from linkshortener.extensions import ma, db


class UserSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    password = ma.String(load_only=True, required=True)
    shortenedLinks = ma.List(ma.Nested("linkshortener.api.schemas.shortenedLink.ShortenedLinkSchema", exclude=["author"], dump_only=True), dump_only=True)

    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True
        exclude = ("_password",)
