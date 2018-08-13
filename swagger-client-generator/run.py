import swagger_parser.SwaggerParser as s

a = s.SwaggerParser('swagger.json')

a.generate_datastructs()
