from jsonschema import validate, Draft7Validator, SchemaError, ValidationError
import json
import os

list_schema = os.listdir('.' + '\\schema')
list_event = os.listdir('.' + '\\event')

with open('README.md', 'w', encoding='utf-8') as readme:

    for schema in list_schema:
        with open(f'schema\\{schema}', 'r') as schema_file:
            schema_data = schema_file.read()
            schema_data = json.loads(schema_data)
        readme.write(f'### Проверка папки по схеме: {schema} \n')
        # readme.write('*' * 100 + '\n')
        # readme.write('\n')
        try:
            Draft7Validator.check_schema(schema_data)
        except SchemaError as er:
            readme.write(str(er))

        for event in list_event:
            # file = dict
            with open(f'event\\{event}', 'r') as check_file:
                file = check_file.read()
                file = json.loads(file)
            # readme.write('*' * 100 + '\n')
            readme.write(f'Начата проверка файла: {event} \n\n')
            try:
                validate(instance=file, schema=schema_data)
                readme.write(f'Файл прошел проверку, ошибок по схеме "{schema}" - не найдено \n\n')
            except ValidationError as er:
                readme.write(f'Найдена ошибка по схеме {schema}: \n\n')
                readme.write(str(er))
            readme.write('-' * 100 + '\n')
            readme.write('\n')
