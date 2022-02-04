from linkshortener.models import ShortenedLink
from linkshortener.extensions import ma, db


class ShortenedLinkSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)
    author = ma.Nested('linkshortener.api.schemas.user.UserSchema', dump_only=True, exclude=["shortenedLinks"])
    linkHash = ma.String(load_only=True)
    timeCreated = ma.DateTime(dump_only=True)


    class Meta:
        model = ShortenedLink
        include_fk = True
        sqla_session = db.session
        load_instance = True
        exclude = ()
