import json
import re

from faker import Faker

fake = Faker()


class Handler:
    def __init__(self, handler, method, request_json, config_name, suffix=""):
        self.handler = handler
        self.method = method
        self.request_json = request_json
        self.config_name = config_name
        self.suffix = suffix
        self.uniq_id = None
        self.form_time = None


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class JsonDumper(object):
    def json(self):
        return json.dumps(self, cls=CustomJsonEncoder)


def set_initializer(self, list_of_objects, **kwargs):
    for name, value in kwargs.items():

        try:
            setattr(self, name, eval(value))
        except:
            setattr(self, name, value)


def add_function(cls, **kwargs):
    def get_randomize_instance(self, list_of_objects):
        for name, value in kwargs.items():

            if 'get_randomize_instance' in str(value) and re.sub(r"\.get_randomize_instance\(.*\)\).*", "",
                                                                 value).replace('[', '') in list_of_objects:
                value = re.sub(r"\.get_randomize_instance\(.*\)\).*", "", value)

                if value[0] == '[':
                    value = value.replace('[', '')
                    kwargs[
                        name] = f'[json.loads(list_of_objects[str("{value}")](list_of_objects).' \
                                f'get_randomize_instance(list_of_objects).json())]'
                else:
                    kwargs[
                        name] = f'json.loads(list_of_objects[str("{value}")](list_of_objects).' \
                                f'get_randomize_instance(list_of_objects).json())'
        return self(list_of_objects, **kwargs)

    setattr(cls, 'get_randomize_instance', classmethod(get_randomize_instance))


def generate_classes(data_structures):
    ar = dict()
    for x in data_structures:
        attrib = {}
        for z in x.attributes:
            attrib[z.name] = z.random_value
        ar[f'{x.name}'] = generate_classes_b(classname=x.name, **attrib)

    return ar


def generate_handlers(data_structures, handlers, debug=False):
    handlers_g = {}
    classes = generate_classes(data_structures)
    for h in handlers:
        for m in h.methods:
            if m.parameters:
                handlers_g[m.parameters] = Handler(h.name, m.name,
                                                   classes[m.parameters].get_randomize_instance(classes).json(),
                                                   m.parameters)
            else:
                pass
                # TODO avoid skipping rev.txt and health_check here
                # handlers_g.append(Handler(h.name, m.name, None, None))
    if debug:
        for key, z in handlers_g.items():
            print(key, z.handler, z.method, z.request_json)

    return handlers_g


def generate_classes_b(classname, **attributes):
    mem_class = type(classname, (JsonDumper,), {"__init__": set_initializer})
    add_function(mem_class, **attributes)
    return mem_class
