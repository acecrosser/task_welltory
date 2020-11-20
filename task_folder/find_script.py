from jsonschema import validate, Draft4Validator, SchemaError
import json
import os


# # with open('schema\cmarker_created.schema', 'r') as file:
# #      schema = file
# # with open('event\\1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json', 'r') as json_file:
# #     validate(json_file, schema)

schema = {}
with open('schema\\workout_created.schema', 'r') as schema_file:
    schema = json.loads(schema_file.read())

try:
    Draft4Validator.check_schema(schema)
except SchemaError as er:
    print(er)

file = {}
with open('event\\1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json', 'r') as check_file:
    file = json.loads(check_file.read())

validate(file, schema)

# schema = open('schema\\workout_created.schema', 'r').read()
# schema = json.loads(schema)
# print(schema)
# file_json = open('event\\3ade063d-d1b9-453f-85b4-dda7bfda4711.json', 'r').read()
# # print(file_json)
#
# validate(file_json, schema)

# from jsonschema import validate
#
# schema = {
#     "type": "object",
#     "properties": {
#         "name": {
#             "type": "string"
#             },
#         "age": {"type": "number",
#                 "minimum": 18,
#                 "maximum": 110
#                 },
#         "role": {
#             "type": "string",
#             "enum": ["admin", "user"]
#             }
#         }
#     }
#
# message = {"name": "Vasya", "age": 15, "role": "user"}
#
# validate(message, schema)