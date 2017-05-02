import swagger_parser.SwaggerParser as s

a = s.SwaggerParser('http://0.0.0.0:81/api/doc.json')
# a.generate_datastructs()

# res = a.generate_handlers_on_a_fly(True)

# print(res)
a.generate_datastructs()
