from apiflask import schemas
from apiflask.fields import strings, Integer

class StatusOutSchema(Schema):
    status = String()
    message = String()
