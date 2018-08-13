import json
import re

class BaseModel:

	def set_attributes(self, params):
		_params = self.to_snake_case_dict(params)
		if hasattr(self, 'ATTR'):
			for attr in self.ATTR:
				if attr in _params and _params[attr] is not None:
					setattr(self, attr, _params[attr])

		if hasattr(self, 'OBJ_ATTR'):
			for var_name, class_name in self.OBJ_ATTR.items():
				if var_name in _params and _params[var_name] is not None:
					setattr(self, var_name, self.obj_or_dict(_params[var_name], class_name))

	def to_snake_case_dict(self, dict):
		sc_dict = {}
		for k in dict:
			sc_dict[self.to_snake_case(k)] = dict[k]
		return sc_dict

	def obj_or_dict(self, params, obj):
		if isinstance(params, dict):
			return obj(params)
		elif isinstance(params, obj):
			return params
		else:
			raise ValueError("{0} requires {1} object or dictionary".format(str(self), str(obj)))

	def to_json(self):
		return json.dumps(self.to_dict())

	def to_dict(self):
		self_dict = {}
		for var, val in self.__dict__.items():
			value = None
			if hasattr(val, 'to_dict'):
				value = val.to_dict()
			elif isinstance(val, list):
				values = map(lambda x: x.to_dict(), val)
			else:
				value = str(val)
			self_dict[self.to_pascal_case(var)] = value
		return self_dict

	def to_pascal_case(self, string):
		first, rest = string.split('_')[0], string.split('_')[1:]
		return first + ''.join(word.capitalize() for word in rest)

	def to_snake_case(self, string):
	    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
	    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

	def set_list_items(self, attr_name, obj):
		items = []
		for item in getattr(self, attr_name):
			items.append(obj(item))
		setattr(self, attr_name, items)