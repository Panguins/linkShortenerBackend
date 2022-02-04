from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from linkshortener.api.schemas import ShortenedLinkSchema
from linkshortener.models import ShortenedLink
from linkshortener.extensions import db
from linkshortener.commons.pagination import paginate

class ShortenedLinkResource(Resource):
    """Single object resource

    ---
    get:
      tags:
        - shortenedlink
      summary: Get a single shortened link
      description: Get a single shortened link by ID
      parameters:
        - in: path
          name: linkHash
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  shortenedLink: ShortenedLinkSchema
        404:
          description: user does not exists
    put:
      tags:
        - shortenedlink
      summary: Update a shortened link
      description: Update a single ShortenedLink by ID
      parameters:
        - in: path
          name: linkHash
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              ShortenedLinkSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: shortened link updated
                  user: ShortenedLinkSchema
        404:
          description: user does not exists
    delete:
      tags:
        - shortenedlink
      summary: Delete a shortened link
      description: Delete a single shortened link by ID
      parameters:
        - in: path
          name: linkHash
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: shortened link deleted
        404:
          description: shortened link does not exists
    """

    method_decorators = [jwt_required()]

    def get(self, linkHash):
        schema = ShortenedLinkSchema()
        # shortened_link = ShortenedLink.query.get_or_404(linkHash)
        shortened_link = ShortenedLink.query.filter(ShortenedLink.linkHash == linkHash).first()
        return {"shortenedLink": schema.dump(shortened_link)}

    def put(self, linkHash):
        schema = ShortenedLinkSchema(partial=True)
        shortened_link = ShortenedLink.query.get_or_404(linkHash)
        shortened_link = schema.load(request.json, instance=shortened_link)

        db.session.commit()

        return {"msg": "shortened link updated", "shortenedLink": schema.dump(shortened_link)}

    def delete(self, linkHash):
        shortened_link = ShortenedLink.query.get_or_404(linkHash)
        db.session.delete(shortened_link)
        db.session.commit()

        return {"msg": "shortened link deleted"}


class ShortenedLinkList(Resource):
    """Creation and get_all

    ---
    get:
      tags:
        - shortenedlink
      summary: Get a list of shortened links
      description: Get a list of paginated shortened links
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/ShortenedLinkSchema'
    post:
      tags:
        - shortenedlink
      summary: Create a shortened link
      description: Create a new shortened link
      requestBody:
        content:
          application/json:
            schema:
              ShortenedLinkSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: shortened link created
                  user: ShortenedLinkSchema
    """

    method_decorators = [jwt_required()]

    def get(self):
        schema = ShortenedLinkSchema(many=True)
        query = ShortenedLink.query
        return paginate(query, schema)

    def post(self):
        schema = ShortenedLinkSchema()
        shortened_link = schema.load(request.json)
        
        db.session.add(shortened_link)
        db.session.commit()

        return {"msg": "shortened link created", "shortenedLink": schema.dump(shortened_link)}, 201

