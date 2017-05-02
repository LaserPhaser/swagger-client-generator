from faker import Faker
from jinja2 import Environment, FileSystemLoader
from requests import get

fake = Faker()


class Model:
    def __init__(self):
        self.code = None
        self.model = None


class Parameter:
    def __init__(self):
        self.name = ''
        self._in = ''
        self.required = True
        self.description = ''
        self.type = ''
        self.patters = ''
        self.schema = ''


class Response:
    def __init__(self):
        self.code = ''
        self.description = ''
        self.schema = ''


class Method:
    def __init__(self, name, data):
        self.description = ''
        self.operationId = ''
        self.consumes = ''
        self.produces = ''
        self.parameters = []
        self.responses = []
        self.name = name
        self.data = data
        self.body_parameters = []
        self.parse_data(data)

    def parse_data(self, data):
        # print(data)
        if 'description' in data:
            self.description = data.pop('description')
        if 'summary' in data:
            self.summary = data.pop('summary')
        if 'parameters' in data:
            self.parse_parameters(data.pop('parameters'))

        if 'responses' in data:
            self.parse_responses(data.pop('responses'))
            # for x, y in data.items():
            #     print('X_X_X', x, y)

    def parse_parameters(self, parameters):
        for parameter in parameters:
            print(parameter)
            if 'in' in parameter:
                place = parameter['in']
                if place == 'body':
                    self.body_parameters.append(parameter['schema']['$ref'].replace('#/definitions/', ''))
                if place == 'query':
                    print(parameter)
                if place == 'path':
                    print(parameter)

    def parse_responses(self, responses):
        pass
        # TODO add auto response checkers


class Handler:
    def __init__(self, url: str, parameters):
        self.url = url
        self.methods = self._get_methods(parameters)

    def _get_methods(self, parameters):
        return [Method(name, data) for name, data in parameters.items()]


class Class:
    def __init__(self, name: str):
        self.name = name
        self.attributes = list()  # list of Variables
        self.sub_classes = []


class Variable:
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type


class SwaggerParser:
    def __init__(self, swagger):
        self.parsed_data = None
        self.swagger = swagger
        self.data_structures = []
        self.data_structures_sorted = []
        self.handlers = []
        self.variables = []
        self.swagger_v2()

    def swagger_v2(self):
        """
        Function read data from swagger V2 json
        and create result json with handlers
        """

        response = get(self.swagger, verify=False)
        # TODO data structs can be not only in definitions also in requests params
        ds = DataStructures(response.json()['definitions'].items())
        for path, path_value in response.json()['paths'].items():
            self.handlers.append(Handler(path, path_value))
        self.data_structures = ds.classes
        # TODO add unroll for nested datastructs  

        self.variables = ds.variables

    def generate_datastructs(self):
        template_env = Environment(
            loader=FileSystemLoader('./swagger-client-generator/templates/'))
        header_template = template_env.get_template('datastruct.txt')
        # print(self.data_structures)
        ds = header_template.render(datastructs=self.data_structures, variables=self.variables)
        # TODO Add file writer for datastructures:
        print(ds)
        # pass


class DataStructures:
    def __init__(self, json_object):

        self.json = json_object
        self.value_matcher = {'string': 'StringField()',
                              'number': 'IntField()',
                              'integer': 'IntField()',
                              'boolean': 'BoolField()',
                              }
        self.classes = []
        self.variables = []
        for definition, definition_value in json_object:
            self.prepare_data_structures(definition, definition_value)

    def prepare_data_structures(self, name, params):
        name = name
        root = None
        if 'properties' in params:
            type = params.pop('type')
            if type == 'object':
                root = Class(name)
                self.classes.append(root)
            else:
                pass
            properties = params['properties']
            self.unroll_nested_structures(properties, root)
        else:

            node = Variable(name, None)
            self.variables.append(node)
            self.check_value_var(name, params, node)

    def unroll_nested_structures(self, properties, node):
        if properties is not None:
            for name, value in properties.items():
                self.check_value(name, value, node)

    def check_value_var(self, name, value, node, extend='{}'):
        if ('type' in value and value['type'] in self.value_matcher) or '$ref' in value:
            node.type = extend.format(self.match_value(value))
            node.update_randomize_value(node.type)

        elif 'type' in value and 'additionalProperties' in value and value['type'] == 'object':
            value = value['additionalProperties']
            self.check_value_var(name, value, node, extend)

        elif 'type' in value and value['type'] == 'array':
            print(name, value)
            extend = 'ListField({})'
            value = value['items']
            self.check_value_var(name, value, node, extend)

    def check_value(self, name, value, node, extend='{}'):
        if ('type' in value and value['type'] in self.value_matcher) or '$ref' in value:

            node.attributes.append(Variable(name, extend.format(self.match_value(value))))
        elif 'type' in value and 'additionalProperties' in value and value['type'] == 'object':
            value = value['additionalProperties']
            self.check_value(name, value, node, extend)
        elif 'type' in value and value['type'] == 'object':
            sub_class = Class(name)
            node.sub_classes.append(sub_class)
            self.unroll_nested_structures(value['properties'], sub_class)

        elif 'type' in value and value['type'] == 'array':
            extend = 'ListField({})'
            value = value['items']
            self.check_value(name, value, node, extend)

    def match_value(self, data):
        if 'type' in data and data['type'] in self.value_matcher:
            return self.value_matcher[data['type']]
        if '$ref' in data:
            return data['$ref'].replace('#/definitions/', '')
