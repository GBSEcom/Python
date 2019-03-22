import openapi_client
import simple
import json

class ObjectBuilder:

  @staticmethod
  def build(object_name, json_params):
    camel_case_key = object_name[:1].lower()+object_name[1:]
    params = {camel_case_key: json.loads(json_params)}
    instance = ObjectBuilder(object_name, params)
    return instance.create_object()

  def __init__(self, object_name, payload):
    self.object_name = object_name
    self.payload = payload

  def create_object(self, object_name=None, payload=None):
    object_name = self.object_name if not object_name else object_name
    payload = self.payload if not payload else payload

    object_ = getattr(openapi_client, object_name)
    payload = payload[object_name[:1].lower()+object_name[1:]]
    attribute_map = object_.attribute_map
    openapi_types = object_.openapi_types
    args = {}
    for attr_snake, attr_cc in attribute_map.iteritems():
      attr_class = openapi_types[attr_snake]
      value = None
      if attr_cc in payload and isinstance(payload[attr_cc], list):
        list_class = openapi_types[attr_snake].replace('list', '').strip('[]')
        value = []
        for instances in payload[attr_cc]:
          value.append(
            self.create_object(list_class, instance)
          )
      elif attr_cc in payload and isinstance(payload[attr_cc], dict):
        corrected_dict = {}
        corrected_dict[attr_class[:1].lower()+attr_class[1:]] = payload[attr_cc]
        args[attr_snake] = self.create_object(attr_class, corrected_dict)
      elif attr_cc in payload and attr_class == 'int' and not isinstance(payload[attr_cc], int):
        args[attr_snake] = int(payload[attr_cc])
      elif attr_cc in payload:
        args[attr_snake] = payload[attr_cc]
    return object_(**args)