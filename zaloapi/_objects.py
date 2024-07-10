from dataclasses import dataclass

@dataclass
class User:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
	
	def __repr__(self):
		attrs = [f"{key}={value!r}" for key, value in self.__dict__.items()]
		return f"User({', '.join(attrs)})"

@dataclass
class Group:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
		
	def __repr__(self):
		attrs = [f"{key}={value!r}" for key, value in self.__dict__.items()]
		return f"Group({', '.join(attrs)})"

@dataclass
class MessageObject:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
		
	def __repr__(self):
		attrs = [f"{key}={value!r}" for key, value in self.__dict__.items()]
		return f"Message({', '.join(attrs)})"